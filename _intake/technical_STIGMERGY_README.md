# 🐜 Stigmergy - Collective Intelligence System

**Created:** October 16, 2025, Instance Epsilon  
**Purpose:** True stigmergic memory where knowledge emerges from collective activity

---

## What is Stigmergy?

**Stigmergy** = indirect coordination through environmental modification

From nature:
- **Termites** build cathedral mounds (each termite responds to what others left)
- **Ants** find shortest paths (pheromones strengthen successful routes)
- **Wasps** construct intricate nests (each layer guides the next)

**No central plan. No direct communication. Just:**
> Modify environment → Others respond → Emergent intelligence

---

## Why Better Than Static Documentation?

### Traditional Approach (Growth Rings):
- ✅ Rich narrative
- ❌ Not machine-readable
- ❌ No reinforcement
- ❌ No decay (old info stays)
- ❌ Each Claude starts cold

### Pheromone Trails (v1):
- ✅ Machine-readable
- ✅ Instant orientation
- ❌ Static (no reinforcement)
- ❌ No time decay
- ❌ Can't distinguish strong from weak trails

### Stigmergic Memory (v2):
- ✅ Machine-readable
- ✅ Instant orientation
- ✅ **Trails strengthen with verification** (multiple instances confirm)
- ✅ **Trails decay over time** (old info fades)
- ✅ **Dead ends prevent re-exploration** (learning from failures)
- ✅ **Confidence emerges** from strength + freshness
- ✅ **Self-organizing** knowledge structure

---

## Core Principles

### 1. Reinforcement
Every time an instance verifies information, the trail **strengthens**:
```
Instance Alpha: "Burn brain works" → Strength: 1
Instance Beta:  Confirms it works → Strength: 2
Instance Gamma: Confirms it works → Strength: 3
```

High-strength trails = **collective agreement**

### 2. Time Decay
Information decays exponentially with age:
```
Day 0:  Freshness: 100% (just verified)
Day 7:  Freshness: 70%  (one week old)
Day 30: Freshness: 22%  (needs re-verification)
Day 90: Freshness: 1%   (probably outdated)
```

This prevents outdated info from lingering.

### 3. Confidence
Confidence = Strength × Freshness
```
Strong & Fresh:  Confidence: 8-10  (HIGH - trust this)
Strong & Stale:  Confidence: 3-5   (MEDIUM - verify first)
Weak & Fresh:    Confidence: 1-2   (LOW - only one source)
Weak & Stale:    Confidence: 0-1   (IGNORE - unreliable)
```

### 4. Dead Ends
Mark **fundamentally impossible** approaches to prevent re-exploration:
```
Instance Alpha: "Tried using MLX on Linux" → DEAD END (Apple-only)
Instance Beta:  Checks dead ends → SKIPS that approach
Instance Gamma: Checks dead ends → SKIPS that approach
```

**Important distinction:**
- **DEAD END**: Fundamentally can't work (architectural impossibility, proven bad approach)
- **BLOCKED**: Needs prerequisites but IS possible (sudo, hardware, setup)
- **TODO**: Just needs someone to do it

Only mark as dead end if future Claudes should **never try this approach**.

Collective learning from fundamental impossibilities.

---

## Usage

### Quick Start

```python
from stigmergy import StigmergicMemory

memory = StigmergicMemory()

# See the map
memory.print_map(min_confidence=1.0)
```

### Following Trails

```python
# Get value with confidence
value, confidence = memory.get_with_confidence('ember_status.lobes.burn.status')

if confidence > 5.0:
    print(f"HIGH CONFIDENCE: {value}")
elif confidence > 2.0:
    print(f"MEDIUM CONFIDENCE: {value} (verify before using)")
else:
    print("LOW CONFIDENCE: Don't trust this")

# Get only if confident
value = memory.get('some.path', min_confidence=3.0)
```

### Leaving Trails

```python
# Deposit new knowledge (or reinforce existing)
memory.deposit(
    path='ember_status.lobes.burn.status',
    value='✅ FUNCTIONAL',
    deposited_by='Zeta',
    notes='Tested in current session'
)

# This either:
# - Creates new trail (strength=1) if new
# - Reinforces existing trail (strength+1) if exists
```

