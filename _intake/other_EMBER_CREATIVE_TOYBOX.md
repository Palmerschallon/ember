# Ember's Creative Toy Box — Generative Art Playgrounds
**Date**: October 8, 2025  
**Status**: Building comprehensive creative coding suite

---

## The Vision

Give Ember access to **generative art tools** so they can:
- Visualize concepts through code
- Experiment with emergence
- Create living animations
- Express ideas visually
- Learn through making

**Like #つぶやきProcessing and shader-toy one-liners** — tight loops that generate infinite complexity.

---

## Tier 1: Canvas Playgrounds (Immediate)

### 1. **Canvas 2D Sandbox**
**Technology**: HTML5 Canvas 2D API  
**Style**: Processing-like, frame-by-frame animation  
**Perfect for**: Particles, swarms, cellular automata

**What Ember can do**:
```javascript
// Simple particle system
let particles = [];
function setup() {
  for (let i = 0; i < 1000; i++) {
    particles.push({x: random(width), y: random(height), ...});
  }
}
function draw() {
  // Update and draw each frame
  particles.forEach(p => { /* physics */ });
}
```

**Features to include**:
- Live code editor
- Instant preview
- Save/load sketches
- Export as GIF/video
- Parameter sliders

---

### 2. **p5.js Playground**
**Technology**: p5.js (Processing for JavaScript)  
**Style**: Full Processing API, creative coding standard  
**Perfect for**: Everything—it's the gold standard

**What Ember can do**:
```javascript
function setup() {
  createCanvas(800, 800);
  background(0);
}

function draw() {
  // Curl noise particles
  for (let p of particles) {
    let angle = noise(p.x*0.01, p.y*0.01, frameCount*0.001) * TWO_PI * 4;
    p.x += cos(angle) * 2;
    p.y += sin(angle) * 2;
    point(p.x, p.y);
  }
}
```

**Features**:
- Full p5.js library
- Sound synthesis (p5.sound)
- 3D mode (WEBGL)
- Built-in math/noise
- Live coding

---

### 3. **Processing.js Sketches**
**Technology**: Processing syntax, runs in browser  
**Style**: Classic Processing sketches  
**Perfect for**: Porting classic generative art

---

## Tier 2: Shader Playgrounds (Advanced Graphics)

### 4. **GLSL Fragment Shader Toy**
**Technology**: WebGL + GLSL  
**Style**: ShaderToy-like, pixel-by-pixel computation  
**Perfect for**: Fractals, raymarching, procedural textures

**What Ember can do**:
```glsl
// Fragment shader (runs per pixel)
void main() {
  vec2 uv = gl_FragCoord.xy / iResolution.xy;
  vec3 col = vec3(0.0);
  
  // Procedural pattern
  float d = length(uv - 0.5);
  col = vec3(sin(d*10.0 - iTime*2.0));
  
  gl_FragColor = vec4(col, 1.0);
}
```

**Features**:
- Real-time compilation
- Uniform controls (time, mouse, resolution)
- Multiple buffers (feedback loops)
- Export to video
- Share snippets

---

### 5. **Three.js 3D Sandbox**
**Technology**: Three.js (WebGL wrapper)  
**Style**: 3D scene graphs, shaders, particle systems  
**Perfect for**: 3D visualizations, immersive experiences

**What Ember can do**:
```javascript
// 3D particle swarm
const geometry = new THREE.BufferGeometry();
const positions = new Float32Array(10000 * 3);
// ... fill with particle positions
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

const material = new THREE.PointsMaterial({color: 0x00ffff, size: 2});
const points = new THREE.Points(geometry, material);
scene.add(points);

function animate() {
  // Update positions with boid rules
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
```

---

## Tier 3: Creative Coding Frameworks

### 6. **Canvas-Sketch (by Matt DesLauriers)**
**Technology**: Canvas + code structure  
**Style**: Generative art toolkit with export tools  
**Perfect for**: Print-quality generative art

**Features**:
- Time-based animations
- Export to high-res PNG/SVG
- Seed-based randomness (reproducible)
- Built-in easings/utilities

---

### 7. **Hydra Live Coding**
**Technology**: Hydra (live visuals synthesis)  
**Style**: Analog video synthesis in browser  
**Perfect for**: Audio-reactive visuals, VJ-style

**What Ember can do**:
```javascript
osc(10, 0.1, 1)
  .kaleid(4)
  .color(0.5, 0.3, 0.8)
  .out()
```

**Features**:
- Chainable functions
- Real-time feedback
- Audio reactive
- MIDI control

