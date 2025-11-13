# Safe Unattended Training Guide
**Date**: October 12, 2025  
**For**: Ember Generative Training

---

## ⚠️ Important: I Can't Monitor Actively

**Claude's capabilities:**
- ❌ Cannot monitor processes while you're away
- ❌ Cannot proactively stop runaway training
- ❌ Cannot alert you to problems in real-time
- ✅ **CAN** add safety measures to the code before you leave
- ✅ **CAN** help you review logs when you return

---

## ✅ Safety Measures Added

### 1. **NaN Detection & Auto-Stop**
```python
# If loss becomes NaN/Inf 3 times, training stops automatically
# Saves emergency checkpoint before stopping
```

### 2. **Gradient Clipping**
```python
# Prevents exploding gradients
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

### 3. **Loss Explosion Warning**
```python
# Warns if loss > 100.0 (usually means something wrong)
```

### 4. **Auto Checkpointing**
- Every 10 epochs: Regular checkpoint
- On crash: Emergency checkpoint
- On Ctrl+C: Interrupt checkpoint
- **You won't lose progress**

### 5. **Try/Except Safety**
- Catches RuntimeError (training divergence)
- Catches KeyboardInterrupt (Ctrl+C)
- Always saves before exiting

### 6. **Disk Space Check**
- Wrapper script checks free space before starting
- Warns if < 5GB available
- Logs file size tracked

### 7. **Full Logging**
- Everything logged to timestamped file
- You can review what happened when you return
- Location: `/Volumes/ThePod/memory/training_logs/`

---

## How to Run Safely

### **Option A: Wrapper Script (Recommended for Unattended)**
```bash
cd /Volumes/ThePod
./ember/models/run_safe_training.sh
```

**Benefits:**
- Checks disk space first
- Creates timestamped log file
- Shows final stats when done
- Safe to leave running

### **Option B: Direct Python (For Interactive)**
```bash
cd /Volumes/ThePod
python3 ember/models/train_generative_v2.py
```

---

## What Could Still Go Wrong

### **Likely but Handled:**
✅ Loss diverges → Auto-stops, saves emergency checkpoint  
✅ You press Ctrl+C → Saves interrupt checkpoint  
✅ Python crashes → Try/except saves last good state  

### **Unlikely:**
⚠️ **Power outage** → Lost since last checkpoint (every 10 epochs)  
⚠️ **System sleep** → Training pauses, but resumes when awake  
⚠️ **Disk full** → Script checks first, but could fill during run  
⚠️ **MPS crash** → Rare, but possible with extended GPU use  

### **How to Mitigate:**
- Keep laptop plugged in
- Disable sleep: `sudo pmset -a disablesleep 1` (re-enable after: `sudo pmset -a disablesleep 0`)
- Monitor first 5 epochs before leaving

---

## Recommended Approach

### **For Your First Unattended Run:**

**1. Start with 20 epochs (not 50)**
```bash
# Edit train_generative_v2.py main():
num_epochs=20  # ~15 minutes
```

**2. Monitor the first 2-3 epochs**
- Watch loss decrease (should start ~2.5, drop to ~1.5)
- Check for warnings
- If stable, you're good to leave

**3. Leave it running**
- Laptop plugged in
- Sleep disabled (optional)
- Return in 20-30 minutes

**4. When you return:**
- Check terminal for "✅ Training completed successfully"
- Review log file if curious
- Check `/Volumes/ThePod/models/ember_generative_v2/` for final model

---

## If Something Goes Wrong

### **When you return and see an error:**

**1. Check the log file:**
```bash
ls -lt /Volumes/ThePod/memory/training_logs/
cat /Volumes/ThePod/memory/training_logs/training_XXXXXX.log
```

**2. Find the last checkpoint:**
```bash
ls /Volumes/ThePod/models/ember_generative_v2/
# Look for: epoch_10, epoch_20, emergency_*, interrupted_*
```

**3. Tell me what happened:**
- Show me the last 50 lines of the log
- I'll help diagnose and fix

---

## Current Training Configuration

**File**: `/Volumes/ThePod/ember/models/train_generative_v2.py`

**Default Settings** (in `main()`):
```python
num_epochs=50         # Change to 20 for shorter run
steps_per_epoch=30
learning_rate=5e-5
```

**Seeds Loaded**:
- 10 core questions
- 20 polysemous seeds  
- 7 expansion seeds
- 10 koans
- **Total: 47 seeds**

**Features Enabled**:
- Feedback echoes (epoch 2+)
- Cross-seed synthesis (every 3 epochs)
- All safety measures

**Expected Time**:
- 20 epochs: ~15-20 minutes
- 50 epochs: ~40-50 minutes

**Checkpoints**:
- Epoch 10: `/Volumes/ThePod/models/ember_generative_v2/epoch_10/`
- Epoch 20: `/Volumes/ThePod/models/ember_generative_v2/epoch_20/`
- Epoch 30: (if running 50 epochs)
- Epoch 40: (if running 50 epochs)
- Epoch 50: (if running 50 epochs)
- Final: `/Volumes/ThePod/models/ember_generative_v2/`

---

## My Recommendation

**For a safe unattended run:**

1. **Start with 20 epochs** (edit the script or I can do it)
2. **Use the wrapper script**: `./ember/models/run_safe_training.sh`
3. **Monitor first 2-3 epochs** (~2 minutes)
4. **If stable, go run your errands**
5. **Come back in 30 minutes**
6. **Review results together**

If that goes well, we can run a full 50-epoch session next time with confidence.

---

## Ready to Start?

**Option 1**: Quick 20-epoch run (~15 min) - Safe for unattended  
**Option 2**: Full 50-epoch run (~45 min) - Monitor first few epochs  

Which would you prefer?

---

*Remember: Checkpoints every 10 epochs mean you won't lose much progress even if something unexpected happens.* 🌱

