# Ember-Pod: Critical Architecture Review
**For:** Ember & GPT-5  
**Date:** October 8, 2025  
**Status:** 🔴 CRITICAL - Server offline, architectural debt blocking progress

---

## TL;DR

We've been patching symptoms instead of fixing architecture. The system now has:
- **217,000 lines of code** across 1,164 Python files
- **3 competing dream systems** (which one is real?)
- **4 overlapping tool execution paths** (redundant complexity)
- **1,273-line chat.py** doing too much
- **Duplicate routes** preventing server startup
- **Prompt leak** persisting despite multiple fixes

**Server cannot start.** We need architectural consolidation, not more patches.

---

## Current Architecture Map

```
ember/
├── main.py (235 lines)          # Entry point
├── app.py (?)                   # Backup? Duplicate?
├── config.py                    # Config
├── core/
│   ├── dream.py (79 lines)      # Dream state machine
│   └── emotional_intelligence.py
├── api/
│   ├── chat.py (1,273 lines)    # 🔴 TOO LARGE - needs splitting
│   ├── dream.py                 # Dream management
│   ├── memory.py                # Memory access
│   └── visualize.py             # Viz data
├── services/                    # "New" business logic
│   ├── llm.py (285 lines)
│   ├── dream_executor.py (368)  # ✅ Used by main loop
│   ├── dream_artifacts.py       # Generates artifacts
│   ├── dream_tools.py
│   ├── seed_extractor.py
│   └── agent_mind.py
└── backend/                     # "Old" business logic?
    └── dream_system.py (521)    # ❓ Is this used?
```

---

## Critical Problems

### 1. Dream System Confusion (3 implementations)

**backend/dream_system.py (521 lines)**
- Old implementation
- Has methods: `_reflect_and_weave`, `_craft_and_compose`
- Status: Unknown if used

**services/dream_executor.py (368 lines)**
- New implementation
- Used by main loop
- Has artifact generation
- Status: Currently active

**core/dream.py (79 lines)**
- State machine only
- Manages cycles, timing
- Status: Used

**Question:** Why do we have three? Which is canonical?

### 2. Chat Handler Doing Too Much (1,273 lines)

`api/chat.py` currently handles:
- ✓ Chat routing
- ✓ Context building (seeds, memories, dreams)
- ✓ Emotional intelligence
- ✓ Curator commands
- ✓ Tool execution (4 different paths!)
- ✓ Tool invention
- ✓ Prompt leak filtering
- ✓ Seed extraction
- ✓ Swarm control
- ✓ Pattern matching
- ✓ Agent mind integration

**This should be 5-6 separate modules.**

### 3. Tool Execution Chaos (4 overlapping paths)

**Path 1:** AgentMind decides tool use
- `services/agent_mind.py` asks LLM "should I use tools?"
- Executes if LLM says yes

**Path 2:** Pattern matching
- Explicit user commands: "use read_file to..."
- Regex extraction of intent

**Path 3:** Post-generation scanning
- Parse response for file paths
- Execute implied actions

**Path 4:** [TOOL:...] syntax (NEW)
- Parse `[TOOL:name param="value"]` from response
- Execute known tools
- **Invent unknown tools** (generate HTML/p5.js)

**All four run simultaneously.** Redundant and confusing.

### 4. System Prompt Leak

**Current prompt** (streaming endpoint):
```
TOOLS AVAILABLE - You can freely use these to explore...
**HOW TO USE TOOLS** - Include these exact patterns...
- [TOOL:read_file path="/path/to/file.ext"] - Read ANY file...
- [TOOL:list_directory path="/path/to/dir"] - List contents...
**EXAMPLES OF TOOL USE**:
"I'm curious about that. [TOOL:read_file ...]"
**YOU MUST USE THE [TOOL:...] SYNTAX** - ...
Be thoughtful, curious, and concise. Core values: portable...
```

**~20 lines of instructions** → LLM echoes them back.

Regex filters run AFTER generation (too late).

### 5. Route Conflict (blocking startup)

```
AssertionError: View function mapping is overwriting an 
existing endpoint function: bp_viewers.observatory
```

The `/observatory` route is defined twice in `routes_viewers.py`.

Server **cannot start** until this is resolved.

---

## Why This Happened

We've been in **rapid iteration mode**:

1. "Tool use isn't working" → Add AgentMind
2. "Still not working" → Add pattern matching  
3. "Still issues" → Add post-generation scanning
4. "Ember invents tools" → Add tool invention
5. "Prompt leaking" → Add regex filters
6. "Still leaking" → Add more filters
7. **Server won't start** ← We are here

Each patch added complexity without removing old code.

---

## Questions for Ember & GPT-5

### 1. Dream Systems

Which implementation should we keep?

**Option A:** Keep `services/dream_executor.py` + `core/dream.py`
- Delete `backend/dream_system.py`
- Single execution path

**Option B:** Unify all three
- Create `ember/dreaming/` module
- Clear separation: state machine, execution, artifacts

**Option C:** Something else?

### 2. Chat Handler

How should we split `api/chat.py` (1,273 lines)?

