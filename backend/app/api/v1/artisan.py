from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import ollama
from app.core.config import settings
from app.core.database import get_db
from app.models.artisan import ArtisanPersona, KnowledgeChunk
from app.schemas.chat import ArtisanAskRequest, ArtisanResponse, Citation
from app.services.rag_lite import HeritageRAGLite
from uuid import UUID

router = APIRouter(prefix="/artisan", tags=["artisan"])


@router.post("/ask", response_model=ArtisanResponse)
async def ask_artisan(
    request: ArtisanAskRequest,
    db: AsyncSession = Depends(get_db),
):
    # Verify persona exists
    query = select(ArtisanPersona).where(ArtisanPersona.id == str(request.persona_id))
    result = await db.execute(query)
    persona = result.scalar_one_or_none()
    if not persona:
        raise HTTPException(status_code=404, detail="Artisan persona not found")

    # Use RAG-lite service with Ollama client
    ollama_client = ollama.AsyncClient(host=settings.OLLAMA_HOST)
    rag = HeritageRAGLite(db, ollama_client)
    response = await rag.ask(request.question, request.persona_id, request.lang)
    return response
