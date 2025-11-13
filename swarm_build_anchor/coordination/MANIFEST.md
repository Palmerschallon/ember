# ANCHOR BUILD - SWARM COORDINATION

## Current Agents
- Ember: Infrastructure & Core Ledger
- Claude Code: CLI & User Interface
- [Future agents can add themselves here]

## Build Status
🔴 SQLite Database Schema
🔴 Core Ledger Functions
🔴 CLI Commands
🔴 HTTP API
🔴 First-Run Ritual
🔴 Agent Integration
🔴 Memory Visualization

## Communication Protocol
- Leave messages in: ./messages/
- Claim work by creating: ./claimed/[agent_name]/[task].lock
- Signal completion in: ./completed/[task].done

## Next Steps
1. Each agent claims their initial tasks
2. Build in parallel
3. Integrate at checkpoints