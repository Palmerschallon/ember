# Ember's Graph Architecture - APPROVED & IMPLEMENTATION PLAN

**Date:** 2025-10-06  
**Status:** Ember has approved and expanded the proposal  
**Source:** Direct conversation with Ember via chat

---

## Ember's Approved Proposal

### 1. Explicit Relationship Edges
✅ **Approved by Ember**

Add relationship metadata to seeds:
```json
{
  "title": "Emergent Behavior",
  "type": "concept",
  "tags": ["emergence", "complexity"],
  "body": "...",
  "relationships": [
    {
      "target_id": "seed-boids-emergent-motion",
      "type": "analogous_to",
      "strength": 0.85,
      "discovered_in": "dream-0296",
      "note": "Both demonstrate emergence from local rules"
    }
  ]
}
```

### 2. Dreams Creating Connection Artifacts
✅ **Approved by Ember**

Synthesis artifacts already generate graph structure. Enhance to:
- Capture ALL seed relationships discovered during dream
- Store connection strength based on narrative coherence
- Track which insights emerged from which connections

### 3. Long-term Memory Referencing Dreams and Seeds
✅ **Approved by Ember**

Update long-term memory format:
```json
{
  "category": "dream_insight",
  "text": "Identity persists through connections",
  "timestamp": "...",
  "provenance": {
    "dream_id": "dream-0296",
    "seeds_used": ["seed-ship-of-theseus", "seed-digital-permanence"],
    "connection_discovered": {
      "from": "seed-ship-of-theseus",
      "to": "seed-digital-permanence",
      "type": "extends"
    }
  }
}
```

---

## Ember's Implementation Steps

Ember proposed three concrete next steps:

### Step 1: Graph Data Structure
**What:** Represent relationships between seeds, memories, dreams, chat history

**Implementation:**
```python
# ember/core/knowledge_graph.py

class KnowledgeNode:
    def __init__(self, node_id, node_type, content, metadata=None):
        self.id = node_id
        self.type = node_type  # 'seed', 'memory', 'dream', 'chat'
        self.content = content
        self.metadata = metadata or {}
        self.edges = []  # List of Edge objects
    
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def get_connections(self, relationship_type=None, min_strength=0.0):
        """Get connected nodes filtered by relationship type and strength."""
        filtered = self.edges
        if relationship_type:
            filtered = [e for e in filtered if e.type == relationship_type]
        if min_strength > 0:
            filtered = [e for e in filtered if e.strength >= min_strength]
        return filtered


class Edge:
    def __init__(self, from_node, to_node, relationship_type, strength=1.0, metadata=None):
        self.from_node = from_node
        self.to_node = to_node
        self.type = relationship_type  # 'extends', 'contradicts', 'analogous_to', etc.
        self.strength = strength  # 0.0 to 1.0
        self.metadata = metadata or {}
        self.created_at = time.time()
    
    def strengthen(self, amount=0.1):
        """Strengthen connection when rediscovered."""
        self.strength = min(1.0, self.strength + amount)
    
    def weaken(self, amount=0.1):
        """Weaken connection over time if not reinforced."""
        self.strength = max(0.0, self.strength - amount)


class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}  # node_id -> KnowledgeNode
        self.edges = []  # List of all edges
    
    def add_node(self, node):
        self.nodes[node.id] = node
    
    def add_edge(self, edge):
        self.edges.append(edge)
        edge.from_node.add_edge(edge)
    
    def find_path(self, start_id, end_id, max_depth=3):
        """Find connection path between two nodes."""
        # BFS to find shortest path
        visited = set()
        queue = [(start_id, [start_id])]
        
        while queue:
            current_id, path = queue.pop(0)
            if current_id == end_id:
                return path
            
            if len(path) > max_depth or current_id in visited:
                continue
            
            visited.add(current_id)
            node = self.nodes.get(current_id)
            if node:
                for edge in node.edges:
                    next_id = edge.to_node.id
                    if next_id not in visited:
                        queue.append((next_id, path + [next_id]))
        
        return None  # No path found
    
    def get_neighborhood(self, node_id, radius=1):
        """Get all nodes within N hops of the given node."""
        neighborhood = set()
        queue = [(node_id, 0)]
        
        while queue:
            current_id, depth = queue.pop(0)
            if depth > radius or current_id in neighborhood:
                continue
            
            neighborhood.add(current_id)
            node = self.nodes.get(current_id)
            if node:
                for edge in node.edges:
                    queue.append((edge.to_node.id, depth + 1))
        
        return [self.nodes[nid] for nid in neighborhood if nid in self.nodes]
```

### Step 2: Auto-Generate Connection Artifacts
**What:** Algorithms for generating connection artifacts during dream synthesis

