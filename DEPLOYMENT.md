# Deployment Guide - VietHeritage

## Migration to OpenRouter Complete

The backend has been migrated from local Ollama to OpenRouter cloud LLM for production deployment.

### Changes Made:
1. **config.py** - Updated `OPENROUTER_MODEL` to `meta-llama/llama-3.2-3b-instruct:free`
2. **embedding_service.py** - Now uses OpenRouter for embeddings (removed Ollama)
3. **rag_lite.py** - Uses OpenRouter as primary LLM provider
4. **small_talk.py** - Uses OpenRouter for small talk (with rule-based fallback)
5. **artisan.py** - Updated to use OpenRouterService
6. **chat.py** - Made small_talk respond async
7. **monitoring.py** - Updated to check OpenRouter instead of Ollama
8. **Dockerfile.prod** - Removed Ollama, simplified for Render
9. **render.yaml** - Removed Ollama/MinIO dependencies, added OPENROUTER_API_KEY
10. **pyproject.toml / requirements.txt** - Removed `ollama` dependency
11. **start.sh** - Removed Ollama startup

---

## 🚀 Deploy to Production

### Step 1: Get OpenRouter API Key
1. Go to [openrouter.ai](https://openrouter.ai)
2. Sign up and get $1 credit (enough for free LLM usage)
3. Copy your API key

### Step 2: Deploy Backend to Render

```bash
# Push to GitHub
git add .
git commit -m "feat: migrate to OpenRouter for cloud deployment"
git push origin main
```

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Create New → Web Service
3. Connect your GitHub repo
4. Set environment variables:
   - `OPENROUTER_API_KEY` = your-api-key
   - `DATABASE_URL` = (auto-set by Render Postgres)
   - `IS_PRODUCTION` = true
5. Deploy!

### Step 3: Deploy Frontend to Netlify

```bash
# In frontend directory
npm run build
# Drag dist/ to Netlify dashboard or connect repo
```

1. Go to [Netlify](https://app.netlify.com)
2. Link your GitHub repo
3. Set build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. Add environment variable:
   - `VITE_API_URL` = https://vietheritage-api.onrender.com

### Step 4: Update CORS (if needed)

In Render dashboard, update `CORS_ORIGINS` to include your Netlify URL.

---

## 📡 Alternative: Cloudflare Tunnel (Development)

If you want to keep local dev and just expose it:

```bash
# Install cloudflared
# Run:
cloudflared tunnel --url http://localhost:8000
# Then update frontend vite.config.ts with the tunnel URL
```

---

## 🔧 Testing Locally

```bash
# Create .env from .env.example
cp backend/.env.example backend/.env

# Edit backend/.env with your OpenRouter API key
# Run locally:
uv run uvicorn app.main:app --reload
```

---

## Architecture Changes

### Before (Local Only):
```
[Frontend] → [FastAPI + Ollama + Phi-3.5 + MinIO + Postgres]
```

### After (Cloud Ready):
```
[Frontend on Netlify] → [FastAPI on Render + OpenRouter API + SQLite]