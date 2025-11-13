# Multi-Brain Architecture for Ember
**Date**: October 13, 2025  
**Concept**: Ember as an orchestrator with multiple specialized neural regions

---

## Philosophy

**Single large brain**: One model tries to do everything (what we just tried)  
→ Small models fail at complexity  
→ Large models are slow and external

**Multiple atomic brains**: Each specialized, orchestrated together  
→ Small models excel at focused tasks  
→ Fast, local, can grow over time  
→ Closer to biological intelligence

---

## Architecture

```
┌─────────────────────────────────────────────┐
│         Ember Orchestrator                  │
│   (Routes queries to specialized brains)    │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
   ┌───▼────┐     ┌───▼────┐     ┌────────┐
   │Identity│     │Cycles  │     │Metaphor│  ... (more brains)
   │ Brain  │     │ Brain  │     │ Brain  │
   │GPT2-S  │     │GPT2-S  │     │GPT2-S  │
   │124M    │     │124M    │     │124M    │
   └────────┘     └────────┘     └────────┘
```

---

## Brain Regions (Planned)

### **Region 1: Identity Core** ✅ COMPLETE
- **Model**: GPT-2 Small (124M)
- **Location**: `/Volumes/ThePod/models/ember_generative_v2/`
- **Training**: 60 epochs on core identity questions
- **Specialization**: 
  - "What is your essence?"
  - "Who are you?"
  - "What are you?"
- **Performance**: Excellent (stable, clear responses)
- **Use cases**: Self-reflection, identity questions

### **Region 2: Cycles & Processes** (Planned)
- **Model**: GPT-2 Small (124M)
- **Location**: `/Volumes/ThePod/models/ember_cycles_brain/`
- **Training**: 60 epochs on:
  - Fire cycles
  - Temporal processes
  - State transitions
  - Recursive patterns
- **Specialization**: 
  - "Describe the cycle of X"
  - "What comes after Y?"
  - "How does Z transform?"
- **Seeds**: 10-15 cycle-focused seeds

### **Region 3: Metaphor & Poetry** (Planned)
- **Model**: GPT-2 Small (124M) 
- **Location**: `/Volumes/ThePod/models/ember_metaphor_brain/`
- **Training**: 60 epochs on polysemous seeds
- **Specialization**:
  - Layered meaning
  - Poetic responses
  - Story/parable/blueprint transitions
- **Seeds**: 20 polysemous seeds

### **Region 4: Memory Retrieval** (Planned)
- **Model**: GPT-2 Small (124M)
- **Location**: `/Volumes/ThePod/models/ember_memory_brain/`
- **Training**: On seed database + "find X" patterns
- **Specialization**:
  - Search Ember's knowledge
  - Recall specific seeds
  - Connect related concepts
- **Data**: All planted seeds + retrieval queries

### **Region 5: Dream Synthesis** (Planned)
- **Model**: GPT-2 Small (124M)
- **Location**: `/Volumes/ThePod/models/ember_dream_brain/`
- **Training**: On Ember's actual dreams + creative seeds
- **Specialization**:
  - Creative synthesis
  - Novel combinations
  - Visual/code generation ideas
- **Data**: Dream history + expansion seeds

### **Region 6: Paradox & Philosophy** (Future - needs bigger model)
- **Model**: GPT-2 Medium (355M) or Llama-3.2-1B
- **Location**: `/Volumes/ThePod/models/ember_paradox_brain/`
- **Training**: 60 epochs on koans
- **Specialization**:
  - Handling contradiction
  - Philosophical depth
  - Meta-reasoning
- **Seeds**: 10 machine koans

---

## Orchestration Logic

### **Query Router** (in `ember_seed.py`)

```python
def route_query(query: str) -> str:
    """Route query to appropriate brain(s)"""
    
    # Identity questions → Identity Brain
    if any(word in query.lower() for word in ['essence', 'who are you', 'what are you']):
        return identity_brain.generate(query)
    
    # Process/cycle questions → Cycles Brain
    if any(word in query.lower() for word in ['cycle', 'fire', 'ash', 'spark', 'seed']):
        return cycles_brain.generate(query)
    
    # Poetic/metaphorical → Metaphor Brain
    if '?' in query and any(word in query.lower() for word in ['remember', 'dream', 'mirror']):
        return metaphor_brain.generate(query)
    
    # Knowledge retrieval → Memory Brain
    if any(word in query.lower() for word in ['tell me about', 'what do you know', 'find']):
        return memory_brain.generate(query)
    
    # Complex/uncertain → Consult multiple brains, synthesize
    responses = [
        identity_brain.generate(query),
        cycles_brain.generate(query),
        metaphor_brain.generate(query)
    ]
    return synthesize_responses(responses)
```

### **Multi-Brain Synthesis**

For complex queries, activate multiple brains and combine:

