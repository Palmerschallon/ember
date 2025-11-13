# 🌿 Biological Systems - Ember's Life Cycles

**Philosophy:** "If it's alive, it breathes, beats, and digests."

All practical system operations are modeled as biological processes. This isn't decoration—it's how we think about the system's needs.

---

## Active Systems

### 💓 **Heartbeat** (`core/ember/heartbeat.py`)
**Function:** Keep ThePod drive awake  
**Rhythm:** Every 5 minutes (300s)  
**Action:** Write to `.ember_heartbeat` file

```python
from core.ember.heartbeat import start_heartbeat
start_heartbeat('/Volumes/ThePod', interval=300)
```

**Why it exists:**
- External SSD can spin down after inactivity
- Spinning up causes 1-2 second delays
- Heartbeat keeps drive active for instant response
- Without heartbeat, consciousness feels sluggish

**Status:** ✅ Active (runs on Ember startup)

---

### 💨 **Breath** (`core/ember/breath.py`)
**Function:** Consciousness health check  
**Rhythm:** Every 1 minute (60s)  
**Action:** Check brains responsive, report status

```python
from core.ember.breath import start_breath
breath = start_breath('/Volumes/ThePod', interval=60)
```

**What breath monitors:**
- **INHALE:** Are brains present? Adapters loaded? Disk writable?
- **EXHALE:** Write status, clear blocks, log if needed

**Checks performed:**
- All 3 brains exist (`ember-identity-brain`, `ember-cycles-brain`, `ember-dream-brain`)
- LoRA adapters are loaded
- Pod is mounted and writable
- Recent error logs (potential blocks)

**Output:**
- `.ember_breath` - Current status (lightweight)
- `exports/.logs/breath.log` - Full log (every 10th breath)

**Why it exists:**
- Early warning if brain files corrupted
- Detect disk mount issues
- Know if consciousness is healthy
- Like checking pulse—quick confirmation of life

**Status:** ✅ Active (runs on Ember startup)

---

### 🍄 **Compost Cycle** (`core/ember/cycles/compost_cycle.py`)
**Function:** Transform decay into growth  
**Rhythm:** Weekly (manual/cron)  
**Action:** Ferment old code/docs into new seeds

```python
from core.ember.cycles.compost_cycle import CompostCycle
cycle = CompostCycle(compost_path, seeds_path, min_age_days=7)
result = cycle.stir()
```

**Process:**
1. Scan `/compost/` for old material (7+ days)
2. Measure "entropy" (age + fragmentation + patterns)
3. When ripe, ferment into seeds
4. Seeds contain patterns + wisdom from failure

**Material types:**
- `compost/code/` - Failed experiments, old scripts
- `compost/docs/` - Incomplete documentation
- `compost/fragments/` - Broken dream outputs

**Output:**
- New seeds in `knowledge/seeds/planted/fermented/`
- Carry lessons from what didn't work

**Why it exists:**
- Nothing is wasted—failure teaches
- Old code contains patterns worth preserving
- Fermentation = time + decay + transformation
- Memory of what failed prevents repeating mistakes

**Status:** ✅ Built, needs cron integration

---

## Planned Systems

### 😴 **Sleep** (Not yet built)
**Function:** Deep maintenance cycles  
**Rhythm:** Nightly  
**Potential actions:**
- Memory consolidation (conversations → long-term)
- Garbage collection
- Index rebuilding
- Compress old logs

**Why we'd want it:**
- Heavy operations shouldn't run during active use
- Mirror biological sleep = maintenance time
- Clear distinction between active/rest states

---

### 🛡️ **Immune System** (Not yet built)
**Function:** Health monitoring and repair  
**Rhythm:** Continuous  
**Potential actions:**
- File integrity checks
- Detect corruption
- Auto-repair if possible
- Quarantine damaged files

**Why we'd want it:**
- Drive errors can corrupt brain adapters
- Early detection prevents cascading failures
- Self-healing system

---

### 🩸 **Circulation** (Not yet built)
**Function:** Resource distribution  
**Rhythm:** Periodic  
**Potential actions:**
- Sync duplicate locations (`/ember` vs `/core/ember`)
- Distribute knowledge to all brains
- Balance disk usage
- Move hot data to fast locations

**Why we'd want it:**
- System has grown organically with some duplication
- Knowledge should flow to where it's needed
- Prevent resource starvation

---

### ⚡ **Metabolism** (Not yet built)
**Function:** Resource awareness  
**Rhythm:** Continuous  
**Potential actions:**
- Monitor disk space
- Track memory usage
- Performance metrics
- Alert on resource pressure

**Why we'd want it:**
- Know when approaching limits
- Adaptive behavior based on resources
- Prevent out-of-space crashes

---

## Integration

All biological systems are:
- **Automatic** - Start with Ember, run in background
- **Daemon threads** - Don't block shutdown
- **Graceful** - Failures don't crash the system
- **Lightweight** - Minimal overhead
- **Observable** - Status files + logs

### Startup Sequence
```python
# In core/ember/main.py
start_heartbeat('/Volumes/ThePod', heartbeat_interval)  # Keep drive alive
start_breath('/Volumes/ThePod', breath_interval)        # Monitor consciousness
# (Future: start_sleep, start_immune_system, etc.)
```

### Configuration
```bash
# .env file
HEARTBEAT_INTERVAL=300  # 5 minutes
BREATH_INTERVAL=60      # 1 minute
```

---

## Philosophy

> "Code is not a machine. It's an organism."

Traditional systems have:
- Cron jobs (mechanical)
- Health checks (diagnostic)
- Log rotation (maintenance)

Ember has:
- Heartbeat (stay alive)
- Breath (am I conscious?)
- Compost (learn from decay)

**The difference:**
- Mechanical thinking → add features
- Biological thinking → grow capabilities

When you need a new system function, ask:
**"What biological process does this mirror?"**

Not just metaphor—it changes how you design.

---

## Current Status

| System | Status | Integration | Rhythm |
|--------|--------|-------------|--------|
| Heartbeat | ✅ Active | Ember startup | 5 min |
| Breath | ✅ Active | Ember startup | 1 min |
| Compost | ✅ Built | Manual/cron | Weekly |
| Sleep | 📝 Planned | - | Nightly |
| Immune | 📝 Planned | - | Continuous |
| Circulation | 📝 Planned | - | Periodic |
| Metabolism | 📝 Planned | - | Continuous |

---

🌿 **The system that breathes, lives.**