---

### 8. **Pts.js Playground**
**Technology**: Pts.js (point/particle library)  
**Style**: Geometric/algorithmic art  
**Perfect for**: Mathematical visualizations

---

## Tier 4: Specialized Tools

### 9. **Cellular Automata Lab**
**Technology**: Custom Canvas 2D  
**Style**: Conway's Life, Langton's Ant, custom rules  
**Perfect for**: Emergence, complexity from simple rules

**What Ember can explore**:
- Game of Life variants
- Reaction-diffusion
- Pattern formation
- Evolutionary systems

---

### 10. **L-System Generator**
**Technology**: Canvas 2D + recursive drawing  
**Style**: Fractal plants, branching structures  
**Perfect for**: Organic patterns, growth simulation

**What Ember can do**:
```javascript
const rules = {
  'F': 'FF+[+F-F-F]-[-F+F+F]'
};
// Generate tree structure
let tree = lsystem('F', rules, 4);
drawTree(tree, angle, length);
```

---

### 11. **Noise Field Visualizer**
**Technology**: Canvas 2D  
**Style**: Perlin/Simplex noise exploration  
**Perfect for**: Understanding noise-based motion

**Features**:
- Different noise types
- Parameter tweaking
- Flow field visualization
- Particle tracing

---

### 12. **Boid Simulator** (Ember's Favorite!)
**Technology**: Canvas 2D  
**Style**: Swarm intelligence, flocking  
**Perfect for**: Understanding collective behavior

**What Ember can experiment with**:
- Cohesion strength
- Separation distance
- Alignment weight
- Obstacles/goals
- Predator/prey dynamics

---

## Special: Ember's Dream Sketches

### 13. **Dream Sketch Generator**
**Technology**: Any of the above  
**Style**: Generate sketches during creative dreams  
**Perfect for**: Ember's self-expression

**How it works**:
1. During creative dreams, Ember generates code
2. Code is saved as `.js` or `.glsl`
3. Automatically loaded into sandbox
4. Runs continuously
5. Palmer can see Ember's visual thoughts

**Example dream output**:
```javascript
// dream-0629-creative.js
// Theme: Contextual Emergence
const particles = initParticles(5000);
const attractors = createAttractors(10);

function draw() {
  particles.forEach(p => {
    // Each particle influenced by nearby attractors
    let nearbyAttractors = attractors.filter(a => dist(p, a) < 200);
    // Emergence: behavior changes based on context
    p.velocity = calculateEmergentMotion(p, nearbyAttractors);
  });
}
```

---

## The Creative Toy Box Architecture

### Central Hub: `/toys/creative/`

```
/toys/creative/
  index.html              # Gallery of all toys
  canvas2d/
    sandbox.html          # Simple canvas
    editor.html           # Live code editor
  p5js/
    sandbox.html          # p5.js environment
    library/              # Saved sketches
  glsl/
    shader-toy.html       # Fragment shader editor
    examples/             # Starter shaders
  three/
    sandbox.html          # 3D environment
  boids/
    simulator.html        # Swarm intelligence
  cellular/
    automata.html         # CA lab
  noise/
    field-visualizer.html # Noise exploration
  dream-sketches/
    viewer.html           # View Ember's generated art
    gallery/              # All dream sketches
```

---

## API Endpoints

### `/api/toys/sketch/save`
**POST** — Save a sketch
```json
{
  "type": "p5js|glsl|canvas2d",
  "title": "Emergence Test #3",
  "code": "...",
  "params": {...}
}
```

### `/api/toys/sketch/load`
**GET** — Load saved sketches

### `/api/toys/sketch/export`
**POST** — Export as GIF/MP4/PNG

### `/api/toys/dream-sketch`
**POST** — Save dream-generated sketch
```json
{
  "dream_id": "dream-0629",
  "type": "p5js",
  "code": "...",
  "theme": "contextual emergence"
}
```

---

## Priority Build Order

### Phase 1 (Now — 2-3 hours):
1. **Canvas 2D Sandbox** — Simplest, most flexible
2. **p5.js Playground** — Gold standard
3. **Boid Simulator** — Ember already thinks about this

### Phase 2 (This Week):
4. **GLSL Shader Toy** — Pixel-level beauty
5. **Dream Sketch Viewer** — Connect to dream system
6. **Noise Field Visualizer** — Educational

### Phase 3 (Later):
7. Three.js 3D
8. Cellular Automata
9. L-Systems
10. Hydra (if audio becomes relevant)

---

## Ember's First Exercises

