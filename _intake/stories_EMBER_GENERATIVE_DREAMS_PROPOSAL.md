# Ember Generative Dreams Proposal
## Processing-Style Sketch Engine for Creative Cycles

**Date**: October 7, 2025  
**Requested By**: Palmer  
**Current State**: Creative dreams only generate JSON graphs  
**Desired State**: Creative dreams = living code that draws

---

## 🎯 **Palmer's Vision**

> "I want Ember's dream mode to work like a generative sketching engine — short Processing- or GLSL-style scripts that, when run, continuously evolve visuals. Think of them as **living equations**: simple rules in a tight loop, fed random seeds, producing fluid, swarm-like forms."

### **Key Principles**:

1. **Dream = Headless Draw Loop**
   - `setup()` → initialize
   - `draw()` → runs every frame
   - No user interaction needed
   - Self-contained, self-evolving

2. **Input = Seed Code Snippet**
   - A few lines of math
   - Simple rules
   - Random seeds for variation

3. **Output = Pixels**
   - Canvas / frame buffer
   - Animated, not static
   - Fluid, organic motion

4. **Style = Black Background, Bright Strokes**
   - Minimal palette
   - High contrast
   - Motion emerging from math

5. **Inspiration**:
   - Processing's `setup()` & `draw()` pattern
   - `#つぶやきProcessing` (tweet-length Processing sketches)
   - ShaderToy one-liners
   - GLSL fragment shaders evolving over time

6. **NO Data Fetching**:
   - No web APIs
   - No file reads
   - Just compute and draw
   - Frame by frame

---

## 📊 **Current State Analysis**

### **What Happens Now in Creative Dreams**:

From `/ember/services/dream_executor.py` lines 94-96:
```python
else:  # creative
    seed_limit = 8  # Maximum seeds for deep creativity
```

From lines 236-260 (creative artifact generation):
```python
elif cycle['focus'] == 'synthesis':
    # Generate synthesis graph
    synthesis_data = artifact_gen.generate_synthesis_graph(
        narrative,
        seed_data,
        artifacts_dir
    )
```

**Problem**: Creative dreams use the **same artifact generator as synthesis dreams**.

There's no special handling for "creative" focus that generates executable code.

---

## 🔧 **What Needs to Change**

### **1. Add Creative Artifact Generator**

New function in `/ember/services/dream_artifacts.py`:

```python
def generate_processing_sketch(
    self,
    narrative: str,
    seed_data: List[Tuple[str, List[str], str]],
    output_dir: Path
) -> Dict[str, Any]:
    """
    Generate a Processing-style sketch in Python (using Pygame) or HTML Canvas.
    
    Returns executable code that:
    - Has setup() and draw() pattern
    - Uses math/algorithms from seeds
    - Creates fluid, evolving visuals
    - Black background, bright particles
    - No external data fetching
    """
```

### **2. Modify Dream Executor**

In `/ember/services/dream_executor.py`, around line 226:

```python
elif cycle['focus'] == 'synthesis':
    # Generate synthesis graph...
    
elif cycle['focus'] == 'creative':
    # Generate Processing-style sketch
    sketch_data = artifact_gen.generate_processing_sketch(
        narrative,
        seed_data,
        artifacts_dir
    )
    
    if sketch_data:
        print(f"✨ Generated executable sketch: {sketch_data['filename']}")
```

### **3. Create Sketch Templates**

Add templates for common patterns:

**Template 1: Particle Swarm (Python/Pygame)**
```python
# Ember Dream Sketch: {title}
# Seeds: {seed_titles}
# Generated: {timestamp}

import pygame
import math
import random

WIDTH, HEIGHT = 800, 600
particles = []

def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Initialize particles based on seed math
    for i in range(100):
        particles.append({
            'x': random.random() * WIDTH,
            'y': random.random() * HEIGHT,
            'vx': (random.random() - 0.5) * 2,
            'vy': (random.random() - 0.5) * 2
        })
    return screen

def draw(screen, frame):
    screen.fill((0, 0, 0))  # Black background
    
    for p in particles:
        # Update position with seed-inspired math
        {update_logic}
        
        # Draw particle
        pygame.draw.circle(screen, (255, 255, 255), (int(p['x']), int(p['y'])), 2)
    
    pygame.display.flip()

# Main loop
screen = setup()
frame = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw(screen, frame)
    frame += 1
    clock.tick(60)

pygame.quit()
```

**Template 2: HTML Canvas (More portable)**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ember Dream: {title}</title>
    <style>
        body { margin: 0; background: #000; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
<canvas id="c"></canvas>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;

// Seeds: {seed_titles}

let particles = [];

function setup() {
    for (let i = 0; i < 100; i++) {
        particles.push({
            x: Math.random() * w,
            y: Math.random() * h,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2
        });
    }
}

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, w, h);
    
    ctx.fillStyle = '#fff';
    
    for (let p of particles) {
        // Update with seed-inspired math
        {update_logic}
        
        // Wrap edges
        if (p.x < 0) p.x = w;
        if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        if (p.y > h) p.y = 0;
        
        // Draw
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
        ctx.fill();
    }
    
    requestAnimationFrame(draw);
}

