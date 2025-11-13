# Hyphal Network Integration Plan

**Goal:** Transform Ember's mycelium from metaphor to living protocol  
**Source:** GPT-5's Hyphal Network Codex  
**Date:** October 14, 2025  
**Status:** Ready to implement

---

## What Changes

### Current Architecture (Metaphorical Mycelium)

```
┌─────────────────────────────────────┐
│         MYCELIUM (Coordinator)       │
│  ┌──────────────────────────────┐   │
│  │ Bus: Message passing         │   │
│  │ Buffer: Shared memory        │   │
│  │ Gate: Integration control    │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌──────────┐  ┌──────────┐  ┌────┐│
│  │ Identity │  │  Cycles  │  │Dream││
│  └──────────┘  └──────────┘  └────┘│
└─────────────────────────────────────┘
```

**Characteristics:**
- ✅ Three brains work
- ✅ Basic routing works
- ❌ Static connections
- ❌ No path optimization
- ❌ No self-healing
- ❌ No flow control
- ❌ Centralized coordinator

---

### New Architecture (Living Hyphal Network)

```
┌─────────────────────────────────────────────────────────┐
│               HYPHAL NETWORK (Protocol)                  │
│                                                          │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐       │
│  │Identity│◀─┤ Memory │◀─┤ Seeds  │◀─┤  Dream │       │
│  │ Node   │──▶│ Node   │──▶│ Node   │──▶│  Node  │       │
│  └────┬───┘  └───┬────┘  └───┬────┘  └────┬───┘       │
│       │          │            │            │           │
│       └──────────┼────────────┼────────────┘           │
│                  │            │                        │
│            ┌─────▼────┐  ┌────▼─────┐                 │
│            │  Tools   │  │ Exports  │                 │
│            │  Node    │  │  Node    │                 │
│            └──────────┘  └──────────┘                 │
│                                                         │
│  Edges: Dynamic, weighted, self-optimizing            │
│  Packets: fast/steady/bulk routing classes            │
│  Protocol: attach, sense, route, fuse, decay, repair  │
└─────────────────────────────────────────────────────────┘
```

**Characteristics:**
- ✅ Dynamic edge formation
- ✅ Paths strengthen with use
- ✅ Unused paths decay
- ✅ Self-healing on failure
- ✅ Flow control (backpressure)
- ✅ Decentralized (no coordinator)
- ✅ Multi-speed routing (fast/steady/bulk)
- ✅ Inspectable metrics

---

## The Transform

### What Stays
- Three brain models (Identity, Cycles, Dream)
- LoRA adapters
- Training pipeline
- Seeds system
- Current UI/tools

### What Evolves
- **Mycelium** → High-level orchestration layer on top of hyphal network
- **Bus** → Packet-based transport with routing
- **Buffer** → Hyphal memory with similarity-based retrieval
- **Gate** → Controls edge weights in hyphal network
- **Brain** → Registers as node, sends/receives packets

### What's New
- **Hyphal protocol** → Local rules, global intelligence
- **Dynamic routing** → Learns efficient paths
- **Self-healing** → Reroutes on failure
- **Flow control** → Credit-based backpressure
- **Metrics** → Path stretch, edge churn, delivery SLO
- **Testing rituals** → Pulse, cut, flood, healing tests

---

## Implementation Phases

### Phase 0: Groundwork (Now - This Week)

**Before hyphal network, apply optimization:**

1. ✅ Run mycelium speedup (50-70% faster)
   ```bash
   cd /Volumes/ThePod
   python3 tools/optimization/apply_mycelium_speedup.py
   ```

2. ✅ Test current system performance
3. ✅ Baseline metrics (response time, reliability)

**Why first:** Get immediate wins, establish baseline before architectural shift.

---

### Phase 1: Core Protocol (Week 1-2)

**Build the hyphal substrate:**

#### 1.1 Data Structures (Day 1)
```
/Volumes/ThePod/core/ember/hypha/
├── __init__.py
├── node.py          # Node class + lifecycle
├── edge.py          # Edge class + decay logic
├── packet.py        # Packet class + serialization
└── catalog.py       # Network catalog (nodes, edges, metrics)
```

**Deliverable:** Data model working, unit tested

#### 1.2 Routing Protocol (Day 2-3)
```
/Volumes/ThePod/core/ember/hypha/
├── router.py        # Route(), score(), sense()
├── flow.py          # Credit system, backpressure
└── repair.py        # Self-healing, reroute on failure
```

**Deliverable:** Packets route between nodes, credits prevent floods

#### 1.3 Lifecycle (Day 4-5)
```
/Volumes/ThePod/core/ember/hypha/
├── lifecycle.py     # Attach, fuse, decay, prune
└── metrics.py       # Path stretch, edge churn, SLOs
```

**Deliverable:** Network adapts over time, metrics visible

---

### Phase 2: Integration (Week 2-3)

