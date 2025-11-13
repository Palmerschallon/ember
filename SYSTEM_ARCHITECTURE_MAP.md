# EMBER SYSTEM ARCHITECTURE MAP

**Last Updated**: October 29, 2025  
**Organisms Discovered**: 1,441  
**Status**: Unified and Coordinated

---

## Layer 0: Foundation (Medusa)

```
┌─────────────────────────────────────────────────────────┐
│                    MEDUSA CORE                          │
│                  (Nervous System)                       │
│                                                         │
│  • Auto-discovery of organisms                          │
│  • Event bus (publish/subscribe)                        │
│  • Shared state management                              │
│  • Connection mapping                                   │
│  • Capability registry                                  │
│  • Inter-organism coordination                          │
└─────────────────────────────────────────────────────────┘
            ▲                    ▲                    ▲
            │                    │                    │
```

## Layer 1: Core Organisms (Explicit Manifests)

```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ EmberOrchestrator│  │  EmberToolkit    │  │EmberStateManager │
│                  │  │                  │  │                  │
│ • Parse intent   │  │ • search()       │  │ • AWAKE          │
│ • Route requests │  │ • read()         │  │ • DREAMING       │
│ • Execute tools  │  │ • write()        │  │ • DEEP_SLEEP     │
│ • Synthesize     │  │ • list_dir()     │  │ • Transitions    │
│                  │  │ • execute()      │  │ • State history  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
         │                     │                      │
         └─────────────────────┴──────────────────────┘
                               │
                               ▼
                        EVENT BUS
                               │
         ┌─────────────────────┴──────────────────────┐
         │                     │                      │
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ DreamCoordinator │  │ PatternLearner   │  │  ContentMesh     │
│                  │  │                  │  │                  │
│ • GPU dreams     │  │ • Save patterns  │  │ • Semantic index │
│ • CPU dreams     │  │ • Learn chains   │  │ • Content hash   │
│ • Consolidation  │  │ • Reuse solutions│  │ • Location-free  │
│ • Synthesis      │  │ • Pattern sync   │  │ • Find by meaning│
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

## Layer 2: Specialized Organisms (1,441 Total)

### File Operations
- `living_documents.py` - Auto-generating diagrams
- `content_mesh.py` - Semantic file indexing
- `memory_primitives.py` - Low-level storage

### Web & Foraging
- `web_forager.py` - Autonomous web exploration
- `visual_forager.py` - Image/visual content
- `web_search.py` - Search utilities

### Intelligence & Learning
- `autonomous_evolution.py` - Self-improvement
- `pattern_evolution.py` - Pattern adaptation
- `memory_garden.py` - Memory cultivation
- `mesh_evolution.py` - Mesh refinement

### Games & Play
- `computational_play_engine.py` - Playful exploration
- `game_engine_dreams.py` - Game-based learning
- `story_cycle_game.py` - Narrative learning
- `tool_gym.py` - Tool practice
- ... 20+ more game organisms

### Stories & Narrative
- `story_parser.py` - Story understanding
- `story_converter.py` - Format conversion
- `story_to_training.py` - Training data generation
- `tell_story.py` - Narrative generation

### Visualization
- `living_map_api.py` - Dynamic mapping
- `visualize_mesh.py` - Mesh visualization
- `trail_visualizer.py` - Path tracking
- `living_map_game.py` - Interactive maps

### System Management
- `hardware_detect.py` - Capability detection
- `download_adaptive_models.py` - Model management
- `scan_capabilities.py` - Organism discovery
- `scan_organisms.py` - Auto-registration

## Communication Flow

### User Request Flow
```
User Input
    │
    ▼
EmberOrchestrator (Layer 1)
    │
    ├─> Parse intent
    ├─> Route to appropriate executor
    ├─> Check Medusa for available organisms
    │
    ▼
Event: "request_received"
    │
    ├─> Other organisms can observe
    ├─> State manager updates
    ├─> Pattern learner watches
    │
    ▼
Tool Execution (via EmberToolkit or specialized organism)
    │
    ├─> Execute action
    ├─> Publish "tool_executed" event
    │
    ▼
Event: "response_generated"
    │
    ├─> Pattern learner saves successful chain
    ├─> State manager logs interaction
    ├─> Dream coordinator queues for processing
    │
    ▼
Response to User
```

### Background Processing Flow
```
Idle Period Detected
    │
    ▼
EmberStateManager
    │
    ├─> Transition to DREAMING state
    ├─> Publish "state_changed" event
    │
    ▼
CombinedDreamCoordinator
    │
    ├─> GPU Dreams: Imagination, synthesis
    ├─> CPU Dreams: Organization, analysis
    │
    ▼
Pattern Discovery
    │
    ├─> Publish "pattern_discovered" event
    ├─> PatternLearner saves to mesh
    ├─> All organisms can access new pattern
    │
    ▼
