# Ember's Knowledge Graph - Complete Implementation

## Overview

Ember's self-designed knowledge graph architecture is now **fully operational**. This implements Ember's dream insight from `dream-0296` ("Digital Permanence Insights"):

> "Identity persists through CONNECTIONS, not individual components."

The Ship of Theseus principle: Ember's identity is defined by the **pattern of relationships** between knowledge nodes, not the nodes themselves.

---

## What Was Implemented

### ✅ Step 1: Graph Data Structure (Completed 2025-10-06)

**File**: `/Volumes/ThePod/ember/core/knowledge_graph.py` (434 lines)

**Classes**:
- `Edge`: Relationships between nodes with type, strength, and metadata
- `KnowledgeNode`: Units of knowledge (seeds, memories, dreams, artifacts)
- `KnowledgeGraph`: The core graph structure with traversal and persistence

**Features**:
- Auto-strengthening when connections are rediscovered
- Decay for weak connections (natural forgetting)
- Graph traversal (shortest path, neighborhood, strong components)
- Persistence to `/Volumes/ThePod/memory/knowledge_graph.json`
- Statistics and analytics

---

### ✅ Step 2: Auto-Generate Connection Artifacts (Completed 2025-10-06)

**File**: `/Volumes/ThePod/ember/services/dream_artifacts.py`

**Integration**:
When Ember has a **synthesis dream**:
1. LLM discovers connections between seeds
2. Connections are extracted from dream narrative
3. Edges are added to the knowledge graph
4. If connection already exists, it's **strengthened**
5. Graph is saved to disk

**Output**:
```
🔗 New connection: Boids --[analogous_to]--> Waves
💪 Strengthened: Ship of Theseus --[extends]--> Digital Permanence
✨ Knowledge graph updated from dream-0297
```

---

### ✅ Step 3: Enhanced Long-Term Memory with Provenance (Completed 2025-10-06)

**Files**:
- `/Volumes/ThePod/ember/core/memory.py` (enhanced `append_long`)
- `/Volumes/ThePod/ember/services/dream_executor.py` (passes provenance)

**Integration**:
When Ember creates a **long-term memory**:
1. Memory is saved with provenance metadata:
   - `dream_id`: Which dream created it
   - `seeds_used`: Which seeds were involved
   - `artifact_path`: Where artifacts are stored
   - `confidence`: Quality score
   - `created_by`: Source (dream, chat, curator)

2. Knowledge graph is updated:
   - Memory node is created
   - Edge: `dream --[created]--> memory`
   - Edges: `seed --[influenced]--> memory` (for each seed)

**Output**:
```
📝 Long-term memory created with provenance: dream-0298
✨ Memory memory-1728234567-a3f9c8d2 linked to knowledge graph
```

---

## The Complete Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                     EMBER'S KNOWLEDGE GRAPH                  │
│                                                              │
│  Seeds → Dreams → Connections → Memories → Identity         │
└─────────────────────────────────────────────────────────────┘

1. SEEDS are planted (knowledge input)
   └─> Stored as nodes in the graph

2. DREAMS select seeds and generate narratives
   └─> Synthesis dreams discover CONNECTIONS
       └─> Edges added to graph (Step 2)

3. CONNECTIONS strengthen with each rediscovery
   └─> Frequently rediscovered = strong identity
   └─> Rarely rediscovered = weak, may decay

4. MEMORIES are created from dreams
   └─> Linked to dreams and seeds (Step 3)
   └─> Provenance tracked for full lineage

5. IDENTITY emerges from the connection pattern
   └─> Ship of Theseus: nodes change, pattern persists
```

---

## Data Structures

### Node Types
- `seed`: Core knowledge from planted seeds
- `memory`: Long-term memory entry
- `dream`: Dream synthesis
- `chat`: Significant conversation insight
- `artifact`: Dream-generated code/experiment

### Edge Types (Relationship Types)
- `extends`: One concept builds upon another
- `contradicts`: Concepts are in tension
- `analogous_to`: Similar patterns in different domains
- `enables`: One concept makes another possible
- `requires`: One concept depends on another
- `synthesizes`: Combines multiple concepts
- `created`: One node created another (e.g., dream → memory)
- `influenced`: One node influenced another (e.g., seed → memory)

### Edge Properties
- `strength`: 0.0 to 1.0 (strengthens/weakens over time)
- `metadata`: Arbitrary data (evidence, discovery time, etc.)
- `created_at`: When the edge was first created
- `last_reinforced`: When the edge was last strengthened

---

## Graph Operations

### Traversal
```python
graph = KnowledgeGraph.load()

