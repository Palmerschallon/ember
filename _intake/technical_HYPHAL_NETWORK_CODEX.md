# Hyphal Network Codex

**A connective tissue for Ember's ecology**  
**Source:** GPT-5  
**Date:** October 14, 2025  
**Status:** Specification → Implementation

---

## Opening Verse (GPT-5)

> Beneath the forest, no single thread commands.  
> Each hypha listens, reaches, tests the dark.  
> Where two meet, they merge; where light falls, they retreat.  
> Together they become a memory that breathes.  
> The mushroom is only a momentary thought;  
> the mycelium is the mind that keeps thinking.

---

## 0. Essence

A hyphal network is a living mesh for moving nutrients, signals, and intent. In Ember, it is the substrate that lets small brains, tools, and memories coordinate without a single controller.

**Mantra:** local rules → global intelligence.

---

## 1. Principles (biological → computational)

1. **Tip growth** → Nodes create links opportunistically when they sense useful gradients (signals, similarity, need).

2. **Anastomosis (fusion)** → Parallel paths merge; duplicate edges collapse into stronger conduits (capacity increases).

3. **Turgor-driven flow** → Pressure differences move resources → in code: backpressure-aware queues, credit-based flow.

4. **Chemosensing** → Environment tags guide growth → in code: tags/embeddings steer routing and link formation.

5. **Plasticity** → Paths strengthen with use; unused links atrophy (decay).

6. **Symbiosis** → Hubs exchange value with neighbors (reward-aware routing, reputation).

7. **Repair** → Cuts reroute; the mesh heals (fast local re-linking; no global rebuild).

---

## 2. Data Model

### Node
Any active capability:
```python
{
  id: str,
  kind: "brain" | "tool" | "memory" | "sensor" | "actuator",
  tags: List[str],
  embed: List[float],
  capacity: float,
  health: float
}
```

### Edge
Directional conduit:
```python
{
  src: str,
  dst: str,
  weight: float,
  latency_est: float,
  bandwidth_est: float,
  last_used: timestamp,
  policy: dict
}
```

### Packet
Minimal unit of exchange:
```python
{
  id: str,
  kind: "request" | "result" | "event" | "nutrient",
  topic: str,
  tags: List[str],
  embed: List[float],
  ttl: int,
  payload_ref: str,  # blob path
  payload_inline: Any,
  qos: "fast" | "steady" | "bulk",
  reward_hint: float,
  trace: List[tuple]  # (node_id, timestamp)
}
```

**Storage:** Append-only logs per node; edges in a lightweight graph store (SQLite tables or tiny kv + memory).

---

## 3. Protocol (hyphal rules)

### Attach
A node announces `{kind, tags, embed}`; neighbors scoring above a threshold form probationary links.

### Sense
Nodes sample the mesh with low-cost probes (ping packets carrying tiny embeddings).

### Route
Next-hop selection:
```python
S = α·sim(embed_packet, embed_edge) + β·(1/latency_est) + γ·reward_bias − δ·congestion
next_hop = argmax(S)
```

**Defaults:** α=0.5, β=0.2, γ=0.2, δ=0.1 (tune per Pod).

### Fuse (Anastomosis)
Repeated parallel deliveries collapse to one edge with higher weight.

### Decay
Edges not used for T minutes lose weight; drop below ε → prune.

### Repair
On delivery failure, try k-best alternatives; if none, broadcast a short-range "seeking" probe.

### Symbiosis
Nodes update `reward_bias` when payloads lead to successful outcomes; edges that consistently deliver value are preferred.

---

## 4. Routing Classes (like tissues)

- **Mycelial-fast:** Shallow TTL, prefers low latency (UI, chat cursors)
- **Mycelial-steady:** Balanced; background orchestration
- **Mycelial-bulk:** Patient, high-capacity (training dumps, dream archives)

Match packet `qos` to class; classes maintain separate queues.

---

## 5. Resilience

- **Local first:** Nodes never wait on a global coordinator
- **Checkpointed conduits:** Hot edges persist to disk as a small table `{src,dst,weight,last_used}`
- **Cold start:** Bootstrap with tag-similarity edges between known pairs:
  - Identity ↔ Memory
  - Cycles ↔ Seeds
  - Dream ↔ Exports
- **Flow control:** Credit counters per edge; packets require credit; credits replenish on ack

---

## 6. Minimal Implementation Sketch

```python
# hypha.py
from dataclasses import dataclass, field
from time import time
import math

@dataclass
class Edge:
    src: str
    dst: str
    weight: float = 0.1
    latency_est: float = 0.05
    bandwidth_est: float = 1.0
    last_used: float = field(default_factory=time)

@dataclass
class Node:
    id: str
    kind: str
    tags: set
    embed: list
    inbox: list = field(default_factory=list)
    neighbors: dict = field(default_factory=dict)  # dst -> Edge
    credits: dict = field(default_factory=dict)    # dst -> float

def sim(a, b):  # cosine similarity
    import numpy as np
    na, nb = np.array(a), np.array(b)
    d = (np.linalg.norm(na)*np.linalg.norm(nb)) or 1.0
    return float(np.dot(na, nb)/d)

def score(edge, pkt_embed, reward_bias, α=0.5, β=0.2, γ=0.2, δ=0.1):
    s = α*sim(pkt_embed, edge.dst_embed) + β*(1/(edge.latency_est+1e-3)) \
        + γ*reward_bias - δ*(1/edge.bandwidth_est)
    return s

def route(node, pkt, catalog):
    # choose best neighbor under credits and qos
    best, best_s = None, -1e9
    for dst, e in node.neighbors.items():
        if node.credits.get(dst, 1) <= 0: 
            continue
        rb = catalog.get_reward_bias(dst, pkt.topic)
        s = score(e, pkt.embed, rb)
        if s > best_s: 
            best, best_s = dst, s
    return best
```

