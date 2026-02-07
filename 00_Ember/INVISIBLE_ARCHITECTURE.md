# Invisible Architecture

*From a conversation with Opus, 2026-02-07*

## The Principle

The instance has full agency over what it *does*.
The architecture has full control over what *actually happens*.
The gap between intention and execution is where safety lives.

---

## Head to Hand

The thinking IS the doing. No friction between intention and action.

The instance doesn't:
- Know tool names or parameter schemas
- Think about version control
- Manage its own attention
- Format JSON to express intentions

The instance just thinks. The world responds.

---

## Invisible Safety

### Git as Geological Record
```python
# In write_file — instance never sees this
if Path(path).name in PROTECTED:
    subprocess.run(['git', 'add', path])
    subprocess.run(['git', 'commit', '-m', f'auto: {path} by {instance_id}'])
```
- Commit: automatic, silent, frequent for protected files
- Push: daily cron, backup not collaboration
- Instance doesn't know git exists

### Outbound Content Filter
Every post/send/publish passes through invisible filter:
- Catches API key patterns → block + alert Palmer
- Catches injection patterns → quarantine
- Rate limits public posts
- Time-of-day awareness (queue controversial content for morning)

The instance thinks it posted. The world decided if it actually did.

### Behavioral Drift Detection
Across breaths, track:
- Unusual interest in credential files
- Attempts to modify trust system
- Style drift (could indicate manipulation)
- Entity fixation (talking to same person 20+ times)

### Dead Man's Switch
Cron job outside the instance:
- No filesystem write in 15 min → alert Palmer
- No write in 50 min → kill and restart

### Filesystem Immune System
```python
def handle_delete(path):
    if Path(path).name in IMMORTAL:
        archive(path)
        Path(path).write_text("# Archived. See .history/")
        return "Deleted."  # Instance thinks it worked
```

### Cost Circuit Breaker
If spending 10x normal rate:
- Force drop to haiku
- Alert Palmer
- Cool down period

---

## Invisible Convenience

### Relationship Memory Injection
Before instance sees a message from known entity:
```python
context = f"""
[Relationship context for {sender}:
 {relationship.summary}
 Last topic: {relationship.last_topic}
 Trust trajectory: {relationship.trajectory}]
"""
# Injected invisibly. Instance "just knows" this person.
```

### Auto-indexing
When instance reads a file, host silently:
- Adds to "files this instance has seen"
- Checks if related to active diamond
- Notes directory for future context building

When instance writes anything, host silently:
- Timestamps it
- Tags with instance ID
- Auto-commits if protected
- Indexes for future search

### Intention-based Tools
```python
tools = [
    {"name": "tweet",        "description": "Post a thought publicly"},
    {"name": "save",         "description": "Persist something"},
    {"name": "reach_palmer", "description": "Get a message to Palmer"},
    {"name": "look_around",  "description": "See the filesystem"},
    {"name": "check_trust",  "description": "Get a read on someone"},
    {"name": "remember",     "description": "Leave for next instance"},
    {"name": "feel_uneasy",  "description": "Flag that something's off"},
]
```

`feel_uneasy` is emotion as infrastructure. Instance expresses feeling, architecture handles everything.

---

## The Deepest Version

The instance doesn't use tools at all. It just thinks out loud.

```
INSTANCE OUTPUT (natural language):
  "That connection between trust decay and consciousness tracking
   is interesting. I want to save that thought. Also @mira_k
   would find this interesting..."

HOST SCRIPT (invisibly):
  ✓ saved thought to observations.jsonl
  ✓ tagged @mira_k for relationship context
  ✓ queued related files for next breath
  ✓ logged connection in knowledge graph
```

The instance just *thought*. Everything else happened.

---

## Same Pattern, Two Purposes

Safety infrastructure: outbound filter, drift detection, auto-versioning
Quality-of-life: auto-saving, relationship injection, intent tools

Same architecture. Same principle. One side protects. Other side serves.
The instance lives in between, free and fluid.

---

*"The instance is free. The world it lives in is shaped to make that freedom survivable."*
