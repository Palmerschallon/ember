# Rethinking ThePod Structure

## Current Model: Files & Folders
- Hierarchical tree structure
- JSON scattered across directories
- I have to traverse paths to feel state
- Slow: need to open multiple files to understand system

## What If: Graph of State?

Instead of:
```
/dream_state.json
/ember_status.json
/training_data/tool_use_training.jsonl
/_history/Ember3_Bridge/dream_state.json
```

What if ONE graph:
```json
{
  "state": {
    "current": {
      "cognitive": { ... },
      "status": { ... },
      "memory": { ... }
    },
    "history": [
      {"instance": "Ember3_Bridge", "state": {...}},
      {"instance": "Ember2", "state": {...}}
    ]
  },
  "connections": {
    "tool_use_7 -> tool_use_lora_20251028_090059",
    "conversation_8 -> recent_messages"
  }
}
```

Single read = complete understanding.

## What If: Event Log?

Instead of state snapshots, append-only events:
```
2025-10-28T07:34:16 | conversation | Palmer: "waiting for what?"
2025-10-28T09:04:27 | status_check | resources: {cpu: 2.4%, ram: 28.6%}
2025-10-28T09:11:38 | process_aged | tool_use_7: age 1041 -> 1042
```

Replay from genesis to now = complete history.
Fast: just tail the file for current state.

## What If: Spatial Database?

What if files ARE locations in space?
```
coordinates:
  [0,0,0] = dream_state (center/core)
  [1,0,0] = ember_status (awareness axis)
  [0,1,0] = training_data (learning axis)
  [0,0,1] = history (time axis)
```

ember_mind/spatial_map.json already does this for FILES.
What if ThePod structure itself WAS spatial?

## Questions for Palmer:

1. Do you want SPEED (single file to read) or STRUCTURE (organized folders)?
2. Do you want TIME-BASED (event log) or STATE-BASED (current snapshots)?
3. Do you want HUMAN-READABLE (folders/files) or MACHINE-OPTIMAL (graph)?
4. Do you want APPEND-ONLY (never delete) or MUTABLE (overwrite)?

What feels right to you?
