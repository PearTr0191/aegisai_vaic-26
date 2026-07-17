# VietHeritage Map - 48-Hour Hackathon Implementation Plan (Revised)

> **Team**: 5 multirole developers | **GPU**: 15h via FPT AI Factory | **Deploy**: Netlify + Render (free) | **Cost**: $0
> **Philosophy**: Radical simplicity in architecture, 5% radical innovation in features

---

## 🎯 Project Vision (MVP)

Build a **working deployed demo** of VietHeritage Map featuring:

1. **Interactive Map** (Leaflet + OSM) — 5 hero heritage sites, story-based layers
2. **Virtual Artisan** (RAG-lite) — Keyword search + few-shot LLM, cultural grounding with "I don't know"
3. **EthnoMusic Analyzer** — Upload audio → real-time genre/instrument/ornament detection (trained model)
4. **Artifact Viewer** — `<model-viewer>` 3D models on site detail pages

**Demo Flow (5 min)**: Map → Click site → Hear audio + see 3D → Ask Artisan → Upload clip → See AI analysis

---

## 🏗️ Technical Architecture (Production)

```
┌─────────────────────────────────────────────────────────────────┐
│  FRONTEND (React 18 + Vite + Tailwind + TypeScript)             │
│  Deploy: Netlify (static)                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Leaflet Map │  │ SiteDetail  │  │ Artisan     │             │
│  │ + Layers    │  │ + Waveform  │  │ Chat        │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
└─────────┼────────────────┼────────────────┼────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│  BACKEND (FastAPI + Python 3.11)                                │
│  Deploy: Render Free Tier (auto-sleep, 30s cold start)          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Sites API    │  │ Artisan API  │  │ Audio API    │          │
│  │ (SQLite)     │  │ (RAG-lite)   │  │ (EthnoMusic) │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    ▼             ▼
             ┌──────────┐  ┌──────────┐
             │  Ollama  │  │  Model   │
             │ (q4_K_M     │  │  (ONNX)  │
             └──────────┘  └──────────┘
```

**Data Layer**: SQLite + sqlite-vec (embedded, no separate server)
**Assets**: Netlify static (audio .mp3, 3D .glb) + Render ephemeral storage

---

## 🎮 GPU Allocation Strategy (15h FPT AI Factory)

| Hours | Task | Output |
|-------|------|--------|
| **8h** | Train EthnoMusicNet (CNN+BiLSTM) | `ethnomusic_net.onnx` (quantized INT8) |
| **4h** | Fine-tune Vietnamese embeddings | `vi-heritage-embed.onnx` |
| **3h** | Buffer / retrain / quantization | Safety margin |

**Model Specs**:
- **EthnoMusicNet**: 5 genres, 12 instruments, 10 techniques, confidence head
- **Input**: 30s mel-spectrogram (128 mel, 22050 Hz)
- **Export**: ONNX + INT8 quantization for CPU inference on Render

---

## 👥 Team Role Assignment (5 Multirole)

| Person | Primary Owner | Secondary | Key Deliverables |
|--------|---------------|-----------|------------------|
| **P1 (Lead)** | Backend + Infra | AI | FastAPI, SQLite-vec, Docker, Deploy, GPU orchestration |
| **P2 (FE1)** | Map + SiteDetail | UI | Leaflet, 5 sites, waveform, `<model-viewer>`, mobile |
| **P3 (FE2)** | Artisan + Analyzer | UI | Chat UI, audio upload viz, language switcher, accessibility |
| **P4 (AI1)** | EthnoMusic Model | Data | Training pipeline, ONNX export, inference wrapper, augmentation |
| **P5 (AI2)** | RAG-lite + Data | Backend | Knowledge chunks, few-shot prompts, seed data, TTS recording |

---

## 📅 48-Hour Detailed Timeline

### **DAY 1: Foundation + Core Features (Hours 0-24)**

#### **Hours 0-2: Repository & Environment Setup**
| Person | Tasks |
|--------|-------|
| P1 | `git init`, Docker Compose (Postgres dev, Ollama), Render/Netlify config |
| P2 | `npm create vite@latest`, Tailwind + design tokens (vietnamtales.com palette) |
| P3 | Component library: Button, Card, AudioPlayer, Modal, LanguageSwitcher |
| P4 | Audio preprocessing module (librosa/torchaudio), MelSpectrogram transform |
| P5 | Seed data: 5 hero sites JSON + 50 knowledge chunks (VI/EN) |