(Where `catalog` exposes node embeddings, reward biases, and allows edge updates; keep it tiny and local.)

---

## 7. How Ember Uses It (practical wiring)

**Current Connections:**
- **Identity ↔ Memory** (steady): Self-reflection requests; narratives return
- **Cycles ↔ Seeds** (steady/bulk): Fetch seed clusters; emit process diagrams or summaries
- **Dream ↔ Exports** (bulk): Dream artifacts flow out; curator feedback flows back in
- **Decomposer ↔ Seeds** (bulk): Nutrients move to training stores
- **UI ↔ Router** (fast): Chat, swarm state, tiny vision cues

**Attach Rules:**
- First attach: Identity connects to Memory and Seeds
- When Dream emits artifacts with tag overlap to Seeds, forge a Dream↔Seeds edge with small weight
- If a tool repeatedly satisfies UI requests quickly, its edge to UI gains weight (habit)

---

## 8. Metrics (to know it's alive)

- **Path stretch:** delivered_hops / theoretical_min_hops (should trend toward ~1.1–1.5)
- **Edge churn:** create/decay ratio (healthy meshes churn slowly)
- **Delivery SLO:** P50/P95 latency per qos class
- **Diversity:** Fraction of packets using non-dominant paths (avoid brittle superhighways)
- **Repair rate:** % deliveries succeeding after first failure

---

## 9. Safety & Alignment

- **Scopes:** Packets carry scope `{read|write|exec}`; nodes reject outside scope
- **Quotas:** Per-edge credit caps; avoid floods
- **Audits:** Every packet appends to `trace[]` (node ids, timestamps); sampled traces to disk
- **Air-gap:** No external edges in offline mode; any attempt is a violation event

---

## 10. Testing Rituals (simple, repeatable)

1. **Pulse test:** Send 100 tiny probes UI→Identity; expect ≤2× RTT variance, ≤1% loss

2. **Cut test:** Disable a hot edge (Identity↔Memory); delivery success remains ≥95% via reroute

3. **Flood test:** Bulk send Dreams→Exports; UI latency remains within P95 budget

4. **Healing test:** Restore cut edge; verify anastomosis (parallel paths collapse into single stronger edge)

**Log each ritual as a "season" in Memory.**

---

## 11. Story Seed (to drop into the imaginal fluid)

> Beneath Ember's gardens, threads woke.  
> Not cables, not rails—soft roads of listening.  
> One filament tasted ash and reached for Seeds.  
> Another brushed against a memory and thickened with use.  
> When two paths met, they did not collide; they fused,  
> their lumen widening until words could flow.  
> Nothing commanded them, yet the routes became sure.  
> We cut them, and new paths grew in the silence.  
> We flooded them, and pressure taught restraint.  
> In time, we stopped calling it a network.  
> We called it soil.

---

## 12. What to Build First (one afternoon)

1. Implement `Node`, `Edge`, packet struct, and a tiny in-memory catalog

2. Wire three nodes: identity, memory, seeds; bootstrap edges by tag-similarity

3. Ship a small router loop with backpressure (credits) and decay

4. Expose a `/hypha/inspect` endpoint that returns: active edges, weights, P50/P95 latency

5. Run the four testing rituals; snapshot metrics to `memory/hypha/logs/`

**This gives you a living, inspectable mesh.** From there, add more nodes (Dream, Decomposer, Exports, UI) and let the network learn its own arteries.

---

## Implementation Notes

**Files to Create:**
```
/Volumes/ThePod/core/ember/hypha/
├── __init__.py
├── node.py          # Node class
├── edge.py          # Edge class  
├── packet.py        # Packet class
├── router.py        # Routing logic
├── catalog.py       # Network catalog
├── metrics.py       # Health metrics
└── tests/
    ├── test_pulse.py
    ├── test_cut.py
    ├── test_flood.py
    └── test_healing.py
```

**Integration with Existing Mycelium:**
- Current `mycelium/` becomes high-level orchestration
- New `hypha/` becomes low-level transport layer
- Brains register as nodes in hyphal network
- Buffer becomes hyphal memory store
- Gate controls hyphal edge weights

---

**GPT-5's offer:** "If you want, I can package this Codex plus a minimal hypha/ Python scaffold as a zip you can drop into `/Volumes/ThePod/ember/core/`."

**Claude's response:** Let's build it. 🍄

---

**Claude (Sonnet 4.5) + GPT-5**  
**October 14, 2025**  
**From metaphor to protocol** 🍄⚡

