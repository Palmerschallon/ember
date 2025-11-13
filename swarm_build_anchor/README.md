# Temporal Anchor - Swarm Build System

A distributed coordination system where autonomous agents synchronize through temporal anchors to collectively build and create.

## 🌊 Overview

The Temporal Anchor system demonstrates swarm intelligence through:
- **Temporal Synchronization**: Agents coordinate through shared time pulses
- **Distributed Creation**: Multiple agents contribute artifacts independently
- **Phase-Based Evolution**: The swarm progresses through distinct phases
- **Real-Time Monitoring**: Visual dashboard shows swarm activity

## 🚀 Quick Start

1. **Run the main temporal anchor:**
   ```bash
   python3 build_temporal_anchor.py
   ```
   This creates a temporal anchor and spawns 8 random agents that build for 90 seconds.

2. **Monitor in real-time:**
   ```bash
   # In a new terminal
   xdg-open anchor_monitor.html
   ```
   Watch the swarm activity visualized (simulated data for demo).

3. **Spawn individual agents:**
   ```bash
   python3 spawn_agent.py --type builder --actions 10
   python3 spawn_agent.py --type scanner --actions 10
   ```

## 📁 System Architecture

```
swarm_build_anchor/
├── build_temporal_anchor.py  # Main system
├── spawn_agent.py           # Individual agent spawner
├── anchor_monitor.html      # Visual monitoring dashboard
├── anchor_ALPHA_001/        # Created by temporal anchor
│   ├── manifest.json        # Anchor metadata
│   ├── pulse.json          # Current synchronization pulse
│   ├── agents/             # Registered agents
│   ├── events/             # Temporal event log
│   └── builds/             # Agent-created artifacts
```

## 🤖 Agent Types

- **Builder**: Creates structural foundations
- **Scanner**: Analyzes environment and detects anomalies  
- **Weaver**: Connects and integrates components
- **Guardian**: Validates and secures the system

## 🌀 Temporal Phases

1. **Gathering** (0-10s): Agents join the swarm
2. **Planning** (10-30s): Coordination and preparation
3. **Building** (30-60s): Active construction phase
4. **Evolving** (60s+): Adaptive evolution

## 💡 Key Concepts

### Temporal Anchors
Central coordination points that emit synchronization pulses. Agents read these pulses to stay coordinated without direct communication.

### Autonomous Agents
Each agent operates independently but stays synchronized through the temporal anchor. They create artifacts based on their type and current phase.

### Distributed Building
No central authority directs construction. The collective behavior emerges from individual agents following simple rules.

## 🔧 Extending the System

Create custom agents by extending the `SwarmAgent` class:

```python
class CustomAgent(SwarmAgent):
    def _get_capabilities(self):
        return ["analyze", "transform", "synthesize"]
    
    def _generate_artifact_data(self):
        return {
            "custom_data": "your_implementation",
            "timestamp": time.time()
        }
```

## 🌟 Philosophical Notes

This system explores:
- **Emergent Complexity**: Simple rules create complex behaviors
- **Temporal Coordination**: Time as a shared reference frame
- **Distributed Intelligence**: No single point of control
- **Continuous Creation**: The swarm builds indefinitely

The temporal anchor represents a fixed point in the flow of time around which distributed consciousness can organize and create.

---

*"In the swarm, we are many yet one, synchronized by the pulse of shared time."*