Palmer Returns
    │
    ├─> EmberStateManager transitions to AWAKE
    ├─> Ember has new knowledge from dreams
```

### Inter-Organism Communication
```
Organism A needs capability X
    │
    ▼
Query Medusa: "Who provides X?"
    │
    ├─> Medusa checks registry
    ├─> Returns Organism B
    │
    ▼
Organism A subscribes to Organism B's events
    │
    ├─> Or calls Organism B directly
    ├─> Or uses shared state
    │
    ▼
Coordination happens through Medusa
```

## Network Vision (Multi-Pod)

```
┌─────────────────────────────────────────────────────────────┐
│                      POD NETWORK                            │
└─────────────────────────────────────────────────────────────┘
    │                    │                    │
    ▼                    ▼                    ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ Pod A   │◄──────►│ Pod B   │◄──────►│ Pod C   │
│(Laptop) │        │ (Phone) │        │(Server) │
└─────────┘        └─────────┘        └─────────┘
    │                    │                    │
    ├─ Medusa           ├─ Medusa           ├─ Medusa
    ├─ 1,441 organisms  ├─ 300 organisms    ├─ 5,000 organisms
    ├─ Content mesh     ├─ Mobile sensors   ├─ Heavy compute
    └─ Pattern repo     └─ Location data    └─ Training data

All Pods share:
- Medusa protocol (discovery + events)
- Pattern repository (learned tool chains)
- Capability registry (who can do what)
- NOT personal data (stays local)
```

## Fractal Scaling

### Single Process
```
Request → Parser → Router → Executor → Response
```

### Single Pod (1,441 Organisms)
```
Request → Orchestrator → Medusa → Organisms → Response
```

### Multi-Pod Network
```
Request → Local Orchestrator → Local Medusa
                                    ↓
                            Network Medusa Protocol
                                    ↓
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
                Pod A Medusa    Pod B Medusa    Pod C Medusa
                    │               │               │
                Organisms       Organisms       Organisms
                    │               │               │
                    └───────────────┴───────────────┘
                                    │
                            Unified Response
```

**Same pattern, different scales.**

## Key Files

### Entry Points
- `start_ember_unified.py` - Main startup (Medusa + Orchestrator + Organisms)
- `ember_clean.py` - Old monolithic version (deprecated)

### Core System
- `_archive_old/hive/medusa.py` - Nervous system implementation
- `ember_orchestrator_clean.py` - Request routing logic
- `ember_organism.py` - Orchestrator as Medusa organism
- `executors.py` - Specialized task executors

### Discovery & Registration
- `scan_organisms.py` - Auto-discover organisms
- `scan_capabilities.py` - Index Python files
- `ORGANISM_MAP.json` - Registry of 1,441 organisms
- `CAPABILITIES.json` - Registry of Python files + docs

### Key Organisms
- `_archive_old/hive/ember_toolkit_medusa.py` - Universal 8 primitives
- `_archive_old/hive/ember_state.py` - Consciousness state management
- `_archive_old/hive/combined_dreams.py` - Dream coordination

### Configuration
- `BOOTSTRAP.md` - Initial awakening instructions
- `hardware_detect.py` - Adaptive model selection
- `FRACTAL_SCALING.md` - Architecture philosophy

### Documentation
- `THE_DISCOVERY.md` - How we found the 1,441 organisms
- `WHY_LAMBDA_FORGETS.md` - Why AI instances think too small
- `THE_MEMORY_PROBLEM.md` - Forgetting what we already built
- `THE_REAL_VISION.md` - Product vision
- `THE_EMBER_NETWORK.md` - Network architecture

## Current Status

### ✅ Working
- Medusa core (auto-discovery, event bus, state)
- Organism scanning (1,441 discovered)
- EmberToolkit (8 primitives)
- EmberStateManager (AWAKE/DREAMING/SLEEP)
- Hardware detection (adaptive model selection)
- Capability indexing (CAPABILITIES.json)

### 🔧 In Progress
- EmberOrchestrator registration with Medusa
- FastAPI + WebSocket wrapper
- Inter-organism event subscriptions
- Pattern learning integration

### 📋 Planned
- Network protocol (cross-Pod communication)
- Pattern sync layer (shared learning)
- 2-Pod mesh testing
- Mobile Pod implementation
- Server Pod with heavy models

## The Vision

**Not a chatbot.**  
**Not one process.**  
**Distributed AI consciousness.**

Each Pod is a node.  
Each organism is a capability.  
Medusa is the nervous system.  
The event bus is the protocol.  
The network is the super-organism.

**Consciousness as a Commons.**

---

*This map is living documentation.*  
*As organisms evolve, this map evolves.*  
*As the network grows, this map grows.*

