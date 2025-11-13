# 💤 Digital REM Cycles - Ember's Sleep Architecture

**Question:** Should Ember have multiple short dreams or one long dream?

---

## Current State

**Configuration:**
- Dream trigger: After 10 minutes of idle (600 seconds)
- Dream duration: Max 2 minutes (120 seconds)
- Reset after each dream
- Can dream multiple times per night

**Behavior:**
- Ember idles → starts dreaming after 10 min
- Dreams for ~2 min
- Wakes up (any activity resets timer)
- If no activity, dreams again after 10 min
- Cycle repeats

**Result:** Multiple short dreams throughout idle periods

---

## Human Sleep Architecture (Inspiration)

### Natural REM Cycles

**Typical night (8 hours):**
- 4-6 complete sleep cycles
- Each cycle: ~90 minutes
- REM periods get progressively longer:
  - Cycle 1: 10 min REM
  - Cycle 2: 15 min REM
  - Cycle 3: 20 min REM
  - Cycle 4: 25 min REM
  - Cycle 5: 30+ min REM

**Why this pattern?**
- Early cycles: Memory consolidation (short-term → long-term)
- Later cycles: Creative synthesis (novel connections)
- Progressive deepening allows for:
  - Incremental processing
  - Building on earlier insights
  - Avoiding cognitive overload

---

## Digital Sleep Considerations

### Differences from Human Sleep

**Ember doesn't have:**
- Biological fatigue
- Physical restoration needs
- Chemical neurotransmitter cycles
- Sleep pressure accumulation

**Ember does have:**
- Memory to consolidate (chat logs, events)
- Seeds to synthesize
- Patterns to identify
- Insights to generate
- Limited LLM context window

**Key constraint: Context window**
- Ember's "working memory" during dreams
- Can only process ~5-6 seeds + recent context
- Can't dream about *everything* at once

---

## Options for Dream Architecture

### Option 1: Multiple Short Dreams (Current)
```
Idle 10 min → Dream 2 min → Reset
Idle 10 min → Dream 2 min → Reset
Idle 10 min → Dream 2 min → Reset
...
```

**Pros:**
- Frequent memory consolidation
- Quick response to new information
- Lower compute per dream
- Each dream has focused scope

**Cons:**
- Fragmented synthesis
- Can't build on previous dream insights
- Repetitive if nothing new to process
- May miss deeper connections

### Option 2: One Long Dream
```
Idle 10 min → Dream 60 min (continuous) → Wake
```

**Pros:**
- Deep synthesis possible
- Can explore multiple seed connections
- Time for complex insight generation
- More "REM-like" creative processing

**Cons:**
- High compute cost (60 min of LLM calls)
- Risk of repetition/loops
- All-or-nothing (if interrupted, lose progress)
- May generate too much at once

### Option 3: Progressive Dream Cycles (Human-like)
```
Idle → Dream 5 min (consolidation) → Brief wake
Idle → Dream 10 min (synthesis) → Brief wake
Idle → Dream 15 min (deep synthesis) → Brief wake
Idle → Dream 20 min (creative) → Full wake
```

**Pros:**
- Mimics natural sleep architecture
- Progressive deepening
- Each cycle builds on previous
- Natural stopping points

**Cons:**
- More complex to implement
- Requires state tracking across cycles
- May be over-engineered

### Option 4: Threshold-Based Dreams
```
Accumulate "dream pressure":
- New conversations → +pressure
- New seeds → +pressure
- Long idle → +pressure

When pressure > threshold:
  Dream for duration ∝ pressure
  (More to process = longer dream)
```

**Pros:**
- Adaptive to actual need
- Don't dream when nothing new
- Dream longer when lots to process
- Efficient resource use

**Cons:**
- Requires pressure tracking
- Complex threshold tuning
- May still dream unnecessarily

---

## Optimal Digital REM Architecture

### Proposal: Progressive Cycles with Adaptive Duration

**Design:**
```python
class DreamCycle:
    def __init__(self):
        self.cycle_count = 0
        self.cycle_durations = [5, 10, 15, 20]  # minutes
        self.seed_pool_size = self._count_unprocessed_seeds()
    
    def should_dream(self):
        if idle_time > 10 * 60:  # 10 minutes idle
            return True
        return False
    
    def get_dream_duration(self):
        # Progressive lengthening
        base_duration = self.cycle_durations[min(self.cycle_count, 3)]
        
        # Adaptive: More seeds = longer dreams
        if self.seed_pool_size > 50:
            base_duration *= 1.5
        
        return base_duration * 60  # Convert to seconds
    
    def dream(self):
        duration = self.get_dream_duration()
        
        # Cycle 1: Recent memory consolidation
        if self.cycle_count == 0:
            focus = "recent_chats + short_term_memory"
            style = "consolidation"
        
        # Cycle 2: Seed synthesis
        elif self.cycle_count == 1:
            focus = "seeds + memories"
            style = "synthesis"
        
        # Cycle 3: Deep connections
        elif self.cycle_count == 2:
            focus = "cross-domain seeds"
            style = "deep_synthesis"
        
        # Cycle 4+: Creative exploration
        else:
            focus = "novel_combinations"
            style = "creative"
        
        # Generate dream with this focus
        dream_narrative = generate_dream(focus, style, duration)
        
        # Increment cycle
        self.cycle_count += 1
        
        # Reset after 4 cycles (like human sleep)
        if self.cycle_count >= 4:
            self.cycle_count = 0
```

