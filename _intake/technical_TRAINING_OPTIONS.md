# 🎯 TRAINING OPTIONS - Complete Cycles & Dream Brains

**Current Status:**
- ✅ Identity: 100% trained (working!)
- ⏸️ Cycles: 52% trained (checkpoint exists)
- ⏸️ Dream: 37% trained (no checkpoint)

---

## Option 1: Resume CPU Training (PyTorch) 📉 SLOW

**Resume from checkpoint:**

### Cycles Brain (52% → 100%)
```bash
cd /Volumes/ThePod

python3.11 tools/training/lora_train.py \
  training_data/cycles_all.jsonl \
  --brain cycles \
  --output-name blueprint_final \
  --epochs 2 \
  --resume-from-checkpoint core/ember/cycles/adapters/blueprint_final/checkpoint-57
```

**Time:** ~2-3 hours (from 52%)  
**Progress:** Continues from where it stopped

### Dream Brain (0% → 100%)
```bash
python3.11 tools/training/lora_train.py \
  training_data/dream_all.jsonl \
  --brain dream \
  --output-name imagery_final \
  --epochs 2
```

**Time:** ~3-4 hours (from 0%)  
**Progress:** Fresh start

**Total time: 5-7 hours**

---

## Option 2: Fresh MLX Training (Apple Silicon) 🚀 FAST

**Use all 3 processors (CPU + GPU + Neural Engine):**

### Both Brains (0% → 100%)
```bash
cd /Volumes/ThePod

# Install MLX training dependencies
python3 -m pip install mlx-lm

# Train Cycles (10-15 min)
python3 tools/training/mlx_lora_train.py \
  training_data/cycles_all.jsonl \
  --brain cycles \
  --output-name mlx_cycles \
  --epochs 2

# Train Dream (10-15 min)  
python3 tools/training/mlx_lora_train.py \
  training_data/dream_all.jsonl \
  --brain dream \
  --output-name mlx_dream \
  --epochs 2
```

**Time:** ~20-30 minutes total (both brains!)  
**Speed:** 10-20x faster than CPU  
**Uses:** CPU (8 cores) + GPU (10 cores) + Neural Engine (16 cores)

**Total time: ~30 minutes**

---

## 📊 Comparison

| Aspect | CPU (Resume) | MLX (Fresh) |
|--------|-------------|-------------|
| Cycles time | ~2-3 hours | ~15 minutes |
| Dream time | ~3-4 hours | ~15 minutes |
| **Total** | **5-7 hours** | **~30 minutes** |
| Checkpoint | Uses existing | Starts fresh |
| Speed/step | ~5 min | ~15-30 sec |
| Hardware used | 1 CPU core | All 3 processors |

---

## 💡 RECOMMENDATION

**Use MLX (Option 2)** because:
1. ✅ **12x faster** even starting from scratch
2. ✅ Uses your M3's full power (CPU + GPU + Neural Engine)
3. ✅ Both brains done in 30 minutes vs 7 hours
4. ✅ Future training will be 10-20x faster
5. ⚠️ Loses the 52% Cycles progress, but finishes faster anyway

---

## 🚀 Quick Start (Recommended)

```bash
cd /Volumes/ThePod

# Run the MLX training script (I'll create this)
./train_with_mlx.sh
```

This will:
1. Check MLX is installed
2. Train Cycles brain (~15 min)
3. Train Dream brain (~15 min)
4. Update adapter registry
5. Test all 3 brains together!

---

## ⚙️ What I Need to Create

To use MLX, I need to create:
1. `tools/training/mlx_lora_train.py` - MLX training script
2. `train_with_mlx.sh` - Simple wrapper script
3. Update `core/ember/session.py` to load MLX adapters

**Want me to build the MLX training pipeline?** It'll take ~10 minutes to implement, then ~30 minutes to train both brains.

---

## 🔄 Or Just Resume CPU?

If you prefer to keep the CPU checkpoint progress:

```bash
# Just run this (but will take 5-7 hours)
cd /Volumes/ThePod
./resume_cpu_training.sh
```

I can create this too - it's simpler but much slower.

---

**Your choice:** MLX (fast, fresh) or CPU (slow, resume)?

