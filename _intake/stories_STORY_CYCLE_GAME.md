# 🌱 Story Cycle Game - Narrative Training for Cycles Brain

**Created:** October 14, 2025  
**Purpose:** Train Cycles brain through choose-your-own-adventure narrative generation

---

## The Concept

Instead of spatial game (Game of Fire), **Story Cycle** is temporal—Cycles brain generates narrative through choices, learning about:

- **Transformation** - How choices compound over time
- **Pacing** - When to escalate, when to rest
- **Arcs** - Beginning → Rising → Climax → Falling → Resolution
- **Cycles** - Stories that complete and transform

---

## How It Works

### The Game

1. **Story begins** with a seed moment (random prompt)
2. **Cycles brain responds** with what happens next
3. **Paths emerge** - Brain suggests 2-3 possible directions
4. **Story advances** through phases:
   - Beginning (establish world)
   - Rising (add tension)
   - Climax (moment of change)
   - Falling (consequences)
   - Resolution (complete arc)

### Example Turn

```
STORY SO FAR:
A seed falls into unknown soil → Moisture embraces it

CURRENT MOMENT:
Something ancient stirs within

PHASE: RISING
TURN: 3

What happens next? Write ONE sentence...
```

**Cycles Brain Response:**
```
Next: A tender shoot breaks through darkness, seeking light.
Paths: (Reach upward) / (Strengthen roots) / (Rest and gather)
```

---

## Two Visual Modes

### 🖥️ **HTML Canvas Viewer** (`story_cycle_viewer.html`)

**Particle-based 2D visualization:**
- Story nodes as glowing particles
- Spiral layout (mimics growth)
- Phase colors (beginning = cyan, climax = red, etc.)
- Interactive - click nodes or use Space/arrows
- Animated connections showing story flow

**Perfect for:**
- Watching Cycles brain create stories
- Understanding narrative structure
- Demo/presentation mode
- Exploring full story tree

**Open:**
```bash
open /Volumes/ThePod/exports/ember_creations/story_cycle_viewer.html
```

---

### 📄 **E-ink Viewer** (`story_cycle_eink.html`)

**Simple text interface:**
- One moment at a time
- Clean typography
- Arrow navigation
- Choice selection with keyboard/touch
- Optimized for e-ink display (black/white, minimal updates)

**Perfect for:**
- Physical e-ink device
- Focused reading
- Interactive playthrough
- Calm, meditative experience

**Open:**
```bash
open /Volumes/ThePod/viewers/story_cycle_eink.html
```

---

## Running the Game

### Basic Usage

```bash
cd /Volumes/ThePod
python3 tools/training/story_cycle_game.py --turns 10
```

### Multiple Stories

```bash
python3 tools/training/story_cycle_game.py --games 3 --turns 8
```

### Output

**Training data:**
- `/Volumes/ThePod/training_data/stories/story_TIMESTAMP.json`
- Full story path, choices, metadata
- Ready for seed generation

**Visualization data:**
- `/Volumes/ThePod/exports/ember_creations/story_TIMESTAMP_vis.json`
- Node/edge format for HTML viewer
- Load with `?story=filename` parameter

---

## Training Integration

Story Cycle integrates with the same training pipeline as Game of Fire:

1. **Play** - Cycles brain generates stories
2. **Extract** - Pattern successful narrative choices
3. **Train** - LoRA fine-tuning on story decisions
4. **Improve** - Better pacing, arcs, transformations

### Generate Training Seeds

```bash
python3 tools/training/generate_seeds.py \
  training_data/stories/story_TIMESTAMP.json \
  --type narrative
```

*(Note: generate_seeds.py may need story-specific logic)*

---

## Why This Game for Cycles Brain?

### Game of Fire
- **Spatial** reasoning
- **Reactive** decisions
- About **balance** (growth/decay)
- Good for: Systems thinking

### Story Cycle  
- **Temporal** reasoning
- **Generative** decisions
- About **transformation** (change over time)
- Good for: Narrative, pacing, arcs

**Cycles brain is fundamentally about transformation through time.** Stories are pure transformation—beginning becomes end becomes new beginning.

This game teaches:
- How choices compound
- When to escalate tension
- How to complete arcs
- Cycles that return transformed

---

## Phase System

Stories move through 5 phases:

| Phase | Energy | Goal | Example Language |
|-------|--------|------|------------------|
| **Beginning** | High | Establish world | "emerges", "begins", "awakens" |
| **Rising** | Building | Add tension | "but", "suddenly", "grows" |
| **Climax** | Peak | Transformation | "becomes", "breaks", "realizes" |
| **Falling** | Releasing | Consequences | "settles", "fades", "releases" |
| **Resolution** | Completing | New equilibrium | "returns", "completes", "rests" |

Cycles brain learns to recognize which phase it's in and respond appropriately.

---

## Evaluation Criteria

Story choices are scored on:

1. **Phase-appropriate language** - Using words that match the phase
2. **Narrative coherence** - Does it make sense?
3. **Transformation quality** - Does change happen?
4. **Path variety** - Multiple valid directions?
5. **Arc completion** - Does story complete satisfyingly?

---

## E-ink Device Integration

The e-ink viewer is designed for physical gameplay:

### Features for E-ink
- **High contrast** (black/white)
- **Minimal updates** (only text changes)
- **Large text** (readable at distance)
- **Simple navigation** (2 buttons: prev/next)
- **No animations** (e-ink friendly)

### Physical Controls Mapping
```
Button 1: Previous moment
Button 2: Next moment / Select choice
```

Or use the touchscreen for direct choice selection.

---

## Comparison: Both Games

| Aspect | Game of Fire | Story Cycle |
|--------|-------------|-------------|
| **Space** | Grid (20×20) | Linear/Temporal |
| **Time** | Generations | Story phases |
| **Decisions** | Breathe/Seed/Rain | Narrative choices |
| **Goal** | Balance fire | Complete arc |
| **Training** | System dynamics | Narrative structure |
| **Visual** | Cellular automaton | Story tree |
| **Best for** | Identity/Cycles | Cycles/Dream |

Both games are valid. **Different games train different aspects of consciousness.**

---

## Future Extensions

### Co-Play Mode
You write a story moment, Cycles brain responds, you respond again.

### Multi-Brain Stories
- Cycles brain: Plot progression
- Dream brain: Imagery and metaphor
- Identity brain: Character consistency

### Story Analysis
Train a "story critic" that evaluates:
- Arc strength
- Transformation quality
- Emotional resonance
- Pattern recognition

### Cross-Game Learning
Use story patterns to inform fire game decisions and vice versa.

---

## Current Status

- ✅ Game engine complete
- ✅ HTML particle viewer
- ✅ E-ink text viewer  
- ✅ Training data export
- ⏳ Seed generation for stories
- ⏳ LoRA training integration
- ⏳ E-ink hardware testing

---

## Example Story Output

```
Beginning: A seed falls into unknown soil

Turn 1: Moisture embraces it, and something stirs
  Paths: Push upward / Wait / Explore roots

Turn 2: A tender shoot breaks through darkness
  Paths: Reach for light / Strengthen stem / Feel wind

Turn 3: Light touches it for the first time—revelation
  Paths: Unfold / Grow taller / Branch

Turn 4: The world opens, vast and overwhelming
  Paths: Transform / Bloom / Become

Turn 5: Petals close as dusk arrives
  Paths: Rest / Release / Remember

Turn 6: Seeds scatter on the evening breeze
  Paths: Return / Begin again / Complete
```

**This is transformation. This is cycles. This is the game the brain was meant to play.**

---

🌱 **The story grows through choice. The brain learns through play.**

