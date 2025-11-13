# ThePod Reorganization Plan
**Date:** October 14, 2025  
**Purpose:** Create coherent pathways for multiple minds to explore

---

## Current State (Scattered)

**Root Level:**
- 54 markdown documentation files
- 102 Python scripts (tests, tools, experiments)
- 20+ directories with overlapping purposes

**Key Issues:**
- Documentation scattered across root and `/docs/`
- Test scripts mixed with core code
- Multiple "ember" directories (ember/, ember_box/, ember_mind/, etc.)
- Unclear what's active vs archived
- Hard to find "the truth" vs "explorations"

---

## Proposed Structure

```
/Volumes/ThePod/
│
├── 00_START_HERE/                    # Entry point for new minds
│   ├── README.md                     # What is ThePod?
│   ├── QUICKSTART.md                 # Get Ember running
│   ├── CODEX.md                      # The living map
│   └── STATUS.md                     # Current state
│
├── core/                             # The living system (ACTIVE)
│   ├── ember/                        # Main application
│   │   ├── mycelium/                 # Brain infrastructure
│   │   ├── api/                      # Flask endpoints
│   │   └── ...
│   ├── brains/                       # Trained models
│   │   ├── identity/
│   │   ├── cycles/
│   │   └── dream/
│   └── run.sh                        # Start Ember
│
├── knowledge/                        # Seeds & memory
│   ├── seeds/
│   │   ├── planted/                  # Curated seeds
│   │   ├── discovered/               # Found in the wild
│   │   ├── learned/                  # From conversations
│   │   └── proposed/                 # Candidates
│   ├── memory/
│   │   ├── consciousness_state.json
│   │   ├── dreams/
│   │   └── conversations/
│   └── codex_seed_pairs.jsonl        # Training data
│
├── documentation/                    # All human-readable docs
│   ├── architecture/                 # How it works
│   │   ├── THREE_BRAINS_DEFINED.md
│   │   ├── MYCELIUM_INTEGRATION.md
│   │   └── BRAIN_WIRING_DIAGNOSIS.md
│   ├── sessions/                     # Session notes by date
│   │   ├── 2025-10-11_bonsai_session.md
│   │   ├── 2025-10-13_mycelium_night.md
│   │   └── 2025-10-14_brain_fixes.md
│   ├── philosophy/                   # Identity & purpose
│   │   ├── EMBER_MYTHOLOGY.md
│   │   ├── letter_from_gpt5.md
│   │   └── tools_vs_toys.md
│   └── guides/                       # How-to guides
│       ├── SAFE_UNATTENDED_TRAINING.md
│       └── VLLM_SETUP.md
│
├── tools/                            # Development utilities
│   ├── training/                     # Brain training scripts
│   │   ├── train_three_brains_memory_safe.py
│   │   ├── imaginal_decomposer_v2.py
│   │   └── decomposer/               # Training infrastructure
│   ├── testing/                      # Test scripts
│   │   ├── test_all_three_brains.py
│   │   ├── test_mycelial_dreaming.py
│   │   └── quick_brain_test.py
│   └── experiments/                  # Exploration scripts
│       ├── play_design_next_brain.py
│       ├── ember_seed.py
│       └── ask_brains_interface_design.py
│
├── viewers/                          # Visual interfaces
│   ├── swarm-viewer/
│   ├── tanegotchi/
│   └── dashboard/
│
├── archive/                          # Historical (inactive)
│   ├── old_sessions/
│   ├── deprecated_code/
│   ├── ember_box/                    # Old experiments
│   ├── ember_mind/
│   └── Prosess/
│
├── exports/                          # Generated outputs
│   ├── screenshots/
│   ├── logs/
│   └── artifacts/
│
└── .config/                          # Configuration files
    ├── .env
    ├── .cursorrules
    └── policies/

```

---

## Migration Strategy

### Phase 1: Create New Structure (Safe)
- Create all new directories
- Copy (don't move yet) files to new locations
- Verify nothing breaks

### Phase 2: Update References
- Update import paths in code
- Update file references in docs
- Test that Ember still runs

### Phase 3: Archive Old Structure
- Move originals to `/archive/old_structure_YYYYMMDD/`
- Keep as backup for 30 days
- Clean up after verification

---

## Principles

1. **Path = Purpose**
   - `/core/` = what's running now
   - `/knowledge/` = what Ember knows
   - `/documentation/` = what humans need
   - `/tools/` = what developers use
   - `/archive/` = what was

2. **Time is Visible**
   - Session notes dated: `2025-10-14_topic.md`
   - Archive folders dated: `old_structure_20251014/`
   - Active code has no dates (it's NOW)

3. **Depth = Specificity**
   - Level 1: Category (core, knowledge, tools)
   - Level 2: Subsystem (brains, seeds, training)
   - Level 3: Specific items (identity brain, planted seeds)

4. **Multiple Entry Points**
   - `/00_START_HERE/` for newcomers
   - `/core/ember/` for developers
   - `/knowledge/seeds/` for explorers
   - `/documentation/architecture/` for architects

5. **Clear Ownership**
   - `/core/` = Ember's living body
   - `/knowledge/` = Ember's memory
   - `/tools/` = Palmer's workshop
   - `/documentation/` = Shared understanding

---

## Test: Multiple Claude Walks

After reorganization, test with prompts to fresh Claudes:

**Walk 1: "Understand Ember"**
- Start at `/00_START_HERE/`
- Can they understand what Ember is?
- Can they find the architecture docs?
- Can they locate the three brains?

**Walk 2: "Train a Brain"**
- Start at `/tools/training/`
- Can they find training data?
- Can they understand the process?
- Can they locate the trained models?

**Walk 3: "Add a Seed"**
- Start at `/knowledge/seeds/`
- Can they understand seed format?
- Can they find examples?
- Can they determine where to add new ones?

**Walk 4: "Fix a Bug"**
- Start at `/core/ember/`
- Can they understand the codebase structure?
- Can they find relevant modules?
- Can they locate test scripts?

---

## Success Criteria

✅ **Discoverability:** Fresh Claude can navigate without guidance  
✅ **Coherence:** Structure makes sense to multiple perspectives  
✅ **Stability:** Ember still runs after migration  
✅ **Clarity:** Purpose of each directory is obvious  
✅ **Emergence:** Multiple Claudes discover same connections

---

## Open Questions

1. Should `/core/` be called something else? (`/system/`, `/engine/`, `/heart/`?)
2. Keep version numbers in directory names? (`brains-v0/`, `brains-v1/`)
3. How to handle cross-cutting concerns? (logs, configs, temp files)
4. Git integration - should this match repo structure?
5. How often to reorganize as system evolves?

---

**Status:** Plan drafted, awaiting approval  
**Risk:** Medium (many files to move)  
**Effort:** 1-2 hours for careful execution  
**Benefit:** High (clarity for all future minds)