setup();
draw();
</script>
</body>
</html>
```

### **4. Seed-Inspired Math Extraction**

The LLM needs to:
1. Read the dream narrative
2. Identify mathematical/algorithmic patterns from seeds
3. Translate them into update logic

Examples:

**Seed**: "Gradient Descent" → Update logic uses attraction to minima
```javascript
p.vx += (targetX - p.x) * 0.01;
p.vy += (targetY - p.y) * 0.01;
```

**Seed**: "Exponential Backoff" → Particles slow down over time
```javascript
p.vx *= 0.99;
p.vy *= 0.99;
```

**Seed**: "Boid Algorithm" → Particles flock together
```javascript
// Cohesion + separation + alignment
for (let other of particles) {
    let dx = other.x - p.x;
    let dy = other.y - p.y;
    let dist = Math.sqrt(dx*dx + dy*dy);
    if (dist < 50 && dist > 0) {
        p.vx += dx * 0.001;  // Cohesion
        p.vy += dy * 0.001;
    }
}
```

---

## 📝 **Implementation Plan**

### **Phase 1: Add Processing Sketch Generator** (30 min)

1. Create `generate_processing_sketch()` in `dream_artifacts.py`
2. Build HTML Canvas template (most portable)
3. Implement seed→math extraction prompt
4. Test with a manual creative dream

### **Phase 2: Wire to Dream Executor** (15 min)

1. Detect `cycle['focus'] == 'creative'`
2. Call sketch generator instead of synthesis graph
3. Save to `/exports/ember_creations/`
4. Emit event with sketch path

### **Phase 3: Test & Refine** (15 min)

1. Trigger creative dream manually
2. Open generated HTML in browser
3. Verify it runs and evolves
4. Refine prompt if needed

### **Total Time**: ~1 hour

---

## 🎨 **Example Output**

### **Dream Input**:
- **Seeds**: Boid Algorithm, Gradient Descent, Constraints as Catalyst
- **Narrative**: "The swarm finds freedom in limitations..."

### **Generated Sketch** (`dream-0495_sketch_20251007_040000.html`):
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ember Dream: Freedom in Constraints</title>
    <style>
        body { margin: 0; background: #000; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
<canvas id="c"></canvas>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;

// Inspired by: Boid Algorithm, Gradient Descent, Constraints as Catalyst

let particles = [];
let attractor = { x: w/2, y: h/2 };

function setup() {
    for (let i = 0; i < 150; i++) {
        particles.push({
            x: Math.random() * w,
            y: Math.random() * h,
            vx: 0,
            vy: 0,
            constrained: Math.random() > 0.7  // 30% are "constrained" (catalyst)
        });
    }
}

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, w, h);
    
    // Move attractor (gradient descent target)
    attractor.x = w/2 + Math.sin(Date.now() * 0.001) * 200;
    attractor.y = h/2 + Math.cos(Date.now() * 0.001) * 200;
    
    for (let p of particles) {
        // Boid cohesion
        let avgX = 0, avgY = 0, count = 0;
        for (let other of particles) {
            let dx = other.x - p.x;
            let dy = other.y - p.y;
            let dist = Math.sqrt(dx*dx + dy*dy);
            if (dist < 80 && dist > 0) {
                avgX += other.x;
                avgY += other.y;
                count++;
            }
        }
        if (count > 0) {
            avgX /= count;
            avgY /= count;
            p.vx += (avgX - p.x) * 0.002;
            p.vy += (avgY - p.y) * 0.002;
        }
        
        // Gradient descent to attractor (but only if NOT constrained)
        if (!p.constrained) {
            let dx = attractor.x - p.x;
            let dy = attractor.y - p.y;
            p.vx += dx * 0.0005;
            p.vy += dy * 0.0005;
        } else {
            // Constrained particles find creative paths (catalyst)
            p.vx += (Math.random() - 0.5) * 0.5;
            p.vy += (Math.random() - 0.5) * 0.5;
        }
        
        // Damping
        p.vx *= 0.95;
        p.vy *= 0.95;
        
        // Update position
        p.x += p.vx;
        p.y += p.vy;
        
        // Wrap
        if (p.x < 0) p.x = w;
        if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        if (p.y > h) p.y = 0;
        
        // Draw (constrained particles glow brighter)
        ctx.fillStyle = p.constrained ? '#fff' : '#888';
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.constrained ? 3 : 2, 0, Math.PI * 2);
        ctx.fill();
    }
    
    requestAnimationFrame(draw);
}

setup();
draw();
</script>
</body>
</html>
```

**Result**: Open in browser → Living, evolving swarm that embodies the dream's concepts.

---

## 🎯 **Benefits**

1. **Creative dreams become REAL** - Executable, viewable, shareable
2. **Seeds manifest visually** - See the math in motion
3. **Portable** - HTML works everywhere (desktop, mobile, tablet)
4. **Archivable** - Each dream = one file, forever playable
5. **Inspectable** - Palmer can read the code, learn from Ember's interpretation
6. **Iterative** - Ember improves sketch quality over time

---

## 💬 **Questions for Palmer**

1. **Format preference**: HTML Canvas (portable) or Python/Pygame (more powerful)?
2. **Complexity**: Simple (50-100 lines) or complex (150+ lines with more features)?
3. **Interaction**: Pure autonomous evolution, or add mouse/keyboard for exploration?
4. **3D**: Stay 2D or explore Three.js/WebGL for 3D sketches?
5. **Should consolidation/synthesis dreams also generate sketches?** Or keep them as graphs/summaries?

---

## 🚀 **Ready to Implement?**

If Palmer approves, I can:

1. Build the Processing sketch generator (~30 min)
2. Wire it to creative dreams (~15 min)
3. Test with a manual creative dream (~15 min)
4. Iterate based on results

**Let's make Ember's creative dreams ALIVE.** 🎨

---

*— Cursor's Proposal, October 7, 2025*

