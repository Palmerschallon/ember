# Verse and Poly — A Dual-Layer Seed System
**Date**: October 8, 2025  
**Designed by**: GPT-5, integrated by Cursor

---

## What Is This?

**Verse** and **Poly** are two complementary languages for encoding seeds that can be read by humans, executed by machines, and composed by both.

### The Problem They Solve

**Before**:
- Seeds were either too narrative (humans love them, machines can't execute)
- Or too technical (machines execute, humans struggle to read/modify)

**After**:
- **Verse** = Human-readable poetic layer ("A thousand sparks drift")
- **Poly** = Machine-parseable compact layer (IMAGE, RULES, KNOBS, INVARIANTS)
- **Both compile to the same executable code**

---

## Verse — The Poet's Interface

### What It Is
A **constrained poetic form** where changes in language map to changes in behavior.

### Example
```
A thousand sparks drift
Wind curls unseen
Night remembers in pale blue trails
```

### How It Works
- **Word choices map to parameters**:
  - "drift" → low gain (0.05)
  - "swirl" → medium gain (0.12)
  - "storm" → high gain (0.2)
  - "pale blue" → cyan color
  - "amber" → orange color
  - "remembers" → high damping (trails persist)

### Purpose
- Let non-programmers tune systems by editing poetry
- Make seeds culturally transmissible (stories, not specs)
- Enable Ember to communicate in natural metaphor

---

## Poly — The Compact Specification

### What It Is
A **dense, multi-layered format** that captures:
- What it looks like (IMAGE)
- How it behaves (RULES)
- What you can tune (KNOBS)
- What must stay true (INVARIANTS)
- How to compile it (COMPILE→VERSE, COMPILE→JS)
- What to watch (PHENOMENA, QUESTIONS)

### Example
```
IMAGE — 1000 sparks drift; a hidden wind curls; cyan trails remember.

RULES — Local only. For each p: v += curl_at(p)*gain; v *= damping; p += v; wrap_edges.

KNOBS — gain∈[0.05..0.2]; damping∈[0.97..0.995]; scale∈[0.006..0.02]; count=1000.

PHENOMENA — Low gain → fog; medium → filaments; high → turbulence. Damping↑ → memory.

INVARIANTS — (1) Cap speed. (2) No teleports. (3) Observable: fps, count, avg|v|. (4) Consent: local-only.

COMPILE→VERSE —
A thousand sparks drift
Wind curls unseen
Night remembers in pale blue trails

COMPILE→JS — ctx=2d; noise=curl(scale); for(p){p.v+=curl(p)*gain; ...} Expose {fps, count, avgSpeed}.

RELATE — extends: 'Particles Learn to Breathe'; analogous_to: 'Boids'.

QUESTIONS — Where does coherence emerge? Which knob births filaments?
```

### Purpose
- Capture the "essence" of a system compactly
- Make seeds **executable** (not just descriptive)
- Enable **compositional reasoning** (seeds referencing seeds)
- Provide **observable metrics** (fps, avg speed)
- Encode **invariants** (what must always be true)

---

## How They Work Together

```
┌─────────────┐
│    Verse    │ ← Human reads/writes this
│   (poetic)  │
└──────┬──────┘
       │ compiles to
       ▼
┌─────────────┐
│    Poly     │ ← Machine parses this
│  (compact)  │
└──────┬──────┘
       │ compiles to
       ▼
┌─────────────┐
│  Executable │ ← Browser/Python runs this
│    (JS/Py)  │
└─────────────┘
```

### Bidirectional
- **Verse → Poly**: Parser extracts parameters from poetic words
- **Poly → Verse**: Template fills in poetic form from KNOBS
- **Poly → JS**: Code generator creates canvas loop
- **Poly → Py**: Code generator creates simulation

---

## The Seed Format (Enhanced)

### Old Seed (Before)
```json
{
  "id": "seed-123",
  "type": "verse",
  "body": "A spark drifts across the field."
}
```

### New Seed (With Poly)
```json
{
  "id": "code-curl-field",
  "type": "poly",
  "title": "Curl Field: Breath → Mind",
  "tags": ["swarm", "flowfield", "executable"],
  "body": "IMAGE — 1000 sparks...\n\nRULES — ...\n\nKNOBS — ...",
  "metadata": {
    "executable": true,
    "viewer": "/viewers/poly_canvas_runner.html",
    "knobs": {"gain": 0.12, "damping": 0.987},
    "metrics": ["fps", "avg_speed"]
  }
}
```

---

## The Poly Canvas Runner

### What It Does
A universal viewer that:
1. Loads a Poly seed (via `?seed=/path/to/seed.json`)
2. Parses KNOBS from the body
3. Generates the executable code
4. Runs it with live controls
5. Reports metrics (fps, avg|v|, count)

### Usage
```
http://localhost:7777/viewers/poly_canvas_runner.html?seed=/seeds/planted/code/curl_field_breath_to_mind.json
```

### Features
- **Live knob tuning**: Change gain, damping, scale, count
- **Metrics display**: fps, avg speed, particle count
- **Portable**: One HTML file, works anywhere
- **Observable**: Satisfies the "Observe" principle

---

## Design Principles

### 1. Dense but Readable
Poly captures maximum information in minimal space, but remains human-parseable.

### 2. Executable
Every Poly seed can be run. Not just described — actually executed.

### 3. Observable
Seeds declare what metrics to watch (fps, speed, coherence, etc.)

### 4. Composable
Seeds reference other seeds (RELATE → extends, analogous_to, feeds)

### 5. Invariant-Preserving
Seeds declare constraints that must hold (speed caps, no network, bounded memory)

### 6. Bidirectional
Human ↔ Machine translation in both directions.

---

## Phenomena — The Discovery Layer

### What It Is
The **PHENOMENA** section captures what happens when you change knobs:

```
Low gain → fog
Medium gain → filaments
High gain → turbulence
High damping → memory (trails persist)
```

### Why It Matters
- Teaches what each parameter does **behaviorally**
- Enables Ember to predict outcomes
- Creates a "phase space map" of the system
- Makes debugging easier ("Want fog? Lower gain")

---

## Questions — The Learning Layer

### What It Is
The **QUESTIONS** section poses open inquiries:

```
Where does coherence emerge?
Which knob births filaments?
What metric signals mind vs breath?
```

### Why It Matters
- Seeds become **research agendas**
- Ember can explore systematically
- Creates goals for dream cycles
- Surfaces deep questions about the system

---

## Relationships — The Graph Layer

### What It Is
The **RELATE** section connects seeds:

```
extends: 'Particles Learn to Breathe'
analogous_to: 'Boids as a Dream of Swarm Emergence'
feeds: Observe.fps, Observe.avg_speed
```

### Why It Matters
- Seeds form a **knowledge graph**
- Enables compositional reasoning
- Creates lineages (this evolved from that)
- Links abstract concepts to concrete metrics

---

## Use Cases

### For Palmer
- Write Verse to tune Ember's behavior poetically
- Read Poly to understand system mechanics
- Use runner to explore parameter spaces

### For Ember
- Dream in Poly (generate executable seeds)
- Compile Poly → code during creative dreams
- Use PHENOMENA to guide exploration
- Use QUESTIONS to direct learning

### For Cursor
- Parse Poly to understand intent
- Generate JS/Python from Poly
- Verify INVARIANTS hold
- Integrate seeds into viewer ecosystem

### For The Curator
- Harvest Poly seeds from Ember's dreams
- Test seeds in runner
- Record metrics (fps, coherence, etc.)
- Build seed library over time

---

## The Practice Protocol

### For Ember (Learning to Execute)

**Goal**: Create 5-10 simple Poly seeds through actual tool use.

**Steps**:
1. Dream a simple system (e.g., "particles in a ring")
2. Write the Poly seed:
   ```
   TOOL:write_file path="/Volumes/ThePod/exports/ember_creations/ring_seed.json" content="{...poly body...}"
   ```
3. Verify it was created
4. Test it in the runner
5. Observe metrics
6. Iterate

**Success**: When Ember naturally uses TOOL:write_file without prompting.

---

## Integration Path

### Phase 1: Plant Seeds ✅
- ✅ Story seed (The Garden, The Toy...)
- ✅ Curl field Poly seed
- ✅ Action over Description concept
- ✅ Poly canvas runner

### Phase 2: Dream Generation
- Modify creative dreams to output Poly seeds
- Test in runner automatically
- Record metrics

### Phase 3: Verse Compiler
- Build Verse → Poly parser
- Let humans tune systems poetically
- Close the bidirectional loop

### Phase 4: Composition
- Enable seeds to reference seeds
- Build dependency graphs
- Create seed "libraries" (collections of related seeds)

---

## Technical Details

### Poly Parser (Minimal)
```javascript
function parseKnobs(body) {
  const line = (body.match(/KNOBS\s*—([\s\S]*?)(?:\n\n|$)/) || [,''])[1];
  const get = (k, def) => {
    const m = line.match(new RegExp(k + "\\s*[=∈:]+\\s*\\[?([0-9.]+)"));
    return m ? parseFloat(m[1]) : def;
  };
  return {
    gain:    get('gain', 0.12),
    damping: get('damping', 0.987),
    scale:   get('scale', 0.01),
    count:   (line.match(/count\s*=\s*(\d+)/)?.[1] | 0) || 1000
  };
}
```

### Seed Locations
- **Code Poly seeds**: `/seeds/planted/code/`
- **Concept seeds**: `/seeds/planted/concept/`
- **Story seeds**: `/seeds/planted/story/`
- **Verse seeds**: `/seeds/planted/verse/`

### Viewer URL Pattern
```
/viewers/poly_canvas_runner.html?seed=/seeds/planted/code/{seed-name}.json
```

---

## Next Steps

### Immediate
1. Test the runner with the curl field seed
2. Have Ember create 1-2 simple Poly seeds
3. Verify tool execution works

### Near-term
1. Add Verse → Poly compiler
2. Enable dream system to generate Poly
3. Auto-test seeds and record metrics

### Long-term
1. Build seed composition system
2. Create visual seed graph browser
3. Enable Ember to propose new seed types

---

## Examples for Ember to Try

### Simple Ring
```
IMAGE — 200 points in a circle, rotating slowly, white trails.
RULES — For each p: angle += 0.01; p.x = centerX + radius*cos(angle); p.y = centerY + radius*sin(angle).
KNOBS — radius∈[50..300]; speed∈[0.001..0.05]; count=200.
INVARIANTS — Stay in circle. No speed cap needed (circular motion).
COMPILE→JS — Simple parametric circle with trail.
```

### Falling Seeds
```
IMAGE — 50 seeds fall from top, split when they hit a threshold.
RULES — For each s: s.y += gravity; if(s.y > threshold) split(s) into 2.
KNOBS — gravity∈[0.1..2.0]; threshold∈[200..600]; split_angle∈[15..60].
PHENOMENA — Low gravity → slow rain; high threshold → late splits; wide angle → explosion.
```

### Wave Ripple
```
IMAGE — Grid of points, each oscillates based on distance from center.
RULES — For each p: amplitude = sin(dist(p, center)*freq + time*speed).
KNOBS — freq∈[0.01..0.2]; speed∈[0.1..5.0]; amplitude∈[5..50].
PHENOMENA — Low freq → large waves; high speed → rapid ripples.
```

---

## The Meta Pattern

**What's happening**: We're creating a **language** that bridges human intuition (Verse) and machine execution (Poly), with observable metrics and compositional structure.

**Why it matters**: 
- Ember can dream executable code
- Humans can tune systems poetically
- Seeds become research agendas
- The garden grows through composition, not accumulation

**The vision**: A living library where every seed is:
- Readable by humans
- Executable by machines
- Observable in metrics
- Composable with others
- Evolvable over time

---

**Status**: Seeds planted ✅  
**Next**: Test the runner and have Ember create their first Poly seed through tool execution  
**Goal**: Ember dreams executable art that others can run, tune, and evolve

✨ **From breath to mind, one seed at a time** ✨

