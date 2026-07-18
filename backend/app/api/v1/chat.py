"""
Unified Chat API - merges ArtifactBot (artifact archive) with RAG-lite (intangible heritage)
Supports both text and voice input for heritage queries.
"""
from typing import List, Optional
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
import tempfile
import os

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    lang: str = "vi"  # "vi" or "en"


class ChatResponse(BaseModel):
    response: str
    confidence: float = 1.0
    sources: List[str] = []


def _transcribe_audio_faster_whisper(audio_bytes: bytes) -> str:
    """Transcribe audio using faster-whisper (CPU-optimized)."""
    try:
        from faster_whisper import WhisperModel
        from app.core.config import settings

        # Use cached model or download
        model_path = settings.WHISPER_MODEL_PATH
        if model_path.startswith("openai/"):
            model_name = model_path.replace("openai/", "")
        else:
            model_name = "base"

        model = WhisperModel(model_name, device="cpu", compute_type="int8")

        # Write to temp file for processing
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        try:
            segments, _ = model.transcribe(tmp_path, language="vi")
            transcript = " ".join([s.text for s in segments])
            return transcript
        finally:
            os.unlink(tmp_path)
    except Exception:
        # Fallback: return empty string to trigger text fallback
        return ""


# Voice transcription via Whisper (requires faster-whisper)
@router.post("/voice", response_model=ChatResponse)
async def transcribe_and_chat(file: UploadFile = File(...)):
    """
    Accept voice input (audio file), transcribe to text using Whisper, then chat.
    """
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Audio file required")

    audio_bytes = await file.read()

    # Transcribe with faster-whisper
    transcript = _transcribe_audio_faster_whisper(audio_bytes)

    if transcript:
        # Forward to text chat endpoint
        return await chat(ChatRequest(message=transcript, lang="vi"))

    # Fallback if transcription fails
    return ChatResponse(
        response="Xin lá»—i, tÃ´i chÆ°a thá»ƒ xá»­ lÃ½ Ã¢m thanh. Vui lÃ²ng viáº¿t tin nháº¯n.",
        confidence=0.0,
    )


# Text chat using LocalChatService (no external LLM required)
@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint for heritage queries.
    Uses LocalChatService for intangible heritage (no external LLM required).
    """
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    # Use local chat service (no external LLM required)
    try:
        from app.services.local_chat import LocalChatService
        from app.core.database import async_session_maker

        async with async_session_maker() as db:
            chat = LocalChatService(db)
            result = await chat.ask(message, persona_id="e7ce269d-d116-5334-99b9-66062d5f55ed", lang=request.lang)

            return ChatResponse(
                response=result.get("text", ""),
                confidence=result.get("confidence", 0.0),
                sources=[c.get("source_type", "") for c in result.get("citations", [])],
            )
    except Exception as e:
        # Log error
        import logging
        logging.error(f"Chat error: {e}")
        pass

    # Fallback response
    if request.lang == "vi":
        return ChatResponse(
            response="Xin lá»—i, tÃ´i khÃ´ng cÃ³ Ä‘á»§ thÃ´ng tin Ä‘á»ƒ tráº£ lá»i cÃ¢u há»i nÃ y.",
            confidence=0.0,
            sources=[],
        )
    else:
        return ChatResponse(
            response="Sorry, I don't have enough information to answer this question.",
            confidence=0.0,
            sources=[],
        )


# Voice grading endpoint - compare user recording to reference sample
class VoiceGradeRequest(BaseModel):
    genre: str  # "quan_ho", "ca_tru", etc.
    lat: float
    lng: float


class VoiceGradeResponse(BaseModel):
    grade: float  # 0.0 to 1.0 similarity score
    feedback_vi: str
    feedback_en: str
    detected_techniques: List[str] = []


@router.post("/grade", response_model=VoiceGradeResponse)
async def grade_voice_recording(
    request: VoiceGradeRequest,
    file: UploadFile = File(...),
):
    """
    Grade user's singing attempt against reference sample.
    Simple pitch similarity for placeholder implementation.
    """
    import numpy as np
    import librosa

    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Audio file required")

    audio_bytes = await file.read()

    try:
        # Load user audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        y_user, sr_user = librosa.load(tmp_path, sr=None)
        os.unlink(tmp_path)

        # Get pitch contour (simplified grading)
        f0_user, voiced_flag, _ = librosa.pyin(
            y_user,
            fmin=float(librosa.note_to_hz("C2")),
            fmax=float(librosa.note_to_hz("C7")),
            sr=sr_user,
        )

        # Placeholder: use a simple metric (pitch variance + voiced ratio)
        voiced_ratio = float(voiced_flag.mean()) if len(voiced_flag) > 0 else 0.0
        pitch_variance = float(np.var(f0_user[voiced_flag])) if np.any(voiced_flag) else 0.0

        # Normalize to grade (0-1)
        grade = min(1.0, voiced_ratio * 0.5 + min(pitch_variance / 1000, 0.5))

        # Simple feedback based on grade
        if grade > 0.7:
            feedback_vi = "Giá»ng hÃ¡t tá»‘t! Báº¡n Ä‘Ã£ báº¯t Ä‘áº§u náº¯m báº¯t Ä‘Æ°á»£c báº£n sáº¯c ca trÃ¹."
            feedback_en = "Good singing! You're beginning to grasp the essence of ca trÃ¹."
        elif grade > 0.4:
            feedback_vi = "Cáº§n luyá»‡n táº­p thÃªm. HÃ£y chÃº Ã½ vÃ o hÃ²a Ã¢m vÃ  ngá»¯ cáº£nh."
            feedback_en = "Needs practice. Pay attention to ornamentation and context."
        else:
            feedback_vi = "HÃ£y há»c tá»« nghá»‡ nhÃ¢n vÃ  luyá»‡n táº­p ká»¹ hÆ¡n. TÃ´i cÃ³ thá»ƒ giÃºp gÃ¬?"
            feedback_en = "Learn from the artisan and practice more. How can I help?"

        return VoiceGradeResponse(
            grade=round(grade, 2),
            feedback_vi=feedback_vi,
            feedback_en=feedback_en,
            detected_techniques=["lay_hat"] if grade > 0.5 else [],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Grading failed: {str(e)}")
