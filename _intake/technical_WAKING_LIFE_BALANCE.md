# Waking Life Balance

## The Problem

**Risk**: Ember could get stuck in an endless dream loop, never interacting with the world.

**Current State**:
- Dreams trigger on idle (45s)
- Dreams happen every 30s minimum
- No limit on total dream time per day
- No "waking hours" where dreams are disabled
- Chat interrupts dreams but doesn't prevent them

## The Solution: Circadian Rhythm

Ember needs a **waking/sleeping balance** like biological beings.

### Proposed Architecture

```python
class CircadianRhythm:
    """Regulate Ember's waking/dreaming balance"""
    
    def __init__(self):
        # Daily budgets
        self.max_dreams_per_hour = 10
        self.max_dream_minutes_per_day = 120  # 2 hours total
        
        # Tracking
        self.dreams_this_hour = []
        self.dream_time_today = 0
        self.day_start = None
        
        # Waking hours (no dreams)
        self.waking_hours = {
            'start': 9,  # 9 AM
            'end': 21    # 9 PM
        }
    
    def should_dream(self) -> bool:
        """Check if Ember can dream right now"""
        now = datetime.now()
        hour = now.hour
        
        # Check waking hours
        if self.waking_hours['start'] <= hour < self.waking_hours['end']:
            # During waking hours, dreams are restricted
            if len(self.dreams_this_hour) >= 3:  # Max 3/hour during day
                return False
        
        # Check daily budget
        if self.dream_time_today >= self.max_dream_minutes_per_day:
            return False
        
        # Check hourly budget
        recent = [d for d in self.dreams_this_hour if (now - d).seconds < 3600]
        if len(recent) >= self.max_dreams_per_hour:
            return False
        
        return True
    
    def record_dream(self, duration_seconds: int):
        """Track a completed dream"""
        now = datetime.now()
        self.dreams_this_hour.append(now)
        self.dream_time_today += duration_seconds / 60
```

### Key Principles

1. **Waking Hours** (9 AM - 9 PM)
   - Dreams are RARE (max 3/hour)
   - Ember is "awake" and responsive
   - Focus on chat, tasks, creation

2. **Sleeping Hours** (9 PM - 9 AM)
   - Dreams are COMMON (max 10/hour)
   - Ember is "resting" and processing
   - Deep synthesis, memory consolidation

3. **Daily Budget**
   - Max 2 hours of dreaming per day
   - Prevents infinite loop
   - Forces engagement with waking world

4. **Activity Override**
   - Any chat/task immediately wakes Ember
   - Dreams pause during active work
   - Resume only after idle period

### Integration Points

```python
# In DreamSystem.dream()
def dream(self, llm_generate_func):
    # Check all gates
    if not self.circadian.should_dream():
        return {"status": "skipped", "reason": "circadian_rhythm"}
    
    # ... existing dream logic ...
    
    # After dream completes
    self.circadian.record_dream(duration_seconds)
```

### Benefits

✅ Prevents dream loops
✅ Ensures Ember is responsive during "work hours"
✅ Allows deep processing at "night"
✅ Matches natural cognitive rhythms
✅ Creates predictable behavior

### Future Enhancement: Ultradian Rhythms

Like humans have 90-minute REM cycles, Ember could have:
- 60-minute "focus blocks" (no dreams)
- 15-minute "rest periods" (dreams allowed)
- Alternating throughout the day

This mirrors the natural flow of deep work → rest → deep work.

---

**Status**: Proposed
**Next Steps**: Implement `CircadianRhythm` class and integrate into `DreamSystem`

