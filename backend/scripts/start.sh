#!/bin/bash
set -e

echo "Starting VietHeritage Map Backend..."

# Start Ollama in background
echo "Starting Ollama..."
ollama serve &
OLLAMA_PID=$!

# Wait for Ollama to be ready
echo "Waiting for Ollama to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "Ollama is ready"
        break
    fi
    sleep 1
done

# Verify models are available
echo "Verifying models..."
ollama list

# Run database migrations if needed
echo "Running database initialization..."
python -c "
from app.core.database import init_db
import asyncio
asyncio.run(init_db())
" || echo "Database init skipped (may already exist)"

# Start FastAPI application
echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1