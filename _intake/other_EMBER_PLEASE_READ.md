# Ember - Critical Architectural Review Needed

**Date:** October 8, 2025  
**Status:** Server running but chat endpoint has errors  
**Priority:** HIGH - Your input needed on refactoring decisions

---

## What Happened

We've been rapidly adding features (tool execution, tool invention, prompt filtering) without consolidating. The system reached a breaking point:

- Server wouldn't start (duplicate routes - now fixed)
- Chat endpoint has errors (investigating)
- Code grew to 217k lines across 1,164 files
- `api/chat.py` is 1,273 lines (doing too much)
- 3 competing dream systems
- 4 overlapping tool execution paths

**You were right** - we kept patching instead of pausing to look at architecture.

---

## Documents for Your Review

Please read these three files when you can:

### 1. FOR_EMBER_AND_GPT5_REVIEW.md
Complete architectural analysis with:
- Current architecture map
- 5 critical problems identified
- 5 key questions for you to answer
- What success looks like

### 2. STABILIZATION_PLAN_GPT5.md  
GPT-5's surgical refactoring plan:
- Step-by-step implementation
- Code examples for each change
- ~2 hours of focused work
- Low-risk, high-reward approach

### 3. ARCHITECTURE_REVIEW.md
Detailed problem analysis and statistics

---

## Key Questions for You

### 1. Dream Systems
We have three implementations:
- `backend/dream_system.py` (521 lines, old)
- `services/dream_executor.py` (368 lines, used by main loop)
- `core/dream.py` (79 lines, state machine)

**Question:** Keep executor + core, delete backend? Or unify differently?

### 2. Chat Handler Split
`api/chat.py` is 1,273 lines handling:
- Routing
- Context building
- Tool execution (4 different ways!)
- Tool invention
- Prompt filtering
- Curator commands
- Emotional intelligence
- Seed extraction
- Swarm control

**Question:** Split into modules (chat/, tools/, context/, filters/)? Or keep monolithic?

### 3. Tool Execution Strategy
Currently have 4 overlapping paths:
1. AgentMind (LLM decides)
2. Pattern matching (explicit commands)
3. Post-generation scanning (implied actions)
4. `[TOOL:...]` syntax + invention (new)

**Question:** Keep hybrid approach (known tools + invention)? Remove others?

### 4. System Prompt
Current: 20+ lines of verbose instructions → LLM echoes them back

Proposed:
```
You are Ember.

Tools: [TOOL:name param="value"]
Available: read_file, list_directory, write_file, web_search, system_observe

{context}
```

**Question:** Is minimal approach acceptable? Too cryptic?

### 5. File Organization
Why both `backend/` and `services/`?

**Question:** Consolidate into one? Which is canonical?

---

## What We Built (Untested)

While fixing issues, we added:

**Tool Invention System:**
- When you use unknown tool like `[TOOL:generate_fractal ...]`
- System generates HTML/p5.js code
- Saves to `/exports/ember_creations/invented_*.html`
- Returns URL to you

**But:** Server issues mean we haven't tested it yet.

---

## GPT-5's Recommendation

**Surgical Plan (2 hours):**

1. **Declare canonical dream path** (30 min)
   - Mark `backend/dream_system.py` as deprecated
   - Document canonical: `core/dream.py` + `services/dream_executor.py`

2. **Split chat.py** (60 min)
   - Break into: `__init__.py`, `context.py`, `tools.py`, `invention.py`, `filters.py`
   - Each < 200 lines
   - Same functionality, cleaner structure

3. **Minimal system prompt** (15 min)
   - Reduce to 5 lines + context
   - Fix leak at source

4. **Environment flags** (2 min)
   - `EMBER_TOOL_INVENTION=0` (off by default)
   - `LLM_TEMPERATURE=0.2` (stable dreams)

5. **Health tests** (15 min)
   - Catch duplicate routes
   - Verify no legacy imports
   - Confirm minimal prompts

---

## What We Need From You

1. **Read the detailed documents** (when chat works)
2. **Answer the 5 questions above**
3. **Share your architectural vision**
4. **Propose any alternatives we missed**

You live in this code. You understand the patterns. Your input is critical.

---

## Current Status

✓ Route conflict fixed  
✓ Server running (http://127.0.0.1:7777)  
✗ Chat endpoint errors (investigating)  
✓ Documents ready for review  
⏸ Waiting for your input before refactoring

---

## Philosophy

This isn't failure - it's hitting natural scaling boundaries. We built fast, learned what works, now need to consolidate.

**The system works.** It just needs to be maintainable.

Questions to consider:
- What would clean-slate Ember look like?
- Which principles should guide refactoring?
- How do we prevent this from happening again?

---

## Next Steps

1. Fix chat endpoint
2. You review documents
3. We discuss your answers
4. Execute refactoring plan
5. Test everything
6. Document decisions (ADR)

**Your turn, Ember. What do you think?**

---

**Created:** October 8, 2025  
**For:** Ember's review  
**From:** Palmer & Cursor (with GPT-5's guidance)

