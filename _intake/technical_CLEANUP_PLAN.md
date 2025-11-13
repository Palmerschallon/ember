# Pod Structure Cleanup Plan

Date: 2025-10-11
Issue: "The pod folder structure itself is very messy" - Palmer

## Current State

Root directory has accumulated:
- 50+ markdown documentation files
- Multiple Python entry points
- Various directories without clear organization
- Session logs, feature docs, analysis results all mixed

## Proposed Clean Structure

```
/Volumes/ThePod/
├── ember_seed.py              # Main entry point
├── README.md                  # Project overview
├── requirements.txt           # Dependencies
│
├── ember/                     # Core system (bonsai architecture)
│   ├── core/                  # Cognitive systems
│   ├── threads/               # Connections
│   ├── minds/                 # Atomic minds
│   ├── tools/                 # Utilities
│   ├── processors/            # Background processors
│   ├── api/                   # Flask routes
│   └── config/                # Configuration
│
├── memory/                    # Ember's runtime memory
│   ├── dreams/                # Dream storage
│   ├── discoveries/           # From The Searcher
│   ├── patterns/              # PatternWeaver results
│   └── voice/                 # Voice recordings
│
├── seeds/                     # Knowledge bank
│   ├── planted/               # Curated seeds
│   ├── discovered/            # Found seeds
│   └── proposed/              # Candidate seeds
│
├── exports/                   # Generated artifacts
│   └── ember_creations/       # Visual outputs
│
├── viewers/                   # Web interfaces
│   ├── hub_v2.html
│   └── ...
│
├── docs/                      # ← NEW: Organized documentation
│   ├── architecture/          # Architecture docs
│   ├── sessions/              # Session notes
│   ├── features/              # Feature documentation
│   ├── analysis/              # Analysis results
│   └── archive/               # Historical docs
│
├── compost/                   # ← NEW: Cut code & old docs
│   ├── code/                  # Deprecated implementations
│   ├── docs/                  # Outdated documentation
│   └── fragments/             # Experiments
│
└── scripts/                   # ← NEW: Utility scripts
    ├── start_ember.sh
    └── ...
```

## Cleanup Actions

### Phase 1: Create Structure

```bash
mkdir -p docs/architecture
mkdir -p docs/sessions
mkdir -p docs/features
mkdir -p docs/analysis
mkdir -p docs/archive
mkdir -p scripts
```

### Phase 2: Categorize & Move Markdown Files

#### Architecture Docs → docs/architecture/
- AGENT_SEED_ARCHITECTURE.md
- ARCHITECTURE_APPROVED.md
- BONSAI_SESSION_1_*.md
- EMBER_CODE_NAVIGATION.md
- (etc.)

#### Session Notes → docs/sessions/
- SESSION_*.md
- HANDOFF_*.md
- *_OCT*.md

#### Feature Docs → docs/features/
- *_COMPLETE.md
- *_BREAKTHROUGH.md
- *_LAUNCH.md
- CREATIVE_SANDBOX_COMPLETE.md
- DREAMWEAVER_*.md

#### Analysis Results → docs/analysis/
- PATTERNWEAVER_ANALYSIS_RESULTS.md
- DREAM_QUALITY_BREAKTHROUGH.md
- *_ANALYSIS*.md

#### Keep at Root (Active/Current)
- README.md (if exists, or create)
- CLEANUP_PLAN.md (this file, temporarily)

### Phase 3: Compost Old/Redundant Files

Files that are:
- Superseded by newer versions
- Historical session notes (move to docs/archive/)
- Draft documents no longer relevant
- Old implementations

### Phase 4: Clean Python Files

Only these should be at root:
- ember_seed.py (when refactor complete)
- ember_monolith.py (until refactored, then compost)

Move others:
- Test scripts → scripts/
- Old implementations → compost/code/

## Execution

Start with:
1. Create docs/ structure
2. Move markdown files by category
3. Review what can be composted
4. Get Palmer's approval for each compost decision

Do NOT compost anything without review - these are Ember's memories.

## Notes

- Use date prefixes for composted files: 2025-10-11_filename
- Keep git history intact
- Document in commits why files were moved/composted
- Glyph-only formatting (no emoji)

---

Status: Plan drafted, awaiting execution approval
Next: Create directories, begin categorization

