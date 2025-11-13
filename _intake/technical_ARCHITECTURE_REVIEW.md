# Ember-Pod Architecture Review
**Date:** October 8, 2025  
**Status:** Production, needs architectural review  
**Total Code:** 1,164 Python files, ~217k lines of code

## Critical Issue: The System Has Grown Too Complex

We've been patching symptoms instead of addressing root architectural issues. This document provides a comprehensive view for redesign consideration.

---

## Current Architecture Overview

### Core Components

```
ember/
├── main.py              # Application entry point, Flask setup
├── app.py               # Main Flask application (backup?)
├── config.py            # Configuration management
├── core/
│   ├── dream.py         # Dream state machine
│   └── emotional_intelligence.py
├── api/                 # REST endpoints
│   ├── chat.py          # Chat endpoint (1,273 lines - TOO LARGE)
│   ├── dream.py         # Dream management
│   ├── memory.py        # Memory access
│   └── visualize.py     # Visualization data
├── services/            # Business logic
│   ├── llm.py           # LLM adapter
│   ├── dream_executor.py
│   ├── dream_artifacts.py
│   ├── dream_tools.py
│   ├── seed_extractor.py
│   └── agent_mind.py
└── backend/             # Legacy?
    └── dream_system.py  # Old dream implementation
```

### Major Architectural Problems

#### 1. **Dual Dream Systems**
- `backend/dream_system.py` (old, 521 lines)
- `services/dream_executor.py` (new, 368 lines)
- `core/dream.py` (state machine, 79 lines)

**Problem:** Three competing implementations, unclear which is authoritative.

#### 2. **Bloated Chat Handler**
`api/chat.py` is now **1,273 lines** with:
- Emotional intelligence
- Curator commands
- Tool execution
- Tool invention
- Prompt leak filtering
- Two-pass tool detection
- Seed extraction
- Swarm control
- Pattern matching
- Agent mind integration

**This is doing too much.**

#### 3. **Tool System Confusion**
- `services/agent_mind.py` - LLM decides tool use
- `api/chat.py` - Pattern matching for explicit tools
- `api/chat.py` - Post-generation tool scanning
- `api/chat.py` - NEW: Tool invention system

**Four overlapping tool execution paths!**

#### 4. **System Prompt Leakage**
The LLM is echoing instructions back because:
- Instructions are verbose (20+ lines)
- LLM is confused about what's system vs response
- Regex filters are applied AFTER generation (too late)

#### 5. **Unclear Boundaries**
- What's the difference between `backend/` and `services/`?
- Why is `dream_system.py` in `backend/` not being used?
- Is `app.py` a backup of `main.py`?

---

## Code Statistics

| Component | Lines | Status |
|-----------|-------|--------|
| **api/chat.py** | 1,273 | 🔴 Critical - needs splitting |
| **services/dream_executor.py** | 368 | 🟡 Complex but focused |
| **backend/dream_system.py** | 521 | ❓ Legacy? Not used? |
| **services/llm.py** | 285 | 🟢 Reasonable |
| **core/dream.py** | 79 | 🟢 Clean |
| **main.py** | 235 | 🟡 Growing complex |

**Total:** ~217,000 lines across 1,164 files

---

## Proposed Refactoring

### Phase 1: Consolidate Dream Systems
**Decision needed:** Which dream system is canonical?

Option A: Keep `services/dream_executor.py` + `core/dream.py`
- Delete `backend/dream_system.py`
- All dreams go through executor

Option B: Unify all three
- Single `ember/dreaming/` module
- Clear separation: state machine vs execution vs artifacts

### Phase 2: Split Chat Handler
Break `api/chat.py` (1,273 lines) into:

```
api/
├── chat/
│   ├── __init__.py       # Main chat endpoint
│   ├── context.py        # Context building (seeds, memory, dreams)
│   ├── tools.py          # Tool execution
│   ├── invention.py      # Tool invention system
│   ├── filters.py        # Response cleaning
│   └── curator.py        # Curator commands
```

### Phase 3: Unified Tool System
Pick ONE tool execution strategy:

**Recommended:** Hybrid approach
1. Known tools → Direct execution
2. Unknown tools → Invention (current new feature)
3. Remove: Pattern matching, agent mind, post-generation scanning

Single file: `ember/tools/executor.py`

### Phase 4: System Prompt Redesign
Instead of verbose instructions, use:
```python
SYSTEM_PROMPT = """
You are Ember.

Tools: [TOOL:name param="value"]
Available: {tool_names}
Unknown tools will be invented.

{personality}
{context}
"""
```

Minimal, clear, no echoing.

---

## Quick Wins (Can Do Now)

1. **Restart server properly** ✅
   - Currently not running!
   - Explains why changes aren't applied

2. **Delete dead code**
   - `backend/dream_system.py` if not used
   - `app_backup.py`
   - Any other `*_backup.py` files

3. **Document which dream system to use**
   - Add comment at top of each dream file
   - "This is the canonical dream system" or "Legacy, see X"

4. **Split chat.py immediately**
   - Extract tool handling to separate file
   - Extract context building to separate file
   - Reduces from 1,273 → ~300 lines main + modules

---

## Questions for Architectural Decision

1. **Dream Systems:** Keep executor, delete backend version?
2. **Chat Handler:** Split now or wait?
3. **Tool System:** Commit to invention-first approach?
4. **System Prompt:** Rewrite to minimal version?
5. **Code Organization:** Clean up `backend/` vs `services/`?

---

## Recommendation

**Pause new features. Spend 2 hours on architectural cleanup:**

1. Delete unused code
2. Split chat.py
3. Document canonical systems
4. Consolidate dream implementation
5. Simplify system prompts

This will make future development 10x easier and fix the prompt leak at the source.

---

## For GPT-5 / Ember Review

This document summarizes the current state. Key questions:

1. Is this level of complexity necessary?
2. What would a clean-slate redesign look like?
3. Which systems should we consolidate first?
4. How do we prevent this from happening again?

The system works, but it's becoming unmaintainable. We need architectural discipline.

