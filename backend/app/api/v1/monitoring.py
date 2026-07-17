from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.cache import cache
from app.core.config import settings
import time
import platform

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.get("/health")
async def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": "production" if settings.IS_PRODUCTION else "development",
        "timestamp": time.time(),
    }


@router.get("/health/models")
async def model_health():
    """Check ONNX model and Ollama availability"""
    import os
    import httpx
    
    model_path = settings.ETHNOMUSIC_MODEL_PATH
    model_exists = os.path.exists(model_path)
    model_size = os.path.getsize(model_path) if model_exists else 0
    
    # Check Ollama
    ollama_status = "unknown"
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{settings.OLLAMA_HOST}/api/tags")
            if resp.status_code == 200:
                models = resp.json().get("models", [])
                phi_available = any("phi" in m.get("name", "") for m in models)
                nomic_available = any("nomic" in m.get("name", "") for m in models)
                ollama_status = "healthy" if phi_available and nomic_available else "degraded"
            else:
                ollama_status = "unhealthy"
    except Exception:
        ollama_status = "unreachable"
    
    return {
        "ethnomusic_model": {
            "path": model_path,
            "exists": model_exists,
            "size_mb": round(model_size / 1024 / 1024, 2) if model_exists else 0,
            "status": "ready" if model_exists else "missing",
        },
        "ollama": {
            "host": settings.OLLAMA_HOST,
            "status": ollama_status,
            "models": [settings.OLLAMA_MODEL, settings.OLLAMA_EMBED_MODEL],
        },
    }


@router.get("/health/db")
async def db_health(db: AsyncSession = Depends(get_db)):
    """Check database connectivity"""
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}


@router.get("/cache/stats")
async def cache_stats():
    """Cache statistics"""
    return cache.stats()


@router.post("/cache/clear")
async def clear_cache():
    """Clear all cache"""
    cache.clear()
    return {"status": "cleared"}


@router.get("/system")
async def system_info():
    """System information for debugging"""
    return {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
    }


@router.get("/metrics")
async def metrics():
    """Basic metrics endpoint (Prometheus-compatible format)"""
    cache_stats = cache.stats()
    
    return f"""# HELP cache_size Current cache size
# TYPE cache_size gauge
cache_size {cache_stats["size"]}

# HELP cache_valid_entries Valid cache entries
# TYPE cache_valid_entries gauge
cache_valid_entries {cache_stats["valid_entries"]}

# HELP cache_expired_entries Expired cache entries
# TYPE cache_expired_entries gauge
cache_expired_entries {cache_stats["expired_entries"]}

# HELP app_info Application info
# TYPE app_info gauge
app_info{{version="{settings.APP_VERSION}",environment="{'production' if settings.IS_PRODUCTION else 'development'}"}} 1
"""