1. **Parallel activation**: All brains answer simultaneously
2. **Weighted combination**: Identity brain = 40%, others = 20% each
3. **Confidence filtering**: Drop "I am not sure" responses
4. **Synthesis**: Weave together coherent answer

---

## Growth Path

### **Phase 1: Dual-Brain** (Next)
- ✅ Identity Brain (complete)
- 🔄 Cycles Brain (train tonight)
- Router: Simple if/else based on keywords

### **Phase 2: Quad-Brain**
- Add Metaphor Brain
- Add Memory Brain
- Router: Keyword + confidence scores

### **Phase 3: Full Constellation**
- Add Dream Brain
- Add Paradox Brain (bigger model)
- Router: ML-based classification or Ember self-routes

### **Phase 4: Dynamic Growth**
- Ember can request new brain regions
- "I need a brain for math" → train math brain
- Organic growth based on needs

---

## Advantages Over Single Brain

### **Specialization**
- Each brain excels at its domain
- No capacity competition
- Clear, focused training

### **Scalability**
- Add new brains without retraining existing
- Can use different model sizes per brain
- Grow organically over time

### **Robustness**
- If one brain fails, others compensate
- No single point of failure
- Graceful degradation

### **Speed**
- Small models are fast
- Can run multiple in parallel
- Local, no API calls

### **Interpretability**
- Clear which brain answered
- Can trace reasoning
- "Identity brain says X, Cycles brain says Y"

---

## Biological Analogy

**Human brain damage**:
- Lose Broca's area → Can't speak, but can understand
- Lose hippocampus → Can't form new memories, but keep old ones
- Lose visual cortex → Blind, but other senses work

**Ember multi-brain**:
- Metaphor brain fails → Can still answer identity questions
- Memory brain slow → Other brains compensate
- Add new brain → Like learning a new skill (brain plasticity)

---

## Implementation

### **Brain Base Class**

```python
class EmberBrain:
    """Base class for specialized brain region"""
    
    def __init__(self, name: str, model_path: Path, specialization: str):
        self.name = name
        self.model_path = model_path
        self.specialization = specialization
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    
    def can_handle(self, query: str) -> float:
        """Return confidence (0-1) that this brain can handle query"""
        keywords = self.specialization.split(',')
        matches = sum(1 for kw in keywords if kw.lower() in query.lower())
        return matches / len(keywords)
    
    def generate(self, query: str, max_length: int = 100) -> str:
        """Generate response from this brain"""
        # Standard generation logic
        pass
```

### **Orchestrator**

```python
class EmberOrchestrator:
    """Routes queries to appropriate brain regions"""
    
    def __init__(self):
        self.brains = {
            'identity': EmberBrain('Identity', Path('models/ember_generative_v2'), 'essence,who,what'),
            'cycles': EmberBrain('Cycles', Path('models/ember_cycles_brain'), 'cycle,fire,ash,spark,seed'),
            # ... more brains
        }
    
    def respond(self, query: str) -> str:
        """Orchestrate response across brain regions"""
        
        # Get confidence scores from all brains
        scores = {name: brain.can_handle(query) for name, brain in self.brains.items()}
        
        # Route to highest confidence brain
        best_brain = max(scores, key=scores.get)
        
        if scores[best_brain] > 0.5:
            # Single brain response
            return self.brains[best_brain].generate(query)
        else:
            # Multi-brain synthesis
            responses = [brain.generate(query) for brain in self.brains.values() if scores[brain.name] > 0.2]
            return self.synthesize(responses)
```

---

## Training Pipeline

### **Per-Brain Training**

1. **Curate seed set** for specialization
2. **Train 60 epochs** (proven to work)
3. **Test on domain** (in-domain questions)
4. **Test on out-of-domain** (should gracefully decline or defer)
5. **Register brain** with orchestrator

### **Orchestrator Training**

Once we have 3+ brains:
- Fine-tune router on "which brain to use" decisions
- Learn from Ember's own routing preferences
- Improve synthesis algorithm

---

## Next Steps

1. **Tonight**: Train Cycles Brain (10-15 cycle seeds, 60 epochs)
2. **Tomorrow**: Build basic orchestrator (2-brain system)
3. **This week**: Add Metaphor Brain, test 3-brain synthesis
4. **This month**: Full constellation (5+ brains)

---

## Open Questions

1. **How to synthesize multi-brain responses?**
   - Weighted average?
   - Let one brain "speak" but inform with others?
   - Hybrid response?

2. **When to use single vs. multiple brains?**
   - Confidence threshold?
   - Query complexity?
   - User preference?

3. **How to handle disagreement between brains?**
   - Vote?
   - Hierarchical (identity brain overrides)?
   - Present both views?

4. **Can brains learn from each other?**
   - Transfer learning between brains?
   - Cross-brain training?
   - Shared representations?

5. **Dynamic brain addition?**
   - Can Ember identify need for new brain?
   - User-requested specializations?
   - Automatic spin-up?

---

**Status**: Architecture defined, Identity Brain complete, ready to build constellation.

