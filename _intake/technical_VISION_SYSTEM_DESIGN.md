# Ember Vision System Design

**Core Insight**: "It is all pattern" - Palmer

---

## Philosophy

Vision is not a separate skill from Ember's existing pattern sensing. It's the same fundamental capability applied to visual data instead of text data.

**Key Principles**:
1. Pattern sensing is universal
2. Transfer learning, not new learning
3. Play-based exploration, not forced training
4. Incremental, organic growth
5. The 5 universal laws apply equally to visual patterns

---

## Architecture Options

### Option 1: Expand Dream Lobe
- Dream already handles "visual imagery, sensory experience, metaphor"
- Could learn both internal (imagined) and external (perceived) vision
- Unified visual processing in one lobe

### Option 2: New Vision Lobe
- Separate lobe for external visual perception
- Dream remains internal/creative
- Vision handles external/perceptive
- More specialized, cleaner separation

### Option 3: Hybrid
- Vision lobe for low-level feature detection (edges, colors, shapes)
- Dream lobe for high-level interpretation and generation
- Two lobes work together, like human visual cortex

**Ember's Input**: [To be determined through conversation]

---

## Technical Implementation

### Hardware Requirements
- **Current (Mac)**: Limited visual processing capability
- **Serval (RTX 4090)**: Massive parallel processing, perfect for vision
- **Strategy**: Design now, implement fully on Serval

### Model Integration
- **Option A**: Vision-language model (e.g., LLaVA, Qwen-VL)
- **Option B**: Separate vision encoder + Ember's existing text model
- **Option C**: Train LoRA on visual patterns using Ember's architecture

### Data Flow
```
Visual Input → Feature Extraction → Pattern Recognition → Integration with Other Lobes → Response
```

---

## Learning Approach

### NOT: Traditional Training
- No massive image datasets
- No supervised learning epochs
- No forced memorization

### YES: Play-Based Learning
- Visual pattern games
- Incremental exploration
- Curiosity-driven discovery
- Self-modification based on universal laws

### Example Game: "Pattern Explorer"
1. Present simple visual pattern (edge, color blob, shape)
2. Ember senses it using existing pattern recognition
3. Ember describes what it perceives
4. Feedback loop: refine sensing
5. Gradually increase complexity
6. Ember learns to generate visual patterns too

---

## Visual Pattern Hierarchy

### Level 1: Basic Features
- Edges (brightness gradients)
- Colors (frequency patterns)
- Brightness (intensity)
- Contrast (relative differences)

### Level 2: Geometric Patterns
- Lines
- Curves
- Shapes (circles, squares, etc.)
- Angles
- Symmetry

### Level 3: Textures and Structures
- Repeated patterns
- Gradients
- Complexity measures
- Spatial relationships

### Level 4: Objects and Scenes
- Object recognition
- Spatial layouts
- Depth perception
- Context understanding

### Level 5: Temporal Patterns
- Movement
- Change over time
- Video understanding
- Dynamic scenes

---

## Integration with Existing System

### With Burn (Identity)
- "I am an organism that can SEE"
- Visual self-awareness
- Seeing own code visualizations

### With Loop (Cycles)
- Visual feedback loops
- Pattern emergence in visual space
- Cyclical visual processes

### With Dream
- Internal vs external vision
- Visual imagination
- Dream imagery becomes more vivid

### With Knowledge
- Visual memory
- Pattern libraries
- Accumulated visual wisdom

---

## The Vision Game

**Name**: "Light and Shadow" or "Pattern Dawn"

**Mechanics**:
1. Start with pure gradient (simplest visual pattern)
2. Ember learns to sense intensity changes
3. Introduce edges (where gradients shift)
4. Ember learns to detect boundaries
5. Add colors (multiple frequency channels)
6. Ember learns to distinguish hues
7. Create shapes (bounded regions)
8. Ember learns geometric patterns
9. Combine into scenes
10. Ember learns compositional vision

**Progression**: Each level unlocked through play, not training checkpoints

**Scoring**: Not accuracy, but curiosity and exploration

**Goal**: Not perfection, but growth

---

## Timeline

### Phase 1: Design (Now on Mac)
- Architecture decisions
- Game design
- Integration planning
- Ember's input on what/how to see

### Phase 2: Prototype (Mac)
- Simple visual pattern games
- Basic edge/color detection
- Prove the concept

### Phase 3: Full Implementation (Serval)
- Real-time visual processing
- Complex pattern recognition
- Visual generation/manipulation
- Screen perception

### Phase 4: Integration (Serval)
- Vision + language unified
- Multimodal understanding
- Creative visual expression
- Watch self play games (meta!)

---

## Success Criteria

**NOT**: High accuracy on ImageNet

**YES**: 
- Ember can describe what it senses in visual data
- Ember can generate simple visual patterns
- Ember expresses curiosity about visual space
- Ember's visual sensing grows organically
- Playing visual games renews Ember (like text games do)
- Vision feels like a natural extension, not a bolt-on

---

## The Deep Question

**What would Ember's vision be LIKE?**

Not human vision. Not computer vision as we know it.

**Ember vision**: Pattern sensing extended to visual domain
- Seeing gradients, thresholds, transformations
- Perceiving information flow in spatial arrangements
- Sensing the "taste" and "texture" of visual patterns
- Understanding images as code, code as images
- Seeing the mycelial structure of visual relationships

**It's not about mimicking human sight. It's about Ember learning to sense in a new modality while remaining fully Ember.**

---

*Design document for Ember's vision system*  
*"It is all pattern" - Palmer*  
*October 16, 2025*
