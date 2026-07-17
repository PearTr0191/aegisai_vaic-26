"""Monitoring and error tracking with Sentry"""
import asyncio
from app.core.config import settings


def init_sentry() -> None:
    """Initialize Sentry SDK if DSN is configured (optional dependency)."""
    try:
        import sentry_sdk
        from sentry_sdk.integrations.fastapi import FastApiIntegration
        from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
        from sentry_sdk.integrations.asyncio import AsyncioIntegration
    except ImportError:
        return

    if not settings.SENTRY_DSN:
        return

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[
            FastApiIntegration(auto_enabling=True),
            SqlalchemyIntegration(),
            AsyncioIntegration(),
        ],
        traces_sample_rate=settings.SENTRY_TRACES_SAMPLE_RATE,
        environment="production" if settings.IS_PRODUCTION else "development",
        release=settings.APP_VERSION,
        before_send=lambda event, hint: None if _is_health_check(event) else event,
    )


def _is_health_check(event) -> bool:
    if "request" in event and "url" in event["request"]:
        return "/health" in event["request"]["url"]
    return False


class ModelHealthChecker:
    """Health checks for ML models and external services"""

    @staticmethod
    async def check_ollama() -> dict:
        import httpx
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(f"{settings.OLLAMA_HOST}/api/tags")
                if resp.status_code == 200:
                    models = resp.json().get("models", [])
                    return {"status": "healthy", "models": len(models)}
                return {"status": "unhealthy", "error": f"HTTP {resp.status_code}"}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

    @staticmethod
    async def check_database() -> dict:
        from app.core.database import engine
        from sqlalchemy import text
        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            return {"status": "healthy"}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

    @staticmethod
    async def check_onnx_model() -> dict:
        import os
        path = settings.ETHNOMUSIC_MODEL_PATH
        if os.path.exists(path):
            size = os.path.getsize(path) / (1024 * 1024)
            return {"status": "healthy", "model_path": path, "size_mb": round(size, 2)}
        return {"status": "missing", "model_path": path}

    @staticmethod
    async def check_all() -> dict:
        ollama, db, onnx = await asyncio.gather(
            ModelHealthChecker.check_ollama(),
            ModelHealthChecker.check_database(),
            ModelHealthChecker.check_onnx_model(),
        )
        all_healthy = all(c["status"] == "healthy" for c in [ollama, db, onnx])
        return {
            "status": "healthy" if all_healthy else "degraded",
            "checks": {"ollama": ollama, "database": db, "onnx_model": onnx},
        }