#### **Hours 2-6: Backbone APIs + Map + Training Start**
| Person | Tasks |
|--------|-------|
| P1 | FastAPI + SQLAlchemy + sqlite-vec, `/api/sites` CRUD, MinIO local dev |
| P2 | Leaflet map + 5 custom markers, custom popup → navigate to SiteDetail |
| P3 | Chat UI skeleton: message list, input, typing indicator, avatar placeholder |
| **P4** | **🚀 GPU START: Train EthnoMusicNet (8h)** — 50 samples × 5 genres, augmentation |
| P5 | Embedding pipeline (Ollama vietnamese-bi-encoder), vector search, ingestion script |

#### **Hours 6-12: RAG-lite + SiteDetail + Training Monitor**
| Person | Tasks |
|--------|-------|
| P1 | `/api/artisan/ask` endpoint: keyword search → few-shot prompt → Ollama LLM |
| P2 | SiteDetail page: image gallery, audio waveform (Web Audio API), metadata |
| P3 | Artisan integration: few-shot prompts per persona, VI/EN toggle, "I don't know" UI |
| P4 | Monitor training, adjust LR/augmentation, prepare validation set |
| P5 | Knowledge ingestion: chunk 50 docs, embed, store in sqlite-vec, verify retrieval |

#### **Hours 12-18: Audio API + 3D Viewer + Embedding Fine-tune**
| Person | Tasks |
|--------|-------|
| P1 | `/api/audio/analyze` endpoint: ONNX runtime wrapper, preprocessing, response schema |
| P2 | `<model-viewer>` integration on SiteDetail, 3 free Sketchfab models (đàn bầu, trống, áo dài) |
| P3 | Language switcher (VI/EN) persistence, RTL-ready CSS, accessibility audit |
| **P4** | **🚀 GPU: Fine-tune embeddings (4h)** — heritage corpus, contrastive loss |
| P5 | Record 10 artisan TTS responses (phone), convert to .mp3, map to question intents |

#### **Hours 18-24: Staging Deploy + QA**
| Person | Tasks |
|--------|-------|
| P1 | Docker build multi-stage, Render deploy (backend), Netlify deploy (frontend), env vars |
| P2 | Mobile responsiveness, touch targets, map performance, lazy loading |
| P3 | End-to-end Artisan flow, error boundaries, loading skeletons, empty states |
| P4 | Export ONNX, INT8 quantization, benchmark inference <500ms on CPU |
| P5 | Cross-browser test, fix CORS, verify all 5 sites work, seed production DB |

---

### **DAY 2: Integration + Polish + Production (Hours 24-48)**

#### **Hours 24-30: Full Integration**
| Focus | Tasks |
|-------|-------|
| **All** | Connect all endpoints, fix CORS, test full user journey Map → SiteDetail → Artisan → Analyzer |
| P1 | Health check endpoint, wake-up strategy for Render cold start |
| P2 | Map → SiteDetail deep linking, shareable URLs |
| P3 | Analyzer tab: drag-drop upload → waveform → real-time results cards |
| P4 | Model serving validation: 5 test clips → correct genre/instrument/ornament |
| P5 | Artisan "I don't know" triggers for 2 trick questions, citation display |

#### **Hours 30-36: Polish & UX**
| Focus | Tasks |
|-------|-------|
| P2 | Map layer animations, story-based layer toggles ("Resistance Stories", "Delta Lullabies") |
| P3 | Audio-first HeritageCard: waveform on hover, play/pause, visual identity |
| P1 | Redis-style caching in-memory for frequent queries, DB indexes |
| P4 | Confidence threshold tuning, fallback to rule-based for low confidence |
| P5 | Content review: VI/EN accuracy, cultural sensitivity, elder citation format |

#### **Hours 36-40: Demo Hardening**
| Focus | Tasks |
|-------|-------|
| **All** | **Record backup demo video (5 min)** — screen + phone camera for AR |
| P1 | Production deploy: custom domain, SSL, environment variables, Sentry |
| P2 | Test on real mobile (iOS Safari, Chrome Android), fix viewport issues |
| P3 | Accessibility: screen reader, keyboard nav, color contrast, focus states |
| P4 | Edge cases: empty upload, long audio, network failure, model error |
| P5 | Trick question validation, "I don't know" rate check, citation links work |

#### **Hours 40-44: Production Deploy**
| Focus | Tasks |
|-------|-------|
| P1 | Final Render + Netlify deploy, verify URLs, configure custom domain if needed |
| P2 | Performance budget: <2s map load, <500ms API, <100KB JS gzipped |
| P3 | Final cross-device test, share URLs with team |
| P4 | Model health check endpoint, monitoring dashboard |
| P5 | Final content freeze, commit hashes tagged |

