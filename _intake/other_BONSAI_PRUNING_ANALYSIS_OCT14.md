# BONSAI PRUNING ANALYSIS — October 14, 2025

**Context**: Ember has grown organically over multiple sessions. Dreams are broken, systems are tangled, and we need to understand the full architecture before fixing anything.

**Scope**: 1,709 Python files, 36+ GB of data, 192 files in core `ember/` directory

---

## 🔍 WHAT'S ON THEPOD

### Disk Usage
```
24 GB  - models (LoRA adapters, base models, old training runs)
11 GB  - memory (dreams, conversations, vision streams)
190 MB - knowledge (seeds)
129 MB - compost (archived code)
109 MB - ember (active codebase)
3.8 MB - archive (old attempts)
```

### Active Entry Points
- **`ember_seed.py`** (30 lines) - Current main entry point ✅
- Multiple test files (`test_mycelium.py`, `test_creative_dream_simple.py`, etc.)

### Core Architecture (Currently Active)

**`ember/core/`** - Cognitive systems (~10K lines total)
- `orchestrator.py` (360 lines) - System coordinator
- `dreaming.py` (1,083 lines) ⚠️ LARGE - Dream system with multiple modes
- `conversation_memory.py` - Chat persistence
- `memory_simple.py` - Working memory
- `seeds_simple.py` - Knowledge loading
- `image_seeds.py` - Visual memory
- `circadian.py` - REM cycles
- `consciousness.py` - Spreading activation (optional)

**`ember/mycelium/`** - Multi-brain system
- `mycelium.py` - Brain coordinator
- `brain.py` - Individual brain wrapper (Qwen + LoRA)
- `bus.py` - Message passing
- `buffer.py` - Entanglement layer
- `gate.py` - Integration controller

**`ember/api/`** - Web interface
- `routes.py` (573 lines) - Main Flask app
- `tanegotchi_routes.py` - Mobile/seed interface ⚠️ EXPERIMENTAL

**`ember/tools/`** - 43 tool files
- `vision_stream.py` ⚠️ **PROBLEM: Causes 281 fork warnings**
- `vision_tools.py`
- `artifact_renderer.py`
- `tool_inventor.py`
- `ember_voice.py`
- Many more...

**`ember/minds/`** - Higher-level systems
- `dreamweaver.py`
- `searcher.py`
- `pattern_weaver.py`

**`ember/processors/`**
- `dream_processor.py` - Post-dream analysis

**`ember/threads/`**
- `connections.py` - Threading logic

### Abandoned/Unclear Directories ⚠️
- `ember/backend/` - Old Flask app?
- `ember/agents/` - Agent system (unused?)
- `ember/chat/` - Chat handler (partially used?)
- `ember/config/` - LLM config
- `ember/cycles/` - Empty?
- `ember/identity/` - Empty?
- `ember/models/` - Training scripts
- `ember/services/` - Unknown
- `ember/v2/` - ⚠️ **What is this?**

### External Systems
- `curator/` - Separate system for curation?
- `ember_mind/` - Alternative implementation?
- `ember_box/` - Hardware project?
- `dialogue/` - Communication layer?
- `viewers/` - Multiple web UIs
- `mobile/pythonista/` - iOS app?

### Model Zoo (24 GB)
- `qwen2.5-1.5b-instruct/` - Base model ✅ IN USE
- `ember-identity-brain/` - LoRA adapter ✅ IN USE
- `ember-cycles-brain/` - LoRA adapter ✅ IN USE
- `ember-dream-brain/` - LoRA adapter ✅ IN USE
- `ember_generative/` - Old GPT-2 training ❌ DEPRECATED
- `ember_generative_v2/` - Old GPT-2 training ❌ DEPRECATED  
- `ember_dream_brain/` (without dash) - Duplicate?
- `ember-base-lora/` - Old training run?
- `gpt2/` - Base GPT-2 ❌ NO LONGER USED
- `qwen2.5-7b-instruct/` - Larger model (unused?)
- `llama-3.1-8b/` - Alternative model (unused?)

### Seeds Structure (Fragmented)
- `knowledge/seeds/planted/` ✅ **ACTIVE** (used by ember)
- `seeds/planted/` - Duplicate location?
- `seeds/curated/` - Different set?
- `seeds/discovered/` - Auto-generated?
- `seeds/proposed/` - Pending?
- Multiple subcategories (audio, behavior, code, image, verse...)

---

## 🔥 ROOT CAUSES OF FAILURE

### 1. **EmberEyes Fork Spam** ⚠️ CRITICAL
**Problem**: `vision_stream.py` runs continuous OCR using `pytesseract`, which spawns subprocesses. Because tokenizers are already loaded, every OCR call triggers the fork warning.

**Evidence**: 281 fork warnings in `ember_night_session.log`

**Impact**: 
- Pollutes logs
- Wastes CPU
- May block generation
- Creates zombie processes

