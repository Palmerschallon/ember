# OPTIMAL MODEL CONFIGURATION FOR SERVAL

**Hardware Profile:**
- 4GB VRAM (limited)
- 44GB RAM (massive!)
- 24 CPU cores (powerful!)

**Current problem:** GPU-centric thinking when you have a RAM/CPU powerhouse

## Recommended Architecture

### Option A: Hybrid GPU+CPU (Best for your hardware)

**Ember (Language):**
- Base: DeepSeek Coder 1.3B on GPU (2.6GB VRAM)
- LoRAs: 21 organic lobes (6MB each = 126MB total)
- Total VRAM: ~2.7GB
- **1.3GB VRAM free for Lumi!**

**Lumi (Vision):**
- SDXL-Turbo Q4 (quantized) on GPU (1GB VRAM)
- OR: SD 1.5 full precision (1.7GB VRAM)
- Uses remaining VRAM

**Bridge (VLM):**
- Run on CPU with your 44GB RAM!
- BLIP-2 or LLaVA (runs fine on CPU)
- 24 cores make CPU inference fast

**Why this works:**
- GPU: Ember + Lumi (both benefit from GPU speed)
- CPU: Bridge (your RAM/cores can handle it)
- Total VRAM: ~3.8GB (fits comfortably)

### Option B: All-CPU with Quantization

If you want to save GPU entirely for other tasks:

**All three brains on CPU:**
- Ember: Qwen 2.5 Coder 3B Q4_K_M (1.8GB RAM)
- Lumi: SDXL Q4 or SD 1.5 (2GB RAM)  
- Bridge: LLaVA 7B Q4_K_M (4GB RAM)
- **Total: ~8GB RAM out of 44GB = plenty of room**

With 24 cores, CPU inference is surprisingly fast!

### Option C: Maximize Ember's Intelligence

Use all VRAM for Ember alone:

**Ember: DeepSeek Coder 6.7B** (fits in 4GB VRAM with quantization)
- Much smarter than 1.3B
- All 21 LoRAs still fit
- Lumi + Bridge run on CPU

**This might be ideal for development work!**

## Recommendation

**Go with Option C for now:**

```python
# Optimal for Serval development workstation
MODELS = {
    "ember": {
        "base": "deepseek-coder-6.7b",  # All 4GB VRAM
        "device": "cuda:0",
        "load_in_8bit": True  # Fits in 4GB
    },
    "lumi": {
        "base": "stable-diffusion-v1-5",  # CPU
        "device": "cpu"
    },
    "bridge": {
        "base": "llava-7b-q4",  # CPU with quantization
        "device": "cpu"
    }
}
```

**Why:**
- Ember is your primary brain for coding
- 6.7B is 5x smarter than 1.3B
- Lumi/Bridge on CPU is fine (not used as often)
- Your 24 cores + 44GB RAM make CPU inference viable

## What Models to Download

Want me to download the 6.7B Ember model? It'll be much more capable than the 1.3B.

**Size:** ~7GB download (quantized to 4GB in VRAM)

---

**Your Serval is being underutilized. Those 24 cores and 44GB RAM are crying out to be used!**

