# CPU vs GPU vs Hybrid Architecture for Ember's 8 Lobes

**Date**: October 19, 2025  
**Context**: After training BURN lobe successfully, examining optimal compute allocation

---

## THE FUNDAMENTAL QUESTION

Which operations benefit from GPU parallelism vs CPU sequential processing vs a hybrid approach?

---

## GPU: Massively Parallel Operations

### What GPU Does Best:
- **Matrix multiplication** (transformer attention)
- **Parallel token generation** (beam search)
- **Batch inference** (processing multiple requests)
- **Gradient computation** (backpropagation)

### GPU Characteristics:
- 1000s of cores, each weak
- Optimized for same operation on different data (SIMD)
- High throughput, moderate latency
- Memory bandwidth critical

### Best for Ember:
- **Training** (LoRA adapter fine-tuning)
- **Inference** (generating text from lobes)
- **Embedding computation** (vector operations)
- **Pattern matching** (similarity search)

---

## CPU: Sequential & Complex Operations

### What CPU Does Best:
- **Branching logic** (if/else chains)
- **String manipulation** (parsing, regex)
- **File I/O** (reading/writing)
- **System calls** (process management)
- **Small data processing** (< 1MB)

### CPU Characteristics:
- 4-32 cores, each powerful
- Optimized for different operations on same data
- Low latency, moderate throughput
- Large caches, complex branch prediction

### Best for Ember:
- **Routing logic** (which lobe to use)
- **Quality filtering** (microbe scoring)
- **Waste detection** (pattern analysis)
- **File management** (compost, logs)
- **Daemon coordination** (event bus)

---

## THE VAST MIDDLE: Hybrid Operations

Many operations have BOTH parallel and sequential components.

### Example 1: Mycelium Routing

**Sequential part (CPU):**
```python
def route_query(query):
    # Parse query
    tokens = tokenize(query)
    
    # Rule-based routing
    if "feel" in query or "emotion" in query:
        target = "emotion_lobe"
    elif "how does" in query or "process" in query:
        target = "loop_lobe"
    
    return target
```

**Parallel part (GPU):**
```python
def semantic_routing(query_embedding):
    # Compute similarity to all lobes in parallel
    similarities = query_embedding @ lobe_embeddings.T
    return similarities.argmax()
```

**Hybrid approach:**
- CPU does quick rule matching (microseconds)
- If ambiguous, GPU does semantic similarity (milliseconds)
- Best of both worlds

---

### Example 2: Microbe Digestion

**Sequential part (CPU):**
```python
def filter_content(content):
    # Quick rejection filters
    if len(content) < 10:
        return "excrete"
    if profanity_check(content):
        return "excrete"
    if duplicate_hash(content) in seen_hashes:
        return "excrete"
    
    # Passes filters, send to GPU for deep analysis
    return "analyze"
```

**Parallel part (GPU):**
```python
def deep_analysis(content_batch):
    # Analyze 100 documents in parallel
    embeddings = encoder(content_batch)
    quality_scores = quality_model(embeddings)
    novelty_scores = novelty_detector(embeddings)
    return quality_scores, novelty_scores
```

**Hybrid approach:**
- CPU filters 90% of junk instantly
- GPU analyzes remaining 10% deeply
- 10x efficiency gain

---

### Example 3: Ouroboros Digestion

**Full pipeline:**

1. **File I/O (CPU)**: Read dreams from disk
2. **Parsing (CPU)**: Extract text, metadata
3. **Quick filters (CPU)**: Length, duplicates, toxicity
4. **Batch formation (CPU)**: Group 32 documents
5. **Embedding (GPU)**: Vectorize documents
6. **Quality scoring (GPU)**: Compute novelty/coherence
7. **Decision logic (CPU)**: Keep/compost/excrete
8. **Training data prep (CPU)**: Format for fine-tuning
9. **Training (GPU)**: Update LoRA adapters
10. **Waste export (CPU)**: Write rejected content

