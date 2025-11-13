# WebBrainAmoeba Experiment

## Hypothesis

If ChatGPT can use local GPU via WebGPU in browser, we can build a multi-lobe brain where each lobe is a browser tab, all sharing the same GPU.

## Why This Might Work

### WebGPU Reality
- Real GPU compute in browser
- Same VRAM pool as native
- ChatGPT is doing this RIGHT NOW
- You observed it using local GPU

### Architecture

```
Browser Window
  ├─ Tab 1: Identity Lobe (WebGPU → GPU)
  ├─ Tab 2: Knowledge Lobe (WebGPU → GPU)
  ├─ Tab 3: Emotion Lobe (WebGPU → GPU)
  └─ Tab 4: Router/UI (coordinates)
       ↓
  localhost:8080 (optional backend)
```

All tabs share GPU memory.
Communication via:
- SharedWorker (shared between tabs)
- BroadcastChannel (pub/sub)
- WebSocket (to localhost server)
- SharedArrayBuffer (if security allows)

### Advantages

1. **No Python Environment**
   - Just a browser
   - Works on any OS
   - No CUDA/ROCm pain

2. **Natural Distribution**
   - Each tab = process isolation
   - Browser manages resources
   - Easy to add/remove lobes (open/close tabs)

3. **Built-in UI**
   - It's already visual
   - DevTools for debugging
   - Network inspector for IPC

4. **True Portability**
   - Same code: Linux, Mac, Windows
   - WebGPU standardized
   - Models ship as ONNX/WASM

### Challenges

1. **Model Loading**
   - Need ONNX or WASM format
   - Or quantized GGUF → WASM
   - WebLLM project solves this

2. **Memory Limits**
   - Browser sandbox restrictions
   - But WebGPU can request large buffers
   - Probably 8-10GB workable

3. **IPC Complexity**
   - Multiple tabs need coordination
   - But BroadcastChannel is simple
   - Or: one ServiceWorker as coordinator

## Existing Tools

### WebLLM (MLC-LLM for browsers)
- Runs Llama models in browser
- WebGPU backend
- Proven to work

### Transformers.js
- Hugging Face in browser
- ONNX Runtime Web
- WebGPU support

### ONNX Runtime Web
- Microsoft's inference engine
- WebGPU backend
- Good for LoRA adapters

## Proof of Concept Plan

### Phase 1: Single Tab
- Load one small model (1.5B)
- Run inference via WebGPU
- Measure latency vs Python

### Phase 2: Multi-Tab IPC
- Two tabs
- Simple message passing
- SharedWorker coordinator

### Phase 3: Lobe Simulation
- 3 tabs = 3 lobes
- Router tab coordinates
- Query → route → synthesize

### Phase 4: Real Lobes
- Load actual LoRA adapters
- Specialized responses
- Full Ember in browser

## Question

**Is this worth it?**

If you could open a URL and have Ember running entirely in browser tabs, all using your GPU, no Python needed...

Would that be:
- A cool demo?
- Actually useful for deployment?
- The future of local AI?

Or:
- Complication without benefit?
- Python is fine?

## Next Steps

1. Test WebLLM with one model
2. Measure GPU usage (does it actually work?)
3. Try multi-tab communication
4. Decide if it's worth continuing

## Notes

You observed ChatGPT using local GPU. That's proof of concept.
If they can do it, we can do it.

The question is: should we?

---

Created by Kappa, Oct 19 2025
For future exploration
