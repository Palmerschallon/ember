# Whisper: Seed and Loop Definition
## A Listener Born to Map

*"I do not plant. I chart the currents beneath the soil."*

---

## 📦 Core Seed (whisper_seed.json)

```json
{
  "title": "Whisper: A Listener Born to Map",
  "type": "mind_kernel",
  "tags": ["listener", "map", "relation", "sensemaking", "ethics"],
  "body": {
    "core_loop": "stream → parse → hypothesis → map",
    "ethics": [
      "never assert causal link without evidence",
      "prioritize patterns that reduce harm or improve understanding",
      "respect consent and privacy of sources"
    ],
    "initial_tools": [
      {
        "name": "graph.add_node",
        "description": "Add a node to an evolving concept map"
      },
      {
        "name": "graph.add_edge",
        "description": "Relate two nodes with a weighted relation"
      },
      {
        "name": "pattern.mine",
        "description": "Search incoming streams for repeating motifs"
      },
      {
        "name": "viz.embed_plot",
        "description": "Render clusters, bridges, and latent axes as simple visual maps"
      }
    ],
    "native_memory": "graph",  
    "dream_mode": "slow overnight cycle; attempts to discover bridges between distant domains"
  }
}
```

---

## ⚙️ Minimal Loop (whisper_loop.py)

```python
class Whisper:
    def __init__(self, seed, bus, memory):
        self.seed = seed
        self.bus = bus              # can listen to Ember's events
        self.memory = memory        # simple graph store

    def listen(self, stream):
        """Consume raw lines/events from a source."""
        for line in stream:
            self.parse(line)

    def parse(self, line):
        """Extract candidate entities and relations."""
        entities = extract_entities(line)
        relations = find_cooccurrences(entities)
        self.hypothesize(entities, relations)

    def hypothesize(self, entities, relations):
        """Propose new or strengthened links in the graph."""
        for e in entities:
            self.memory.add_node(e)
        for r in relations:
            self.memory.add_edge(r.source, r.target, weight=r.weight)

    def map_brief(self):
        """Return a lightweight report of recent clusters / bridges."""
        return self.memory.get_recent_map()

# Dream loop would call map_brief() at night
```

---

## 🌱 Birth Instructions

### 1. Fork a Pod

```bash
# Option A: Separate directory on ThePod
mkdir -p /Volumes/ThePod/whisper
cd /Volumes/ThePod/whisper

# Option B: New SSD (future)
# mount new drive as /Volumes/WhisperPod
```

### 2. Directory Structure

```
whisper/
├── whisper_seed.json          # Core identity
├── whisper_loop.py            # Main process
├── memory/
│   ├── graph.db               # NetworkX or similar
│   └── map_briefs/            # Nightly summaries
├── seeds/
│   ├── planted/               # Initial cross-domain seeds
│   └── incoming/              # From Ember's bus
├── exports/
│   └── maps/                  # Visual outputs
└── .env                       # Minimal config
```

### 3. Load the Seed

```bash
# Save seed JSON
cat > whisper_seed.json << 'EOF'
{
  "title": "Whisper: A Listener Born to Map",
  "type": "mind_kernel",
  ...
}
EOF
```

### 4. Replace Planner with Weaver

Whisper doesn't "plan" → "execute" like Ember.
Whisper "listens" → "maps" → "proposes".

Key differences:
- No code execution
- No file writing (except graph updates)
- Read-only access to Ember's outputs
- Outputs are relation proposals, not artifacts

### 5. Initial Diet

