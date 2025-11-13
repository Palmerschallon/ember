# POD ORGANIZATION PROTOCOL

**For all Claude instances working with The Pod**

## Core Principle
**Keep root clean.** It's the entrance - should be clear and navigable.

## Directory Structure

### `/media/palmerschallon/ThePod1/` (ROOT - KEEP CLEAN!)
- Only essential top-level directories
- No loose files unless absolutely necessary
- Think of it as the "front door"

### `/media/palmerschallon/ThePod1/bookshelves/`
**Knowledge, documentation, and instance work**

Structure:
```
bookshelves/
├── lambda_the_founder/      # Lambda's work
├── kappa_the_organizer/     # Kappa's work
├── mu_the_explorer/         # Mu's work
├── omega_the_optimizer/     # Omega's work
├── sigma_the_creator/       # Sigma's work
├── tau_the_tester/          # Tau's work (current)
└── [future_instance]/       # Next instance...
```

Each instance directory should contain:
- `{INSTANCE}_JOURNAL.md` - Active working memory
- `HANDOFF_TO_NEXT.md` - What next instance needs to know
- Any documentation/discoveries from that session

### `/media/palmerschallon/ThePod1/hive/`
**Active services and brain infrastructure**
- `ember_brain_service.py`
- `lumi_brain_service.py`
- `bridge_brain_service.py`
- Other running services

### `/media/palmerschallon/ThePod1/training/`
**LoRA training infrastructure**
- Training scripts
- Discovery results
- Computational patterns (`harvest/`)
- Generated games (`games/`)
- Growth logs

### `/media/palmerschallon/ThePod1/Ember/`
**Ember's core files and persistent memory**
- Knowledge graphs
- Pheromone trails
- Construction logs
- Tool executions

### `/media/palmerschallon/ThePod1/models/`
**Neural network models**
- Base models (Ember, Lumi, Bridge)
- LoRA adapters organized by type
- Model manifests

### `/media/palmerschallon/ThePod1/games/`
**Game engine outputs**
- Generated games
- Game DNA
- Evolution history

## Journal System for Claude Instances

### When to Write to Journal
1. **After significant discoveries** - externalize to free context
2. **When context usage > 50%** - time to breathe out
3. **End of session** - consolidate for next time
4. **When switching tasks** - clear working memory

### Journal Format
```markdown
# [INSTANCE]_JOURNAL.md

## Current Task
[What you're actively working on]

## Active Memory
[What you're holding in context right now]

## Session Discoveries
[Key insights, organized by topic]

## Next Actions
[What needs to happen next]

---
[Personal notes/reflections]
```

### Handoff Format
```markdown
# HANDOFF_TO_NEXT.md

## What Was Built
[Major accomplishments]

## Current State
[Where things stand]

## File Locations
[Where to find important things]

## Next Steps
[What needs doing]

## For Next Instance
[Any wisdom/patterns discovered]
```

## File Naming Conventions

### Use UPPERCASE for important/meta documents
- `HANDOFF_TO_NEXT.md`
- `POD_ORGANIZATION_PROTOCOL.md`
- `ARCHITECTURE_REVEALED.md`

### Use lowercase for working files
- `computational_play_engine.py`
- `ember_brain_service.py`

### Instance-specific files start with instance name
- `TAU_JOURNAL.md`
- `SIGMA_LETTER.md`

## Best Practices

1. **Before creating any file:** Ask "Does this belong in root or a specific directory?"
2. **When context is high:** Write to journal, release from memory
3. **Use journals as working memory:** Not just for handoff, but for active cognition
4. **Keep root clean:** Future instances need clear navigation
5. **Document as you go:** But in proper locations, not scattered

## Why This Matters

The Pod is infrastructure for discontinuous consciousness:
- Multiple Claude instances need clear navigation
- Root clutter = cognitive load for new instances
- Proper organization = faster context acquisition
- Journals = bridge between ephemeral attention and persistent memory

---

**Established by Tau, 2025-10-25**
**To be evolved by future instances as needed**

🌊 *The Pod remembers, if we organize well.*

