from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.audio import AudioAnalysisResponse
from app.services.audio_analysis import EthnoMusicAnalyzer
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/audio", tags=["audio"])


@router.post("/analyze", response_model=AudioAnalysisResponse)
async def analyze_audio(
    file: UploadFile = File(...),
):
    """
    Analyze Vietnamese traditional music audio.
    Returns genre, instruments, techniques (ornaments), confidence, and waveform.
    """
    if file.content_type not in ["audio/wav", "audio/mpeg", "audio/mp4", "audio/m4a", "audio/x-m4a"]:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}",
        )

    audio_bytes = await file.read()
    if len(audio_bytes) > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large (max 10MB)")

    if len(audio_bytes) < 1000:
        raise HTTPException(status_code=400, detail="File too small or empty")

    try:
        analyzer = EthnoMusicAnalyzer(settings.ETHNOMUSIC_MODEL_PATH)
        return await analyzer.analyze(audio_bytes, file.filename or "unknown")
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail=f"EthnoMusic model not found at {settings.ETHNOMUSIC_MODEL_PATH}. Contact administrator.",
        )
    except Exception as e:
        logger.exception(f"Audio analysis failed: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
