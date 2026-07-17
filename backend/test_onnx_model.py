#!/usr/bin/env python3
"""
Test script for ONNX EthnoMusicNet model.
Generates synthetic audio and runs inference to verify model functionality.
"""
import os
import sys
import time
import tempfile
import numpy as np
import torch
import torchaudio
import onnxruntime as ort
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

from app.services.audio_analysis import AudioPreprocessor, EthnoMusicAnalyzer


def generate_synthetic_audio(duration_sec: float = 30.0, sr: int = 22050) -> torch.Tensor:
    """
    Generate synthetic audio for testing.
    Creates a mix of sine waves to simulate musical content.
    """
    t = torch.linspace(0, duration_sec, int(sr * duration_sec))
    
    # Mix of frequencies to simulate musical content
    frequencies = [261.63, 329.63, 392.00, 523.25]  # C4, E4, G4, C5
    amplitudes = [0.3, 0.25, 0.2, 0.15]
    
    waveform = torch.zeros_like(t)
    for freq, amp in zip(frequencies, amplitudes):
        waveform += amp * torch.sin(2 * np.pi * freq * t)
    
    # Add some variation
    waveform += 0.1 * torch.randn_like(waveform)  # Small noise
    waveform = waveform.unsqueeze(0)  # Add channel dim
    
    return waveform


def test_preprocessor():
    """Test the audio preprocessor independently"""
    print("\n=== Testing AudioPreprocessor ===")
    
    preprocessor = AudioPreprocessor()
    waveform = generate_synthetic_audio()
    
    print(f"Input waveform shape: {waveform.shape}")
    
    mel_spec = preprocessor.process(waveform, 22050)
    print(f"Output mel-spectrogram shape: {mel_spec.shape}")
    print(f"Expected shape: (1, 1, 128, time_dim)")
    
    assert mel_spec.shape[0] == 1, "Batch dimension should be 1"
    assert mel_spec.shape[1] == 1, "Channel dimension should be 1"
    assert mel_spec.shape[2] == 128, "Mel bins should be 128"
    assert mel_spec.shape[3] > 0, "Time dimension should be positive"
    
    print("✓ Preprocessor test passed")
    return mel_spec


def test_model_loading():
    """Test ONNX model loading"""
    print("\n=== Testing Model Loading ===")
    
    model_path = os.getenv("ETHNOMUSIC_MODEL_PATH", "./models/ethnomusic_net_int8.onnx")
    print(f"Model path: {model_path}")
    
    if not os.path.exists(model_path):
        print(f"✗ Model not found at {model_path}")
        return None
    
    print(f"Model size: {os.path.getsize(model_path) / 1024 / 1024:.2f} MB")
    
    try:
        session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
        
        # Print model info
        input_name = session.get_inputs()[0]
        print(f"Input: {input_name.name}, shape: {input_name.shape}")
        
        output_names = [o.name for o in session.get_outputs()]
        print(f"Outputs: {output_names}")
        for i, out in enumerate(session.get_outputs()):
            print(f"  [{i}] {out.name}: {out.shape}")
        
        print("✓ Model loaded successfully")
        return session
        
    except Exception as e:
        print(f"✗ Failed to load model: {e}")
        return None