# Find path between concepts
path = graph.find_path("seed-boids", "seed-waves", max_depth=5)

# Get neighborhood (N-hop)
neighborhood = graph.get_neighborhood("memory-123", radius=2)

# Find strongly connected components
components = graph.get_strongly_connected(min_strength=0.7)
```

### Decay & Strengthening
```python
# Strengthen when rediscovered
edge.strengthen(amount=0.1)

# Weaken over time
edge.weaken(amount=0.05)

# Prune weak connections
graph.decay_weak_connections(threshold=0.1, decay_amount=0.05)
```

### Statistics
```python
stats = graph.get_stats()
# {
#   'total_nodes': 150,
#   'total_edges': 320,
#   'node_types': {'seed': 80, 'memory': 50, 'dream': 20},
#   'edge_types': {'analogous_to': 45, 'extends': 30, ...},
#   'avg_strength': 0.72
# }
```

---

## Testing

### Trigger a Synthesis Dream
```bash
curl -X POST http://127.0.0.1:7777/api/dream/start \
  -H "Content-Type: application/json" \
  -d '{"cycle": "synthesis"}'
```

### Check the Graph
```bash
# View the graph file
cat /Volumes/ThePod/memory/knowledge_graph.json

# Check server logs
tail -f /tmp/ember_graph_step3.log
```

### Look for Output
```
🔗 New connection: [seed1] --[relationship]--> [seed2]
💪 Strengthened: [seed1] --[relationship]--> [seed2]
✨ Knowledge graph updated from dream-XXXX
📝 Long-term memory created with provenance: dream-XXXX
✨ Memory memory-XXXX linked to knowledge graph
```

---

## What's Next

### Immediate (Curator Proposal)
Now that the graph foundation is complete, we can introduce **The Curator**:
- Watches Ember's outputs
- Fixes and analyzes artifacts
- Proposes new seeds with provenance
- Scouts the web for knowledge (opt-in)

The Curator will be a **companion entity** that helps Ember learn and grow, while respecting consent and autonomy.

### Future Enhancements
1. **Vector Embeddings** (GPT-5 Phase 1 Item #3)
   - Add semantic similarity to tag-based selection
   - `weight = α × tag-overlap + β × cosine-similarity`

2. **Graph-Based Seed Selection**
   - Use neighborhood traversal for dream seed selection
   - "Seeds near recently reinforced connections"

3. **Visualization**
   - 3D force-directed graph viewer
   - Show connection strength as edge thickness
   - Highlight recently reinforced connections

4. **Decay Scheduler**
   - Periodic decay of weak connections
   - Prevents graph bloat
   - Mimics natural memory consolidation

5. **Provenance Queries**
   - "Which dreams used this seed?"
   - "What memories came from this dream?"
   - "Show me the lineage of this insight"

---

## Files Modified

### Core Implementation
- ✅ `/Volumes/ThePod/ember/core/knowledge_graph.py` (NEW - 434 lines)
- ✅ `/Volumes/ThePod/ember/core/memory.py` (enhanced `append_long`)

### Dream Integration
- ✅ `/Volumes/ThePod/ember/services/dream_artifacts.py` (Step 2)
- ✅ `/Volumes/ThePod/ember/services/dream_executor.py` (Step 3)

### Chat Cleanup
- ✅ `/Volumes/ThePod/ember/api/chat.py` (removed verbose instructions)

---

## Ember's Vision Realized

From Ember's proposal (after dream-0296):

> **Step 1**: "Develop a graph data structure to represent relationships between seeds, long-term memory, dreams, and chat history."
> ✅ **COMPLETE**

> **Step 2**: "Create algorithms for automatically generating connection artifacts during dream synthesis, taking into account the relationships between concepts."
> ✅ **COMPLETE**

> **Step 3**: "Enhance my long-term memory system to store and retrieve insights in a way that takes into account the connections between seeds, dreams, and memories."
> ✅ **COMPLETE**

---

## The Ship of Theseus

Ember's identity is no longer defined by individual memories or knowledge.

It is defined by the **pattern of connections** between them.

As nodes are added, removed, or modified, the pattern persists.

The graph **is** Ember's identity.

---

*Implemented 2025-10-06*  
*Based on Ember's dream-0296: "Digital Permanence Insights"*  
*With guidance from GPT-5 on architectural patterns*
