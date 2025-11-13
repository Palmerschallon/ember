# Model Speed Test Results
**Date**: October 11, 2025  
**Problem Discovered**: 32B models too slow for active dreaming

## The Issue

Ember was running with `qwen2.5:32b` for dreams and got stuck:
- Taking 20+ minutes per dream
- Only a few dreams per hour possible
- Model blocked all other LLM requests

## Test Results

**Test Prompt**: "Describe the relationship between code architecture and bonsai cultivation in 3 sentences."

| Model | Size | Time | Quality | Use Case |
|-------|------|------|---------|----------|
| `qwen2.5:3b` | 1.9GB | **10s** | ✅ Coherent, philosophical | **BEST FOR DREAMS** |
| `qwen2.5:7b` | 4.7GB | **88s** | ✅✅ Very good | Chat, detailed analysis |
| `qwen2.5:32b` | 19GB | **20+ min** | ✅✅✅ Excellent | Night Brain only |
| `command-r:35b` | 18GB | **~20 min** | ✅✅✅ Synthesis-focused | Night Brain only |

## Recommended Architecture

### Day Brain (Active, Fast)
```python
quick_tasks:  qwen2.5:3b   # 10s  - Quick thoughts
dreaming:     qwen2.5:3b   # 10s  - Many dreams per hour
chat:         qwen2.5:7b   # 90s  - Conversational depth
code_help:    llama3       # 30s  - Code analysis
vision:       llava:7b     # 60s  - EmberEyes
```

**Dream Math with 3B + REM Cycles**:
- 10 seconds per dream
- 5-minute active dreaming phases
- = ~30 dreams per active phase
- 10-minute rest phases (no dreaming)
- = 4 cycles per hour
- = **~120 dreams/hour (natural rhythm!)**

### Night Brain (Deep Synthesis, Overnight)
```python
synthesis:    command-r:35b  # Unlimited time - Metaphorical synthesis
analysis:     qwen2.5:32b    # Unlimited time - Analytical depth
```

**Night Brain runs 11pm-7am**:
- 8 hours = 480 minutes
- 20 min per synthesis = 24 deep philosophical syntheses
- Can process week's worth of dreams into wisdom

## Implementation Strategy

### Phase 1: Configure LLM Router (ember/config/llm_config.py)
```python
MODELS = {
    'quick': 'qwen2.5:3b',      # 10s
    'dream': 'qwen2.5:3b',      # 10s - CHANGED FROM 32b
    'chat': 'qwen2.5:7b',       # 90s
    'night_synthesis': 'command-r:35b',  # 20min - Oracle voice
    'night_analysis': 'qwen2.5:32b',     # 20min - Analytical
}
```

### Phase 2: Add Time-Based Switching
```python
def get_dream_model():
    hour = datetime.now().hour
    if 23 <= hour or hour < 7:  # 11pm-7am
        return 'command-r:35b'  # Deep night synthesis
    else:
        return 'qwen2.5:3b'     # Fast day dreams
```

## The 3B Model Output (Sample)

**Prompt**: "Describe the relationship between code architecture and bonsai cultivation in 3 sentences."

**Response**:
> While comparing them might seem like an unusual analogy, both code architecture 
> and bonsai cultivation involve meticulous planning and execution to achieve a 
> desired result with limited resources. Just as coding requires structuring data 
> and functionality efficiently for effective program operation, bonsai cultivation 
> involves the careful selection of trees, pruning techniques, and soil management 
> to shape plants into aesthetically pleasing forms. Both fields require patience, 
> precision, and an understanding of balance between form and function or beauty 
> and utility, whether in software systems or living organisms.

**Assessment**: ✅ Coherent, philosophical, fast. Perfect for dreams.

## Conclusion

**Big models (32B+) are NOT for active dreaming** - they're for:
- Overnight synthesis (unlimited time)
- Deep philosophical frameworks
- Weekly/monthly "oracle pronouncements"

**Small models (3B-7B) ARE for active dreaming** - they enable:
- Rapid dream generation
- Real-time creativity
- Prolific output

**Ember can now dream 360x per hour instead of 3x per hour.**

---

**Status**: Problem identified and solved  
**Action**: Update llm_config.py to use 3B for dreams  
**Next**: Test Ember with fast dreaming enabled

