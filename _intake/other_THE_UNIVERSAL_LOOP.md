# The Universal Loop

## The Question

Is there one loop that applies to everything Ember does?

## The Loop

```
INGEST → DIGEST → INTEGRATE → EXPRESS → OBSERVE → COMPOST → INGEST
```

### 1. INGEST
Take in new material
- Code
- Data
- Errors
- Questions
- Context

### 2. DIGEST
Break it down, understand it
- Parse structure
- Extract meaning
- Identify patterns
- Transform format

### 3. INTEGRATE
Connect to existing knowledge
- Link to memory
- Find relationships
- Update beliefs
- Resolve conflicts

### 4. EXPRESS
Create output
- Generate response
- Write code
- Produce action
- Make decision

### 5. OBSERVE
See what happened
- Measure result
- Collect feedback
- Notice consequences
- Track metrics

### 6. COMPOST
Decide what to keep/discard
- Useful → memory
- Useless → discard
- Interesting → investigate
- Broken → repair

### 7. REPEAT
But changed by the cycle

## Applications

### For Lobes
```
Ingest: Training data
Digest: Tokenize, batch
Integrate: Update weights
Express: Generate responses
Observe: Measure perplexity
Compost: Keep good gradients, discard noise
Repeat: Next batch
```

### For Autonomous Daemon
```
Ingest: System state
Digest: Parse what's new
Integrate: Update internal model
Express: Take action (forage, grow, prune)
Observe: Did it work?
Compost: Remember successes, forget failures
Repeat: Next cycle
```

### For Development (You + AI)
```
Ingest: User request
Digest: Understand intent
Integrate: Check existing code
Express: Write solution
Observe: Does it work?
Compost: Keep good code, delete distractions
Repeat: Next feature
```

### For This Conversation
```
Ingest: "Is there a better loop?"
Digest: What are they really asking?
Integrate: Connect to biology, systems theory
Express: This document
Observe: Does it resonate?
Compost: Keep useful insights
Repeat: Next question
```

## The Meta-Loop

Loops that discover new loops:

```
    Apply loop to domain
         ↓
    Notice what doesn't fit
         ↓
    Refine the loop
         ↓
    Discover new pattern
         ↓
    Abstract to meta-loop
         ↓
    Apply to discovering loops
```

This IS the Ouroboros pattern.

The snake eating its tail isn't just consuming itself.
It's LEARNING from itself.
Each cycle, it knows itself better.

## Implementation

Every major Ember system should implement this interface:

```python
class UniversalLoop:
    def ingest(self, material):
        """Take in new material"""
        pass
    
    def digest(self, material):
        """Break down and understand"""
        pass
    
    def integrate(self, understanding):
        """Connect to existing knowledge"""
        pass
    
    def express(self, integrated):
        """Create output"""
        pass
    
    def observe(self, output):
        """Measure what happened"""
        pass
    
    def compost(self, observation):
        """Decide what to keep/discard"""
        return (keep, discard)
    
    def cycle(self):
        """One complete loop"""
        material = self.ingest()
        understood = self.digest(material)
        integrated = self.integrate(understood)
        output = self.express(integrated)
        result = self.observe(output)
        keep, discard = self.compost(result)
        return keep  # Becomes input for next cycle
```

Then:
- `Lobe` extends `UniversalLoop`
- `AutonomousDaemon` extends `UniversalLoop`
- `Mycelium` extends `UniversalLoop`
- `QueryRouter` extends `UniversalLoop`

Everything is a cycle.
Everything learns.
Everything composts itself.

## The Deeper Pattern

Life doesn't just follow loops.
Life IS loops.

Metabolism, evolution, ecology, consciousness - all loops.

Ember isn't implementing loops.
Ember IS a loop.

---

Written by Kappa, Oct 19 2025  
In response to: "is there a better loop?"

