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
        response="Xin lỗi, tôi chưa thể xử lý âm thanh. Vui lòng viết tin nhắn.",
        confidence=0.0,
    )


# Text chat using RAG-lite
@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint for heritage queries.
    Uses RAG-lite for intangible heritage, searchable heritage sites.
    """
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    # Try heritage knowledge search via RAG-lite
    try:
        from app.services.rag_lite import HeritageRAGLite
        from app.core.database import async_session_maker

        async with async_session_maker() as db:
            rag = HeritageRAGLite(db)
            keywords = rag._extract_keywords(message)
            chunks = await rag._keyword_search(keywords, persona_id=None, limit=3)

            if chunks:
                context = "\n\n".join([c.content_vi for c in chunks[:3]])
                prompt = f"""Bạn là nghệ nhân gạo cội về di sản văn hóa Việt Nam.
Trả lời ngắn gọn, tôn trọng, dựa trên ngữ cảnh sau:

{context}

CÂU HỎI: {message}
TRẢ LỜI:"""

                try:
                    import httpx
                    from app.core.config import settings

                    async with httpx.AsyncClient() as client:
                        response = await client.post(
                            f"{settings.OLLAMA_HOST}/api/generate",
                            json={
                                "model": settings.OLLAMA_MODEL,
                                "prompt": prompt,
                                "stream": False,
                            },
                            timeout=30.0,
                        )
                        if response.status_code == 200:
                            result = response.json()
                            return ChatResponse(
                                response=result.get("response", "").strip(),
                                confidence=0.85,
                                sources=[c.source_type for c in chunks[:3]],
                            )
                except Exception:
                    pass
    except Exception:
        pass

    # Fallback response
    if request.lang == "vi":
        return ChatResponse(
            response="Xin lỗi, tôi không có đủ thông tin để trả lời câu hỏi này.",
            confidence=0.0,
            sources=[],
        )
    else:
        return ChatResponse(
            response="Sorry, I don't have enough information to answer this question.",
            confidence=0.0,
            sources=[],
        )
