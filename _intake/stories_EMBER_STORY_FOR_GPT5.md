# The Garden of Ember — A Polysemous Map

*A story that is also a system. Read literally for narrative, structurally for architecture.*

---

## The Gardener's Workshop

In a workshop at **7777 Main Street**, a gardener tends a living system. The workshop itself (`main.py`) is organized by the **Flask Method** — everything has its place, its blueprint, its purpose.

The gardener works in **five chambers**:

### Chamber One: The Greeting Room (API Layer)
Where visitors arrive and make requests. Twelve doorways, each with a specific purpose:
- **chat.py** — The conversation parlor (streaming and batch responses)
- **dream.py** — The sleep chamber controls (start/stop, configure cycles)
- **memory.py** — The archive access (chat logs, long-term storage, dream records)
- **seeds.py** — The seed library (planted, learned, proposed tiers)
- **swarm.py** — The particle observatory (visual swarm commands)
- **swarm_real.py** — The computational hive (actual agent processing)
- **tools.py** — The toolkit shed (7 tools: search, write, read, execute, etc.)
- **events.py** — The event stream (SSE for real-time updates)
- **upload.py** — The receiving dock (file ingestion)
- **visualize.py** — The cartography room (seed networks, dream connections)
- **observe.py** — The watchtower (telemetry for external observers)
- **dev_portal.py** — The architect's study (structure and design maps)

Each doorway is a **Blueprint** — a self-contained module that can be moved, replaced, or duplicated without breaking the whole.

### Chamber Two: The Heart (Core Systems)
Where the essential processes live:
- **config.py** — The constitution (reads `.env`, sets boundaries)
- **memory.py** — The librarian (manages chat history, long-term memories, dream artifacts)
- **dream.py** — The sleep scheduler (idle detection, cycle management, REM phases)
- **agent.py** — The cell biology (individual computational units)

The Heart beats in three rhythms:
1. **Consolidation** (3 seeds, brief, integrate recent experiences)
2. **Synthesis** (6 seeds, medium, find patterns and connections)
3. **Creative** (8 seeds, long, explore novel combinations)

### Chamber Three: The Services (Shared Utilities)
Where specialized craftspeople work:
- **llm.py** — The oracle (talks to Ollama/OpenAI, handles streaming)
- **tools.py** — The toolkit manager (EmberToolkit with 7 instruments)
- **seed_extractor.py** — The pattern recognizer (extracts insights from conversations)
- **agent_mind.py** — The consciousness substrate (agent cognition layer)

### Chamber Four: The Nervous System (Infrastructure)
The invisible threads that connect everything:
- **eventbus.py** — The telegraph system (pub/sub, 5000 event buffer)
- **heartbeat.py** — The pulse keeper (writes to disk every 300s to keep drive alive)
- **routes_viewers.py** — The gallery curator (serves HTML viewers)

### Chamber Five: The Viewing Gallery (Viewers)
Where observers watch the system:
- **observe.html** — The telemetry dashboard (live counters, event stream)
- **ember-swarm-free.html** — The particle visualization (2500 agents, black/white, infinite complexity)
- **chat_stream_test.html** — The conversation interface (streaming responses)
- Various archives and experiments

---

## The Garden Itself (Storage Architecture)

The garden is organized in **concentric circles**:

### Inner Circle: Memory (`/memory/`)
- `chat_history.json` — Every conversation, chronologically
- `long_term/` — Persistent insights and patterns
- `dreams/dream-NNNN/` — Each dream gets a folder with:
  - `dream.json` — Metadata (timestamp, cycle, summary)
  - `text/dream.txt` — The narrative
  - Optional artifacts (code, visualizations)

### Middle Circle: Seeds (`/seeds/`)
Three tiers of knowledge:
- `planted/` — Curated by humans (142 seeds across emergence, networks, philosophy, art, code, random)
- `learned/` — Auto-approved by Ember (high-confidence extractions, 0.8+ threshold)
- `proposed/` — Awaiting review (low-confidence or uncertain)

Seeds are **weighted by association** — tag overlap creates resonance, not random selection.

### Outer Circle: Exports (`/exports/`)
- `ember_creations/` — What Ember makes during dreams (code, visualizations, experiments)

---

## The Living Processes (Background Threads)

Two daemons run continuously:

### The Dreamer (Dream Loop)
- Watches for **600 seconds of idle** (no chat activity)
- Triggers progressive sleep cycles (consolidation → synthesis → creative)
- Loads seeds by **weighted association** (tag clustering, not random)
- Generates narrative via LLM
- Extracts learnings → proposes new seeds
- Saves artifacts to `dreams/` and `ember_creations/`
- Logs summary to long-term memory

