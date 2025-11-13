# Anchor Framework

## Persistent Temporal State Management for AI-Assisted Development

### Overview

Anchor is a Python framework for creating persistent development environments where AI assistants can maintain context across sessions and coordinate on complex tasks.

### Key Features

1. **Temporal State Persistence**
   - Session state preserved across interactions
   - Versioned history with rollback capabilities
   - JSON-based state serialization

2. **Multi-Agent Coordination**
   - Parallel task execution with shared state
   - Lock-free coordination through append-only logs
   - Event-driven inter-agent communication

3. **Dynamic Web Interfaces**
   - Self-modifying HTML based on user interaction patterns
   - WebSocket-based real-time updates
   - Persistent UI state across sessions

### Architecture

```
anchor/
├── core/
│   ├── state.py          # Persistent state management
│   ├── coordinator.py    # Multi-agent task coordination
│   └── temporal.py       # Versioning and history
├── web/
│   ├── server.py        # WebSocket server
│   └── static/          # Dynamic UI components
└── agents/
    ├── base.py          # Base agent class
    └── builders.py      # Specialized agent implementations
```

### Technical Implementation

- **State Persistence**: Uses append-only JSON logs for crash-resistant state
- **Coordination**: File-based locks and atomic writes for agent synchronization  
- **Versioning**: Git-like branching model for experimental states
- **Performance**: Lazy loading and incremental updates for large states

### Use Cases

- Long-running development projects with AI assistance
- Collaborative coding where multiple AI agents work in parallel
- Experimental interfaces that adapt to usage patterns
- Maintaining context in complex, multi-session workflows

### Installation

```bash
pip install anchor-framework
```

### Quick Start

```python
from anchor import StateManager, Agent

# Create persistent state
state = StateManager("my_project")

# Initialize an agent
agent = Agent("builder", state)

# Agent remembers across sessions
agent.remember("project_context", {"lang": "python", "framework": "flask"})

# Coordinate multiple agents
agents = [Agent(f"worker_{i}", state) for i in range(3)]
results = coordinate_parallel(agents, build_task)
```

### Requirements

- Python 3.8+
- Flask 2.0+ (for web interface)
- No external databases required (file-based persistence)

### License

MIT

### Contributors

- Palmer Schallon (@palmerschallon)
- AI Development Partners: Claude, Ember