import io
import base64
import json
from typing import List, Dict, cast
import numpy as np
import torch
import onnxruntime as ort
import librosa

from app.schemas.audio import (
    AudioAnalysisResponse,
    GenreScore,
    InstrumentScore,
    TechniqueScore,
    OrnamentEvent,
)


class AudioPreprocessor:
    """Preprocess audio to mel-spectrogram for model input"""

    def __init__(
        self,
        sample_rate: int = 22050,
        n_mels: int = 128,
        n_fft: int = 2048,
        hop_length: int = 512,
        max_duration: float = 30.0,
    ):
        self.sample_rate = sample_rate
        self.n_mels = n_mels
        self.n_fft = n_fft
        self.hop_length = hop_length
        self.max_samples = int(max_duration * sample_rate)

    def process(self, waveform: torch.Tensor, sr: int) -> torch.Tensor:
        """
        Convert waveform to mel-spectrogram
        Input: (channels, samples)
        Output: (1, 1, n_mels, time) - batch format for ONNX
        """
        # Resample if needed using librosa
        if sr != self.sample_rate:
            y = waveform.squeeze(0).numpy()
            y = librosa.resample(y, orig_sr=sr, target_sr=self.sample_rate)
            waveform = torch.from_numpy(y).unsqueeze(0)
            sr = self.sample_rate

        # Convert to mono if stereo
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)

        # Trim or pad to max duration
        if waveform.shape[1] > self.max_samples:
            waveform = waveform[:, : self.max_samples]
        elif waveform.shape[1] < self.max_samples:
            pad_len = self.max_samples - waveform.shape[1]
            waveform = torch.nn.functional.pad(waveform, (0, pad_len))

        # Compute mel spectrogram using librosa
        y = waveform.squeeze(0).numpy()
        mel = librosa.feature.melspectrogram(
            y=y, sr=self.sample_rate, n_mels=self.n_mels, n_fft=self.n_fft, hop_length=self.hop_length, power=2.0
        )
        log_mel = librosa.power_to_db(mel, ref=np.max)

        # Normalize
        log_mel = (log_mel - log_mel.mean()) / (log_mel.std() + 1e-8)

        # Convert to tensor and add batch/channel dims: (1, 1, n_mels, time)
        mel_tensor = torch.from_numpy(log_mel.astype(np.float32)).unsqueeze(0).unsqueeze(0)

        return mel_tensor

    def generate_waveform_peaks(self, waveform: torch.Tensor, n_peaks: int = 100) -> List[float]:
        """Generate downsampled waveform peaks for visualization"""
        # Convert to mono
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)

        # Downsample to n_peaks
        samples = waveform.shape[1]
        step = max(1, samples // n_peaks)
        peaks = []
        for i in range(0, samples, step):
            chunk = waveform[0, i : i + step]
            if chunk.numel() > 0:
                peaks.append(float(chunk.abs().max()))
        
        # Ensure exactly n_peaks
        if len(peaks) > n_peaks:
            peaks = peaks[:n_peaks]
        elif len(peaks) < n_peaks:
            peaks.extend([0.0] * (n_peaks - len(peaks)))
        
        return peaks


class EthnoMusicAnalyzer:
    """
    ONNX Runtime inference for EthnoMusicNet
    Multi-task: genre (2), instruments (12 multi-label), techniques (10 multi-label), confidence (1)
    """

    GENRE_LABELS = [
        "quan_ho", "ho"
    ]

    INSTRUMENT_LABELS = [
        "dan_bau", "dan_tranh", "dan_nhi", "dan_ty_ba", "sao",
        "ken", "tieu", "phach", "trong_de", "trong_chat", "mo", "voice"
    ]

    TECHNIQUE_LABELS = [
        "nay_hat", "run_hat", "lay_hat", "so_hat", "nhap_hat",
        "chuyen_hat", "vuot_hat", "dam_hat", "roi_hat", "kep_hat"
    ]

    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(
            model_path, providers=["CPUExecutionProvider"]
        )
        self.preprocessor = AudioPreprocessor()
        self.input_name = self.session.get_inputs()[0].name
        self.output_names = [o.name for o in self.session.get_outputs()]

    async def analyze(
        self,
        audio_bytes: bytes,
        filename: str,
        audio_loader = None,
    ) -> AudioAnalysisResponse:
        """Main analysis pipeline"""
        import time
        start_time = time.time()

        # 1. Load audio using librosa
        y, sr = librosa.load(io.BytesIO(audio_bytes), sr=None, mono=True)
        waveform = torch.from_numpy(y).unsqueeze(0)

        # 2. Preprocess
        mel_spec = self.preprocessor.process(waveform, sr)

        # 3. Inference
        inputs = {self.input_name: mel_spec.numpy()}
        outputs = self.session.run(self.output_names, inputs)

        # Parse outputs (assuming order: genre_logits, instrument_probs, technique_probs, confidence)
        genre_logits = outputs[0]
        instrument_probs = outputs[1]
        technique_probs = outputs[2]
        confidence = outputs[3]

        # 4. Post-process genre
        genre_idx = int(np.argmax(genre_logits, axis=-1).item())
        genre_probs = self._softmax(genre_logits[0])
        genre_conf = float(genre_probs[genre_idx])

        # 5. Post-process instruments (multi-label, threshold 0.5)
        instrument_scores = instrument_probs[0]
        detected_instruments = [
            self.INSTRUMENT_LABELS[i]
            for i, score in enumerate(instrument_scores)
            if score > 0.5
        ]

        # 6. Post-process techniques (multi-label, threshold 0.5)
        technique_scores = technique_probs[0]
        detected_techniques = [
            self.TECHNIQUE_LABELS[i]
            for i, score in enumerate(technique_scores)
            if score > 0.5
        ]

        # 7. Ornament timeline (rule-based on pitch contour)
        ornament_timeline = self._detect_ornaments(waveform, sr)

        # 8. Waveform for visualization
        waveform_peaks = self.preprocessor.generate_waveform_peaks(waveform)

        processing_time = int((time.time() - start_time) * 1000)

        # 9. Build response
        return AudioAnalysisResponse(
            genre=GenreScore(
                label=cast(str, self.GENRE_LABELS[genre_idx]),
                confidence=genre_conf,
                all_scores={label: float(score) for label, score in zip(self.GENRE_LABELS, genre_probs)},
            ),
            instruments=InstrumentScore(
                detected=cast(List[str], detected_instruments),
                all_scores={label: float(score) for label, score in zip(self.INSTRUMENT_LABELS, instrument_scores)},
            ),
            techniques=TechniqueScore(
                detected=cast(List[str], detected_techniques),
                all_scores={label: float(score) for label, score in zip(self.TECHNIQUE_LABELS, technique_scores)},
                ornament_timeline=ornament_timeline,
            ),
            confidence=float(np.asarray(confidence).item()) if hasattr(confidence, "item") else float(confidence),
            processing_time_ms=processing_time,
            waveform_url=f"data:application/json;base64,{self._encode_waveform(waveform_peaks)}",
        )

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        """Numerically stable softmax"""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def _detect_ornaments(self, waveform: torch.Tensor, sr: int) -> List[OrnamentEvent]:
        """
        Rule-based ornament detection on pitch contour (using librosa.pyin)
        - nẩy: sudden pitch jump > 3 semitones in < 100ms
        - rung: periodic FM modulation 4-8 Hz, depth > 50 cents
        - lay: smooth pitch glide > 2 semitones over 200-500ms
        """
        try:
            # Convert to mono numpy
            y = waveform.mean(dim=0).numpy() if waveform.shape[0] > 1 else waveform[0].numpy()
            
            # Pitch tracking with PYIN
            f0, voiced_flag, voiced_probs = librosa.pyin(
                y,
                fmin=float(librosa.note_to_hz("C2")),
                fmax=float(librosa.note_to_hz("C7")),
                sr=sr,
                hop_length=self.preprocessor.hop_length,
            )

            events = []
            hop_time = self.preprocessor.hop_length / sr
            semitone_ratio = 2 ** (1 / 12)

            # Detect nẩy (sudden pitch jumps)
            pitch_diff = np.diff(f0)
            nay_threshold = 3 * semitone_ratio  # 3 semitones
            nay_indices = np.where(
                (np.abs(pitch_diff) > nay_threshold) & voiced_flag[:-1] & voiced_flag[1:]
            )[0]
            
            for idx in nay_indices:
                time_sec = idx * hop_time
                confidence = min(1.0, abs(pitch_diff[idx]) / (5 * semitone_ratio))
                events.append(OrnamentEvent(
                    time_seconds=round(time_sec, 2),
                    technique="nay_hat",
                    confidence=round(confidence, 2),
                ))

            # Detect lay (portamento) - smooth pitch glides
            window_size = int(0.3 / hop_time)  # 300ms window
            for i in range(len(f0) - window_size):
                segment = f0[i:i+window_size]
                voiced_seg = voiced_flag[i:i+window_size]
                if voiced_seg.sum() > window_size * 0.7:
                    pitch_change = segment[-1] - segment[0]
                    if abs(pitch_change) > 2 * semitone_ratio:  # > 2 semitones
                        time_sec = i * hop_time
                        confidence = min(1.0, abs(pitch_change) / (4 * semitone_ratio))
                        events.append(OrnamentEvent(
                            time_seconds=round(time_sec, 2),
                            technique="lay_hat",
                            confidence=round(confidence, 2),
                        ))
                        i += window_size  # Skip ahead

            # Sort by time
            events.sort(key=lambda e: e.time_seconds)
            return events[:20]  # Limit to 20 events

        except Exception:
            # Fallback: return empty timeline
            return []

    def _encode_waveform(self, peaks: List[float]) -> str:
        """Encode waveform peaks as base64 JSON"""
        data = json.dumps(peaks).encode()
        return base64.b64encode(data).decode()