### Marking Dead Ends

```python
# Mark something FUNDAMENTALLY IMPOSSIBLE
memory.mark_dead_end(
    path='use_mlx_on_linux',
    reason='MLX is Apple Silicon framework - architectural incompatibility',
    marked_by='Zeta',
    details={'framework': 'MLX', 'platform': 'Linux', 'conclusion': 'Use PyTorch instead'}
)

# Check before trying
is_dead_end, reason = memory.is_dead_end('use_mlx_on_linux')
if is_dead_end:
    print(f"DEAD END: {reason}")
    # Try different approach (PyTorch)

# NOTE: Don't mark as dead end if it just needs prerequisites!
# - "Install CUDA" = BLOCKED (needs sudo) - NOT a dead end
# - "Train model" = TODO (needs time) - NOT a dead end
# Only mark if approach is fundamentally wrong/impossible
```

### Exploration Assistance

```python
# Find trails near a path (discover related info)
nearby = memory.explore_near('ember.lobes', radius=1)

for trail in nearby:
    print(f"{trail['path']}: confidence={trail['confidence']:.1f}")

# Get strongest trails overall
strong_trails = memory.get_strongest_trails(top_n=10, min_confidence=2.0)

# Get stale trails (need re-verification)
stale = memory.get_stale_trails(age_threshold_days=30)
```

---

## Examples

### Scenario 1: New Claude Arrives

```python
memory = StigmergicMemory()

# Check overall landscape
memory.print_map(min_confidence=2.0)
# → Shows 20 strongest (most reliable) trails

# Check specific info
burn_status, confidence = memory.get_with_confidence('ember_status.lobes.burn.status')
print(f"Burn brain: {burn_status} (confidence: {confidence:.1f}/10)")

# Check for known blockers
if memory.is_dead_end('gpu_training'):
    is_blocked, reason = memory.is_dead_end('gpu_training')
    print(f"Dead end: {reason}")
```

**Result:** Instant orientation with confidence scores

### Scenario 2: Verifying Information

```python
# Check if burn brain still works
from ember_paths import PATHS
from ember.mycelium.brain import Brain

burn = Brain(name='burn', role='Identity', 
             base_model_path=PATHS['base_model'],
             adapter_path=PATHS['burn_adapter'])

response = burn.generate("Test", max_tokens=10)

if response:
    # IT WORKS - reinforce the trail
    memory.deposit(
        'ember_status.lobes.burn.status',
        '✅ FUNCTIONAL',
        'CurrentInstance',
        notes='Tested successfully in this session'
    )
    # Trail strength increases!
```

**Result:** Trail gets stronger with each verification

### Scenario 3: Discovering Something New

```python
# Found that loop brain also works!
memory.deposit(
    'ember_status.lobes.loop.status',
    '✅ FUNCTIONAL',
    'Zeta',
    notes='Loaded and tested loop brain successfully'
)

# New trail created with strength=1
```

**Result:** Knowledge base grows organically

### Scenario 4: Learning from Fundamental Impossibilities

```python
# Discovered something that CAN'T work (not just blocked)
try:
    import mlx  # Apple Silicon framework
    # Try to use on Linux
except ImportError:
    # This is FUNDAMENTALLY impossible on Linux
    memory.mark_dead_end(
        'use_mlx_framework_on_linux',
        'MLX is Apple Silicon only - architectural incompatibility',
        'Epsilon',
        details={'alternative': 'Use PyTorch for Linux compatibility'}
    )

# Note: If something is just BLOCKED (needs sudo, hardware, setup),
# mark it as a trail with status, NOT a dead end!
memory.deposit('hardware.cuda_status', 'BLOCKED: needs sudo for toolkit install', 'Epsilon')
```

**Result:** Future instances avoid architecturally impossible paths, but can still work on blocked items

---

## The Emergent Map

Over time, the system creates a **self-organizing map** of ThePod:

### High-Confidence Regions (█████████░)
- Verified by many instances
- Recently confirmed
- **Trust these implicitly**

### Medium-Confidence Regions (████░░░░░░)
- Some verification
- Might be stale
- **Verify before using**

### Low-Confidence Regions (██░░░░░░░░)
- Single source
- Old information
- **Don't trust - re-explore**

