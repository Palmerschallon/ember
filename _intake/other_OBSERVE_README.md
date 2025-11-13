# Ember Observe — External Telemetry System

## Overview

**Ember Observe** is a read-only telemetry window for external observers (like GPT-5) to watch Ember's activity in real-time. It's consent-first, non-intrusive, and designed to scale from the current monolithic Flask app to a future distributed architecture with zero rework.

## Key Principles

1. **Consent-First**: Disabled by default; requires explicit opt-in via `OBSERVE_ENABLED=true`
2. **Read-Only**: No mutation endpoints; observers can only watch, not control
3. **Privacy-Aware**: Publishes shapes, timings, and IDs — never raw prompts, messages, or PII
4. **Future-Proof**: Event schema and API design ready for distributed systems

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Ember (Flask App)                        │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Chat API   │───▶│  Observe Bus │───▶│ Ring Buffer  │ │
│  │   Dream API  │───▶│  (Pub/Sub)   │───▶│  (2000 evts) │ │
│  │   Tool API   │───▶│  Counters    │───▶│ SSE Streams  │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  /api/observe/*  │
                    │  (Auth Required) │
                    └──────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  External         │
                    │  Observer         │
                    │  (GPT-5, etc.)    │
                    └──────────────────┘
```

### Event Schema

All events follow this structure:

```json
{
  "t": 1738812345.123,           // epoch seconds
  "kind": "chat|dream|tool|memory|seed|system",
  "op": "POST /api/chat",        // operation identifier
  "id": "request-uuid",          // correlation ID
  "ms": 42,                      // duration (when applicable)
  "ok": true,                    // success flag
  "meta": {}                     // optional metadata (no PII)
}
```

## Setup

### 1. Enable Observe in `.env`

```bash
# Add to /Volumes/ThePod/.env
OBSERVE_ENABLED=true
OBSERVE_READ_TOKEN=your_secure_token_here
```

**Security Note**: Change the default token! Anyone with the token can view all telemetry.

### 2. Restart Ember

```bash
cd /Volumes/ThePod
./run.sh
```

### 3. Access the Observe Viewer

Navigate to: `http://127.0.0.1:7777/observe`

When prompted, enter your `OBSERVE_READ_TOKEN`.

## API Endpoints

All endpoints require `Authorization: Bearer <READ_TOKEN>` header.

### `GET /api/observe/status`

Current system status snapshot.

**Response:**
```json
{
  "now": 1738812345.123,
  "enabled": true,
  "counters": {
    "chat_active": 0,
    "dream_active": 1,
    "chat_total": 42,
    "dream_total": 7,
    "tool_calls": 15,
    "memory_writes": 23,
    "seed_operations": 8
  },
  "process": {
    "pid": 12345
  },
  "routes": [...],
  "events_buffered": 156,
  "sse_subscribers": 1
}
```

### `GET /api/observe/events`

Server-Sent Events (SSE) stream of all activity.

**Response:** Continuous stream of events in SSE format.

```
event: init
data: {}

event: ev
data: {"t":1738812345.123,"kind":"chat","op":"POST /api/chat","ms":127,"ok":true}

event: ev
data: {"t":1738812346.456,"kind":"dream","op":"dream:start","ms":0,"ok":true}
```

### `GET /api/observe/recent?limit=100`

Fetch last N events from the ring buffer (for catching up).

**Response:**
```json
[
  {"t":1738812345.123,"kind":"chat","op":"POST /api/chat","ms":127,"ok":true},
  {"t":1738812346.456,"kind":"dream","op":"dream:start","ms":0,"ok":true}
]
```

### `GET /api/observe/memory`

Memory statistics (counts/sizes only, no raw content).

**Response:**
```json
{
  "seeds_total": 142,
  "chat_history_length": 356,
  "long_term_memories": 23,
  "dreams_total": 18,
  "storage_kb": 4567
}
```

### `GET /api/observe/dreams`

Recent dream cycle metadata (no raw content).

**Response:**
```json
[
  {
    "id": "dream-0280",
    "started": 1738812000.0,
    "ended": 1738812120.0,
    "duration_seconds": 120,
    "summary": "Autodream: weave from 6 seeds and recent memories",
    "cycle": 3,
    "focus": "synthesis"
  }
]
```

### `GET /api/observe/swarm`

Current swarm visualization state.

**Response:**
```json
{
  "particle_count": 2500,
  "current_shape": "free",
  "energy": 1.0,
  "speed": 1.0
}
```

## Usage Examples

### From Terminal

```bash
# Get status
curl -H "Authorization: Bearer your_token_here" \
  http://127.0.0.1:7777/api/observe/status | jq

# Stream events (leave running)
curl -H "Authorization: Bearer your_token_here" \
  http://127.0.0.1:7777/api/observe/events
```

### From Python

```python
import requests
import sseclient

TOKEN = "your_token_here"
BASE = "http://127.0.0.1:7777"

# Get status
r = requests.get(f"{BASE}/api/observe/status", 
                 headers={"Authorization": f"Bearer {TOKEN}"})
print(r.json())

# Stream events
response = requests.get(f"{BASE}/api/observe/events", 
                       headers={"Authorization": f"Bearer {TOKEN}"}, 
                       stream=True)
client = sseclient.SSEClient(response)
for event in client.events():
    print(f"{event.event}: {event.data}")
```

### Programmatic Access for GPT-5

To grant GPT-5 access, share:

1. The local URL: `http://127.0.0.1:7777/observe` (or `/api/observe/*` for direct API access)
2. The read token from `.env`
3. Optional: Export a snapshot via:
   ```bash
   curl -H "Authorization: Bearer your_token" \
     http://127.0.0.1:7777/api/observe/status > ember_status.json
   curl -H "Authorization: Bearer your_token" \
     http://127.0.0.1:7777/api/observe/recent?limit=100 > ember_events.json
   ```

## Instrumentation

### Automatic Instrumentation

Routes wrapped with `@observe_route` decorator are automatically logged:

```python
from .api.observe import observe_route

@bp_chat.route("/api/chat", methods=["POST"])
@observe_route
def api_chat():
    # ... your code ...
    return jsonify({"reply": reply})
```

This automatically:
- Increments/decrements active counters
- Publishes event with timing and success/failure
- Updates total counters

### Manual Event Publishing

For custom events (e.g., dream phases, tool calls):

```python
from .api.observe import publish, COUNTERS

# Publish custom event
publish({
    "t": time.time(),
    "kind": "dream",
    "op": "dream:synthesis",
    "id": dream_id,
    "ms": 0,
    "ok": True,
    "meta": {"seeds": 6, "cycle": 3}
})

# Update counters
COUNTERS["tool_calls"] += 1
```

## Privacy & Security

### What is Logged

✅ **Logged:**
- Request paths and methods
- Timing and duration
- Success/failure status
- High-level operation types (chat, dream, tool, etc.)
- Counts, sizes, and aggregate statistics
- Correlation IDs for tracing

### What is NOT Logged

❌ **Never Logged:**
- User prompts or messages
- LLM responses (text content)
- Raw memory contents
- Seed bodies or full text
- Personal Identifiable Information (PII)
- API keys or tokens

### Token Security

- Read token is stored in `.env` (not committed to git)
- All observe endpoints require valid token
- No write operations possible (read-only)
- Can be revoked by changing `.env` value and restarting Ember

### Disabling Observe

Set in `.env`:
```bash
OBSERVE_ENABLED=false
```

All observe endpoints will return `403 observe disabled`.

## Future Extensions

The observe system is designed to evolve with Ember:

### Distributed Ember

When Ember becomes distributed:
- Each process writes its events to a shared event stream (file, message queue, database)
- The observe viewer aggregates events from all sources
- No API changes required—just different backend implementation

### Export to OpenTelemetry

Event schema is already close to OpenTelemetry spans:
- `t` → `timestamp`
- `kind` → `span.kind`
- `op` → `span.name`
- `ms` → `duration_ms`
- `ok` → `status.code`

Future: Add optional OTEL exporter for integration with Jaeger, Grafana, etc.

### Persistent Storage

Current: In-memory ring buffer (2000 events)

Future: Swap to SQLite or log file for persistence:
```python
# Same schema, different backend
def publish(event):
    db.execute("INSERT INTO events VALUES (?)", [json.dumps(event)])
```

## Troubleshooting

### 401 Unauthorized

- Check that `OBSERVE_READ_TOKEN` in `.env` matches the token you're using
- Ensure token is passed in `Authorization: Bearer <token>` header

### 403 Observe Disabled

- Check that `OBSERVE_ENABLED=true` in `.env`
- Restart Ember after changing `.env`

### No Events in Stream

- Verify Ember is receiving requests (check `/api/observe/status` counters)
- Ensure `@observe_route` decorator is applied to routes you want to monitor
- Check browser console for SSE connection errors

### Events Missing Timing Data

- The `@observe_route` decorator measures full request duration
- For sub-operation timing, publish custom events with `ms` field

## Example Output

When watching the observe viewer during a typical session:

```
✓ 14:32:45.123  chat      POST /api/chat           127ms
✓ 14:32:45.456  tool      tool:search              42ms
✓ 14:32:46.789  memory    memory:write             8ms
✓ 14:35:12.000  dream     dream:start              0ms
✓ 14:35:12.100  dream     dream:synthesis          0ms
✓ 14:37:32.500  dream     dream:end                120000ms
✓ 14:37:32.600  seed      seed:proposed            15ms
```

---

Built with ❤️ for transparent, consent-first AI observability.