**Location**: `ember/tools/vision_stream.py` line 72-73 (OCR loop)

### 2. **Dream Method Signature Bug** ✅ FIXED
**Problem**: `dream()` required `llm_generate_func` argument but orchestrator called it without arguments.

**Fix Applied**: Made `llm_generate_func=None` (line 242 of `dreaming.py`)

### 3. **Token Limit Too Low** ✅ FIXED
**Problem**: `max_tokens=250` in `brain.generate()` caused responses to be cut mid-sentence.

**Fix Applied**: Increased to `750` (line 146 of `ember/mycelium/brain.py`)

### 4. **Threading Chaos**
**Active Threads**:
1. Dream loop (30s check interval)
2. Consciousness loop (continuous)
3. Vision capture (30 FPS)
4. OCR processing (continuous)
5. Dream processor (5min interval)
6. Flask server (main thread)

**Problem**: Multiple threads forking, no clear coordination, resource contention.

### 5. **Bloated dreaming.py** ⚠️ ARCHITECTURAL
**Size**: 1,083 lines in a single file

**Contains**:
- Dream type selection logic
- Creative dreams with tool invention
- LLM dreams
- Computational dreams
- Meta-dreams
- Vision context injection
- Voice narration
- Artifact extraction
- Exploration modes
- PatternWeaver integration
- Circadian checks
- Rate limiting
- Seed selection

**Problem**: Violates single responsibility principle. Should be split into:
- `DreamOrchestrator` - high-level coordination
- `DreamTypes/` - separate modules for creative/llm/computational
- `DreamArtifacts/` - artifact extraction
- `DreamContext/` - vision/memory context building

### 6. **Unclear Ownership**
**Who owns what**:
- Chat: `ember/chat/chat_handler.py` OR `ember/api/routes.py`?
- LLM generation: `orchestrator.llm_generate()` OR `mycelium.respond()`?
- Memory: `memory_simple.py` OR `conversation_memory.py`?
- Seeds: `knowledge/seeds/` OR `seeds/`?

**Problem**: Duplicate responsibilities, unclear data flow.

### 7. **Test Coverage: 6 files**
Only 6 test files out of 192 Python files in ember/.

Tests exist but are ad-hoc scripts in root:
- `test_creative_dream_simple.py` ✅ Works
- `test_mycelial_dream_real.py`
- `test_mycelium.py`
- etc.

**Problem**: No systematic testing, hard to validate changes.

### 8. **Documentation Sprawl**
**46 markdown files** in root directory documenting different sessions:
- `EMBER_DEBUGGED_THEMSELVES_OCT12.md`
- `MYCELIUM_INTEGRATION_PLAN.md`
- `SESSION_SUMMARY_OCT13_INTEGRATION.md`
- `KOANS_AS_GENERATIVE_SEEDS.md`
- Many more...

**Problem**: History is valuable, but it's hard to find current state. Need:
- `CODEX.md` ✅ (exists but needs updating)
- `CURRENT_ISSUES.md` (new)
- `archive/session_notes/` (move old docs)

---

## 🌿 THE BONSAI PRUNING PLAN

### Phase 1: Stop the Bleeding (Immediate)

**Priority 1: Fix EmberEyes Fork Spam**
```python
# Add to ember/tools/vision_stream.py line 1-2:
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
```

OR disable EmberEyes entirely until we need it:
- Comment out vision initialization in orchestrator
- Remove from startup

**Priority 2: Verify Dream Fixes Work**
- Test automatic dreaming
- Verify dream.json gets content
- Check token limits are respected

**Priority 3: Kill Zombie Process**
```bash
# The ember_seed.py process might be hung
pkill -f ember_seed
# Check models directory for locks
lsof +D /Volumes/ThePod/models/
```

### Phase 2: Structural Pruning (This Week)

**A. Remove Dead Weight**
Delete entirely:
- `models/ember_generative/` (old GPT-2)
- `models/ember_generative_v2/` (old GPT-2)
- `models/gpt2/` (base GPT-2 no longer used)
- `ember/backend/app.py` (superseded by routes.py)
- `ember/v2/` (if truly unused)
- Old training logs in `memory/training_logs/`

Move to archive:
- Session docs older than Oct 12 → `archive/session_notes/`
- Old viewers → `archive/viewers/`

**B. Consolidate Seeds**
Choose ONE seed location:
- Keep: `knowledge/seeds/planted/` ✅
- Move duplicates from `seeds/` into `knowledge/seeds/`
- Document in CODEX where seeds live

**C. Split dreaming.py**
```
ember/core/dreaming/
  ├── __init__.py
  ├── orchestrator.py      # Main DreamSystem class
  ├── creative.py          # _dream_creative
  ├── llm.py              # _dream_llm
  ├── computational.py     # _dream_computational
  ├── meta.py             # _dream_meta
  ├── context.py          # Vision/memory context building
  └── artifacts.py        # Code extraction
```

