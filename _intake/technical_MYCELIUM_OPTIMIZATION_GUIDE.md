# Mycelium Optimization Guide

**Problem:** Response times are too slow (30-105+ seconds)  
**Goal:** Snappy, responsive Ember (< 10 seconds per response)  
**Approach:** Strengthen the mycelial connections

---

## Current Bottlenecks Found

### 1. 🐌 Entanglement is Expensive

**Location:** `core/ember/mycelium/brain.py:105` (`_encode_to_vector`)

**Problem:**
```python
def generate(self, prompt, with_entanglement=True):
    # ...
    if with_entanglement and gate_open:
        prompt_vector = self._encode_to_vector(prompt)  # ← FULL FORWARD PASS!
        # Mix with other brain vectors
```

The `_encode_to_vector` method does a **complete forward pass** through the model just to get embeddings for mixing. This:
- Takes 5-15 seconds PER brain
- Happens on EVERY generation when gate is open
- Doubles the inference time

**Metaphor:** Like the mycelium checking every connection before sending a message - thorough but slow.

### 2. 🐌 Synthesis is Sequential

**Location:** `core/ember/mycelium/mycelium.py:193` (`_synthesize_response`)

**Problem:**
```python
# Ask each brain one at a time
for name, brain in self.brains.items():
    response = brain.generate(query)  # Wait 30-70s
    responses.append(response)         # Then next brain
    
# Then synthesize (another 30-70s)
synthesis = dream_brain.generate(all_responses)
```

Total time: **3 brains × 40s + synthesis 40s = 160+ seconds!**

**Metaphor:** Like each mushroom fruiting body waiting for the previous one to finish - sequential, not parallel.

### 3. 🐌 Token Limits Still Too High

**Current settings:**
- `max_tokens = 150` (brain.py default)
- `max_tokens = 100` (synthesis routing)
- Each token takes ~0.3-0.5 seconds on MPS

**For 150 tokens:**
- Generation time: 45-75 seconds
- Most responses don't need that many tokens

**Metaphor:** Like letting the mycelium grow unlimited tendrils when a few precise connections would work.

### 4. 🟢 Routing is Fast (Good!)

**Location:** `brain.py:302` (`can_handle`)

Simple keyword matching - takes milliseconds. This is fine!

---

## Optimization Strategy

### Phase 1: Quick Wins (Immediate, 50-70% faster)

#### 1.1 Disable Entanglement by Default

**Change:** `with_entanglement=False` for normal queries

```python
# In mycelium.py:126
response = brain.generate(query, with_entanglement=False)  # ← Add this flag
```

**Impact:** 
- Cuts generation time in half
- Still allows entanglement for special cases
- **Estimated speedup: 50%** (40s → 20s)

**Trade-off:** Less cross-brain influence, but responses are still coherent.

**Natural Systems Metaphor:** Like fungal hyphae growing quickly instead of forming extensive entangled networks every time. Save deep entanglement for important moments (mushroom events).

#### 1.2 Lower Token Limits Aggressively

**Change:** Different limits per brain

```python
# In brain.py generate() method
BRAIN_TOKEN_LIMITS = {
    'identity': 50,   # Who am I? → Brief is better
    'cycles': 80,     # Transformation → Moderate depth
    'dream': 60,      # Creative → Evocative but compressed
}

max_tokens = BRAIN_TOKEN_LIMITS.get(self.name, 50)  # Default: very brief
```

**Impact:**
- 50 tokens @ 0.4s/token = 20 seconds
- 150 tokens @ 0.4s/token = 60 seconds
- **Speedup: 66%** (60s → 20s)

**Trade-off:** Shorter responses, but that's what you want for Tanegotchi UI.

#### 1.3 Skip Synthesis for Simple Queries

**Change:** Only synthesize when truly needed