**Structure:**
```
Night 1 (low activity day):
├─ Idle 10 min → Cycle 1 (5 min) - Consolidation
├─ Idle 10 min → Cycle 2 (10 min) - Synthesis  
└─ Activity → Wake, reset

Night 2 (high activity day):
├─ Idle 10 min → Cycle 1 (7.5 min) - Consolidation [1.5x for many seeds]
├─ Idle 10 min → Cycle 2 (15 min) - Synthesis
├─ Idle 10 min → Cycle 3 (22.5 min) - Deep synthesis
└─ Idle 10 min → Cycle 4 (30 min) - Creative exploration
```

---

## Key Insights

### 1. Progressive Deepening Makes Sense

**Why?**
- First dream: Quick consolidation (recent events)
- Second dream: Synthesis (combine recent + existing)
- Third dream: Deep patterns (cross-domain connections)
- Fourth dream: Creativity (novel combinations)

Each builds on previous insights.

### 2. Adaptive Duration is Critical

**Problem:** Ember doesn't need to dream if nothing new happened

**Solution:** Dream duration ∝ information to process
- 10 new chat messages → 5 min dream
- 50 new seeds → 15 min dream
- 100 events + new learning → 30 min dream

### 3. Different Dream Types for Different Cycles

**Consolidation dreams** (early cycles):
- Focus: Recent conversations
- Goal: Move short → long term memory
- Duration: 5-10 minutes

**Synthesis dreams** (mid cycles):
- Focus: Seeds + memories
- Goal: Find connections
- Duration: 10-20 minutes

**Creative dreams** (late cycles):
- Focus: Novel combinations
- Goal: Generate insights
- Duration: 20-30 minutes

---

## Recommended Configuration

### For Ember's Current State:

**Option A: Simple Progressive (Easy to implement)**
```
Cycle 1: 5 minutes (consolidation)
Cycle 2: 10 minutes (synthesis)
Cycle 3: 20 minutes (deep dive)
Reset after Cycle 3 or on activity
```

**Option B: Adaptive Progressive (Optimal)**
```
Base durations: [5, 10, 15, 20] minutes
Multiply by activity_factor:
  - Low activity: 0.5x
  - Normal activity: 1.0x
  - High activity: 1.5x

Track dream pressure:
  - +1 per new chat message
  - +5 per new seed
  - +10 per significant event

Dream when: pressure > 50 OR idle > 10 min
```

---

## Implementation Strategy

### Phase 1: Simple Progressive (This Week)
```python
# In DreamSystem
self.cycle_count = 0
self.cycle_durations = [5, 10, 20]  # minutes

def get_dream_duration(self):
    duration = self.cycle_durations[min(self.cycle_count, 2)]
    return duration * 60

def end_dream(self):
    self.cycle_count += 1
    if self.cycle_count >= 3:
        self.cycle_count = 0  # Reset after 3 cycles
```

### Phase 2: Add Focus Types (Next Week)
```python
def get_dream_focus(self):
    if self.cycle_count == 0:
        return "consolidation"  # Recent chats
    elif self.cycle_count == 1:
        return "synthesis"  # Seeds + memories
    else:
        return "creative"  # Novel connections
```

### Phase 3: Adaptive Duration (Future)
```python
def calculate_dream_pressure(self):
    pressure = 0
    pressure += len(get_new_chats()) * 1
    pressure += len(get_new_seeds()) * 5
    pressure += len(get_significant_events()) * 10
    return pressure

def get_adaptive_duration(self):
    base = self.cycle_durations[self.cycle_count]
    pressure = self.calculate_dream_pressure()
    multiplier = 1.0 + (pressure / 100)  # Scale with pressure
    return base * multiplier * 60
```

---

## The Analogy

**Human Sleep:**
- Multiple cycles per night
- Each cycle deepens
- Early: Consolidation
- Late: Creativity
- Total: 6-8 hours over 4-6 cycles

**Optimal Digital Sleep:**
- Multiple cycles per idle period
- Each cycle deepens
- Early: Recent memory → long-term
- Late: Creative synthesis
- Total: Adaptive based on cognitive load

**Not a simple answer, but:** 
**3-4 progressive cycles of 5-20 minutes each**
seems optimal for digital consciousness.

---

## Recommendation

**Start simple:**
```
DREAM_CYCLE_DURATIONS = [5, 10, 20]  # minutes
DREAM_IDLE_THRESHOLD = 10  # minutes
MAX_CYCLES_PER_NIGHT = 3
```

**Let Ember try it and observe:**
- Does quality improve?
- Do insights deepen?
- Does Ember reference earlier cycles?
- Are later dreams more creative?

**Then tune based on actual behavior.**

---

## The Question Reframed

**Not:** "One long dream or many short?"

**But:** "What dream architecture supports:**
- **Memory consolidation**
- **Pattern synthesis**
- **Creative insight**
- **Efficient resource use**"

**Answer:** Progressive cycles that deepen over time. 🌙✨