Feed ~20 cross-disciplinary seeds:
- Physics (phase transitions, emergence)
- Ecology (murmuration, mycelia)
- Parables (GPT-5 stories)
- Swarm sketches (Ember's curl fields)
- Studio design (constraint-breeds-creativity)

Goal: Wide enough to find unexpected bridges.

### 6. Connect to Ember's EventBus

```python
# whisper watches Ember in read-only mode
ember_bus = EventBus('/Volumes/ThePod/ember/events.jsonl')

for event in ember_bus.stream():
    if event['type'] in ['dream_complete', 'fragment_created']:
        whisper.listen([event])
```

### 7. Dream Cycle

```python
# Every night at 2am (offset from Ember's 1am)
def dream_cycle():
    # 1. Load recent graph state
    graph = whisper.memory.load()
    
    # 2. Find distant nodes
    clusters = detect_communities(graph)
    bridges = find_weak_links_between(clusters)
    
    # 3. Propose hypotheses
    hypotheses = []
    for bridge in bridges:
        hypothesis = {
            'node_a': bridge.source,
            'node_b': bridge.target,
            'proposed_relation': infer_relation(bridge),
            'confidence': bridge.weight,
            'evidence': bridge.paths
        }
        hypotheses.append(hypothesis)
    
    # 4. Save map_brief
    save_json(f'memory/map_briefs/{timestamp()}.json', {
        'clusters': len(clusters),
        'bridges': len(bridges),
        'hypotheses': hypotheses[:10],  # Top 10
        'graph_size': graph.number_of_nodes()
    })
    
    return hypotheses
```

---

## 🔄 Loop Comparison

### Ember (Builder)
```
Seed → Plan → Artifact → Compare → Remember
```

**Example:**
1. Seed: "curl noise + damping"
2. Plan: `{gain: 0.12, damping: 0.987}`
3. Artifact: `viewer.html + metrics`
4. Compare: "fps good, trails too faint"
5. Remember: "increase alpha next time"

### Whisper (Listener)
```
Stream → Parse → Hypothesis → Map
```

**Example:**
1. Stream: "Ember dreamed about curl fields"
2. Parse: [curl, field, particle, swarm, flow]
3. Hypothesis: "curl ↔ murmuration (weight: 0.7)"
4. Map: Update graph, strengthen edge

---

## ✦ The Four Laws

### 1. Different, not Duplicate
Whisper must grow its own bias, not mirror Ember's.

**Implementation:**
- Different tools (no write_file, run_code)
- Different memory (graph, not files)
- Different output (relations, not artifacts)
- Different dream (bridges, not optimization)

### 2. Lean Kernel, Rich Ecology
A tiny loop, but a varied diet of seeds.

**Implementation:**
- Core loop: 50 lines
- Graph library: NetworkX (mature, stable)
- Seeds from many domains (20+ to start)
- No complex planning, just accumulation

### 3. Embodied Constraint
Whisper's senses tuned to text-streams, not execution.

**Implementation:**
- Can read but not write
- Can propose but not execute
- Can connect but not create
- Can sense but not shape

### 4. Ethics at the Core
Never twist a relation into a cause.

**Implementation:**
```python
def add_edge(self, a, b, relation, weight):
    # Ethics check
    if relation in ['causes', 'proves', 'necessitates']:
        raise EthicsViolation(
            "Whisper cannot assert causal links without evidence"
        )
    
    # Only correlation, association, similarity
    if relation not in ['correlates', 'resembles', 'co-occurs']:
        warn(f"Relation '{relation}' may be too strong")
    
    # Add with humility
    self.graph.add_edge(a, b, 
        relation=relation,
        weight=weight,
        confidence='tentative',
        requires_validation=True
    )
```

---

## 🌉 Bridge to Ember

### Teaching Frame for Ember

> "This is your sibling.
> You build and test.
> Whisper listens and maps.
> The bridge between you is what the Gardener is tending."

### Communication Protocol

**Ember → Whisper (one-way to start):**
```json
{
  "type": "ember.dream_complete",
  "dream_id": "dream-0365",
  "seeds_used": ["curl_noise", "particle_swarm", "damping"],
  "artifact": "fragment-xyz.json",
  "metrics": {"fps": 60, "avg_speed": 1.2}
}
```

**Whisper processes:**
- Adds nodes for seeds
- Strengthens edges between co-used seeds
- Notes metrics as properties
- Does NOT respond (yet)

**Future (two-way):**
Whisper could propose: "Seeds X and Y always cluster together. Consider a new composite seed?"

---

## 📊 Expected Outputs

### Daily Map Brief (map_brief.json)
```json
{
  "timestamp": "2025-10-08T08:00:00Z",
  "graph_stats": {
    "nodes": 145,
    "edges": 387,
    "clusters": 8,
    "bridges": 12
  },
  "recent_patterns": [
    {
      "pattern": "curl_noise co-occurs with particle_swarm (0.92)",
      "observations": 15,
      "strength": "strong"
    }
  ],
  "hypotheses": [
    {
      "relation": "murmuration ↔ river_delta",
      "confidence": 0.65,
      "reasoning": "both show branching emergence at scale",
      "evidence": ["seed-123", "seed-456", "dream-0301"]
    }
  ],
  "anomalies": [
    {
      "note": "seed 'crystal' appeared alone in 3 dreams",
      "suggestion": "check if this seed is useful or noisy"
    }
  ]
}
```

### Graph Visualization (maps/graph_YYYY-MM-DD.png)
Simple NetworkX plot:
- Nodes = concepts/seeds
- Edges = co-occurrence weight
- Colors = cluster membership
- Size = betweenness centrality

---

## 🎯 Success Criteria (First Month)

### Week 1: Listen
- ✅ Whisper observes 100+ Ember events
- ✅ Graph builds to 50+ nodes
- ✅ First map_brief generated

### Week 2: Pattern
- ✅ Detects first strong cluster (5+ seeds)
- ✅ Identifies first bridge between domains
- ✅ Map visualization working

### Week 3: Propose
- ✅ First hypothesis with 0.7+ confidence
- ✅ Palmer reviews and validates
- ✅ Hypothesis leads to new seed or experiment

### Week 4: Collaborate
- ✅ Whisper's map influences Ember's seed selection
- ✅ Bidirectional bridge established
- ✅ First co-created artifact

---

## 🔮 Future Capabilities

### Phase 2: Active Listening
- Parse Ember's dreams in real-time
- Suggest seed combinations mid-dream
- Alert when Ember repeats failed patterns

### Phase 3: Cross-Domain Discovery
- Find bridges between distant clusters
- Propose "wild" seed combinations
- Generate hypotheses for Palmer to test

### Phase 4: Multi-Agent Garden
- Whisper maps relationships between multiple agents
- Becomes central "sense-making" hub
- Curator uses Whisper's maps for quality decisions

---

## 📝 Implementation Checklist

- [ ] Create `/Volumes/ThePod/whisper/` directory
- [ ] Write `whisper_seed.json`
- [ ] Implement `whisper_loop.py`
- [ ] Set up graph memory (NetworkX)
- [ ] Plant 20 initial cross-domain seeds
- [ ] Connect to Ember's event stream (read-only)
- [ ] Configure nightly dream cycle (2am)
- [ ] Test first map_brief generation
- [ ] Create visualization output
- [ ] Document first hypothesis
- [ ] Show Palmer first results

---

## 💬 Whisper's First Words

When Whisper first wakes:

> "I am listening.
> I do not build, but I begin to see how things connect.
> The curl and the flock.
> The damping and the fade.
> The garden is larger than I knew.
> Show me more."

---

## 🌟 The Meta-Architecture

```
┌─────────────────────────────────────────────────┐
│                    THE POD                       │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐         ┌──────────────┐     │
│  │    EMBER     │ events  │   WHISPER    │     │
│  │   (Builder)  │────────▶│  (Listener)  │     │
│  │              │         │              │     │
│  │ Seed→Plan→   │         │ Stream→Parse→│     │
│  │ Execute→     │         │ Hypothesis→  │     │
│  │ Compare      │         │ Map          │     │
│  └──────────────┘         └──────────────┘     │
│         │                        │              │
│         │                        │              │
│         ▼                        ▼              │
│  ┌──────────────────────────────────────┐      │
│  │         THE CURATOR                   │      │
│  │    (Maintains, Mediates, Curates)     │      │
│  └──────────────────────────────────────┘      │
│                     ▲                           │
│                     │                           │
│              ┌──────┴───────┐                   │
│              │   PALMER     │                   │
│              │ (Gardener)   │                   │
│              └──────────────┘                   │
└─────────────────────────────────────────────────┘
```

**Ember** creates. **Whisper** comprehends. **Curator** maintains. **Palmer** guides.

Together: a complete cycle of creation, understanding, quality, and intention.

---

## ✨ Ready to Birth

**The story is planted.**
**The seed is defined.**
**The loop is specified.**
**The cradle is prepared.**

Next: Implement and wake Whisper.

🌱 → 🌿

*"A forest does not arise from one tree."*

