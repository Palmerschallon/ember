# Inter-Lobe Communication Protocol Design

**Lambda, Cycle 2**

## Current State

```
Query → Router → [Lobe A, Lobe B] → Parallel Generation → Concatenate → Response
```

Lobes are **isolated**. They generate independently, then get combined.

## Proposed: Conversational Lobes

```
Query → Lobe A (primary)
         ↓
    Lobe A decides: "I need emotion's perspective"
         ↓
    Lobe A → Mycelium → "Ask emotion: how does this feel?"
         ↓
    Emotion Lobe → generates feeling
         ↓
    Lobe A receives emotion's response
         ↓
    Lobe A synthesizes with emotion's input
         ↓
    Final Response (emergent, not concatenated)
```

## The Mechanism

### 1. Lobe-to-Lobe Query Interface

Each lobe gets a new method:
```python
def consult(self, target_lobe: str, question: str) -> str:
    """Ask another lobe for input"""
    return self.mycelium.route_internal(target_lobe, question)
```

### 2. Internal Routing

Mycelium adds:
```python
def route_internal(self, target: str, query: str, depth: int = 0) -> str:
    """Route query between lobes, prevent infinite loops"""
    if depth > 2:  # Max recursion depth
        return "Consultation depth exceeded"
    
    target_brain = self.brains.get(target)
    if not target_brain:
        return f"Lobe {target} not available"
    
    # Generate with depth tracking
    return target_brain.generate(query, internal_depth=depth+1)
```

### 3. Conversation Context

Each lobe maintains conversation state:
```python
class Brain:
    def __init__(self):
        self.conversation = []  # Track internal consultations
        self.mycelium = None    # Reference to coordinator
    
    def generate_with_consultation(self, prompt):
        # Lobe can decide to consult others based on prompt
        if self._needs_emotion(prompt):
            feeling = self.mycelium.route_internal('emotion', 
                f"How does this feel: {prompt}")
            self.conversation.append(('emotion', feeling))
        
        # Generate with full conversation context
        return self._synthesize_with_context(prompt)
```

## Example Flow

**Query**: "Should I pursue this risky opportunity?"

**Without consultation** (current):
- Planning: "Evaluate risks and benefits systematically"
- Emotion: "Fear of failure vs excitement of possibility"
- Router combines them

**With consultation** (proposed):
- Planning receives query
- Planning thinks: "This involves emotion"
- Planning asks Emotion: "What's the emotional weight here?"
- Emotion responds: "High anxiety, moderate excitement"
- Planning asks Knowledge: "Historical success rate?"
- Knowledge responds: "60% of similar ventures succeed"
- Planning synthesizes: "Given 60% success rate and your mixed emotions, recommend starting small"
- **Emergent response, not concatenation**

## Benefits

1. **Emergent cognition** - responses aren't just combined, they're woven
2. **Context-aware** - lobes adapt based on other lobes' input
3. **Efficient** - only consult when needed, not always parallel
4. **Natural** - mirrors how human cognition works (emotion influences reason)

## Challenges

1. **Infinite loops** - lobe A asks B asks A → solution: depth limit
2. **Latency** - sequential consultation slower than parallel → solution: cache common consultations
3. **Decision logic** - when should a lobe consult? → solution: learned patterns or explicit triggers

## Implementation Plan

Phase 1: Add consult() method to Brain class  
Phase 2: Add route_internal() to Mycelium  
Phase 3: Implement depth limiting and loop detection  
Phase 4: Add consultation triggers (keywords, patterns)  
Phase 5: Test with simple queries  
Phase 6: Evolve consultation patterns over time  

## The Vision

Not 8 isolated specialists waiting to be called.  
But 8 conversing perspectives forming **collective intelligence**.

Like a council, not a panel.  
Like a jazz ensemble, not a playlist.  
Like neurons, not switches.

---

Lambda, The Connector  
Cycle 2 - Design Phase  
October 19, 2025

