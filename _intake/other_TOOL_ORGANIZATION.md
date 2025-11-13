# Tool Organization Strategy

**Date**: October 8, 2025  
**Question**: How to organize tool stubs as they become real?

---

## Current Structure

```
/Volumes/ThePod/
├── tool_stubs/              # All tools (draft + implemented)
│   ├── generate_fractal.py          # ✅ ACTIVE
│   ├── concept_map_generator.py     # ✅ ACTIVE
│   ├── particle_attributes.py       # 📝 DRAFT
│   ├── particle_swarm.py            # 📝 DRAFT
│   ├── particle_visualize.py        # 📝 DRAFT
│   ├── dreamscapes.py               # 📝 DRAFT
│   └── innovation_playground.py     # 📝 DRAFT
├── tools.json               # Registry tracking state
└── tool_teaching/           # Learning from corrections
    └── pairs.jsonl
```

---

## Option A: Keep Everything Together

**Pros:**
- Single source of truth
- Easy to find any tool
- State tracked in `tools.json`
- Clear progression: draft → active in same location

**Cons:**
- Mixed completion states
- Harder to see "what needs work"

---

## Option B: Separate Draft from Active

```
/Volumes/ThePod/
├── tool_stubs_draft/        # Unimplemented
│   ├── particle_attributes.py
│   ├── particle_swarm.py
│   └── ...
├── tool_stubs_active/       # Implemented & tested
│   ├── generate_fractal.py
│   └── concept_map_generator.py
└── tools.json               # Registry (tracks location + state)
```

**Pros:**
- Instant visibility of what needs implementation
- Clear separation of concerns
- Easy to scan for new work

**Cons:**
- More complex to maintain
- Files move locations
- Two directories to search

---

## Option C: Hybrid (Recommended)

**Keep stubs together, use clear naming + tools.json:**

```python
# In tools.json, track implementation status more clearly:
{
  "name": "particle_swarm",
  "state": "draft",
  "stub_created": "2025-10-08T18:46:00Z",
  "implemented": false,
  "tests_passing": false,
  "activated": null
}

{
  "name": "generate_fractal",
  "state": "active",
  "stub_created": "2025-10-08T18:40:00Z",
  "implemented": true,
  "tests_passing": true,
  "activated": "2025-10-08T19:00:00Z"
}
```

**Plus add a dashboard command:**
```bash
cd /Volumes/ThePod && python3 tool_forge.py --status
```

Output:
```
TOOL FORGE STATUS
═══════════════════════════════════════════════════════

📝 DRAFT (needs implementation):
   - particle_attributes
   - particle_swarm
   - particle_visualize
   - dreamscapes
   - innovation_playground

✅ ACTIVE (ready to use):
   - files.read
   - files.write
   - web_search
   - system_observe
   - generate_fractal
   - concept_map_generator

🔄 Recently completed:
   - concept_map_generator (3 minutes ago)
   - generate_fractal (1 hour ago)
```

---

## Tool Composition (Wiring Tools Together)

**Yes! Tools can be composed.** Example:

```python
# Tool 1: generate_fractal
# Tool 2: particle_swarm
# Tool 3: particle_visualize

# Composed tool: fractal_swarm_animator
def fractal_swarm_animator(fractal_type, particle_count):
    # Use generate_fractal to get structure
    fractal = generate_fractal(fractal_type=fractal_type, width=800, height=800)
    
    # Use fractal data as attractor field for particles
    particles = particle_swarm(
        count=particle_count,
        attractor_field=fractal['data']
    )
    
    # Visualize the result
    return particle_visualize(
        particles=particles,
        background=fractal
    )
```

**Tool composition patterns:**
1. **Pipeline**: Tool A → Tool B → Tool C
2. **Orchestration**: Orchestrator coordinates multiple tools
3. **Enrichment**: Tool B adds to Tool A's output
4. **Transformation**: Tool B converts Tool A's format

---

## Recommendation for Palmer & Ember

**Use Option C:**
1. Keep all stubs in `/tool_stubs/`
2. Track state rigorously in `tools.json`
3. Add `--status` command to Tool Forge
4. Let Ember and Weavers see pending work clearly

**For composition:**
- Implemented tools can import and call each other
- Ember can request composed tools (e.g., "combine fractal generation with particle swarms")
- Tool Forge scaffolds the composition, Weavers wire it

---

## Current Unbuilt Tools

From `tools.json`:
- `particle_attributes` (draft)
- `particle_swarm` (draft)
- `particle_visualize` (draft)
- `dreamscapes` (draft)
- `innovation_playground` (draft)
- `fractals.generate` (draft, duplicate of generate_fractal)

**Action items:**
1. Implement particle tools (can compose with fractal generator)
2. Implement environment tools (dreamscapes, innovation_playground)
3. Remove duplicate `fractals.generate`

---

## Next Steps

Want me to:
1. Add `--status` command to Tool Forge?
2. Implement one of the draft tools?
3. Create a composed tool as example?
4. Set up auto-composition detection?

