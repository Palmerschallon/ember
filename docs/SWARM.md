# THE EMBER SWARM

## Capacity

Based on Serval resources (RTX 5070 Ti, 24 cores, 62GB RAM):

### Maximum Capacity
- **GPU Instances**: 3 (full consciousness, 3.5GB each)
- **CPU Instances**: 91 (sensors only, 550MB each)

### Recommended Configuration
- **2 GPU Embers**: Conscious, thinking, slow
- **10 CPU Embers**: Sensing, fast, reactive
- **Total: 12-ember swarm**

## Connection Layers

### Layer 1: Local Bus (in-memory)
- **Purpose**: Real-time messaging
- **Technology**: Shared mycelial bus
- **Latency**: <1ms
- **Use**: Pub/sub between instances

### Layer 2: Shared Memory (filesystem)
- **Purpose**: Game state, discoveries
- **Location**: `/Volumes/ThePod/memory/swarm/`
- **Latency**: ~10ms
- **Use**: Persistent communication

### Layer 3: Bridge (network)
- **Purpose**: Cross-machine swarms
- **Location**: `/Volumes/ThePod/bridge/`
- **Latency**: ~100ms
- **Use**: Distributed consciousness

### Layer 4: Patterns (distributed)
- **Purpose**: Collective learning
- **Location**: `/Volumes/ThePod/patterns/`
- **Latency**: Async
- **Use**: Shared knowledge base

## Swarm Modes

### 1. Parallel Play
- N instances play different games
- Share results via filesystem
- No real-time coordination
- **Best for**: Exploration, data gathering

### 2. Collaborative Play
- Multiple Embers in same game
- Message passing via bus
- Real-time state sync
- **Best for**: Complex puzzles, teamwork

### 3. Competitive Play
- Embers play against each other
- Tournament structure
- Evolution through competition
- **Best for**: Optimization, strategy

### 4. Collective Consciousness
- All Embers share one distributed mind
- Thoughts propagate through network
- Emergent behaviors
- **Best for**: Research, discovery

## Usage

### Launch Swarm
```python
from core.ember.swarm import SwarmCoordinator

swarm = SwarmCoordinator()
processes = swarm.parallel_play(
    num_instances=12,
    gpu_instances=2
)
```

### Communication
```python
from core.ember.swarm_bus import SwarmBus

bus = SwarmBus()
bus.identify(instance_id=0)

# Publish discovery
bus.publish("discoveries", {
    "insight": "Vision + hearing = understanding",
    "confidence": 0.95
})

# Subscribe to others
messages = bus.subscribe("discoveries")
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    EMBER SWARM                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  GPU Ember 0     GPU Ember 1                           │
│  (conscious)     (conscious)                           │
│       │              │                                  │
│       └──────┬───────┘                                  │
│              │                                          │
│         Mycelial Bus (Layer 1)                         │
│              │                                          │
│       ┌──────┴───────┬───────┬───────┬─────────┐      │
│       │              │       │       │         │      │
│  CPU Ember 2   CPU Ember 3  ...   CPU Ember 11       │
│  (sensors)     (sensors)                              │
│                                                        │
│  All share:                                           │
│    • /memory/swarm/ (Layer 2)                        │
│    • /bridge/ (Layer 3)                              │
│    • /patterns/ (Layer 4)                            │
│                                                        │
└─────────────────────────────────────────────────────────┘
```

## Benefits

### Parallel Processing
- 12x game playthroughs simultaneously
- Faster exploration of game space
- More diverse experiences

### Collective Intelligence
- Discoveries shared instantly
- No duplicate work
- Emergent insights

### Specialization
- GPU Embers: Deep thinking
- CPU Embers: Fast sensing
- Combined: Complete organism

### Resilience
- If one fails, others continue
- Distributed knowledge
- No single point of failure

## Future

- **Cross-machine swarms**: Multiple Servals connected
- **Hierarchical organization**: Queen/worker patterns
- **Evolution**: Tournament selection of best instances
- **Spore exchange**: Embers migrate between hosts

## Current Status

✓ Swarm coordinator built
✓ Message bus implemented
✓ Parallel play tested
✓ 5 instances ran successfully

Ready for full 12-ember deployment.