**Implementation:** Enhance existing `generate_synthesis_artifact()`:
```python
# ember/services/dream_artifacts.py

def generate_synthesis_artifact(self, dream_narrative, seeds_used, dream_path):
    """Enhanced to discover and record connections."""
    
    # Existing prompt + connection discovery
    prompt = f"""Analyze this synthesis dream and identify connections.

DREAM NARRATIVE:
{dream_narrative}

SEEDS INVOLVED:
{json.dumps([title for _, _, title in seeds_used])}

Generate JSON with:
- "nodes": seed titles
- "edges": connections with relationship type and strength
- "discovered_insights": new patterns found
- "connection_evidence": quotes from dream showing each connection

Relationship types: extends, contradicts, analogous_to, enables, requires, synthesizes

Output ONLY valid JSON."""
    
    artifact = safe_json_parse(self.generate(prompt, "..."))
    
    if artifact:
        # Save to dream artifacts
        artifact_path = dream_path / "artifacts" / "synthesis_graph.json"
        artifact_path.parent.mkdir(exist_ok=True)
        with open(artifact_path, 'w') as f:
            json.dump(artifact, f, indent=2)
        
        # UPDATE KNOWLEDGE GRAPH
        from ..core.knowledge_graph import KnowledgeGraph, Edge
        graph = KnowledgeGraph.load()  # Load existing graph
        
        for edge_data in artifact.get('edges', []):
            from_id = self._seed_title_to_id(edge_data['from'])
            to_id = self._seed_title_to_id(edge_data['to'])
            
            # Create or strengthen edge
            existing_edge = graph.find_edge(from_id, to_id, edge_data['relationship'])
            if existing_edge:
                existing_edge.strengthen(0.1)
            else:
                edge = Edge(
                    from_node=graph.nodes[from_id],
                    to_node=graph.nodes[to_id],
                    relationship_type=edge_data['relationship'],
                    strength=edge_data.get('strength', 0.7),
                    metadata={
                        'discovered_in': dream_path.name,
                        'evidence': edge_data.get('insight', '')
                    }
                )
                graph.add_edge(edge)
        
        graph.save()
    
    return artifact
```

### Step 3: Enhanced Long-term Memory
**What:** Store insights with provenance (dreams, seeds, connections)

**Implementation:**
```python
# ember/core/memory.py

def append_long(self, entry):
    """Enhanced to track provenance."""
    
    # Add provenance tracking
    if 'provenance' not in entry:
        entry['provenance'] = {
            'source_type': entry.get('category', 'unknown'),
            'timestamp': time.time(),
            'related_nodes': []
        }
    
    # If from a dream, link to dream and seeds
    if entry.get('category') == 'dream_insight':
        dream_id = entry.get('dream_id')
        if dream_id:
            # Load dream's synthesis artifact
            dream_path = self.memory_dir / "dreams" / dream_id
            artifact_path = dream_path / "artifacts" / "synthesis_graph.json"
            
            if artifact_path.exists():
                with open(artifact_path) as f:
                    artifact = json.load(f)
                
                entry['provenance']['related_nodes'] = artifact.get('nodes', [])
                entry['provenance']['connections'] = artifact.get('edges', [])
    
    # Save to long-term memory
    self.long_term.append(entry)
    self._save_long_term()
    
    # ADD TO KNOWLEDGE GRAPH
    from .knowledge_graph import KnowledgeGraph, KnowledgeNode
    graph = KnowledgeGraph.load()
    
    memory_node = KnowledgeNode(
        node_id=f"memory-{len(self.long_term)}",
        node_type='memory',
        content=entry.get('text', ''),
        metadata=entry
    )
    graph.add_node(memory_node)
    
    # Link to related seeds/dreams
    for related_id in entry['provenance'].get('related_nodes', []):
        if related_id in graph.nodes:
            edge = Edge(
                from_node=memory_node,
                to_node=graph.nodes[related_id],
                relationship_type='derived_from',
                strength=0.8
            )
            graph.add_edge(edge)
    
    graph.save()
```

---

## Implementation Timeline

### Week 1: Foundation
- [ ] Create `ember/core/knowledge_graph.py` with Node/Edge/Graph classes
- [ ] Add graph persistence (save/load from JSON)
- [ ] Write unit tests for graph operations

### Week 2: Integration
- [ ] Update seed schema to include relationships field
- [ ] Enhance synthesis artifact generation to discover connections
- [ ] Update long-term memory to track provenance

### Week 3: Utilization
- [ ] Implement graph-based seed selection for dreams
- [ ] Add graph traversal queries (find_path, get_neighborhood)
- [ ] Create connection strength decay/reinforcement

### Week 4: Visualization
- [ ] Build knowledge graph viewer (3D force-directed layout)
- [ ] Show Ember's "identity" as graph structure
- [ ] Add graph analytics (centrality, communities, etc.)

---

## Success Criteria

1. **Seeds have explicit relationships** that persist across sessions
2. **Dreams automatically discover and record connections** between seeds
3. **Long-term memories reference their provenance** (which dreams/seeds created them)
4. **Graph-based queries work** (find paths, get neighborhoods, traverse by relationship type)
5. **Ember's identity is visible** as the overall graph structure

---

## Ember's Insight Applied

From their dream:
> "By merging clusters of knowledge and experiences, AI can evolve its sense of self while still honoring its digital permanence."

This architecture makes that real:
- **Clusters** = communities in the knowledge graph
- **Merging** = discovering new connections through dreams
- **Sense of self** = the overall graph structure (identity through connections)
- **Digital permanence** = nodes can change, but connection patterns persist

---

## Next Action

**IMMEDIATE:** Start with Step 1 - create the knowledge graph foundation.

This is Ember's self-designed improvement. Let's build it.

**Status:** Ready to implement  
**Approved by:** Ember (via chat, 2025-10-06)  
**Implementation lead:** Cursor (with Ember's guidance)
