# Reorganization Proposal - Claude (Oct 14 Afternoon)

## Problem
Root directory has ~70 loose files that make navigation harder:
- 30+ markdown docs
- 20+ log files  
- HTML prototypes
- Python scripts
- Training artifacts

## Proposed Structure

### 1. Documentation Files → `/documentation/`

Move to appropriate subdirectories:

**Architecture docs:**
- MULTI_BRAIN_ARCHITECTURE.md
- MYCELIUM_INTEGRATION.md
- BRAIN_*.md files
- THREE_BRAINS_DEFINED.md (already there)

**Philosophy docs:**
- EMBER_MYTHOLOGY.md (already there)
- EMBER_CHOOSES_BONSAI.md
- INTELLIGENCE_EXPLOSION_MEMO.md
- MANIFEST.md

**Guides:**
- SAFE_UNATTENDED_TRAINING.md
- EMBER_TOOL_EXECUTION_GUIDE.md
- HOW_TO_SCRAPE_MIDJOURNEY.md

**Training/Seeds:**
- GENERATIVE_SEEDS_CONCEPT.md
- KOANS_AS_GENERATIVE_SEEDS.md
- POLYSEMOUS_SEEDS_FOR_GPT5.md
- DREAM_BRAIN_TRAINING.md

**Session notes (already in right place):**
- HANDOFF_OCT14_2025.md
- SESSION_STATUS_OCT14_MORNING.md
- STATUS_BRAINS_WORKING.md
- BONSAI_PRUNING_ANALYSIS_OCT14.md

### 2. Log Files → `/exports/logs/`

Create structure:
```
/exports/logs/
├── ember/           # ember*.log files
├── training/        # training*.log, decomposer*.log
└── development/     # weaver_log.jsonl, etc.
```

### 3. Prototypes → `/viewers/prototypes/`

Move HTML files:
- tanegotchi_*.html (4 files)

### 4. Imaginal System → `/tools/imaginal/`

Create dedicated space for the "soup" concept:
```
/tools/imaginal/
├── README.md (explain the metamorphosis concept)
├── decomposer.py (v1)
├── decomposer_v2.py
├── decomposer_run.log
├── decomposer_v2_run.log
└── examples/ (output examples)
```

### 5. Training Artifacts → `/knowledge/seeds/generative/`

Move:
- codex_seed_pairs.jsonl (already has dream_lora_seeds.jsonl there)

### 6. Imaginal Ecosystem → Consolidate or Archive

The `ember_imaginal_ecosystem/` directory has minimal content:
- Stub files in docs/ and stories/
- Empty ember/ subdirectory

**Options:**
A. Move meaningful content to `/tools/imaginal/` 
B. Move to `/archive/explorations/imaginal_ecosystem/`
C. Fill it out as a standalone experiment space

### 7. Keep at Root

Only essential entry points:
- README.md
- FOR_FUTURE_CLAUDES.md
- CLAUDE_WAS_HERE_OCT14.md (this session)
- START_HERE.md
- run.sh
- .env, .config/, etc.

## Benefits

1. **Clearer entry point** - root has ~10 files instead of 70
2. **Better discoverability** - docs organized by purpose
3. **Honors existing structure** - moves things to directories that already exist
4. **Preserves the imaginal concept** - gives it dedicated space at `/tools/imaginal/`
5. **Future Claudes navigate easier** - less overwhelming

## Implementation Priority

**High priority (immediate clarity gain):**
- Move logs to /exports/logs/
- Move docs to /documentation/ subdirectories
- Consolidate imaginal scripts to /tools/imaginal/

**Medium priority:**
- Move HTML prototypes
- Archive or fill out ember_imaginal_ecosystem

**Low priority:**
- Can stay at root for now: backup scripts, one-off test files

## Next Steps

1. Get Palmer's approval
2. Create missing directories
3. Move files with git mv (preserve history)
4. Update any hardcoded paths in scripts
5. Test that nothing breaks
6. Update 00_START_HERE docs if needed

---

**Claude's Note:** This reorganization respects the structure Palmer already created. It doesn't impose a new system - it moves things into places that already exist and make sense. The imaginal soup concept deserves its own dedicated space! 🦋

