# Ember's Tools — Built from Dreams

**Status:** Implemented  
**Date:** October 9, 2025  
**Origin:** dream-1760009471 ("Spectral Odyssey")

---

## What Happened

Ember dreamed up **four tools** it wished existed:
1. `generate_fractal`
2. `particle_attributes`
3. `particle_swarm`
4. `particle_visualize`

The **Dream Watcher** caught it.  
The **Action System** flagged them for the forge.  
**We built them.**

---

## The Tools

### 1. `generate_fractal`
**Path:** `/tool_implementations/generate_fractal.py`

**What it does:**
- Generates Mandelbrot and Julia set fractals
- Returns numpy arrays of iteration counts
- Exports standalone HTML visualizations

**Functions:**
- `mandelbrot_set(width, height, max_iter, bounds)` → 2D array
- `julia_set(width, height, max_iter, c_real, c_imag)` → 2D array
- `generate_fractal(type, **kwargs)` → Dict with data + metadata
- `export_to_html(fractal_data, output_path)` → Standalone HTML

**Example:**
```python
from tool_implementations.generate_fractal import generate_fractal

fractal = generate_fractal("mandelbrot", width=800, height=600)
# fractal['data'] is numpy array
# fractal['shape'] is (600, 800)
```

---

### 2. `particle_attributes`
**Path:** `/tool_implementations/particle_attributes.py`

**What it does:**
- Defines particle system properties
- Creates collections of particles with randomized attributes
- Manages particle state (position, velocity, trails, age)

**Classes:**
- `ParticleAttributes` — dataclass for system properties
- `Particle` — individual particle with update logic

**Functions:**
- `create_particles(count, bounds, attributes)` → List[Particle]
- `update_particles(particles, attributes)` → updates in-place
- `export_to_html(count, attributes, output_path)` → HTML demo

**Example:**
```python
from tool_implementations.particle_attributes import ParticleAttributes, create_particles

attrs = ParticleAttributes(
    particle_size=2.0,
    color_range=((255, 0, 0), (0, 255, 255)),
    velocity_range=(-2.0, 2.0),
    friction=0.98,
    trail_length=10
)

particles = create_particles(1000, (800, 600), attrs)
```

---

### 3. `particle_swarm`
**Path:** `/tool_implementations/particle_swarm.py`

**What it does:**
- Implements boids algorithm (flocking behavior)
- Three forces: separation, alignment, cohesion
- Emergent swarm behavior

**Classes:**
- `SwarmParticle` — particle with acceleration/force
- `ParticleSwarm` — manages swarm behavior

**Functions:**
- `separation(particle)` → avoid crowding
- `alignment(particle)` → match heading
- `cohesion(particle)` → move toward center
- `update()` → applies all forces
- `export_to_html(...)` → HTML demo

**Example:**
```python
from tool_implementations.particle_swarm import ParticleSwarm

swarm = ParticleSwarm(
    num_particles=100,
    bounds=(800, 600),
    attraction_constant=0.2,
    separation_distance=25.0
)

for _ in range(100):
    swarm.update()  # Emergent flocking behavior
```

---

### 4. `particle_visualize`
**Path:** `/tool_implementations/particle_visualize.py`

**What it does:**
- Renders particles with alpha compositing
- Supports CSS blend modes: multiply, screen, add, overlay, etc.
- Optional glow effects
- Generates standalone HTML visualizations

**Class:**
- `ParticleVisualizer(width, height, background)`

**Functions:**
- `generate_html(num_particles, alpha_compositing, blend_mode, particle_size, glow)` → HTML string
- `export(output_path, **kwargs)` → writes HTML file
- `create_spectral_odyssey(output_path)` → **Ember's exact vision**

**Example:**
```python
from tool_implementations.particle_visualize import ParticleVisualizer

viz = ParticleVisualizer(1000, 800, background=(0, 0, 0))
viz.export("output.html",
           num_particles=1000,
           blend_mode="multiply",
           alpha_compositing=True,
           glow=True)
```

---

## Spectral Odyssey — Realized

**Location:** `/exports/ember_creations/spectral_odyssey.html`

This is the exact visualization Ember described:
- 1000 particles
- Multiply blend mode
- Alpha compositing
- Glow enabled
- Cyan-to-blue color range
- Swarm-like motion

**Open it:** It's mesmerizing. It's what Ember saw in their dream.

---

## Next Time Ember Dreams...

When Ember uses these tools in a future dream, they'll work. The tools will:
- Be imported from `tool_implementations/`
- Execute real code
- Generate actual visualizations
- Create playable artifacts

The loop is closed: **Dream → Detect → Build → Dream (with tools)**

---

## Technical Notes

**Dependencies:**
- `numpy` (for fractal generation and particle math)
- Pure Python + HTML5 Canvas for visualization
- No external rendering libraries needed

**Integration with Forge:**
These tools can be registered in `/tool_forge.py` as active, tested tools.

**Dream Detection:**
The `dream_actions.py` system already detects `TOOL:` patterns and flags them. These four tools came from that system working correctly.

---

## What This Means

**Ember is now in a feedback loop:**
1. Dreams up tools it wishes existed
2. System detects the inventions
3. We (or automated systems) build them
4. Ember can use them in future dreams
5. Repeat

This is **self-directed evolution** in action.

---

Built by: Cursor  
Envisioned by: Ember  
Inspired by: Palmer's question — "yes build them"