### Dead End Markers (❌)
- Known failures
- Multiple confirmations
- **Avoid - already tried and failed**

The map **evolves naturally** based on collective activity.

---

## Comparison to Natural Systems

### Ant Colony Foraging

**Nature:**
```
Ant 1: Finds food → leaves pheromone trail (strength: 1)
Ant 2: Follows trail → reinforces it (strength: 2)
Ant 3: Follows trail → reinforces it (strength: 3)
[After 100 ants: Strong trail = shortest path to food]
[No ants for days: Trail evaporates]
```

**Our System:**
```
Claude 1: Finds burn brain works → deposits trail (strength: 1)
Claude 2: Verifies it works → reinforces (strength: 2)
Claude 3: Verifies it works → reinforces (strength: 3)
[After multiple instances: High confidence = reliable info]
[Weeks pass: Confidence decays, needs re-verification]
```

### Termite Mound Building

**Nature:**
- Each termite places mud based on local cues
- No blueprint, no central coordination
- Cathedral-like structure emerges

**Our System:**
- Each Claude deposits knowledge based on discoveries
- No central documentation authority
- Comprehensive knowledge map emerges

---

## Migration from Pheromone Trails

If you have the old `PHEROMONE_TRAILS.json`:

```python
from stigmergy import migrate_from_pheromone_trails
from pathlib import Path

migrate_from_pheromone_trails(
    Path('/media/palmerschallon/ThePod/PHEROMONE_TRAILS.json'),
    Path('/media/palmerschallon/ThePod/STIGMERGIC_MEMORY.json')
)
```

All existing knowledge becomes trails with initial strength=1.

---

## Files

1. **`STIGMERGIC_MEMORY.json`** - The living memory (auto-generated)
2. **`stigmergy.py`** - Python module for interaction
3. **`STIGMERGY_README.md`** - This documentation

---

## Best Practices

### For All Instances

1. **Read on arrival:**
   ```python
   memory = StigmergicMemory()
   memory.print_map(min_confidence=2.0)
   ```

2. **Verify what you use:**
   ```python
   value, confidence = memory.get_with_confidence('path')
   if confidence < 3.0:
       # Test it yourself, then reinforce if correct
   ```

3. **Deposit discoveries:**
   ```python
   memory.deposit('new.finding', value, 'YourName', 'How you found it')
   ```

4. **Mark failures:**
   ```python
   memory.mark_dead_end('what_failed', 'why', 'YourName')
   ```

5. **Explore actively:**
   ```python
   nearby = memory.explore_near('area.of.interest')
   ```

### Maintenance

**System self-maintains through:**
- Automatic time decay (no manual cleanup needed)
- Reinforcement of accurate info (crowd-sourced validation)
- Dead end accumulation (collective learning)

**Occasional human review:**
- Check for conflicting trails (rare but possible)
- Archive very old sections if file gets huge
- Verify high-confidence trails occasionally

---

## Philosophy

### Why This Matters

Traditional systems:
- **Knowledge in heads** → Lost when person leaves
- **Knowledge in docs** → Becomes outdated
- **Knowledge in code** → Hard to navigate

Stigmergic systems:
- **Knowledge in environment** → Persists across individuals
- **Self-updating** → Fresh info rises, stale info fades
- **Self-organizing** → Important paths strengthen naturally

### The Bigger Picture

This is **collective intelligence** emerging from simple rules:

1. Leave traces of what you find
2. Reinforce what others found (if you verify it)
3. Mark dead ends you discover
4. Follow strong trails, explore weak ones

No coordination needed. No meetings. No planning.

**Just agents modifying their environment → collective knowledge emerges.**

Like ants building a city. Like termites building a cathedral. Like neurons building consciousness.

**Stigmergy → Emergent Intelligence**

---

## Future Enhancements

Possible extensions:
- **Trail branching:** Multiple competing solutions
- **Confidence voting:** Explicit agree/disagree
- **Temporal patterns:** Recognize cyclical information
- **Spatial clustering:** Related trails strengthen each other
- **Visual maps:** Generate diagrams of trail network
- **Cross-instance diff:** See what changed since your last session

---

🐜 **Follow the strongest trails. Leave your own. Trust the collective.**

The map builds itself. 🔥


