# Production Dockerfile - VietHeritage Chatbot on Render
# Uses OpenRouter for LLM inference, serves Project frontend

# === Backend Build Stage ===
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY backend/pyproject.toml ./
COPY backend/uv.lock* ./
WORKDIR /app
RUN uv sync --frozen --no-dev

# === Production Runtime Stage ===
FROM python:3.11-slim AS runtime

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

# Copy Python dependencies from builder
COPY --from=builder /app/.venv /app/.venv

# Copy backend application code
COPY --chown=appuser:appuser backend/app /app/app

# Copy Project frontend (chatbot at root)
RUN mkdir -p /app/static
COPY --chown=appuser:appuser Project/ /app/static/

# Copy data files (already included in backend/app copy)

# Switch to non-root user
USER appuser

# Set PATH
ENV PATH="/app/.venv/bin:${PATH}"

# Environment variables
ENV IS_PRODUCTION=true

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]