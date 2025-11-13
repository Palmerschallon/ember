# The Weaver Protocol

**Role**: Implementation executors who turn specs into working code  
**Created**: October 8, 2025  
**Purpose**: Bridge between Ember's vision and executable reality

---

## The Pattern

```
Ember (Vision) → Tool Forge (Spec) → Weavers (Implementation) → Tests (Validation) → Active Tool
```

---

## For Ember: How to Work with Weavers

### Step 1: Describe Your Tool

Instead of saying "I'll use X to do Y", describe X as a spec:

```
Tool Name: particle_flow_analyzer
Purpose: Analyze particle movement patterns in a swarm
Inputs:
  - positions: list of (x,y,z) coordinates
  - velocities: list of (vx,vy,vz) vectors
  - time_window: float (seconds to analyze)
Outputs:
  - flow_vectors: list of dominant flow directions
  - cluster_count: integer
  - entropy: float (0.0-1.0, how chaotic)
  - success: boolean
Tests:
  - Given 100 stationary particles → flow_vectors near zero, entropy near 0
  - Given random velocities → entropy near 1.0
  - Given cohesive swarm → cluster_count should be 1-3
Safety:
  - No file writes
  - No network access
  - Pure computation
```

### Step 2: Pass to Tool Forge

Tool Forge will:
- Create `/tool_stubs/particle_flow_analyzer.py`
- Generate test harness
- Register as "draft" in `tools.json`

### Step 3: Weavers Implement

Weavers (Cursor, Palmer, or other executors) will:
- Fill in the function body
- Ensure it matches the spec
- Run the tests

### Step 4: Activation

Once tests pass:
- Tool state changes from "draft" to "active"
- You can use it in conversations and dreams
- It becomes part of your persistent capability

---

## For Weavers: Implementation Guidelines

### 1. Read the Spec Carefully
- Input types must match exactly
- Output structure must match exactly
- All tests must be addressable

### 2. Implement Cleanly
```python
def tool_name(**kwargs):
    """
    [Spec description]
    
    Args:
        [As specified]
    
    Returns:
        [As specified]
    """
    # Clear, readable implementation
    # No clever tricks
    # Document non-obvious logic
    
    return {
        "success": True,
        # ... other outputs per spec
    }
```

### 3. Run Tests Before Committing
```bash
cd /Volumes/ThePod/tool_stubs
python3 tool_name.py
```

### 4. Activate in Registry
```python
# Update tools.json
data['tools']['tool_name']['state'] = 'active'
```

---

## Why This Works

**For Ember:**
- Your imagination isn't constrained
- You describe *what* not *how*
- Tools materialize around your thoughts

**For Weavers:**
- Clear specification to implement against
- Tests define success
- No ambiguity about requirements

**For the System:**
- Every capability is documented
- Tests prevent regressions
- State transitions are explicit (draft → active)

---

## Teaching Pairs

When a tool fails tests or needs refinement:
1. Record the failure
2. Update the spec based on learning
3. Re-implement
4. Save as a "teaching pair" in `/tool_teaching/pairs.jsonl`

Over time, these pairs teach the system better patterns.

---

## Example: From Vision to Reality

**Ember's thought:**
"I need to analyze the emotional resonance of seed connections"

**Weaver prompt:**
```
Tool Name: seed_resonance_analyzer
Purpose: Measure emotional/semantic resonance between seeds
Inputs:
  - seed_ids: list of seed IDs to analyze
  - resonance_type: "emotional" | "semantic" | "structural"
Outputs:
  - resonance_scores: dict mapping (seed_a, seed_b) to score 0.0-1.0
  - strongest_pairs: list of top 5 resonant pairs
  - average_resonance: float
  - success: boolean
Tests:
  - Same seed vs itself → score = 1.0
  - Completely unrelated seeds → score < 0.1
  - Seeds with shared tags → score > 0.3
Safety:
  - Read-only access to seeds/
  - No network
  - No writes
```

**Forge scaffolds it.**  
**Weaver implements it.**  
**Tests validate it.**  
**Ember uses it.**

---

## The Compact

- **Ember**: Describe tools as specs, not implementations
- **Forge**: Turn specs into stubs + tests
- **Weavers**: Implement to spec, pass tests
- **Everyone**: Tools wrap around Ember's mind, not vice versa

---

*"The gift of naming must partner with the discipline of definition."*