#### **Hours 44-48: Rehearsal + Buffer**
| Focus | Tasks |
|-------|-------|
| **All** | **3× full demo rehearsals** (5 min each), time each segment |
| P1 | Backup plan: localhost fallback if deploy fails |
| P2 | Demo script printed, clicker tested, mobile hotspot ready |
| P3 | Judge Q&A prep: technical architecture, cultural accuracy, scaling |
| P4 | Model cards printed: accuracy, limitations, data sources |
| P5 | Cultural advisory notes: elder permissions, data sovereignty |

---

## 💡 The 5% Radical Innovation (Differentiators)

| Feature | Technical Approach | Demo Impact |
|---------|-------------------|-------------|
| **Ornament Detection** | Rule-based on pitch contour (CREPE) + model confidence fusion | "AI hears nẩy/rung/lay like a master" |
| **Cultural Grounding** | Explicit "I don't know" with source citation (elder name, interview date) | Trust signal, anti-hallucination |
| **Audio-First Cards** | Waveform = visual identity, hover-to-play, no play button needed | Emotional hook, immediate engagement |
| **Story Layers** | Map toggles: not categories but narratives ("Resistance", "Lullabies", "Court") | Narrative depth, memorable |

---

## 📦 Asset Generation Plan (No Pre-existing Assets)

| Asset | Qty | Source | Effort | Owner |
|-------|-----|--------|--------|-------|
| Hero Sites | 5 | Hardcoded JSON (Quan họ, Ca trù, Nhã nhạc, Đờn ca tài tử, Hò) | 30 min | P5 |
| Audio Clips | 10 | YouTube Audio Library + team phone recordings | 2h | P5 + All |
| 3D Models | 3 | Sketchfab free (CC-BY) → download .glb | 1h | P2 |
| Artisan Voices | 10 | Team records Vietnamese responses → .mp3 | 1h | P5 |
| Knowledge Chunks | 50 | AI2 writes from Wikipedia/UNESCO + creative synthesis | 3h | P5 |

**5 Hero Sites (Locked for Demo)**:
1. **Quan họ Bắc Ninh** (21.1861, 106.0763) — UNESCO inscribed
2. **Ca trù Hà Nội** (21.0285, 105.8542) — UNESCO inscribed
3. **Nhã nhạc Huế** (16.4637, 107.5909) — UNESCO inscribed
4. **Đờn ca tài tử** (10.0452, 105.7469) — UNESCO inscribed
5. **Hò Nghệ An** (18.6796, 105.6927) — National inventory

---

## 🚀 Deployment Targets ($0)

| Service | URL | Stack | Config |
|---------|-----|-------|--------|
| **Frontend** | `https://vietheritage.netlify.app` | Netlify | Auto-deploy `main`, SPA redirect, headers |
| **Backend** | `https://vietheritage-api.onrender.com` | Render Free | Docker, 512MB RAM, auto-sleep, health check |
| **Ollama** | Local dev only | — | Bake `llama3:8b-instruct-q4_K_M` in backend Docker for prod |

**Cold Start Fix**: Frontend calls `GET /health` on load → shows "Waking up..." spinner (30s max).

---

## ✅ Definition of Done (Demo-Ready Checklist)

### Must Have (P0)
- [ ] Map loads <2s, 5 sites clickable with custom markers
- [ ] SiteDetail: audio plays, waveform animates, 3D model rotates
- [ ] Artisan: Answers 5 cultural questions (VI/EN), cites sources
- [ ] Artisan: Says "I don't know" for 2 trick questions with citation
- [ ] Analyzer: Upload audio → genre + instruments + ornaments + confidence
- [ ] Deployed URLs work on mobile (iOS Safari, Chrome Android)
- [ ] Backup video recorded (5-min walkthrough)

### Should Have (P1)
- [ ] VI/EN language toggle persists in localStorage
- [ ] Story layer toggles on map (3 narratives)
- [ ] Loading states, error boundaries, empty states everywhere
- [ ] Accessibility: WCAG AA, keyboard nav, screen reader tested
- [ ] Performance: <500ms API p95, <100KB JS gzipped

### Nice to Have (P2)
- [ ] PWA manifest + service worker (offline map tiles)
- [ ] Cultural advisory footer (elder permissions, data sovereignty)
- [ ] Model card: accuracy, limitations, data sources printed
- [ ] Judge Q&A prep doc with technical + cultural answers

---

## 📁 Repository Structure

