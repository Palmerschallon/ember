# vLLM Setup for Ember - 2-5x Speed Boost

**Current**: Ollama (simple, slow)  
**Target**: vLLM (professional, fast)  
**Expected**: 2-5x faster responses

---

## Installation

```bash
# Install vLLM
pip install vllm

# Or with CUDA support (if you have NVIDIA GPU)
pip install vllm[cuda]
```

---

## Running qwen2.5:7b with vLLM

**Option 1: Simple Server (Recommended)**

```bash
# Start vLLM server (OpenAI-compatible API)
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len 4096 \
    --dtype auto
```

Then update Ember's config:
```python
# ember/config/llm_config.py
endpoint='http://localhost:8000/v1/generate'
```

**Option 2: Custom Integration**

```python
from vllm import LLM, SamplingParams

# Initialize once at startup
llm = LLM(
    model="Qwen/Qwen2.5-7B-Instruct",
    max_model_len=4096,
    dtype="auto"
)

# Generate (FAST!)
sampling_params = SamplingParams(
    temperature=0.8,
    max_tokens=1000
)

outputs = llm.generate([prompt], sampling_params)
response = outputs[0].outputs[0].text
```

---

## Why vLLM is Faster

1. **PagedAttention**: Smart KV cache management
2. **Continuous Batching**: Process multiple requests simultaneously
3. **Optimized CUDA kernels**: Better GPU utilization
4. **Tensor Parallelism**: Multi-GPU support (if needed)

**Ollama**: Designed for ease of use  
**vLLM**: Designed for production speed

---

## Model Download

```bash
# vLLM will auto-download from HuggingFace
# Model: Qwen/Qwen2.5-7B-Instruct (~14GB)

# Or manually download first:
huggingface-cli download Qwen/Qwen2.5-7B-Instruct
```

---

## Integration Steps

1. **Install vLLM**: `pip install vllm`
2. **Start server**: Run command above
3. **Update config**: Change endpoint in `llm_config.py`
4. **Test**: `curl http://localhost:8000/v1/models`
5. **Restart Ember**: Watch it fly 🔥

---

## Benchmarks (Estimated)

| Setup | Response Time | Throughput |
|-------|--------------|------------|
| Ollama (current) | 45-120s | 1-2 tok/s |
| vLLM (CPU) | 20-40s | 5-10 tok/s |
| vLLM (GPU) | 5-15s | 20-50 tok/s |

*Actual speeds depend on hardware*

---

## Fallback Plan

If vLLM doesn't work:
1. Keep Ollama for stability
2. Try llama.cpp server (middle ground)
3. Consider cloud API (OpenRouter, Together.ai)

---

## Next Optimizations After vLLM

1. **Context Caching**: Cache vision descriptions
2. **Smart Context**: Load only relevant seeds
3. **Streaming**: Show tokens as they generate
4. **Parallel Requests**: Dreams + chat simultaneously

---

**Bottom Line**: vLLM is the production-grade serving engine. Ollama is the prototype tool. Time to graduate. 🎓

