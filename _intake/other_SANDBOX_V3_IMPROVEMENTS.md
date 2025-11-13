# Sandbox v3 Improvements
**Date**: October 7, 2025  
**Fixes**: Chat visibility, seed behaviors, visual variety

---

## Issues Fixed

### 1. Chat Input Not Visible ✅
**Problem**: Chat input was there but hard to see  
**Solution**: 
- Improved contrast and borders
- Added placeholder text
- Better focus states
- Larger, more visible input field

### 2. Seeds Don't Do Anything ✅
**Problem**: Clicking seeds just reset particles, same behavior  
**Solution**: **8 unique visual behaviors**:
- **Curl** — Divergence-free flow (original)
- **Spiral** — Inward/outward rotation
- **Wave** — Interference patterns
- **Turbulent** — Chaotic flow with randomness
- **Attractor** — Gravitational pull to moving point
- **Mandala** — Sacred geometry symmetry
- **Field** — Electric field lines
- **Vortex** — Dual swirling motion

### 3. Boring Seed Names ✅
**Problem**: Seeds have generic names  
**Solution**: 
- Seeds mapped to behaviors by keywords
- "Curl" → curl behavior
- "Spiral" → spiral behavior
- "Wave" → wave behavior
- "Turbulent/chaos" → turbulent
- Etc.

Even boring-named seeds now DO something interesting!

---

## How It Works

### Behavior Mapping
Each seed is analyzed for keywords:
```javascript
const title = seed.title.toLowerCase();
const body = seed.body.toLowerCase();

if (text.includes('curl')) return 'curl';
if (text.includes('spiral')) return 'spiral';
if (text.includes('wave')) return 'wave';
// ... etc
```

### Visual Algorithms
Each behavior has unique math:

**Curl** (divergence-free):
```javascript
vx = sin(y * k + t) * 0.6
vy = -cos(x * k - t) * 0.6
```

**Spiral**:
```javascript
angle = atan2(dy, dx)
vx = cos(angle + k*0.1) * 0.5
vy = sin(angle + k*0.1) * 0.5
```

**Attractor**:
```javascript
cx = centerX + sin(t * 0.5) * 200  // moving target
dx = cx - p.x
vx = dx / dist * 2 + sin(p.y * k)
```

---

## New Parameters

### Density (500-8000)
How many particles render

### Trail Length (0.01-0.15)
How fast previous frames fade  
- Low = sharp, crisp lines
- High = long, flowing trails

### Complexity (0.001-0.02)
The 'k' parameter in equations  
- Low = broad, smooth patterns
- High = dense, intricate details

---

## Canvas 2D

Yes, this uses **Canvas 2D**, not WebGL.

**Advantages**:
- Simple, fast, widely supported
- Can do 2000-8000 particles easily
- Perfect for 2D patterns

**Can it do dense Processing sketches?**

**Yes!** With optimizations:
1. **Increase density** → 5000-8000 particles
2. **Lower trail** → 0.01-0.02 (crisp lines)
3. **Adjust complexity** → 0.008-0.015 (intricate)
4. **Use field or mandala behaviors** → natural complexity

**For even more complexity**:
- Add multiple behavior layers
- Implement feedback loops
- Add color variation
- Use additive blending

**For 3D/WebGL complexity**:
- Would need to build separate WebGL toy
- Can achieve #つぶやきProcessing density
- Future enhancement

---

## Example Dense Setup

**Configuration**:
- Seed: "Mandala Symmetry" or "Electric Field"
- Density: 6000
- Trail: 0.02
- Complexity: 0.012
- Speed: 1.5x

**Result**: Dense, intricate, evolving patterns

---

## Ember Integration

When you chat:
```
"What's happening in this pattern?"
```

Ember receives:
```
[Context: Looking at seed "Mandala Symmetry" 
(mandala behavior) in sandbox] What's happening...
```

Ember knows:
- Which seed you're viewing
- What behavior it's using
- Can explain the math
- Can suggest variations

---

## Future Enhancements

### More Behaviors
- Reaction-diffusion
- Perlin noise fields
- Boids/flocking
- Cellular automata
- L-systems

### Color Modes
- Hue based on velocity
- Rainbow gradients
- Heat maps
- Complementary colors

### Compositing
- Mix multiple behaviors
- Layer effects
- Blend modes

### Export
- Save as image
- Record GIF
- Generate code

---

## Access

**v3 (Enhanced)**:
```
http://localhost:7777/toys/seed_sandbox_v3.html
```

**v2 (Original with chat)**:
```
http://localhost:7777/toys/seed_sandbox_v2.html
```

---

## Try These Seeds

**Best for visual exploration**:
1. Any seed with "curl", "flow", "field" → Flow patterns
2. Any seed with "spiral", "rotation" → Circular motion
3. Any seed with "symmetry", "pattern" → Geometric
4. Any seed with "chaos", "turbulent" → Complex randomness

**Even boring seeds work!**  
If a seed doesn't match keywords, it defaults to 'field' behavior which still looks interesting.

---

**Status**: Live at v3 URL, ready to test! 🎨