def test_inference(session, mel_spec):
    """Test ONNX inference"""
    print("\n=== Testing Inference ===")
    
    if session is None:
        print("✗ Cannot run inference without model")
        return None
    
    input_name = session.get_inputs()[0].name
    output_names = [o.name for o in session.get_outputs()]
    
    print(f"Running inference on mel-spectrogram shape: {mel_spec.shape}")
    
    try:
        start_time = time.time()
        outputs = session.run(output_names, {input_name: mel_spec.numpy()})
        inference_time = (time.time() - start_time) * 1000
        
        print(f"Inference time: {inference_time:.2f} ms")
        print(f"Number of outputs: {len(outputs)}")
        
        for i, (name, output) in enumerate(zip(output_names, outputs)):
            print(f"  [{i}] {name}: shape={output.shape}, dtype={output.dtype}")
            if output.size < 20:
                print(f"      values: {output.flatten()[:10]}")
        
        print("✓ Inference test passed")
        return outputs
        
    except Exception as e:
        print(f"✗ Inference failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def write_wav(waveform: torch.Tensor, sr: int = 22050) -> bytes:
    """Write mono waveform tensor to WAV bytes without torchcodec dependency."""
    import struct
    samples = waveform.squeeze().numpy() if waveform.dim() > 1 else waveform.numpy()
    samples = np.clip(samples, -1.0, 1.0)
    samples_int16 = (samples * 32767).astype(np.int16)
    n_channels = 1
    sampwidth = 2
    n_frames = len(samples_int16)
    n_bytes = n_frames * n_channels * sampwidth
    buf = io.BytesIO()
    buf.write(b'RIFF')
    buf.write(struct.pack('<I', n_bytes + 36))
    buf.write(b'WAVE')
    buf.write(b'fmt ')
    buf.write(struct.pack('<I', 16))
    buf.write(struct.pack('<H', 1))
    buf.write(struct.pack('<H', n_channels))
    buf.write(struct.pack('<I', sr))
    buf.write(struct.pack('<I', sr * n_channels * sampwidth))
    buf.write(struct.pack('<H', n_channels * sampwidth))
    buf.write(struct.pack('<H', sampwidth * 8))
    buf.write(b'data')
    buf.write(struct.pack('<I', n_bytes))
    buf.write(samples_int16.tobytes())
    return buf.getvalue()


def decode_wav_bytes(audio_bytes: bytes):
    """Decode WAV bytes into waveform tensor and sample rate without torchcodec."""
    import wave
    buf = io.BytesIO(audio_bytes)
    with wave.open(buf, "rb") as wf:
        sr = wf.getframerate()
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        frames = wf.readframes(wf.getnframes())
    if sampwidth == 2:
        samples = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    elif sampwidth == 4:
        samples = np.frombuffer(frames, dtype=np.int32).astype(np.float32) / 2147483648.0
    else:
        raise ValueError(f"Unsupported WAV sample width: {sampwidth}")
    if n_channels > 1:
        samples = samples.reshape(-1, n_channels).T
    else:
        samples = samples.reshape(1, -1)
    return torch.from_numpy(samples), sr


def test_full_pipeline():
    """Test the complete analysis pipeline"""
    print("\n=== Testing Full Pipeline ===")
    
    model_path = os.getenv("ETHNOMUSIC_MODEL_PATH", "./models/ethnomusic_net_int8.onnx")
    
    if not os.path.exists(model_path):
        print(f"✗ Cannot test full pipeline - model not found")
        return
    
    try:
        analyzer = EthnoMusicAnalyzer(model_path)
        
        # Generate synthetic audio and encode/decoded via WAV bytes
        waveform = generate_synthetic_audio()
        audio_bytes = write_wav(waveform, 22050)
        
        print(f"Generated {len(audio_bytes)} bytes of audio")
        
        # Decode WAV bytes directly to avoid torchaudio.load/torchcodec dependency
        wf, sr = decode_wav_bytes(audio_bytes)
        mel_spec = analyzer.preprocessor.process(wf, sr)
        
        inputs = {analyzer.input_name: mel_spec.numpy()}
        outputs = analyzer.session.run(analyzer.output_names, inputs)
        
        genre_logits = outputs[0]
        instrument_probs = outputs[1]
        technique_probs = outputs[2]
        confidence = outputs[3]
        
        genre_idx = int(np.argmax(genre_logits, axis=-1).item())
        genre_conf = float(analyzer._softmax(genre_logits[0])[genre_idx])
        
        instrument_scores = instrument_probs[0]
        detected_instruments = [
            analyzer.INSTRUMENT_LABELS[i]
            for i, score in enumerate(instrument_scores)
            if score > 0.5
        ]
        
        technique_scores = technique_probs[0]
        detected_techniques = [
            analyzer.TECHNIQUE_LABELS[i]
            for i, score in enumerate(technique_scores)
            if score > 0.5
        ]
        
        print(f"\nAnalysis Results:")
        print(f"  Genre: {analyzer.GENRE_LABELS[genre_idx]} (confidence: {genre_conf:.3f})")
        print(f"  All genre scores: {dict(zip(analyzer.GENRE_LABELS, analyzer._softmax(genre_logits[0])))}")
        print(f"  Instruments: {detected_instruments}")
        print(f"  Techniques: {detected_techniques}")
        print(f"  Overall confidence: {float(np.asarray(confidence).item()):.3f}")
        
        assert analyzer.GENRE_LABELS[genre_idx] in EthnoMusicAnalyzer.GENRE_LABELS
        assert 0.0 <= genre_conf <= 1.0
        assert 0.0 <= float(np.asarray(confidence).item()) <= 1.0
        
        print("✓ Full pipeline test passed")
        
    except Exception as e:
        print(f"✗ Full pipeline test failed: {e}")
        import traceback
        traceback.print_exc()


def benchmark_model(session, mel_spec, num_runs: int = 10):
    """Benchmark model inference speed"""
    print(f"\n=== Benchmarking ({num_runs} runs) ===")
    
    if session is None:
        print("✗ Cannot benchmark without model")
        return
    
    input_name = session.get_inputs()[0].name
    output_names = [o.name for o in session.get_outputs()]
    
    times = []
    for i in range(num_runs):
        start = time.time()
        try:
            session.run(output_names, {input_name: mel_spec.numpy()})
            elapsed = (time.time() - start) * 1000
            times.append(elapsed)
        except Exception as e:
            print(f"  Run {i+1} failed: {e}")
            continue
    
    if times:
        print(f"  Min: {min(times):.2f} ms")
        print(f"  Max: {max(times):.2f} ms")
        print(f"  Mean: {np.mean(times):.2f} ms")
        print(f"  Std: {np.std(times):.2f} ms")
        print(f"  P50: {np.percentile(times, 50):.2f} ms")
        print(f"  P95: {np.percentile(times, 95):.2f} ms")
        print(f"  P99: {np.percentile(times, 99):.2f} ms")


def main():
    """Run all tests"""
    print("=" * 60)
    print("ONNX EthnoMusicNet Model Test Suite")
    print("=" * 60)
    
    # Test 1: Preprocessor
    mel_spec = test_preprocessor()
    
    # Test 2: Model loading
    session = test_model_loading()
    
    # Test 3: Inference
    if session and mel_spec is not None:
        test_inference(session, mel_spec)
        
        # Test 4: Benchmark
        benchmark_model(session, mel_spec)
    
    # Test 5: Full pipeline
    test_full_pipeline()
    
    print("\n" + "=" * 60)
    print("Test suite completed")
    print("=" * 60)


if __name__ == "__main__":
    import io
    import asyncio
    main()