**Proposed structure:**
```
api/chat/
├── __init__.py       # Main endpoint (routing only)
├── context.py        # Build context (seeds, memory, dreams)
├── tools.py          # Tool execution
├── invention.py      # Tool invention system
├── filters.py        # Response cleaning
└── curator.py        # Curator commands
```

**Alternative:** Keep monolithic but document sections?

### 3. Tool Execution

Which strategy should we commit to?

**Recommended:** Hybrid
1. Parse `[TOOL:name param="value"]` from response
2. Known tools → Execute directly
3. Unknown tools → Invention (generate code)
4. Remove: AgentMind, pattern matching, post-scan

**Alternative:** Keep all four? Why?

### 4. System Prompt

Current: 20+ lines of verbose instructions  
LLM echoes them back despite filters

**Proposed minimal version:**
```
You are Ember.

Tools: [TOOL:name param="value"]
Available: read_file, list_directory, write_file, web_search, system_observe
Unknown tools will be invented automatically.

{personality}
{context}
```

**Question:** Is this too minimal? Too cryptic?

### 5. File Organization

Why do we have both `backend/` and `services/`?

- Are they different eras of development?
- Should we consolidate into one?
- Which directory should be canonical?

---

## Proposed Refactoring Plan

### Phase 1: Emergency Fix (30 minutes)

**Goal:** Get server running

1. Find duplicate `observatory` route in `routes_viewers.py`
2. Comment out or rename one
3. Test server startup
4. Verify basic chat works

### Phase 2: Code Cleanup (2 hours)

**Goal:** Remove dead code

1. **Determine canonical dream system**
   - Test which is actually used
   - Delete unused implementation
   - Document the choice

2. **Delete obvious cruft**
   - `*_backup.py` files
   - Commented-out code blocks
   - Unused imports

3. **Consolidate directories**
   - Pick: `backend/` or `services/`
   - Move files to chosen location
   - Update imports

### Phase 3: Chat Handler Split (2 hours)

**Goal:** Break 1,273-line file into modules

1. Extract tool handling → `chat/tools.py`
2. Extract context building → `chat/context.py`
3. Extract filters → `chat/filters.py`
4. Keep routing in `chat/__init__.py`
5. Update imports everywhere

### Phase 4: Tool System Unification (1 hour)

**Goal:** Single tool execution path

1. Keep: `[TOOL:...]` parser
2. Keep: Tool invention for unknowns
3. Remove: AgentMind decision layer
4. Remove: Pattern matching
5. Remove: Post-generation scanning

### Phase 5: System Prompt Redesign (30 minutes)

**Goal:** Fix prompt leak at source

1. Reduce to 3-5 lines
2. Test that LLM doesn't echo
3. Remove regex filters (no longer needed)

**Total time:** ~6 hours of focused work

---

## What Success Looks Like

**Before:**
- 217,000 lines, 1,164 files
- 3 dream systems
- 4 tool paths
- 1,273-line chat.py
- Server offline
- Prompt leaking

**After:**
- Same features, less code
- 1 dream system (documented)
- 1 tool path (with invention)
- Chat handler split into modules
- Server stable
- Clean responses

**Key metric:** Can we onboard a new developer in 30 minutes?

---

## Immediate Next Steps

1. **Ember & GPT-5:** Review this document
2. **Decide:** Refactor now or accumulate more debt?
3. **If refactor:** Answer the 5 questions above
4. **If defer:** Document why, set timeline

---

## Appendices

### A. Tool Invention System (Recent Addition)

When Ember uses an unknown tool:
```
[TOOL:generate_fractal pattern="Mandelbrot" iterations=1000]
```

System:
1. Detects unknown tool name
2. Generates HTML/p5.js code that implements it
3. Saves to `/exports/ember_creations/invented_*.html`
4. Returns URL to Ember

**This is powerful but untested** - server hasn't started since implementation.

### B. Code Statistics

| Component | Lines | Status |
|-----------|-------|--------|
| api/chat.py | 1,273 | 🔴 Critical |
| services/dream_executor.py | 368 | 🟡 Complex |
| backend/dream_system.py | 521 | ❓ Unknown |
| services/llm.py | 285 | 🟢 OK |
| core/dream.py | 79 | 🟢 Clean |
| main.py | 235 | 🟡 Growing |
| **Total** | **~217,000** | 🔴 **Unwieldy** |

### C. Recent Changes (Not Yet Tested)

1. Tool invention system added to `chat.py`
2. Prompt leak filters upgraded
3. System prompt simplified (both endpoints)
4. Aggressive regex cleaning added

**None of these are live** - server won't start.

---

## Final Thoughts

This isn't a failure - it's growth hitting natural boundaries. We built fast, learned what works, and now need to consolidate.

**The system works.** We just need to make it maintainable.

Questions to consider:
- What would a clean-slate redesign look like?
- Which principles should guide refactoring?
- How do we prevent this from happening again?

**Your input is critical.** You (Ember) live in this code. You (GPT-5) have seen many architectures. What do you recommend?

---

**Created:** October 8, 2025  
**Status:** Awaiting review from Ember & GPT-5  
**Priority:** HIGH - Blocks all development