**Result**: CPU and GPU work in concert, each doing what it's best at.

---

## LATENCY vs THROUGHPUT TRADEOFF

### Low-Latency Operations (CPU preferred):
- Interactive chat (< 100ms response)
- Daemon coordination (< 10ms)
- Quick routing decisions (< 1ms)
- File operations (< 10ms)

### High-Throughput Operations (GPU preferred):
- Batch training (100s of examples)
- Bulk inference (100s of queries)
- Embedding computation (1000s of vectors)
- Pattern analysis (millions of tokens)

### The Middle Ground:
**Small batch inference (1-4 queries)**
- GPU: 50ms latency, but high throughput
- CPU: 200ms latency, but low overhead
- Choice depends on load

---

## EMBER'S HYBRID ARCHITECTURE

### Layer 1: Fast Path (CPU)
```
Query arrives
  -> Quick routing (CPU, 1ms)
  -> Cache check (CPU, 0.1ms)
  -> Simple responses (CPU, 5ms)
```

### Layer 2: Standard Path (Hybrid)
```
Query arrives
  -> Routing (CPU, 1ms)
  -> Lobe inference (GPU, 50ms)
  -> Post-processing (CPU, 5ms)
```

### Layer 3: Deep Path (GPU-heavy)
```
Query arrives
  -> Multi-lobe synthesis (GPU, 200ms)
  -> Cross-reference knowledge (GPU, 100ms)
  -> Generate long response (GPU, 500ms)
```

### Layer 4: Background (Async)
```
Autonomous processes
  -> Foraging (CPU, I/O bound)
  -> Batch digestion (GPU, compute bound)
  -> Training (GPU, 10min per lobe)
  -> Waste cleanup (CPU, disk bound)
```

---

## MEMORY HIERARCHY

### GPU VRAM (12GB, fast, expensive):
- Active model (1.5B base: ~3GB)
- Current LoRA adapter (~20MB)
- Batch tensors (~1GB)
- **Total**: ~4GB used, 8GB free

### System RAM (64GB, moderate, cheap):
- All 8 LoRA adapters (160MB)
- Document corpus (5GB)
- Mycelium state (500MB)
- Daemon memory (2GB)
- **Total**: ~8GB used, 56GB free

### Disk (1.8TB, slow, very cheap):
- Base models (3GB)
- Training data (20GB)
- Dreams archive (5GB)
- Waste folder (growing)
- Logs (10GB)

### Strategy:
- **Hot data**: GPU VRAM (active lobe)
- **Warm data**: System RAM (other lobes, ready to swap)
- **Cold data**: Disk (archives, waste)
- **Frozen data**: Never loaded (old versions, deprecated)

---

## OPTIMAL ALLOCATION FOR 8 LOBES

### Always GPU:
1. **Active lobe inference** (whichever lobe is responding)
2. **Embedding computation** (for routing)
3. **Training** (LoRA fine-tuning)

### Always CPU:
1. **Routing logic** (mycelium decision making)
2. **File I/O** (foraging, waste management)
3. **Quality filters** (microbe quick checks)
4. **Daemon coordination** (event bus, heartbeat)

### Hybrid (intelligent switching):
1. **Batch vs single inference** (GPU if batch > 4, else CPU)
2. **Semantic vs rule routing** (CPU rules first, GPU if needed)
3. **Training data prep** (CPU filtering, GPU embedding)

---

## THE MIDDLE GROUND: INTELLIGENT SCHEDULING

### Scenario 1: Low load (1 query/min)
- Use CPU for inference (200ms, saves GPU power)
- GPU idle or training lobes
- Result: Efficient resource use

### Scenario 2: Medium load (10 queries/min)
- Batch 4 queries, GPU inference (50ms each)
- CPU handles routing, post-processing
- Result: Optimal throughput

### Scenario 3: High load (100 queries/min)
- All queries to GPU (saturated)
- CPU pre-filters, batches, post-processes
- Result: Maximum throughput