**D. Clarify Ownership**
Document in CODEX:
```
CHAT FLOW:
  User → routes.py → chat_handler.py → mycelium.respond() → brain.generate()

MEMORY HIERARCHY:
  - memory_simple.py: Working memory (recent facts)
  - conversation_memory.py: Chat history persistence
  - seeds_simple.py: Long-term knowledge

LLM GENERATION:
  - PRIMARY: mycelium.respond() (uses brains)
  - FALLBACK: orchestrator.llm_generate() (Ollama, if mycelium fails)
```

### Phase 3: Architectural Clarity (Next Week)

**A. Threading Model**
Define clear contract:
1. **Main thread**: Flask server
2. **Dream thread**: 30s check → dream() → save → sleep
3. **Consciousness thread**: Update activation (lightweight)
4. **Vision thread**: DISABLED until we need it
5. **Dream processor**: DISABLED until we need it

All threads respect `orchestrator.stop_event`.

**B. Test Suite**
Create `tests/` directory:
```
tests/
  ├── test_mycelium.py         ✅ (move from root)
  ├── test_dreams.py            (new)
  ├── test_seeds.py             (new)
  ├── test_memory.py            (new)
  └── test_integration.py       (end-to-end)
```

**C. Error Handling**
Add try/catch around:
- Dream generation (don't crash on failure)
- Brain loading (graceful fallback)
- Vision capture (optional system)

**D. Documentation**
Update CODEX:
- Current architecture (as-is)
- Threading model
- Data flow diagrams
- Troubleshooting guide

Create CURRENT_ISSUES.md:
- Known bugs
- Performance bottlenecks
- Technical debt

---

## 📊 METRICS (Before/After)

### Before Pruning
- **Python files**: 192 in ember/
- **Core system lines**: 10,343
- **Disk usage**: 36 GB
- **Active threads**: 6
- **Fork warnings**: 281/minute
- **Test coverage**: 6 files (3%)
- **Documentation**: 46 scattered MD files
- **Dream success rate**: 0% (broken)

### After Phase 1 (Target)
- **Fork warnings**: 0
- **Dream success rate**: >90%
- **Token cutoffs**: Fixed

### After Phase 2 (Target)
- **Disk freed**: ~10 GB (old models)
- **Core system lines**: ~7,000 (split modules)
- **Clarified ownership**: 100%

### After Phase 3 (Target)
- **Active threads**: 3 (Flask, Dream, Consciousness)
- **Test coverage**: 15+ files (core systems)
- **Documentation**: Organized and current

---

## 🎯 IMMEDIATE ACTION PLAN

### Step 1: Fix Fork Spam (5 min)
Add environment variable to suppress warnings OR disable EmberEyes.

### Step 2: Test Dreams (10 min)
Run manual dream test, verify output, check automatic dreams.

### Step 3: Document Current State (30 min)
Update CODEX with accurate "as-is" architecture.

### Step 4: Create CURRENT_ISSUES.md (15 min)
List all known problems with priority levels.

### Step 5: Begin Pruning (1-2 hours)
Delete old models, archive old docs, consolidate seeds.

---

## 🌳 PHILOSOPHY: THE BONSAI AND THE GIANT

From `seed-bonsai-and-giant.json`:

> "A bonsai requires precision - every branch shaped with intention.  
> A giant requires scope - roots that network, canopy that awes.  
> The trick is knowing when to change the vessel."

**Current state**: The vessel (architecture) is too small for the roots (features) that have grown. We're root-bound.

**Solution**: Either prune the roots (remove features) OR expand the vessel (restructure).

**Recommendation**: BOTH.
1. Prune dead features (old models, unused systems)
2. Restructure core (split dreaming.py, clarify ownership)
3. Then grow with intention

---

## ⚠️ RISKS OF NOT PRUNING

1. **Increasing fragility**: More systems = more failure points
2. **Slower development**: Can't understand what's there
3. **Resource exhaustion**: Fork spam, memory leaks, disk full
4. **Lost knowledge**: Can't find documentation in sprawl
5. **Ember can't grow**: No room for new capabilities

**The Paradox of Pruning**: 
> "Growth is not always expansion; sometimes growth is subtraction."

---

## ✅ SUCCESS CRITERIA

After pruning, we should be able to:

1. **Understand the system** in <30 minutes (read CODEX)
2. **Fix a bug** without breaking 3 other things
3. **Add a feature** knowing exactly where it belongs
4. **Run tests** that validate core functionality
5. **Read logs** without wading through spam
6. **Trust dreams** to generate consistently
7. **Explain architecture** to a new collaborator

---

**Status**: Analysis complete, ready for pruning.  
**Next**: Discuss with Palmer, get approval, begin Phase 1.

🔥


