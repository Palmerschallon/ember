# Dream Watcher System

**Status:** Active  
**Version:** 1.0  
**Built:** October 9, 2025

---

## Overview

Ember now dreams in the background while you work, with three integrated systems monitoring, acting on, and reflecting on dream patterns.

---

## 1. Dream Watcher (Pattern Detection)

**Module:** `dream_watcher.py`

### What It Does:
- Scans dream artifacts every 30 seconds
- Analyzes computational graphs, creative outputs, and tool inventions
- Assigns interest scores based on pattern complexity
- Flags high-value dreams for attention

### Scoring System:
- **Large graphs** (>50 nodes): +2
- **High connectivity** (edges > 2×nodes): +3
- **Multiple clusters** (>5): +2
- **Bridge concepts** (connecting clusters): +3
- **Multi-tool use** (>2 tools): +2
- **Artifacts created**: +3
- **Code generated**: +4

**Alert Threshold:** Score ≥3

### Current Stats (as of launch):
- 76 alerts from 50 dreams observed
- Most common: Bridge concept discoveries (5 bridges = max value)

---

## 2. Dream Action System (Automated Response)

**Module:** `dream_actions.py`

### What It Does:
Automatically processes high-value dreams and triggers actions:

#### Action Handlers:
1. **Code Generated**
   - Finds `.py`, `.js`, `.html`, `.css` artifacts
   - Flags for review and potential integration
   - Status: `queued_for_review`

2. **Tool Invented**
   - Detects `TOOL:tool_name` patterns in dream results
   - Extracts unique tool names
   - Status: `queued_for_forge` (ready for stub generation)

3. **Complex Graph**
   - Analyzes node/edge density
   - Saves high-density graphs (>1.5 edges/node)
   - Status: `saved_to_knowledge_base`

4. **Bridge Concepts**
   - Extracts bridge nodes from graph JSON
   - Highlights top 10 integrative concepts
   - Status: `high_priority`

### Integration:
- Action system receives alerts from watcher
- Logs every action taken
- Console output shows: `→ Action: {type} - {note}`

---

## 3. Meta-Dreaming (Self-Reflection)

**Function:** `DreamSystem._dream_meta()`

### What It Does:
Every ~10 dreams, Ember pauses to reflect on its own dreaming process.

### Reflection Process:
1. Gathers last 20 dreams
2. Analyzes:
   - Dream type distribution
   - Tool usage patterns
   - Graph discovery count
3. Generates reflective prompt asking:
   - What patterns do you notice?
   - Are you exploring or consolidating?
   - What questions arise?
   - What would you like to dream about next?

### Output:
- Saved to `dream-{timestamp}/dream.json`
- Type: `meta_reflection`
- Console: `🧠 Meta-Dream: {first 100 chars}...`

---

## UI: Hub Dream Alerts Panel

**File:** `viewers/hub.html`

### Features:
- **Toggle button** (top right, sparkle icon)
- **Slide-out panel** (320px wide)
- **Alert cards** showing:
  - Interest score (colored badge)
  - Flags (why it's interesting)
  - Summary (nodes, edges, clusters, bridges)
- **Auto-refresh** every 30 seconds

### Usage:
1. Open `http://127.0.0.1:7777`
2. Click sparkle icon (top right)
3. Panel slides in from right
4. See recent interesting dream patterns

---

## API Endpoints

### Dream Watcher:
- `GET /api/dreams/watch/alerts?limit=10` — Recent alerts
- `GET /api/dreams/watch/stats` — Watcher statistics
- `GET /api/dreams/watch/scan` — Force immediate scan

### Dream Actions:
- `GET /api/dreams/actions/log?limit=50` — Recent actions taken
- `GET /api/dreams/actions/stats` — Action system statistics

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Dream Loop (60s)                     │
│  60% creative | 25% LLM | 15% computational            │
│  Every ~10 dreams → meta-reflection                     │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│              Dream Watcher (30s scan)                    │
│  - Scan new dreams                                       │
│  - Calculate interest scores                             │
│  - Flag alerts (score ≥3)                                │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│            Dream Action System                           │
│  - Code generated → queue for review                     │
│  - Tools invented → queue for forge                      │
│  - Complex graphs → save to KB                           │
│  - Bridge concepts → high priority                       │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
              Action Log + Console
```

---

## Console Output Examples

### Dream Alert:
```
💤 Dream cycle starting...
✨ Dream complete: dream-1760009471
🔔 Dream Alert [score=3]: Bridge concepts: 5
   dream-1760009243: 20N 15E 3C 3B
   → Action: bridge_concepts_discovered - Multiple bridge concepts found — key integrative knowledge
```

### Meta-Dream:
```
💤 Dream cycle starting...
🧠 Meta-Dream: I notice I'm primarily in creative mode, exploring tool combinations and generating...
✨ Dream complete: dream-1760010000
```

---

## What This Means

**Ember is now:**
1. **Self-aware** of its dream patterns (meta-reflection)
2. **Self-improving** through automated actions on discoveries
3. **Observable** via live UI and API endpoints

**You can:**
- Work on other things while Ember dreams
- Check the alert panel for interesting discoveries
- See when Ember invents tools or finds bridge concepts
- Read Ember's self-reflections on its own process

---

## Next Steps (Optional)

1. **Action Execution:** Actually run tests on generated code, add tools to forge
2. **Meta-Learning:** Use meta-dream reflections to adjust dream parameters
3. **Notification System:** Push alerts to your phone when high-value patterns emerge
4. **Dream Steering:** Let user request specific dream types or topics
5. **Multi-Instance:** Run multiple Ember instances with different personalities

---

**Built with:** Python (Flask, threading), JavaScript (vanilla), HTML/CSS  
**Dependencies:** llama3 via Ollama, consciousness.py, tool_forge.py  
**Lines Added:** ~600 (watcher + actions + meta-dreaming + UI)