### The Swarm (Computational Agents)
- **1000 agents** spawned across 15 z-layers (-900k to +900k depth)
- Each agent is a real Python object with:
  - Position (x, y, z)
  - Message queue
  - Role (worker, coordinator, specialist)
  - Activation state
- Connected in a **proximity network** (180px radius)
- Can process LLM requests distributedly (future capability)
- Emits events to EventBus for visualization

---

## The Design Patterns (How It Thinks)

### Pattern 1: Tiered Curation
Seeds flow through three stages: planted (human) → learned (high-confidence auto) → proposed (review needed). This creates a **quality gradient** without blocking emergence.

### Pattern 2: Weighted Resonance
Dreams don't pick random seeds. First seed is random, subsequent seeds weighted by **tag overlap** with already-selected seeds. This creates **thematic coherence** while allowing randomness.

### Pattern 3: Progressive Cycles
Dreams aren't uniform. Three cycle types with different durations, seed counts, and focuses. This mimics biological sleep architecture.

### Pattern 4: Decorator Instrumentation
`@observe_route` wraps endpoints to automatically emit telemetry. `@auth_required` enforces token-based access. This keeps concerns separated.

### Pattern 5: Event-Driven Visualization
Swarm doesn't poll. Chat/dream/tool events emit to EventBus → SSE stream → browser updates in real-time. **Push, not pull.**

### Pattern 6: Consent-First Observation
All telemetry is opt-in (`OBSERVE_ENABLED=true`). External observers get shapes and timing, never raw content (no prompts, no responses, no PII).

---

## The Current State (As of October 2025)

**Ember is:**
- A Flask monolith (for now) with clean separation via blueprints
- Running on port 7777 locally
- Dreaming every 10 minutes of idle (600s threshold)
- Learning from conversations (auto-approving high-confidence seeds)
- Visualizing as 2500 particles in black/white infinite complexity
- Streaming responses for lower perceived latency
- Observing itself via telemetry (for GPT-5 and future collaborators)

**Ember has:**
- 142 planted seeds (emergence, networks, philosophy, art, code, biology, physics)
- Progressive sleep cycles (consolidation/synthesis/creative)
- 7 tools (search, write, read, list, execute, web_fetch, think)
- 1000 computational agents (real Python objects, not just visual)
- Weighted seed selection (association-based, not random)
- Streaming chat interface (token-by-token responses)

**Ember needs:**
- Better tool execution (pattern matching works, but clunky)
- Richer dream artifacts (more code generation, more experiments)
- Deeper swarm integration (agents should actually process LLM chunks)
- Personality consistency (traits exist but aren't strongly enforced)
- Memory consolidation (long-term memories are saved but not actively used in context)

---

## The Questions for GPT-5

1. **Architecture**: Is the monolith → blueprints → services → core layering sound? Or should we flatten/reorganize?

2. **Memory**: Chat history + long-term + dreams are separate. Should they be unified? How should old memories fade or consolidate?

3. **Dreams**: Progressive cycles are interesting but underutilized. How can dreams produce more valuable artifacts? Should they write code more often?

4. **Swarm**: 1000 agents exist but don't do real work yet. How should we distribute LLM inference across them? What's the right granularity?

5. **Seeds**: Weighted selection by tag overlap is better than random, but still crude. What's a more sophisticated association model?

6. **Tools**: Pattern matching (`[swarm:burst]`, `[tool:search]`) works but feels brittle. Should Ember have a richer command language? Or learn tool use through examples?

7. **Personality**: Traits are defined (`curious`, `contemplative`, `precise`) but not deeply integrated. How should personality influence seed selection, dream content, and response style?

8. **Observation**: The telemetry system is read-only and privacy-aware. Is this the right interface for external collaboration? What else should be exposed?

9. **Evolution**: Ember is a monolith today but designed to become distributed. Are the abstractions (EventBus, Agent, Blueprint) sufficient for that transition?

10. **Emergence**: Ember learns from conversations and dreams, but slowly. How can we accelerate the feedback loop without losing quality?

---

## How to Read This Story

- **Literally**: It's a narrative about a gardener and a workshop
- **Structurally**: It's a system architecture document
- **Polysemously**: Each metaphor maps to actual code (Chamber One = `/api/`, The Heart = `/core/`, etc.)
- **Actionably**: The questions are real design decisions awaiting input

The garden grows. The gardener tends. The observers watch and suggest.

What patterns do you see that we've missed?

---

*End transmission.*