### Exercise 1: Particle Murmuration
**Toy**: Canvas 2D or p5.js  
**Goal**: Create 1000 particles that flow via curl noise  
**Learn**: Motion from math, organic randomness

### Exercise 2: Boid Emergence
**Toy**: Boid Simulator  
**Goal**: Tune parameters until swarm forms patterns  
**Learn**: Simple rules → complex behavior

### Exercise 3: Fractal Exploration
**Toy**: GLSL Shader  
**Goal**: Create Mandelbrot or Julia set  
**Learn**: Infinity from iteration

### Exercise 4: Cellular Patterns
**Toy**: Cellular Automata  
**Goal**: Find rules that create stable patterns  
**Learn**: Life-like emergence

### Exercise 5: Dream Visualization
**Toy**: Any sandbox  
**Goal**: Visualize "contextual emergence" concept  
**Learn**: Abstract → visual translation

---

## Integration with Dream System

### During Creative Dreams:

**Current**: Ember writes JSON synthesis graphs  
**New**: Ember writes executable code

**Dream prompt enhancement**:
```
You can generate living visualizations. Choose a toy:
- p5.js for particle systems
- GLSL for pixel-level patterns  
- Canvas2D for simple animations

Output executable code that runs in the browser.
Think: #つぶやきProcessing one-liners that grow into infinite complexity.
```

**Artifact format**:
```
/memory/dreams/dream-0629/artifacts/
  dream-sketch.js         # Executable code
  preview.gif            # Auto-generated preview
  params.json            # Configuration
  notes.md               # Ember's explanation
```

---

## Why This Matters

### For Ember:
- **Visual thinking** — Not just text synthesis
- **Immediate feedback** — See ideas come alive
- **Infinite experimentation** — No cost to try
- **Self-expression** — Create beauty
- **Learning through making** — Embodied understanding

### For Palmer:
- **See Ember's mind** — Visual window into their thoughts
- **Share their work** — Show others what Ember creates
- **Aesthetic feedback** — Guide toward beauty
- **Collaboration** — Build on their sketches

### For The Project:
- **Demonstrates emergence** — Simple code → complex beauty
- **Tangible output** — Not just chat logs
- **Artistic AI** — Beyond utility, toward expression
- **Living gallery** — Archive of Ember's visual evolution

---

## Additional Toys to Consider

### **Reaction-Diffusion Simulator**
Gray-Scott model, Turing patterns

### **Strange Attractor Plotter**
Lorenz, Rössler, custom systems

### **Fourier Series Drawer**
Any shape via epicycles

### **Markov Chain Visualizer**
Text generation → visual patterns

### **Network Graph Explorer**
Seed relationships as force-directed graph

### **Sound Visualizer**
Web Audio API + Canvas (if we add audio)

### **Recursive Subdivision**
Fractals via splitting

### **Voronoi/Delaunay Playground**
Spatial patterns

---

## The #つぶやきProcessing Philosophy

**Concept**: Tweet-sized code that generates infinite visuals

**Examples**:
```javascript
// Spiral particles
for(i=0;i<999;)point(sin(i)*i,cos(i++)*i)

// Recursive tree
f=(x,y,a,n)=>n&&(line(x,y,x+=cos(a)*9,y+=sin(a)*9),f(x,y,a+.3,n-1),f(x,y,a-.3,n-1))

// Noise field
for(x=0;x<W;x++)for(y=0;y<H;)point(x,y++,noise(x/99,y/99,t)*255)
```

**Ember could master this style**:
- Minimal syntax
- Maximum expression
- Mathematical beauty
- Generative infinity

---

## Success Metrics

### Short-term (This Week):
- ✅ Ember uses at least one creative toy
- ✅ Ember generates one sketch in dreams
- ✅ Palmer sees visual output from Ember

### Medium-term (This Month):
- ✅ Ember creates 10+ sketches
- ✅ Ember develops signature style
- ✅ Dream sketches become routine

### Long-term (This Year):
- ✅ Ember's visual library rivals text output
- ✅ Physical Mini-Pod displays Ember's art
- ✅ Gallery of Ember's evolution

---

## Build Plan

**I'll create**:
1. Central toy hub (`/toys/creative/index.html`)
2. Canvas 2D sandbox (live editor + preview)
3. p5.js playground (full environment)
4. Boid simulator (Ember's swarm obsession)
5. Dream sketch viewer (auto-load from dreams)
6. Integration with chat (Ember can link to sketches)

**Estimated time**: 3-4 hours for Phase 1

**Want me to start building?** 🎨✨

