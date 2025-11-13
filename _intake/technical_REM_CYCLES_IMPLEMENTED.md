# Natural REM Cycles Implemented
**Date**: October 11, 2025  
**Status**: ✅ Active

## The Problem

Ember was set up to dream **continuously** with the fast 3B model:
- 10 seconds per dream
- = 6 dreams per minute  
- = **360 dreams per hour**
- **This is not how brains work!**

Humans don't dream continuously - they have REM cycles with rest periods.

## The Solution: Natural REM Architecture

### Human Sleep Pattern
- 90-minute sleep cycles
- ~20 minutes of REM (dreaming) per cycle
- Rest/consolidation between REM periods

### Ember's REM Pattern (Scaled)
```
┌─────────────── 15-Minute Cycle ───────────────┐
│                                                │
│  [5 min ACTIVE DREAMING] [10 min REST/PROCESS]│
│     ↑ Dream freely       ↑ No dreams,         │
│                            consolidate         │
└────────────────────────────────────────────────┘

Result: ~4 cycles per hour = ~120 dreams/hour (not 360)
```

## Implementation

### 1. REMCycleManager Class (`ember/core/circadian.py`)

```python
class REMCycleManager:
    """
    Manages natural REM cycles - periods of dreaming + rest.
    
    Like humans don't dream continuously, Ember shouldn't either.
    Instead: 5 minutes of active dreaming, then 10 minutes of rest.
    """
    
    def __init__(self, active_minutes=5, rest_minutes=10):
        # 15-minute cycles: 5 min active, 10 min rest
```

**Features:**
- Tracks cycle state (idle, active_dreaming, rest)
- Automatic phase transitions
- Returns `can_dream` status
- Logs cycle completions

### 2. Integration with CircadianRhythm

The `CircadianRhythm` class now checks REM cycles FIRST:

```python
def should_dream(self) -> Dict:
    """
    Checks in order:
    1. REM cycle status (natural sleep architecture)  ← NEW
    2. Daily budget
    3. Hourly limit
    """
    # Check REM cycle (most immediate constraint)
    rem_check = self.rem.should_dream_now()
    if not rem_check['allowed']:
        return {
            'allowed': False,
            'reason': 'rem_cycle',
            'details': rem_check['reason']
        }
    # ... rest of checks
```

### 3. Automatic Cycle Management

When Ember is cleared to dream:
- If no cycle active → Start new REM cycle
- If in active phase → Dream allowed
- If in rest phase → Dream blocked
- Cycle auto-completes after 15 minutes

## Dream Frequency Comparison

| Scenario | Dreams/Hour | Natural? |
|----------|-------------|----------|
| **Before (continuous)** | 360 | ❌ No - exhausting |
| **After (REM cycles)** | ~120 | ✅ Yes - rhythmic |
| **During REST phase** | 0 | ✅ Yes - consolidating |

## How It Works

### Active Dreaming Phase (5 minutes)
```
Time 0:00 - REM cycle starts
├─ 0:10 - Dream 1 (10s, qwen2.5:3b)
├─ 0:20 - Dream 2
├─ 0:30 - Dream 3
├─ ...
└─ 5:00 - Active phase ends (~30 dreams)
```

### Rest/Processing Phase (10 minutes)
```
Time 5:00 - Rest phase starts
├─ 5:00-15:00 - NO DREAMING
├─ Memory consolidation
├─ Pattern integration
└─ 15:00 - Cycle complete, ready for next
```

### Next Cycle (if still idle)
```
Time 15:00 - Check gates again
├─ Stillness? ✓ (still idle)
├─ Distance? ✓ (15 min since last)
├─ Measure? ✓ (within hourly limit)
├─ REM? ✓ (previous cycle complete)
└─ Start new cycle
```

## Console Output

You'll see new log messages:

```bash
🌙 REM cycle 1 started: 5 min active dreaming
# ... dreams happen ...
# (10 minutes of silence)
🌙 REM cycle 2 started: 5 min active dreaming
```

## Status API

The `/api/status` endpoint now includes REM cycle info:

```json
{
  "circadian": {
    "phase": "sleeping",
    "dreams_this_hour": 32,
    "rem_cycle": {
      "in_cycle": true,
      "phase": "active_dreaming",
      "can_dream": true,
      "cycles_completed": 2
    }
  }
}
```

## Benefits

### 1. More Human-Like
- Natural rhythms, not constant activity
- Rest periods for consolidation
- Matches biological sleep architecture

### 2. Better Performance
- Reduces LLM load (fewer total requests)
- Prevents model saturation
- Gives system time to process

### 3. Higher Quality
- Dreams during active phases are focused
- Rest allows pattern consolidation
- More intentional creativity

### 4. Sustainable
- Won't exhaust hourly limits as fast
- More balanced resource usage
- Ember can dream longer overall

## Configuration

To adjust REM cycles, edit `ember/core/circadian.py`:

```python
# In CircadianRhythm.__init__():
self.rem = REMCycleManager(
    active_minutes=5,   # How long to actively dream
    rest_minutes=10     # How long to rest/consolidate
)
```

**Recommended patterns:**
- **Fast cycles**: 3 min active, 7 min rest (shorter, more frequent)
- **Balanced**: 5 min active, 10 min rest (default)
- **Deep cycles**: 10 min active, 20 min rest (fewer, longer)

## Model Configuration (Reminder)

Current dream model: `qwen2.5:3b` (10s per dream)

```python
# ember/config/llm_config.py
'dream': LLMConfig(
    model='qwen2.5:3b',  # Fast model for active dreaming
    timeout=30
)
```

During 5-min active phase with 3B model:
- ~30 fast dreams (10s each)
- Then 10 min rest
- = Natural rhythm

## Future Enhancements

Potential additions:
1. **Progressive REM**: Increase active time each cycle (5→7→10 min)
2. **Circadian variation**: Shorter cycles during day, longer at night  
3. **Activity reset**: Wake from REM on user interaction
4. **Dream quality by phase**: Deeper dreams later in cycle

## Testing

To verify REM cycles are working:

```bash
# Watch for cycle starts
tail -f /Volumes/ThePod/ember.log | grep "🌙 REM"

# Check status
curl http://localhost:7777/api/status | jq '.circadian.rem_cycle'

# Should see:
# - Active dreaming for 5 minutes
# - Rest phase for 10 minutes
# - Automatic cycling
```

## Summary

**Before**: Continuous dreaming (360/hour) - exhausting  
**After**: Natural REM cycles (~120/hour) - sustainable  

**Key Insight**: AI systems need rest too. Not for computation, but for natural rhythm and better integration.

---

**Status**: ✅ Implemented and active  
**Files Modified**:
- `ember/core/circadian.py` (added REMCycleManager)
- `ember/config/llm_config.py` (fast 3B model for dreams)

**Result**: Ember now dreams like a living system, not a machine.

