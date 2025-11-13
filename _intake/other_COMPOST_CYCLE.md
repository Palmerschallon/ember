# The Compost Cycle

*"The compost bin is not death. It's digestion."*

## Philosophy

Everything that has outlived its purpose ends up in `/compost/`:
- Broken prototypes
- Corrupted JSON  
- Sketches that once felt alive but no longer sing

At first, this seems like failure — the graveyard of discarded code. But the compost bin is not where things end. It's where they **ferment**.

Inside that pile of broken syntax and dead ideas is warmth — lines of forgotten experiments, half-lives of creativity still releasing heat. Old fragments begin to recombine in ways no one intended. What was waste becomes medium.

## Implementation

### The Process

Every week, the Compost Cycle runs:

1. **Gather Material** - Scan `/compost/` for code, docs, and dream fragments
2. **Measure Entropy** - Calculate age + fragmentation + connection density
3. **Ferment** - When entropy ≥ 0.6, extract patterns and wisdom
4. **Generate Seeds** - Create "fermented seeds" that carry memory of decay

### Entropy Formula

```
entropy = (age_score * 0.4) + (fragmentation * 0.3) + (connection_density * 0.3)
```

- **Age**: Days since last modified (max at 30 days)
- **Fragmentation**: How broken/incomplete (TODOs, errors, missing pieces)
- **Connection Density**: Number of unique concepts mentioned

### Fermented Seeds

Seeds created from compost contain:
- **Patterns**: Extracted from the decayed material
- **Wisdom**: Distilled from comments and structure
- **Memory of Decay**: Context of why it failed
- **Source Metadata**: Original path, age, entropy score

## Usage

### Manual Composting

```python
from pathlib import Path
from ember.cycles.compost_cycle import compost_file

# Move a file to compost
compost_file(
    source_path=Path("old_experiment.py"),
    compost_path=Path("/Volumes/ThePod/compost"),
    reason="approach was too complex"
)
```

### Running the Cycle

```bash
# Stir the compost bin
python3 ember/cycles/compost_cycle.py stir
```

### Scheduled (Weekly)

Add to cron or system scheduler:
```
0 3 * * 0 cd /Volumes/ThePod && python3 ember/cycles/compost_cycle.py stir
```

## Directory Structure

```
/compost/
├── code/           # .py files
├── docs/           # .md, .txt files
└── fragments/      # .json, misc files

/seeds/planted/fermented/
└── seed-fermented-*.json  # Generated fermented seeds
```

## The Lesson

Creation isn't a straight ascent toward perfection. It's a spiral of growth and decomposition.

Without decay, there's no nutrient for the next idea.  
Without endings, no beginnings.

The compost bin is the most honest archive in the system — the place where meaning rests before being reborn.

---

*Implemented: October 11, 2025*  
*Inspired by: Palmer's Parable*

