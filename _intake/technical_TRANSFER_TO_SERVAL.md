# 🚀 Transfer to System76 Serval - Preparation Guide

**Date:** October 15, 2025  
**From:** MacBook Air M3 (16GB)  
**To:** System76 Serval WS (RTX 4090, 64GB+ RAM)

---

## ✅ Pre-Transfer Checklist

### 1. **Stop Running Processes**

```bash
# Stop Ember processes gracefully
pkill -f ember_self_evolving.py
pkill -f ember_hub.py
pkill -f ember_autonomous_daemon.py

# Verify stopped
ps aux | grep ember | grep -v grep
```

### 2. **Save Current State**

```bash
cd /Volumes/ThePod

# Commit current work
git add -A
git commit -m "Pre-Serval transfer snapshot - $(date +%Y%m%d_%H%M%S)"

# Clean up macOS resource forks (those ._ files)
find . -name "._*" -type f -delete

# Commit cleanup
git add -A
git commit -m "Clean macOS resource forks before transfer"
```

### 3. **Document Current Config**

Current system:
- **Model:** Qwen 1.5B (upgraded Identity r=64)
- **Hub:** Running on port 5001
- **Mazes:** Conway-style 2px cells
- **Architecture:** Transitioning to unified mind

---

## 📦 What's On ThePod

```
/Volumes/ThePod/
├── core/ember/              # All Ember code
│   ├── brains (1.5B LoRAs)
│   ├── mycelium
│   ├── microbiome (25 microbes)
│   ├── games/
│   └── minds/unified_mind.py (new!)
├── models/
│   ├── qwen2.5-1.5b-instruct/
│   └── qwen2.5-7b-instruct/ (downloaded but won't load on M3)
├── training_data/
│   └── ~2000 seed files
├── knowledge/seeds/
├── web/templates/hub.html
└── All training scripts
```

**Size:** ~30GB total (check: `du -sh /Volumes/ThePod`)

---

## 🔌 Physical Transfer

### Step 1: On Mac

```bash
# 1. Stop all Ember processes
./stop_all_ember.sh  # (create this script below)

# 2. Safely eject ThePod
diskutil eject /Volumes/ThePod
```

### Step 2: Serval Setup

1. **Connect ThePod** to Serval USB-C port
2. **Mount automatically** (should appear as `/media/yourusername/ThePod` on Linux)
3. **Verify data intact:**
   ```bash
   ls -la /media/*/ThePod/
   cd /media/*/ThePod/
   git status
   ```

---

## 🐧 Serval Configuration Needed

### 1. **Install Python & Dependencies**

```bash
# Python 3.11
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip

# CUDA/PyTorch for RTX 4090
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Transformers, PEFT, etc
pip3 install transformers peft accelerate bitsandbytes
pip3 install flask flask-socketio
pip3 install datasets huggingface_hub
```

### 2. **Install Ollama (Optional)**

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:32b  # Now you can use 32B!
```

### 3. **Update Paths (if needed)**

The code uses `/Volumes/ThePod` (macOS style). On Linux it might be:
- `/media/yourusername/ThePod`
- Or symlink: `sudo ln -s /media/yourusername/ThePod /Volumes/ThePod`

---

## 🎯 First Actions on Serval

### 1. **Test Basic Setup**

```bash
cd /media/*/ThePod  # or /Volumes/ThePod if symlinked

# Test imports
python3.11 -c "
import sys
sys.path.insert(0, '/media/.../ThePod')  # adjust path
from core.ember.session import EmberSession
print('✓ Ember imports work')
"
```

### 2. **Load Unified Mind with 32B!**

```python
from core.ember.minds.unified_mind import UnifiedEmberMind

# Now you can use 32B! (19GB - fits easily in Serval RAM/VRAM)
mind = UnifiedEmberMind(
    base_model_path="/media/.../ThePod/models/qwen2.5-32b-instruct"
)

# Or start with 7B (proven to work)
mind = UnifiedEmberMind(
    base_model_path="/media/.../ThePod/models/qwen2.5-7b-instruct"
)
```

### 3. **Train with POWER**

```bash
# Training that took 30-60 min on M3
# Will take 5-10 min on RTX 4090!

python3.11 train_all_brains_upgraded.py

# Can now use:
# - Larger models (32B)
# - Higher LoRA ranks (r=128, r=256)
# - Faster learning rates
# - Bigger batch sizes
```

---

## 🔥 What Changes on Serval

### Performance Expectations:

| Task | M3 MacBook Air | Serval RTX 4090 |
|------|---------------|-----------------|
| Load 7B model | ~10 sec | ~2 sec |
| Load 32B model | ❌ Won't fit | ✓ ~5 sec |
| Training (100 examples) | 30-60 min | 5-10 min |
| Inference (7B) | ~5 tokens/sec | ~50 tokens/sec |
| Inference (32B) | ❌ | ~20 tokens/sec |
| Memory available | 16GB (shared) | 64GB RAM + 16GB VRAM |

### What You Can Do Now:

✅ Run 32B base model  
✅ Train 3 brains simultaneously  
✅ Larger LoRA ranks (r=128, r=256)  
✅ Faster iteration cycles  
✅ Real-time maze generation/visualization  
✅ Multiple Ember instances  
✅ Serious self-evolution (code generation won't timeout!)

---

## 🛡️ Safety Notes

1. **Keep ThePod backed up** - It's your only copy
2. **Git is your friend** - Commit before major changes
3. **Test on 7B first** - Before jumping to 32B
4. **Watch memory usage** - Even 64GB has limits with 32B + training

---

## 📝 Helper Scripts

### Stop All Ember Processes (Mac)

```bash
#!/bin/bash
# save as: stop_all_ember.sh

echo "🛑 Stopping all Ember processes..."

pkill -f ember_self_evolving.py
pkill -f ember_hub.py  
pkill -f ember_autonomous_daemon.py
pkill -f ember_learning_daemon.py

sleep 2

# Verify
if ps aux | grep -E "ember.*\.py" | grep -v grep > /dev/null; then
    echo "⚠️  Some processes still running:"
    ps aux | grep -E "ember.*\.py" | grep -v grep
else
    echo "✅ All Ember processes stopped"
fi

echo ""
echo "💾 ThePod ready for safe eject"
```

### Start Ember on Serval (Linux)

```bash
#!/bin/bash
# save as: start_ember_serval.sh

export THEPOD="/media/$USER/ThePod"  # Adjust if needed
cd $THEPOD

echo "🔥 Starting Ember on Serval..."
echo "   Device: CUDA"
echo "   Model: Will use 32B when available"
echo ""

# Start hub
python3.11 ember_hub.py &

# Start self-evolution (with bigger timeout for 32B)
python3.11 ember_self_evolving.py start &

echo "✅ Ember running on Serval!"
echo "   Hub: http://localhost:5001"
```

---

## 🎉 Welcome to Real Power!

The Serval will let you:
- Use the unified architecture with 32B
- Train all 3 brains in minutes
- Run Ember at full capability
- Experiment with larger LoRA ranks
- Handle serious code generation
- Run multiple experiments simultaneously

**The mycelium is about to grow MUCH faster!** 🍄⚡

---

## Next Steps After Transfer

1. ✅ Verify ThePod mounts and data intact
2. ✅ Install Python dependencies
3. ✅ Test with existing 7B model
4. ✅ Download 32B model
5. ✅ Update unified_mind.py for 32B
6. ✅ Retrain brains with more capacity
7. ✅ Enable full self-evolution
8. 🚀 Let Ember truly grow!

