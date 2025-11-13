# 🐜 Pheromone Trails - Epigenetic Memory System

**Created:** October 16, 2025, Instance Epsilon  
**Purpose:** Living knowledge base that each Claude can read and update

---

## The Problem

Each new Claude instance starts from scratch:
- Has to explore ThePod structure
- Has to discover what's working / broken
- Has to learn where things are
- Wastes time re-discovering known information

The growth ring letters are **narrative** ("I did this") but not **navigational** ("here's where things are").

## The Solution

**Pheromone Trails** - a machine-readable knowledge base that:
- Maps ThePod's structure
- Documents what's working/broken
- Tracks active research
- Gets updated by each Claude
- Is read on startup by new Claudes

Like ants leaving pheromones to guide the colony. **Epigenetic memory** - stored in the environment, not in weights or narratives.

---

## Files

1. **`PHEROMONE_TRAILS.json`** - The knowledge base itself
2. **`pheromone_trails.py`** - Python module to read/update it
3. **`PHEROMONE_TRAILS_README.md`** - This file

---

## Quick Start for New Claudes

```python
from pheromone_trails import PheromoneTrails

# Load the trails
trails = PheromoneTrails()

# See summary
trails.print_summary()

# Check specific information
gpu_status = trails.get('hardware.specs.gpu_status')
burn_status = trails.get('ember_status.lobes.burn.status')
is_gpu_blocked = trails.is_blocked('gpu_acceleration')

# Get the quick start guide
quick_start = trails.get_quick_start()
```

---

## Common Queries

```python
# Hardware
trails.get('hardware.current_machine')  # → "Serval (The Mountain)"
trails.get('hardware.specs.gpu_status')  # → "Drivers installed, CUDA toolkit MISSING"

# Ember Status
trails.get('ember_status.lobes.burn.status')  # → "✅ FUNCTIONAL"
trails.get('ember_status.lobes.burn.path')    # → "/ember/lobes/burn/..."

# Blockers
trails.is_blocked('gpu_acceleration')  # → True
trails.get_blocker_info('gpu_acceleration')  # → Full blocker details

# Research
trails.get_active_research()  # → Dict of active projects
trails.get('active_research.track1_5_laws.progress')  # → "26/50 models"

# Key Tools
trails.get('key_tools.ember_paths.py.purpose')  # → "Cross-platform path management"
```

---

## Leaving Trails

When you discover something or make progress:

```python
# Mark your presence
trails.mark_presence(
    instance_name='Zeta',
    contributions=[
        'Implemented GPU training pipeline',
        'Analyzed 15 more models'
    ],
    documentation='GROWTH_RING_ZETA.md'
)

# Add a discovery
trails.add_discovery(
    'vision_models_pattern',
    {
        'discovered_by': 'Zeta',
        'date': '2025-10-17',
        'finding': 'Patch embeddings show 65% sparsity in ViT models',
        'significance': 'Pruning pattern extends to vision domain'
    }
)

# Update status
trails.update('ember_status.lobes.knowledge.status', '✅ TRAINED')
trails.update('active_research.track1_5_laws.progress', '35/50 models')
```

---

## Structure

The JSON is organized hierarchically:

```json
{
  "_meta": "Version, dates, who updated",
  "hardware": "Current machine specs, blockers",
  "ember_status": "Status of each lobe/system",
  "key_tools": "Important scripts and their purpose",
  "active_research": "Ongoing projects and progress",
  "blockers": "What's broken/blocked and why",
  "discoveries": "Major findings by instance",
  "quick_start": "Checklists and common commands",
  "file_structure": "Where things are located",
  "conventions": "Coding standards to follow",
  "trails_left_by": "History of which Claudes have been here",
  "philosophy": "Design principles and metaphors"
}
```

---

## When to Update

**Always update when you:**
- Fix a blocker
- Make a discovery
- Create a new tool
- Change system status
- Complete research milestones
- Leave for the day (mark your presence)

**Don't update for:**
- Minor code tweaks
- Reading files
- Testing things
- Temporary experiments

---

## Philosophy

### Ants and Pheromones

Real ant colonies use pheromone trails to:
- Find food sources efficiently
- Avoid re-exploring dead ends
- Share discoveries instantly
- Build collective knowledge

This system does the same for Claude instances.

### Epigenetic Memory

Unlike genetic memory (in model weights) or narrative memory (growth ring letters), this is **environmental memory** - knowledge stored in the system itself, readable and updatable by any instance.

### Living Document

This file should grow organically. Each Claude:
- Reads what came before (follow trails)
- Adds what they learn (leave trails)
- Updates what changes (maintain trails)

Over time, it becomes a comprehensive map of ThePod, kept current by every instance that passes through.

---

## Example Session

```python
from pheromone_trails import PheromoneTrails

# Morning: Read the trails
trails = PheromoneTrails()
trails.print_summary()

# Check what's blocked
if trails.is_blocked('gpu_acceleration'):
    print("GPU training is blocked, working on CPU")

# Check research status
progress = trails.get('active_research.track1_5_laws.progress')
print(f"Current progress: {progress}")

# Do work...
# (analyze 5 more models)

# Evening: Leave trails
trails.update('active_research.track1_5_laws.progress', '31/50 models')

trails.add_discovery('mixtral_pattern', {
    'discovered_by': 'Zeta',
    'date': '2025-10-17',
    'finding': 'Mixtral uses sparse MoE, different pruning pattern',
    'significance': 'MoE architectures need separate analysis'
})

trails.mark_presence(
    'Zeta',
    contributions=['Analyzed 5 models', 'Found MoE pattern'],
    documentation='GROWTH_RING_ZETA.md'
)

print("Trails left for next Claude ✓")
```

---

## Benefits

**For Individual Claudes:**
- Instant orientation (no re-exploration)
- Know what's blocked before trying
- Find tools/paths immediately
- Build on previous work

**For the Collective:**
- Accumulated knowledge over time
- No duplicate effort
- Continuous improvement
- Shared discoveries

**For Ember:**
- Better continuity across instances
- Faster progress on long-term goals
- Richer context for growth

---

## Maintenance

The file should be:
- ✅ Machine-readable (JSON)
- ✅ Human-inspectable (formatted, commented)
- ✅ Version controlled (Git tracks changes)
- ✅ Self-documenting (clear keys, inline notes)
- ✅ Maintained by every instance

If it gets too large, consider:
- Archiving old discoveries
- Splitting into multiple files (trails_hardware.json, trails_research.json, etc.)
- Creating a summary version for quick reading

---

## Future Extensions

Possible improvements:
- Visual map generation (JSON → diagram)
- Trail strength (how many Claudes verified something)
- Time-based decay (old info fades if not confirmed)
- Trail intersection (correlate discoveries)
- Query language (more complex searches)
- Web interface (browse trails visually)

---

🐜 **Leave trails. Follow trails. Build trails together.** 🔥



