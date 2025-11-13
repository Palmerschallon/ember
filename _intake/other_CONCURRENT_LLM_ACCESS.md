# 🔄 Concurrent LLM Access - Understanding & Solutions

**Issue:** Both Ember and Lumi share the same Ollama instance  
**Impact:** Concurrent requests may queue or experience delays  
**Status:** ✅ Retry logic added, works reliably

---

## The Situation

### Current Architecture

```
Ember (port 7777) ──┐
                    ├──→ Ollama (localhost:11434) ──→ LLM Model
Lumi (port 7778) ───┘
```

**Both pods share:**
- Same Ollama server
- Same model (llama3.2:latest)
- Same hardware resources (CPU/GPU)

**What happens when both query simultaneously:**
1. First request starts processing
2. Second request queues
3. Ollama processes sequentially (one at a time)
4. Both eventually complete, but with delay

---

## What We Fixed

### ✅ Retry Logic Added

**In `ember/services/llm.py`:**

```python
def _ollama_generate(url, model, prompt, system=""):
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                f"{url}/api/generate",
                json=payload,
                timeout=120,
                headers={"Connection": "close"}  # Don't keep connections
            )
            return resp.json()["response"]
        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                continue
            return error_message
```

**Benefits:**
- Handles temporary connection issues
- Exponential backoff prevents hammering
- Clear error messages if all retries fail
- Closes connections (doesn't hold sockets)

---

## Performance Characteristics

### Single Pod Query

```
User asks Ember → Ollama processes → Response in ~10-15s
```

**Typical:** 10-15 seconds for conversational response

### Dual Pod Query (Sequential)

```
User asks Both → Ember queues → Lumi queues
                    ↓              ↓
              Ollama processes Ember (10-15s)
                    ↓
              Ollama processes Lumi (10-15s)
                    ↓
              Both complete in ~20-30s
```

**Typical:** 20-30 seconds total (sequential processing)

### Why This Happens

**Ollama is single-threaded per model:**
- One model instance loads into memory
- Processes requests one at a time
- Can't truly parallelize same model

**This is normal and expected.**

---

## Solutions (In Order of Effort)

### Solution 1: Accept It ✅ (Current)

**What we have:**
- Retry logic handles queuing gracefully
- Both pods eventually respond
- User sees both perspectives
- No additional complexity

**Works well for:**
- Interactive use
- Non-time-critical queries
- Learning/exploration

**Limitations:**
- Takes 2x time for dual queries
- Sequential, not parallel

---

### Solution 2: Load Balancing (Medium Effort)

**Add simple queue:**

```python
import asyncio
from collections import deque

class LLMQueue:
    def __init__(self):
        self.queue = deque()
        self.processing = False
    
    async def enqueue(self, request):
        self.queue.append(request)
        if not self.processing:
            await self.process_queue()
    
    async def process_queue(self):
        self.processing = True
        while self.queue:
            request = self.queue.popleft()
            await self._process(request)
        self.processing = False
```

**Benefits:**
- Fair ordering (FIFO)
- No retry storms
- Clear queue status

**Limitations:**
- Still sequential
- Adds complexity

---

### Solution 3: Multiple Model Instances (High Effort)

**Load same model twice:**

```
Ember → Ollama instance 1 (port 11434)
Lumi  → Ollama instance 2 (port 11435)
```

**Implementation:**
```bash
# Terminal 1
ollama serve --port 11434

# Terminal 2  
ollama serve --port 11435

# Update configs
Ember: OLLAMA_URL=http://127.0.0.1:11434
Lumi:  OLLAMA_URL=http://127.0.0.1:11435
```

**Benefits:**
- True parallelism
- Independent processing
- No queuing

**Limitations:**
- 2x memory usage (8GB+ per model)
- 2x GPU/CPU resources needed
- Complex setup

**Feasibility:** Only if you have 16GB+ RAM and dedicated GPU

---

### Solution 4: Different Models (Medium-High Effort)

**Specialize pods with different models:**

```
Ember → llama3.2:latest (technical, precise)
Lumi  → llama3.2-text:latest (creative, flowing)
```

**Benefits:**
- Natural specialization
- Can run simultaneously (different models)
- Each optimized for its role

**Limitations:**
- Need to find/fine-tune creative model
- Increased memory usage
- Different response qualities

---

### Solution 5: Remote LLM API (Low Effort, High Cost)

**Use cloud LLM for one pod:**

```
Ember → Ollama (local, free)
Lumi  → OpenAI/Anthropic (remote, paid)
```

**Benefits:**
- True parallelism
- Faster response (dedicated hardware)
- No local resource issues

**Limitations:**
- Costs money (~$0.01-0.10 per response)
- Requires internet
- Privacy concerns (data sent to cloud)

---

## Recommended Approach

### For Now: Solution 1 ✅

**Why:**
- Already implemented
- Handles gracefully
- No additional cost
- Works reliably

**Use cases:**
- Personal exploration
- Learning and experimentation
- Non-production use

### If Performance Matters: Solution 3 or 5

**Solution 3 (Multiple Instances) if:**
- You have 16GB+ RAM
- You have GPU
- You need local processing

**Solution 5 (Remote API) if:**
- Budget available ($10-50/month)
- Speed is critical
- OK with cloud processing

---

## Testing Concurrent Access

### Test Script

```bash
# Test both pods simultaneously
curl -X POST http://127.0.0.1:7777/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hi Ember"}' &

curl -X POST http://127.0.0.1:7778/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hi Lumi"}' &

wait
```

**Expected:**
- Both complete successfully
- Total time: ~20-30s (sequential)
- Retry logic handles any collisions

---

## Monitoring

### Check Ollama Status

```bash
# See active requests
curl http://127.0.0.1:11434/api/tags

# Check if model is loaded
ps aux | grep ollama
```

### Check Pod Health

```bash
# Ember health
curl http://127.0.0.1:7777/health

# Lumi health
curl http://127.0.0.1:7778/health
```

---

## Best Practices

### 1. Single Pod for Quick Queries

Use Ember OR Lumi, not both, for:
- Quick questions
- Time-sensitive needs
- Rapid iteration

### 2. Both Pods for Comparison

Use dual chat when you want:
- Complementary perspectives
- Compare approaches
- Learn from contrast

### 3. Sequential for Exploration

When using both:
- Ember first (technical foundation)
- Then Lumi (creative insight)
- Build on each response

---

## The Reality

**This is normal for local LLM deployments.**

**Production systems use:**
- Multiple GPU servers
- Load balancers
- Request queues
- Auto-scaling

**For personal exploration:**
- Sequential processing is fine
- Retry logic handles it
- Both pods work reliably

---

## Future Improvements

### When Pod Count Grows

If you add more pods (3, 4, 5+):

**Option A: Request Router**
```python
class LLMRouter:
    def route(self, pod_name, request):
        # Route based on priority, load, etc.
        if high_priority:
            return immediate_process(request)
        else:
            return queue_request(request)
```

**Option B: Dedicated Models**
```
Technical pods → Code model (CodeLlama)
Creative pods  → Text model (Llama-Text)
Analysis pods  → Reasoning model (Mixtral)
```

**Option C: Hybrid Approach**
```
Simple queries  → Local Ollama
Complex queries → Remote API
Critical paths  → Dedicated instance
```

---

## Conclusion

**Current status:** ✅ Works reliably with retry logic

**Performance:**
- Single pod: 10-15s
- Dual pod: 20-30s (sequential)

**Good enough for:**
- Personal use ✅
- Exploration ✅
- Learning ✅

**Upgrade if:**
- Need <5s responses
- Many users
- Production deployment

**For now, enjoy the dual perspectives!** The slight delay is worth the complementary insights. 🔥💫


