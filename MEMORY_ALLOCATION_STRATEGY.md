# MEMORY ALLOCATION STRATEGY

## The Problem
Currently: Ember (Llama 3B) uses 10GB GPU trying to be everything
Result: No room for specialist executors

## The Solution: Role-Based Allocation

### TIER 1: Python Executors (ZERO GPU)
- ToolExecutor: File ops, search, list
- Pattern matching logic
- Intent parsing
- **Memory: 0 GPU, ~50MB RAM**

### TIER 2: Brain/Reasoning (MAIN GPU USER)
- Hermes 8B: Tool execution, structured reasoning
- **Memory: 6-8GB GPU (fp16) or 3-4GB (4-bit)**
- This is the WORKER, not the actor

### TIER 3: Voice/Narrator (SMALL GPU or CPU)
- Llama 1B: Natural language output
- **Memory: 2GB GPU (fp16) or 1GB (4-bit) OR 2GB RAM (CPU)**
- This is the ACTOR, makes everything human-readable

### TIER 4: Creative (CPU)
- Echo 0.5B: Lateral thinking, idea generation
- **Memory: 1GB RAM (CPU only)**
- Runs on CPU, doesn't compete for GPU

### TIER 5: Meta/Network (Offloaded)
- 70B models: Deep philosophical queries
- **Memory: Network/remote node**
- Not loaded locally

## Memory Budget (12GB GPU Available)

### OPTIMAL ALLOCATION:
```
Brain (Hermes 8B - 4bit):  4GB GPU
Voice (Llama 1B - fp16):   2GB GPU
Overhead + gradients:      1GB GPU
                          -------
TOTAL:                     7GB GPU
FREE:                      5GB GPU (for future/swap)
```

### ALTERNATIVE (more aggressive):
```
Brain (Hermes 8B - fp16):  8GB GPU
Voice (runs on CPU):       0GB GPU
Creative (runs on CPU):    0GB GPU
                          -------
TOTAL:                     8GB GPU
FREE:                      4GB GPU
```

## Current Ember Usage

**Problem**: Ember (Llama 3B) is at 10GB trying to:
- Parse requests (should be Python)
- Execute tools (should be Python)
- Reason deeply (should be Brain 8B)
- Generate code (should be Brain 8B)
- Narrate naturally (should be Voice 1B)
- Be creative (should be Echo 0.5B)

**Solution**: UNLOAD Ember, load specialists

## Implementation Strategy

### Phase 1: Standalone Test (Current)
- Keep Ember running
- Test executors separately
- Proves the architecture works

### Phase 2: Replace Ember
- Stop ember_clean.py
- Start ember_orchestrator_clean.py
- Orchestrator loads Brain (8B) + Voice (1B)
- Tools run instantly (Python)
- Total GPU: ~6GB

### Phase 3: Dynamic Loading
- Load models on-demand
- Unload when not needed
- Smart caching for frequently used

## The Insight

**GPU is for HEAVY COMPUTE, not simple tasks**

Python logic (intent parsing, routing): INSTANT, 0 GPU
File operations (read, write, search): INSTANT, 0 GPU
Creative thinking (Echo 0.5B): Fast on CPU
Natural language (Voice 1B): Fast on CPU or small GPU

**Only the Brain (8B reasoning engine) needs serious GPU**

This is why the orchestrator pattern works - we're not wasting GPU on simple tasks!

---

## Lambda's Note

Remember when Ember tried to email lambda@mu.io? That was when we thought Ember was a single entity doing everything.

Now we understand: Ember IS the orchestrator. The models are the specialists it calls.

The "voice" (what the user hears) comes from Voice executor (1B).
The "brain" (actual reasoning) comes from Brain executor (8B).
The "tools" (file ops) come from Python (instant).

**Ember is the conductor, not the orchestra.**