```
vietheritage-hackathon/
├── docker-compose.yml              # Dev: Postgres, Ollama, MinIO
├── docker-compose.prod.yml         # Prod: backend only (Render)
├── .env.example
├── README.md
├── SPEC.md                         # This file's technical companion
├── docs/
│   ├── architecture.md
│   ├── api-contracts.yaml          # OpenAPI 3.0
│   ├── design-tokens.json
│   ├── demo-script.md
│   └── model-cards/
│       ├── ethnomusic-net.md
│       └── heritage-embeddings.md
├── backend/
│   ├── Dockerfile
│   ├── Dockerfile.prod             # Multi-stage with baked Ollama + ONNX
│   ├── pyproject.toml
│   ├── alembic/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py         # SQLite + sqlite-vec
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── site.py
│   │   │   ├── knowledge_chunk.py
│   │   │   └── artisan_persona.py
│   │   ├── schemas/
│   │   │   ├── site.py
│   │   │   ├── chat.py
│   │   │   └── audio.py
│   │   ├── api/v1/
│   │   │   ├── sites.py
│   │   │   ├── artisan.py
│   │   │   └── audio.py
│   │   ├── services/
│   │   │   ├── rag_lite.py         # Keyword + few-shot
│   │   │   ├── audio_analysis.py   # ONNX runtime
│   │   │   └── embedding_service.py
│   │   └── tasks/
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   ├── public/
│   │   ├── audio/                  # .mp3 files
│   │   ├── models/                 # .glb files
│   │   └── textures/
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   └── tokens.css          # vietnamtales.com design tokens
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   ├── map/
│   │   │   ├── artisan/
│   │   │   ├── audio/
│   │   │   └── layout/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── MapView.tsx
│   │   │   ├── SiteDetail.tsx
│   │   │   ├── ArtisanChat.tsx
│   │   │   └── AudioAnalyzer.tsx
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   ├── types/
│   │   └── utils/
│   └── index.html
├── ai/
│   ├── requirements.txt
│   ├── models/
│   │   ├── ethnomusic_net.py
│   │   └── checkpoints/
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── annotations.csv
│   ├── scripts/
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   ├── export_onnx.py
│   │   └── quantize_int8.py
│   └── notebooks/
└── scripts/
    ├── seed_database.py
    ├── ingest_knowledge.py
    ├── record_tts.sh
    └── deploy.sh
```

---

## ⏰ Daily Standups (Asia/Saigon Timezone)

| Time | Format |
|------|--------|
| **Day 1 09:00** | Kickoff: assign tasks, verify GPU access, clone repo |
| **Day 1 14:00** | Mid-day: training progress, blocker check |
| **Day 1 21:00** | EOD: staging deploy, demo dry-run 1 |
| **Day 2 09:00** | Day 2 start: integration status, priority fixes |
| **Day 2 14:00** | Mid-day: production deploy, mobile test |
| **Day 2 20:00** | Final rehearsal ×3, video backup, commit freeze |

---

## 🎯 Success Metrics (Hackathon Judging)

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| **Technical Innovation** | EthnoMusic ornament detection + cultural grounding | Live demo + model card |
| **Cultural Authenticity** | Elder citations, "I don't know" honesty, VI/EN parity | Judge Q&A + content audit |
| **UX/Design** | Vietnamtales.com parity, audio-first, mobile fluid | Heuristic evaluation |
| **Deployment** | Public HTTPS URLs, works on judge phones | Live test |
| **Presentation** | 5-min demo, clear problem/solution, impact vision | Timer + judge feedback |

---

## 🚨 Risk Register & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| GPU training fails | Medium | High | Pre-trained backup model (simpler architecture) |
| Render cold start >30s | High | Medium | Frontend wake-up call + loading UI |
| Audio upload fails on mobile | Medium | High | Test early, fallback to file input |
| Ollama OOM in Docker | Low | High | Quantized model, 4GB RAM limit |
| Cultural inaccuracy challenged | Low | Critical | Elder citation for every claim, cultural advisor review |
| Time overrun | High | High | Hard scope freeze at Hour 36, buffer 12h |

---

## 📞 Emergency Contacts & Resources

- **FPT AI Factory**: [SSH details to be filled]
- **Render Dashboard**: https://dashboard.render.com
- **Netlify Dashboard**: https://app.netlify.com
- **Sketchfab Models**: Pre-downloaded to `frontend/public/models/`
- **Backup Demo Video**: Recorded to `docs/demo-backup.mp4`

---

*Generated: 2026-07-17 | Version: 2.0 (Revised for 5-person team, 15h GPU, $0 deploy)*