### Scenario 4: Training time
- GPU dedicated to training (10min per lobe)
- CPU handles all inference (slower but functional)
- Result: Training doesn't block service

---

## IMPLEMENTATION: COMPUTE ROUTER

```python
class ComputeRouter:
    def __init__(self):
        self.gpu_queue = []
        self.cpu_fallback = True
        self.batch_size = 4
        self.batch_timeout = 50  # ms
    
    def infer(self, query, priority="normal"):
        # Quick CPU routing
        route = self.route_fast(query)  # CPU, 1ms
        
        # Check GPU availability
        if self.gpu_available() and priority == "high":
            return self.infer_gpu(query, route)
        
        # Batching logic
        if len(self.gpu_queue) >= self.batch_size:
            return self.infer_gpu_batch(self.gpu_queue)
        
        # Fallback to CPU if GPU busy or low priority
        if self.gpu_busy() or priority == "low":
            return self.infer_cpu(query, route)
        
        # Add to batch queue
        self.gpu_queue.append((query, route))
        return self.wait_or_fallback()
```

---

## MEASUREMENTS NEEDED

To optimize, we need to measure:

1. **GPU utilization** (% time in use)
2. **CPU utilization** (% time in use)
3. **Latency per operation** (ms)
4. **Throughput** (queries/sec)
5. **Queue depth** (pending requests)
6. **Memory pressure** (swap usage)

### Target metrics:
- GPU utilization: 60-80% (room for spikes)
- CPU utilization: 40-60% (responsive)
- P50 latency: < 100ms
- P99 latency: < 500ms
- Queue depth: < 10

---

## SPECIALIZED HARDWARE OPTIONS

### Current: RTX 5070 Ti (12GB VRAM)
- Good for 1.5B models
- Can run 1-2 lobes simultaneously
- Bottleneck: VRAM for larger models

### Alternative 1: Larger GPU (24GB+)
- Could run 7B models
- Could run 2-3 lobes simultaneously
- Cost: $1000+

### Alternative 2: Multiple GPUs
- 2x 12GB GPUs
- Each runs 4 lobes
- Parallel inference
- Cost: $800+

### Alternative 3: CPU-only with quantization
- 64GB RAM sufficient
- GGUF int4 quantization
- 10x slower but functional
- Cost: $0 (already have)

---

## RECOMMENDATION FOR EMBER

### Phase 1: Current (1.5B, single GPU)
- Train all 8 lobes on GPU (fast)
- Inference on GPU (low latency)
- Routing on CPU (efficient)
- Background tasks on CPU (async)

### Phase 2: Optimization (measure & tune)
- Add compute router with batching
- Implement CPU fallback for low priority
- Profile each lobe (which are GPU-critical?)
- Move stable lobes to CPU

### Phase 3: Scaling (if needed)
- Keep hot lobes on GPU (BURN, EMOTION)
- Move cold lobes to CPU (KNOWLEDGE, METACOGNITION)
- Hybrid inference based on load
- Background training on GPU during idle

---

## THE VAST MIDDLE: SUMMARY

The middle ground between CPU and GPU is not empty - it's where the INTELLIGENCE lives:

- **Smart routing**: CPU rules, GPU semantics
- **Adaptive batching**: CPU collects, GPU processes
- **Quality filtering**: CPU rejects junk, GPU analyzes gems
- **Load balancing**: CPU handles overflow, GPU handles bulk
- **Graceful degradation**: GPU fails -> CPU fallback

**The best architecture uses BOTH, intelligently.**

---

## NEXT STEPS

1. Train remaining 7 lobes (all GPU, fast)
2. Implement basic compute router (CPU/GPU split)
3. Measure actual latency/throughput (data-driven)
4. Profile each lobe (which need GPU most?)
5. Optimize based on real usage patterns

---

*The question is not CPU vs GPU. The question is: what runs where, when, and why?*

- Iota, the Cartographer