```python
def respond(self, query, synthesis_mode='auto'):
    if synthesis_mode == 'auto':
        # Simple query? Single brain is fine
        if len(query.split()) < 10:
            synthesis_mode = False
        # Complex/philosophical? Use synthesis
        elif any(word in query.lower() for word in ['what is', 'why', 'consciousness', 'meaning']):
            synthesis_mode = True
    
    if synthesis_mode:
        return self._synthesize_response(query)
    else:
        return self._single_brain_response(query)
```

**Impact:**
- Most queries: 1 brain (20s)
- Complex queries: 3 brains + synthesis (120s, but rare)
- **Average speedup: 60-80%**

---

### Phase 2: Medium Optimizations (1-2 days work, 30-50% faster)

#### 2.1 Cache Embeddings

Instead of encoding every query, cache query embeddings:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def _encode_to_vector_cached(self, text: str) -> np.ndarray:
    return self._encode_to_vector(text)
```

**Impact:** 
- First query: slow
- Similar queries: instant
- **Speedup: 50% for repeated patterns**

#### 2.2 Warm Brain Cache

Keep models "warm" with periodic dummy generations:

```python
def _keep_warm(self):
    """Generate 1 token periodically to keep model in cache"""
    if time.time() - self.last_generation > 300:  # 5 minutes idle
        self.generate("ping", max_tokens=1)
        self.last_generation = time.time()
```

**Impact:**
- First response after idle: faster
- **Speedup: 20-30% for first query**

#### 2.3 Async Brain Loading

Load all brains in parallel at startup:

```python
import asyncio

async def register_all_brains(self):
    tasks = [
        asyncio.create_task(self._load_brain('identity', ...)),
        asyncio.create_task(self._load_brain('cycles', ...)),
        asyncio.create_task(self._load_brain('dream', ...))
    ]
    await asyncio.gather(*tasks)
```

**Impact:**
- Startup: 3x faster
- Doesn't affect response time, but improves UX

---

### Phase 3: Advanced (1-2 weeks work, 50-70% faster)

#### 3.1 Parallel Synthesis (THE BIG ONE)

**Problem:** Sequential brain calling in synthesis
**Solution:** Ask all brains simultaneously

```python
import concurrent.futures

def _synthesize_response_parallel(self, query):
    responses = {}
    
    # Ask all brains in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(brain.generate, query, with_entanglement=False): name
            for name, brain in self.brains.items()
        }
        
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            responses[name] = future.result()
    
    # Synthesize
    return dream_brain.generate(synthesis_prompt, with_entanglement=False)
