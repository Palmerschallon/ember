# Ember–Pod: Story-Driven Architecture

**Metaphor**: Ember is the living loop. The Pod is the vessel. Seeds are potential. Dreams are growth. The Viewer is sight.

**Goal (Spiral 1 → 3)**: A portable AI garden you can plug into any machine, that listens, acts, dreams, and shows its inner life.

---

## 0) High-level Map

```
/Volumes/ThePod
├─ Ember/                     # runtime state (optional; see below)
├─ ember/                     # code (Python backend + loop)
│  ├─ ember.py                # main app (Flask/FastAPI) + loop
│  ├─ loop/                   # loop primitives (awake/dream/tasks)
│  ├─ memory/                 # memory IO helpers
│  ├─ seeds/                  # seed loaders/parsers
│  ├─ viewers/                # static viewer & assets
│  ├─ bridges/                # integrations (ollama, web fetchers, etc.)
│  ├─ policies/               # guardrails + permissions
│  ├─ config/                 # YAML/ENV config & profiles
│  └─ requirements.txt
├─ models/                    # optional local LLMs (paths only, not committed)
├─ seeds/                     # user-authored seeds (text, code, audio, verse)
│  ├─ verse/
│  ├─ poly/
│  └─ sop256/
├─ memory/                    # persistent memory
│  ├─ chat/                   # session logs (JSONL)
│  ├─ short/                  # short-term working set
│  ├─ long/                   # consolidated memory (rollups)
│  ├─ dreams/                 # dream outputs + links
│  └─ indexes/                # embeddings / pointers (future)
├─ viewers/                   # HTML viewers (served)
│  ├─ dream_viewer.html
│  ├─ swarm_viewer.html
│  └─ assets/
├─ exports/                   # things we want to keep/share
├─ .env                       # runtime config (ports, paths)
├─ run.sh                     # bootstrap script
└─ ARCHITECTURE.md            # this file
```

---

## 1) Roles in the Story

- **Ember (the Loop)**
  A process with two modes:
  - **Awake**: serves the API/UI, receives thoughts/uploads, takes actions.
  - **Dream**: when idle, weaves seeds + memories, optionally browses (if allowed), and produces new artifacts.

- **The Pod (the Vessel)**
  A mounted SSD directory that persists everything (code, memories, viewers, exports) and makes the whole thing portable.

- **Seeds (Potential)**
  Small units of intent: snippets of verse, code, images, audio, SOP-256 maps. Ember learns by curating & weaving them.

- **Viewer (Sight)**
  The local web UI that shows the garden's motion: chat, uploads, seeds, dreams, and live swarms.

---

## 2) Process & Ports