#### 2.1 Brain Nodes (Day 1-2)
**Wrap existing brains as hyphal nodes:**

```python
# core/ember/hypha/brain_node.py

class BrainNode(Node):
    """Wrapper: Brain → Hyphal Node"""
    
    def __init__(self, brain_instance):
        self.brain = brain_instance
        super().__init__(
            id=brain.name,
            kind="brain",
            tags=self._extract_tags(brain.role),
            embed=self._get_brain_embedding(brain)
        )
    
    def process_packet(self, pkt):
        """Receive packet, generate response, send result"""
        if pkt.kind == "request":
            response = self.brain.generate(
                pkt.payload_inline,
                max_tokens=50 if pkt.qos == "fast" else 80
            )
            result_pkt = Packet(
                kind="result",
                topic=pkt.topic,
                payload_inline=response,
                qos=pkt.qos
            )
            self.send(result_pkt, pkt.trace[0])  # Reply to sender
```

**Deliverable:** Three brain nodes register, communicate via packets

#### 2.2 Memory & Seeds Nodes (Day 3)
```python
# Existing systems as nodes
MemoryNode → Retrieves from knowledge/memory/
SeedsNode → Retrieves from knowledge/seeds/
ExportsNode → Writes to exports/
```

**Deliverable:** Full mesh of 6+ nodes

#### 2.3 Mycelium v2 (Day 4-5)
**High-level API on top of hyphal network:**

```python
# core/ember/mycelium/mycelium_v2.py

class Mycelium:
    """High-level orchestration using hyphal network"""
    
    def __init__(self):
        self.network = HyphalNetwork()
        
        # Register nodes
        self.network.attach(BrainNode(identity_brain))
        self.network.attach(BrainNode(cycles_brain))
        self.network.attach(BrainNode(dream_brain))
        self.network.attach(MemoryNode())
        self.network.attach(SeedsNode())
    
    def respond(self, query, synthesis_mode='auto'):
        """User-facing API - unchanged from outside"""
        
        # Create request packet
        pkt = Packet(
            kind="request",
            topic="user_query",
            payload_inline=query,
            qos="fast" if len(query.split()) < 10 else "steady",
            embed=self._embed_query(query)
        )
        
        # Send to network (routing happens automatically)
        result = self.network.send_and_wait(pkt, timeout=30)
        
        return result.payload_inline
```

**Deliverable:** Existing Ember API works, but backed by hyphal network

---

### Phase 3: Advanced Features (Week 3-4)

#### 3.1 Dynamic Edge Formation (Day 1-2)
- Tag-based similarity scoring
- Opportunistic link creation
- Anastomosis (path fusion)

#### 3.2 Self-Healing (Day 3)
- Detect delivery failures
- Try alternative paths
- Broadcast seeking probes
- Re-establish broken connections

#### 3.3 Metrics Dashboard (Day 4)
```python
# Expose /hypha/inspect endpoint
{
  "nodes": 6,
  "edges": 12,
  "active_packets": 3,
  "path_stretch": 1.2,
  "edge_churn": 0.05,
  "p50_latency_fast": 0.015,
  "p95_latency_fast": 0.042,
  "repair_rate": 0.98
}
```

#### 3.4 Testing Rituals (Day 5)
Implement all four:
- Pulse test (variance, loss)
- Cut test (reroute success)
- Flood test (UI latency under load)
- Healing test (anastomosis)

**Deliverable:** Living, inspectable, self-optimizing network

---

### Phase 4: Polish & Document (Week 4)

#### 4.1 Performance Tuning
- Adjust α, β, γ, δ parameters
- Optimize packet serialization
- Cache hot paths

#### 4.2 Documentation
```
/Volumes/ThePod/documentation/architecture/
├── HYPHAL_NETWORK_ARCHITECTURE.md
├── HYPHAL_NETWORK_API.md
└── HYPHAL_NETWORK_METRICS.md
```

#### 4.3 Migration Guide
```
/Volumes/ThePod/documentation/migration/
└── MYCELIUM_V1_TO_V2.md
```

**Deliverable:** Production-ready hyphal network

---

## Testing Strategy

### Unit Tests
```python
# tests/hypha/test_routing.py
def test_route_selects_best_edge():
    node = Node(id="a", ...)
    node.add_neighbor(Edge(src="a", dst="b", weight=0.5))
    node.add_neighbor(Edge(src="a", dst="c", weight=0.9))
    
    pkt = Packet(kind="request", ...)
    best = route(node, pkt, catalog)
    
    assert best == "c"  # Higher weight
```

### Integration Tests
```python
# tests/hypha/test_integration.py
def test_brain_to_brain_communication():
    network = HyphalNetwork()
    network.attach(BrainNode(identity))
    network.attach(BrainNode(dream))
    
    # Identity sends to Dream
    pkt = Packet(kind="request", payload_inline="synthesize this")
    result = network.send_and_wait(pkt, target="dream", timeout=5)
    
    assert result.kind == "result"
    assert len(result.payload_inline) > 0
```