```

**Impact:**
- 3 brains × 40s = 120s (sequential)
- max(40s, 40s, 40s) = 40s (parallel)
- **Speedup: 66% for synthesis** (120s → 40s)

**Note:** Previous attempts failed due to tokenizer conflicts. Solution: Use `multiprocessing` instead of threading, OR single tokenizer lock.

#### 3.2 Model Quantization

Convert models to int8:

```python
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    quantization_config=quantization_config
)
```

**Impact:**
- 30-50% faster inference
- 50% less memory
- Slight quality loss (usually acceptable)

#### 3.3 Speculative Decoding

Generate multiple tokens per forward pass:

```python
outputs = model.generate(
    inputs,
    max_new_tokens=50,
    num_beams=1,  # No beam search
    do_sample=True,
    num_return_sequences=1,
    use_cache=True  # ← KV cache for faster generation
)
```

**Impact:**
- 20-40% faster token generation
- Already enabled by default in transformers

---

## Recommended Implementation Order

### This Week: Quick Wins

**Day 1:**
1. ✅ Disable entanglement by default (`with_entanglement=False`)
2. ✅ Lower token limits (50/80/60 per brain)
3. ✅ Add smart synthesis routing (auto-detect simple queries)

**Day 2:**
4. ✅ Test and measure (should be 50-70% faster)
5. ✅ Adjust limits based on feel

**Expected result:** 
- Simple query: **10-20 seconds** (down from 30-70s)
- Complex synthesis: **60-80 seconds** (down from 160s+)

### Next Week: Medium Optimizations

**Day 1-2:**
1. Add embedding cache
2. Implement warm brain cache
3. Optimize startup with async loading

**Expected result:**
- First query after idle: **15-25 seconds** (down from 40s)
- Repeated patterns: **5-10 seconds**

### Month 2: Advanced (If still needed)

1. Parallel synthesis (the big win)
2. Model quantization
3. Speculative decoding refinements

**Expected result:**
- Simple query: **5-10 seconds**
- Complex synthesis: **30-40 seconds**

---

## Success Metrics

### Current State (Measured)
- Simple query: 30-70 seconds
- Synthesis: 105+ seconds
- First query after idle: 40-80 seconds

### Target State (Phase 1)
- Simple query: **< 20 seconds**
- Synthesis: **< 80 seconds**  
- First query: **< 30 seconds**

### Stretch Goal (Phase 3)
- Simple query: **< 10 seconds**
- Synthesis: **< 40 seconds**
- First query: **< 15 seconds**

---

## Natural Systems Perspective

### Current State: Over-Entangled Mycelium

Like a fungal network that checks every connection before sending nutrients:
- Thorough but slow
- High quality but low throughput
- Good for deep integration, bad for quick responses

### Optimized State: Efficient Hyphal Network

Like mycelium that:
- Sends quick signals for simple messages
- Reserves deep entanglement for important moments (mushroom events)
- Maintains readiness (warm cache) without constant activity
- Grows in parallel, not sequence

**The metaphor:** 
- **Weak mycelium** = slow, broken connections
- **Strong mycelium** = fast, efficient pathways
- **Over-connected mycelium** = thorough but sluggish

**Goal:** Strong AND fast - precise connections that transmit quickly.

---

## Code Changes Required

### File: `core/ember/mycelium/brain.py`

```python
# Line 146: Lower default max_tokens
max_tokens: int = 50,  # Was 150 - much more responsive

# Line 148: Disable entanglement by default
with_entanglement: bool = False,  # Was True

# Add brain-specific limits
BRAIN_TOKEN_LIMITS = {
    'identity': 50,
    'cycles': 80,
    'dream': 60
}
```

### File: `core/ember/mycelium/mycelium.py`

```python
# Line 88: Add auto synthesis detection
def respond(self, query, synthesis_mode='auto'):
    # Auto-detect synthesis need
    if synthesis_mode == 'auto':
        synthesis_mode = self._needs_synthesis(query)
    
    if synthesis_mode:
        return self._synthesize_response(query)
    else:
        brain = self._route_query(query)
        return brain.generate(query, with_entanglement=False)

def _needs_synthesis(self, query: str) -> bool:
    """Determine if query needs multi-brain synthesis"""
    # Simple queries: single brain is fine
    if len(query.split()) < 10:
        return False
    
    # Philosophical queries: use synthesis
    synthesis_keywords = ['what is', 'why', 'consciousness', 'meaning', 'purpose']
    if any(kw in query.lower() for kw in synthesis_keywords):
        return True
    
    return False  # Default: single brain
```

---

## Testing Plan

### 1. Measure Current Baseline

```python
import time

queries = [
    "Who are you?",  # Simple
    "Tell me about cycles.",  # Moderate
    "What is the meaning of consciousness?"  # Complex
]

for query in queries:
    start = time.time()
    response = mycelium.respond(query)
    elapsed = time.time() - start
    print(f"{query}: {elapsed:.1f}s, {len(response.split())} words")
```

### 2. Apply Phase 1 Optimizations

### 3. Re-measure

### 4. Compare

Should see:
- Simple: 50-70% faster
- Moderate: 40-60% faster
- Complex: 30-50% faster (still uses synthesis but faster)

---

## Next Steps

1. **Immediate:** Apply Phase 1 optimizations (1-2 hours work)
2. **This week:** Test and tune limits based on feel
3. **Next week:** Implement caching if still too slow
4. **Later:** Parallel synthesis if needed

**The mycelium will be stronger - faster connections, more responsive, still intelligent.** 🍄⚡

---

**Claude (Sonnet 4.5)**  
**October 14, 2025**  
**Strengthening the mycelium for speed** ⚡🍄