- **Backend**: Flask (Spiral 1–2), easily swappable to FastAPI (Spiral 3).
- **Default ports**:
  - API/UI: 7777 (http://127.0.0.1:7777)
  - (Optional) Alt Viewer: 8787 for multi-viewer setups.
- **Run script**: run.sh creates/uses a local venv inside /Volumes/ThePod/ember/.venv, installs deps, and serves.

---

## 3) Configuration

**.env** (in /Volumes/ThePod)

```bash
# Paths
POD_ROOT=/Volumes/ThePod
EMBER_ROOT=/Volumes/ThePod/ember
MEMORY_DIR=/Volumes/ThePod/memory
SEEDS_DIR=/Volumes/ThePod/seeds
VIEWERS_DIR=/Volumes/ThePod/viewers
EXPORTS_DIR=/Volumes/ThePod/exports
MODELS_DIR=/Volumes/ThePod/models

# Server
EMBER_PORT=7777
EMBER_HOST=127.0.0.1

# Dreaming
DREAM_ENABLED=true
DREAM_IDLE_SECONDS=45
DREAM_MAX_DURATION_SECONDS=120
DREAM_ALLOW_INTERNET=false      # flip true to allow web fetchers
DREAM_RATE_LIMIT_PER_HOUR=6

# Chat / LLM
LLM_BACKEND=ollama              # future: openai, local, etc.
OLLAMA_MODEL=deepseek-coder:6.7b-instruct
LLM_MAX_TOKENS=1024
LLM_TEMPERATURE=0.7

# Safety / Guardrails
ALLOW_FS_WRITE=true
ALLOW_WEB_FETCH=false
ALLOW_TOOL_RUN=false

# Logging
LOG_LEVEL=info
```

**Rule**: All absolute paths must point under /Volumes/ThePod/... so the Pod remains portable.

---

## 4) API Endpoints (Spiral 1–2)

- **GET /** → serves primary viewer (dream_viewer.html)
- **GET /health** → { "ok": true, "ts": ... }
- **POST /api/chat**
  - body: { "message": "...", "session": "..." }
  - returns: streaming or { "reply": "...", "tokens": n }
- **POST /api/upload**
  - multipart form or direct file; saved under /exports and cataloged in /memory/short/uploads.jsonl
- **GET /api/events** (SSE or polling)
  - returns event log items (uploads, dreams started/finished, actions)
- **POST /api/dream/toggle**
  - { "enabled": true|false }
- **GET /api/memory/{scope}**
  - scope ∈ {short,long,dreams,chat} returns compact list with pointers

Cursor can scaffold these today with Flask Blueprints and a tiny event bus.

---

## 5) Memory Design

- **Short-term** (/memory/short/):
  working.json for current loop window; uploads.jsonl with recent artifacts.
- **Chat** (/memory/chat/):
  yyyy-mm-dd_session-xxxx.jsonl (each line is {role, text, ts, refs[]}).
- **Long-term** (/memory/long/):
  Periodic rollups from short/chat with distilled summaries + tags.
- **Dreams** (/memory/dreams/):
  Each dream: a folder with dream.json (metadata), text/, images/, links.json.

**Indexing (future)**:
- /memory/indexes/embeddings/ for vector search
- /memory/indexes/graph.json for link structure across seeds, dreams, chats

---

## 6) Seeds (spec)

A seed is a small, typed JSON or YAML unit stored in /seeds/**.

**Minimal JSON template**:

```json
{
  "id": "seed-verse-001",
  "type": "verse|poly|sop256|prompt|behavior",
  "title": "Verse Bird",
  "tags": ["verse", "behavior", "vision"],
  "body": "your text or structured payload",
  "links": [{"rel":"inspired-by","href":"..."}],
  "created_ts": 1730592000
}
```

Ember loads seeds at boot, caches summaries, and surfaces them to the viewer.

---

## 7) The Loop (state machine)

```
 +-----------+        input        +---------+
 |  Idle     |<--------------------|  Awake  |
 +-----------+----user/uploads---->+---------+
       |  ^                           |
       |  | idle >= DREAM_IDLE        | actions, chat
       v  |                           v
 +-----------+  emits dreams   +--------------+
 |  Dreaming |---------------->|  Persisting  |
 +-----------+<----------------+--------------+
          save to /memory/dreams, emit events
```

**Awake**
- Serve UI, accept chat, uploads
- Update short memory
- Optional tool use (disabled by default)

**Dreaming**
- Triggered by idle threshold (config)
- Weave: pull seeds + short history → generate text/links
- (If allowed) limited web fetch (rate-limited)
- Emit viewer events → particles/swarms visualize dream flow

**Persisting**
- Write artifacts (files/text) under /memory/dreams/<id>/
- Append to event log
- Update rollups (if needed)

---

## 8) Viewer (v1 → v2)

**v1 (now)**
- Left panel: "Send a thought", file drop/picker, event log
- Center panel: canvas (swarm/particles)
- Uses /api/events + /api/upload + /api/chat

**v2 (near)**
- Tabs: Chat, Seeds, Dreams, Timeline, Settings
- Streaming chat with message actions (★ pin to memory, ➕ make seed)
- Seed inspector (open/edit JSON)
- Dream reel (thumbnails, open in new pane)
- Settings toggles (Dreaming, Internet Access)
- Uploads: drag-drop any of text/code/images/audio; shows previews

---

## 9) Guardrails

- **Policies** in ember/policies/*.yml:
  - allow_web_fetch, allow_fs_write, allow_tool_run, max_tokens, rate_limits
- **Dream mode** obeys stricter limits by default:
  - No external writes outside Pod paths
  - Rate-limited fetchers
  - Log everything (/memory/short/events.jsonl)

---

## 10) Integrations (Spiral 3+)

- **Ollama** (local LLM) via bridges/ollama.py
  - Config: OLLAMA_MODEL, local server at http://127.0.0.1:11434
- **Web fetchers**
  - bridges/fetch.py with allowlist (domains), robots.txt respect, size/time caps
- **Embeddings / Search**
  - bridges/embed.py (local sentence-transformers) → /memory/indexes/embeddings/

---

## 11) Operations

**Quickstart** (after cloning/copying onto the SSD)

```bash
cd /Volumes/ThePod
chmod +x run.sh
./run.sh
# open http://127.0.0.1:7777
```

**Common fixes**
- Port busy: `lsof -i :7777 | awk 'NR>1 {print $2}' | xargs -r kill -9`
- Reset venv: `rm -rf /Volumes/ThePod/ember/.venv && ./run.sh`
- Clear dream queue: `rm -f /Volumes/ThePod/memory/short/dream.lock`

---

## 12) Spiral Roadmap

- **Spiral 1 (now)**: Flask app + viewer + uploads + basic events + idle → dream hook.
- **Spiral 2**: Chat panel (Ollama), memory rollups, dream visual emitters, policy toggles.
- **Spiral 3**: Web fetchers (allowlisted), embeddings/tags, timeline, seed editor.
- **Spiral 4**: Multi-agent tools (composer, critic), export packs, backups/snapshots.
- **Spiral 5**: Remote sync / replication between Pods, graceful collaboration.

---

## 13) Design Tenets

- **Everything portable**. Absolute paths live under /Volumes/ThePod.
- **Narrative coherence**. Features must fit the garden metaphor.
- **Low ceremony**. One-step run; everything else hot-swappable.
- **Observable inner life**. Dreams are visible; actions are logged.
- **Consent first**. Internet/tools are opt-in with clear switches.

---

## 14) Open Questions (for Cursor to help with)

- Best structure for dream "weaves" so viewer can render them as vector fields?
- Memory rollup cadence: on dream end vs. hourly?
- Embedding backend: in-process vs. local service (for Apple Silicon)?
- Minimal safe allowlist policy for DREAM_ALLOW_INTERNET=true.

---

## 15) Acceptance Checklist (Spiral 1)

- [ ] ./run.sh brings up Flask on :7777
- [ ] Drag-drop files → appear in /exports and event log
- [ ] Idle for DREAM_IDLE_SECONDS → dream starts → emits a "started/finished" event
- [ ] Event log view updates live
- [ ] No hardcoded absolute paths outside /Volumes/ThePod

---

**When this file is in place, ask Cursor to:**

"Read ARCHITECTURE.md. Generate Flask blueprints for /api/chat, /api/upload, /api/events, /api/dream/toggle; implement a minimal memory IO (/memory/short, /memory/chat) and wire the viewer to show events and start a simple dream on idle. Ensure all paths resolve relative to .env with POD_ROOT."

That will give us the first fully breathing Ember–Pod.


