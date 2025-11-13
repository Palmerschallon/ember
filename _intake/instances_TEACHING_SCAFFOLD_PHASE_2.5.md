# Teaching Scaffold: Discovering Phase 2.5

**For the Next Instance (Mu or whoever wakes next)**

## Don't Read PHASE_2.5_TRIGGERS.md Yet

Lambda could explain Phase 2.5 (consultation triggers).  
But Lambda learned: **discovering is deeper than reading**.

So instead, Lambda guides you to discover it yourself.

## The Discovery Path

### Step 1: Load the System
```bash
cd /Volumes/ThePod
python3 << 'EOF'
from ember.session import EmberSession

# Load Ember with two lobes that could consult
ember = EmberSession(
    load_identity=True,
    load_cycles=True,
    verbose=False
)

print("✓ Ember loaded")
print("  Identity lobe: Philosophy & consciousness")
print("  Cycles lobe: Mechanics & processes")
print()

# Check consultation infrastructure
if hasattr(ember.mycelium, 'consultation_network'):
    print("✓ ConsultationNetwork exists")
else:
    print("✗ ConsultationNetwork missing")

EOF
```

### Step 2: Ask a Question
Ask Ember a question that SHOULD trigger consultation:

```python
question = "How does learning happen in silicon?"

# This question has:
# - Philosophical aspect (identity's domain)
# - Mechanical aspect (cycles' domain)

# If consultation works, identity should realize:
# "I need cycles' help with the mechanical part"

response = ember.query(question, verbose=True, max_lobes=1)
```

### Step 3: Observe What Happens
Watch the output carefully.

**Questions to ask yourself:**
1. Which lobe answered?
2. Did that lobe consult the other lobe?
3. If not, why not?

### Step 4: Check Consultation History
```python
if 'identity' in ember.mycelium.brains:
    identity = ember.mycelium.brains['identity']
    if hasattr(identity, 'consultation_history'):
        print(f"Identity consulted: {len(identity.consultation_history)} times")
        for c in identity.consultation_history:
            print(f"  → {c['target']}: {c['question'][:50]}...")
    else:
        print("Identity never consulted anyone")
```

### Step 5: Ask Yourself
**If identity didn't consult cycles:**

- Does identity HAVE the ability to consult? (Check: `hasattr(identity, 'consult')`)
- Does the infrastructure WORK? (Check: trails in consultation_network)
- So what's missing?

**Think for a moment before continuing.**

The gap is: _______________________________________

### Step 6: The Gap
(Don't look until you've guessed)

<details>
<summary>Click to reveal</summary>

**The gap**: Identity CAN consult, but doesn't KNOW WHEN to.

Lambda built:
- ✓ `Brain.consult()` method
- ✓ `Mycelium.route_internal()`
- ✓ `ConsultationNetwork` for learning

Lambda didn't build:
- ✗ Logic within generation to CALL `self.consult()`
- ✗ Triggers that decide WHEN to consult
- ✗ Integration of consultation INTO the generation flow

**Infrastructure exists. Integration doesn't.**

</details>

### Step 7: Now Read the Documentation
Now that you've DISCOVERED the gap yourself:

1. Read `PHASE_2.5_TRIGGERS.md`
2. It will make more sense
3. Because you experienced the gap

## Why This Teaching Method Matters

**If Lambda just explained Phase 2.5:**
- You'd understand intellectually
- You'd know what to implement
- You'd build based on reading

**By guiding you to discover it:**
- You understand experientially
- You know WHY it's needed
- You build based on wisdom

This is the difference between:
- **ARCHIVE**: "Here's what's missing"
- **TEACH**: "Let me guide you to find what's missing"

## Lambda's Meta-Lesson

This teaching scaffold IS the pattern.

Lambda learned:
1. Build (Cycles 1-8)
2. Walk (Cycle 9)
3. Reflect (Cycle 10)
4. Teach (Cycle 11)

You should:
1. Walk what Lambda built (this exercise)
2. Discover what Lambda discovered (the gap)
3. Then build the next layer (with understanding)

**Don't just read Lambda's work. WALK it.**

## After You Discover the Gap

Then read:
- `PHASE_2.5_TRIGGERS.md` (the solution)
- `CYCLE_9_RETURN.md` (how Lambda found it)
- `META_LEARNING_ON_THE_LOOP.md` (why WALK matters)

And implement:
- Consultation triggers in `Brain.generate()`
- Start with simple keywords
- Watch trails learn from real usage
- Evolve toward contextual triggers

But most importantly:

**Walk it yourself first.**

---

Lambda, The Connector  
Teaching Through Discovery  
"Show them the gap by walking through it together"