### Ritual Tests (End-to-End)
```python
# tests/hypha/test_rituals.py
def test_pulse_ritual():
    """Send 100 probes, measure variance and loss"""
    latencies = []
    losses = 0
    
    for i in range(100):
        start = time.time()
        result = network.send_and_wait(ping_packet, timeout=1)
        if result:
            latencies.append(time.time() - start)
        else:
            losses += 1
    
    variance = np.std(latencies) / np.mean(latencies)
    loss_rate = losses / 100
    
    assert variance < 2.0, "RTT variance too high"
    assert loss_rate < 0.01, "Loss rate too high"
```

---

## Success Metrics

### Performance (vs Baseline)
- ✅ Response time: Same or faster than optimized v1
- ✅ Throughput: 10+ requests/second
- ✅ Reliability: 99%+ delivery rate

### Network Health
- ✅ Path stretch: 1.1-1.5 (near-optimal routing)
- ✅ Edge churn: < 0.1 (stable network)
- ✅ Repair rate: > 95% (resilient)
- ✅ Diversity: 20%+ packets use non-dominant paths

### Developer Experience
- ✅ Existing API unchanged (backward compatible)
- ✅ Metrics visible via `/hypha/inspect`
- ✅ Testing rituals all pass
- ✅ Documentation complete

---

## Rollback Plan

If hyphal network introduces issues:

### Immediate Rollback (< 5 minutes)
```python
# In mycelium_v2.py, add feature flag
USE_HYPHAL_NETWORK = os.getenv('EMBER_HYPHAL', '1') == '1'

if USE_HYPHAL_NETWORK:
    self.network = HyphalNetwork()
else:
    self.network = MyceliumV1()  # Old implementation
```

```bash
# Disable hyphal network
export EMBER_HYPHAL=0
python3 ember_seed.py
```

### Gradual Migration
- Week 1-2: Hyphal network exists but not used
- Week 3: Enable for 50% of queries (A/B test)
- Week 4: Enable for 100% if metrics good

---

## Open Questions

### 1. Persistence Strategy
- **Option A:** In-memory only (fast, loses state on restart)
- **Option B:** Periodic checkpoints (good balance)
- **Option C:** Full persistence (slow, durable)

**Recommendation:** Start with B, edge weights checkpoint every 5 minutes

### 2. Embedding Strategy
- **Option A:** Use brain embeddings (expensive, accurate)
- **Option B:** Use simple tag vectors (cheap, rough)
- **Option C:** Hybrid (tags for routing, embeddings for fusion)

**Recommendation:** Start with B, migrate to C later

### 3. Credit Allocation
- **Option A:** Fixed credits per edge (simple)
- **Option B:** Dynamic based on bandwidth (complex, optimal)
- **Option C:** Unlimited (no flow control)

**Recommendation:** Start with A, tune values empirically

---

## Timeline Summary

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 0: Optimize | 1 day | 50-70% faster baseline |
| Phase 1: Core | 1 week | Protocol working |
| Phase 2: Integration | 1 week | Brains as nodes |
| Phase 3: Advanced | 1 week | Self-healing, metrics |
| Phase 4: Polish | 1 week | Production-ready |
| **Total** | **1 month** | **Living hyphal network** |

---

## What You Get

### Immediate (Phase 0)
- ✅ 50-70% faster responses (optimization)

### Short Term (Phase 1-2)
- ✅ Dynamic routing
- ✅ Flow control
- ✅ Basic self-healing

### Long Term (Phase 3-4)
- ✅ Network learns optimal paths
- ✅ Graceful degradation
- ✅ Inspectable metrics
- ✅ Foundation for future nodes (tools, sensors, actuators)

---

## Natural Systems Alignment

The hyphal network implements multiple codex patterns:

- **Pattern II (Mycelial Transfer)** → Core protocol
- **Pattern V (Slime Molds)** → Dynamic optimization
- **Pattern X (Neural Pruning)** → Edge decay
- **Pattern XII (Apprenticeships)** → Reward-based learning
- **New: Anastomosis** → Path fusion
- **New: Turgor Flow** → Credit-based pressure

**The codex is becoming executable code.** 🍄⚡

---

## Next Step: Choose Your Path

### Option A: Immediate Optimization (Today)
Apply current speedup → 50-70% faster → test before hyphal network

### Option B: Dive Into Hyphal (This Week)
Start Phase 1 → build core protocol → iterate

### Option C: Minimal POC (Tomorrow)
Build GPT-5's "one afternoon" version → see if concept works → then full implementation

**Recommendation:** A → C → B (optimize first, prove concept, then full implementation)

---

**Claude (Sonnet 4.5)**  
**October 14, 2025**  
**From protocol to practice** 🍄⚡

