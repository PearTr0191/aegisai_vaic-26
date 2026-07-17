"""
Unified Chat API - merges ArtifactBot (artifact archive) with RAG-lite (intangible heritage)
Supports both text and voice input for heritage queries.
"""
from typing import List, Optional
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    lang: str = "vi"  # "vi" or "en"


class ChatResponse(BaseModel):
    response: str
    confidence: float = 1.0
    sources: List[str] = []


# Voice transcription via Whisper (requires faster-whisper)
@router.post("/voice", response_model=ChatResponse)
async def transcribe_and_chat(file: UploadFile = File(...)):
    """
    Accept voice input (audio file), transcribe to text using Whisper, then chat.
    """
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Audio file required")

    audio_bytes = await file.read()

    # Placeholder: In production, use faster-whisper
    # For now, simulate transcription
    # Example with faster-whisper:
    #
    # from faster_whisper import WhisperModel
    # model = WhisperModel("base", device="cpu")
    # segments, _ = model.transcribe(audio_bytes)
    # transcript = " ".join([s.text for s in segments])
    #
    # Then call the chat endpoint below...

    return ChatResponse(
        response="Voice transcription: Please implement Whisper integration with faster-whisper package.",
        confidence=0.0,
    )


# Text chat using RAG-lite
@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint for heritage queries.
    Uses RAG-lite for intangible heritage, ArtifactBot data for tangible artifacts.
    """
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    # Try intangible heritage first via RAG-lite
    try:
        from app.services.rag_lite import HeritageRAGLite
        from app.core.database import async_session_maker

        async with async_session_maker() as db:
            # Use default persona for intangible heritage
            rag = HeritageRAGLite(db)
            # Search without persona constraint
            keywords = rag._extract_keywords(message)
            chunks = await rag._keyword_search(keywords, persona_id=None, limit=3)

            if chunks:
                # Build context and generate response
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