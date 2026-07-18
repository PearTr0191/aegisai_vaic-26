import io
import time
from typing import Dict, Tuple
from pathlib import Path
import numpy as np
import librosa
from scipy.spatial.distance import cosine
from app.schemas.audio import AudioScoreResponse


# Reference audio paths mapping - maps heritage item IDs to reference vocal audio files
REFERENCE_AUDIO_PATHS: Dict[int, Path] = {
    3: Path(__file__).resolve().parents[3] / "Project" / "audio" / "quanho-embed.wav",
    17: Path(__file__).resolve().parents[3] / "Project" / "audio" / "ho-embed.wav",
}


class VocalSimilarityAnalyzer:
    """
    Compare user's singing against reference vocal samples using MFCC similarity.
    Returns a 0-100 score indicating how close the user's voice matches the reference style.
    Includes vocal activity detection to filter out non-vocal audio.
    """

    def __init__(self, reference_dir: str = "Project/audio"):
        self.reference_dir = Path(reference_dir)

    def _extract_mfcc(self, y: np.ndarray, sr: int, n_mfcc: int = 13) -> np.ndarray:
        """Extract MFCC features from audio signal."""
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        return np.mean(mfccs, axis=1)

    def _compute_vocal_confidence(self, y: np.ndarray, sr: int) -> Tuple[float, str]:
        """
        Compute confidence that the audio contains sung vocals.
        Uses multiple acoustic features with strict thresholds.
        Returns (confidence_score, reason).
        """
        # Use librosa's harmonic/percussive source separation
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        
        # 1. Harmonic-to-percussive ratio - vocals are primarily harmonic
        harmonic_energy = np.mean(y_harmonic ** 2)
        percussive_energy = np.mean(y_percussive ** 2)
        hpss_ratio = harmonic_energy / (percussive_energy + 1e-10)
        
        # 2. Pitch activity using pyin
        f0, voiced_flag, _ = librosa.pyin(y, fmin=80, fmax=400, sr=sr)
        pitches = f0[~np.isnan(f0)]
        pitch_activity = len(pitches) / len(f0) if len(f0) > 0 else 0
        
        # 3. Spectral flatness - vocals are more tonal (lower flatness)
        spectral_flatness = librosa.feature.spectral_flatness(y=y)
        mean_flatness = np.mean(spectral_flatness)
        
        # 4. Zero crossing rate - vocals have low-mid ZCR
        zcr = librosa.feature.zero_crossing_rate(y)
        mean_zcr = np.mean(zcr)
        
        # 5. RMS energy variance - vocals have stable energy
        rms = librosa.feature.rms(y=y)
        rms_var = np.var(rms)
        rms_mean = np.mean(rms)
        
        # Strict vocal detection: ANY check failing = non-vocal
        # HPSS check: vocals should be mostly harmonic
        if hpss_ratio < 5.0:
            return 1.0, "percussive"
        
        # Pitch activity check: sustained pitch
        if pitch_activity < 0.7:
            return 1.0, "low_pitch"
        
        # Spectral flatness check: not noise-like
        if mean_flatness > 0.2:
            return 1.0, "noise_like"
        
        # ZCR check: percussive sounds have high ZCR
        if mean_zcr > 0.15:
            return 1.0, "percussive"
        
        # Energy variance check: vocals have stable energy
        if rms_var / (rms_mean + 1e-6) > 1.5:
            return 1.0, "percussive"
        
        # All checks passed - likely vocals
        return 100.0, "vocal_detected"

    def _compute_similarity(self, user_mfcc: np.ndarray, ref_mfcc: np.ndarray, 
                          vocal_confidence: float) -> float:
        """
        Compute spectral similarity using MFCC cosine similarity.
        Returns 0-100 similarity score.
        """
        # Cosine similarity on MFCC means
        cosine_sim = max(0, 1 - cosine(user_mfcc, ref_mfcc)) * 100
        
        # Apply vocal confidence penalty
        # Very low confidence for non-vocal = very low scores
        if vocal_confidence < 10:
            confidence_penalty = vocal_confidence / 100  # e.g., 1.0 -> 0.01
        elif vocal_confidence < 50:
            confidence_penalty = vocal_confidence / 50   # e.g., 25 -> 0.5
        else:
            confidence_penalty = 1.0
        
        # Final score
        final_score = cosine_sim * confidence_penalty
        return round(final_score, 1)

    def _get_feedback(self, score: float, item_id: int, vocal_reason: str) -> str:
        """Generate human-readable feedback based on score."""
        if vocal_reason != "vocal_detected":
            return "No clear vocal detected. Please sing or hum into the microphone more clearly."
        
        if score >= 80:
            return "Excellent! Your singing closely matches the traditional style's fluidity and character."
        elif score >= 65:
            return "Good! Your voice shows strong resemblance to the traditional style."
        elif score >= 50:
            return "Fair. Try matching the melodic contour and rhythm more closely."
        elif score >= 30:
            return "Needs improvement. Listen carefully to the reference and try to emulate the vocal style."
        else:
            return "Keep practicing! Focus on the phrasing and tonal characteristics of the tradition."

    def analyze(
        self,
        user_audio_bytes: bytes,
        item_id: int,
    ) -> AudioScoreResponse:
        """
        Analyze user recording against reference.
        
        Args:
            user_audio_bytes: Raw audio bytes from user recording
            item_id: Heritage item ID to identify which reference to use
            
        Returns:
            AudioScoreResponse with similarity score
        """
        start_time = time.time()

        # Load user audio
        try:
            user_y, user_sr = librosa.load(io.BytesIO(user_audio_bytes), sr=22050, mono=True)
        except Exception as e:
            raise ValueError(f"Failed to load user audio: {e}")

        # Check for vocal activity
        vocal_confidence, vocal_reason = self._compute_vocal_confidence(user_y, user_sr)

        # Get reference path
        ref_path = REFERENCE_AUDIO_PATHS.get(item_id)
        if not ref_path:
            raise ValueError(f"No reference audio available for item ID {item_id}")

        # Load reference audio
        try:
            ref_y, ref_sr = librosa.load(ref_path, sr=22050, mono=True)
        except Exception as e:
            raise ValueError(f"Failed to load reference audio: {e}")

        # Extract MFCC features
        user_mfcc = self._extract_mfcc(user_y, user_sr)
        ref_mfcc = self._extract_mfcc(ref_y, ref_sr)

        # Compute similarity score
        similarity = self._compute_similarity(user_mfcc, ref_mfcc, vocal_confidence)

        processing_time = int((time.time() - start_time) * 1000)

        return AudioScoreResponse(
            score=similarity,
            feedback=self._get_feedback(similarity, item_id, vocal_reason),
            processing_time_ms=processing_time,
        )