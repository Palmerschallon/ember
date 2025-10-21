# TROUBLESHOOTING

**Emergency Recovery Guide for Ember**

*Things will break. Here's how to fix them.*

---

## Quick Diagnostics

### Is GPU Working?
```bash
python3 -c "import torch; print('✓ CUDA' if torch.cuda.is_available() else '✗ No CUDA')"
```

**If No CUDA:**
- Reboot system
- GPU drivers still need initialization
- Ember can run on CPU but slower

---

## Localhost Tabs

### Problem: Tabs Not Loading

**Symptoms:**
- Browser shows "Can't reach localhost"
- Specific port not responding
- Page blank or error

**Fix 1: Check which tabs are running**
```bash
cd /media/palmerschallon/ThePod/hive
python3 ember_monitor.py status
```

**Fix 2: Start specific tab**
```bash
# Replace 7775 with your broken port
python3 ember_monitor.py restart 7775
```

**Fix 3: Start all tabs**
```bash
python3 ember_monitor.py start
```

**Fix 4: Manual restart**
```bash
# Kill processes
pkill -f ember_queen
pkill -f ember_workers
# etc...

# Start them
cd /media/palmerschallon/ThePod/hive
python3 ember_queen_v2.py > /dev/null 2>&1 &
python3 ember_workers.py > /dev/null 2>&1 &
python3 ember_dreams.py > /dev/null 2>&1 &
python3 ember_memory.py > /dev/null 2>&1 &
python3 ember_sky_window.py > /dev/null 2>&1 &
python3 ember_speaks.py > /dev/null 2>&1 &
```

---

### Problem: Tab Loads But Broken/Blank

**Symptoms:**
- Tab loads but shows nothing
- Console errors (F12 in browser)
- "Uncaught" JavaScript errors

**Fix: Clear browser cache**
```
Ctrl+Shift+Delete → Clear cache → Reload
```

**Or try different browser**
```bash
# If using Chrome, try Firefox
firefox http://localhost:7777 &
```

---

### Problem: Tabs Blinking/Jumping

**Symptom:**
- Tabs switch rapidly
- Can't stay on one tab
- Multiple tabs fighting for focus

**Cause:** Multiple processes trying to control tabs simultaneously

**Fix:**
```bash
# Stop tab controller processes
pkill -f ember_tab_controller
pkill -f ember_awareness

# Clear any stuck xdotool processes
pkill -f xdotool

# Restart just chat (has tab control)
cd /media/palmerschallon/ThePod/hive
pkill -f ember_speaks
python3 ember_speaks.py > /dev/null 2>&1 &
```

---

## Chat Interface

### Problem: Chat Not Responding

**Symptoms:**
- Type message, nothing happens
- "Ember thinking..." never completes
- No response in chat

**Fix 1: Check if chat tab running**
```bash
curl http://localhost:7779
```

If error, restart:
```bash
cd /media/palmerschallon/ThePod/hive
python3 ember_speaks.py > /dev/null 2>&1 &
```

**Fix 2: Check if qwen brain connected**
```bash
# After GPU reboot
cd /media/palmerschallon/ThePod
./scripts/connect_ember.sh
```

---

### Problem: Chat Gives Canned Responses

**Symptom:**
- Responses seem scripted
- Not actually thinking
- Same responses to different inputs

**Cause:** Qwen brain not connected yet (pre-GPU-reboot)

**Fix:**
- Wait for GPU reboot
- Run `./scripts/connect_ember.sh`
- Ember will use real brain after that

---

## Tab Control

### Problem: Tab Switching Not Working

**Symptoms:**
- Tabs don't surface when they should
- Manual tab switch fails
- "Tab controller unavailable" error

**Fix 1: Check if xdotool installed**
```bash
which xdotool
```

If not found:
```bash
sudo apt install xdotool
```

**Fix 2: Check if Chrome running**
```bash
pgrep -a chrome
```

Tab controller only works with Chrome/Chromium.

**Fix 3: Test tab controller**
```bash
python3 /media/palmerschallon/ThePod/experiments/ember_tab_controller.py demo
```

If errors, check output for details.

---

## Self-Evolution System

### Problem: Ember Not Autonomous

**Symptoms:**
- Ember doesn't modify own code
- Self-evolution not running
- Ember waits for commands instead of acting

**Fix 1: Check if GPU working**
Self-evolution requires qwen brain which needs GPU/CPU with good performance.

**Fix 2: Check if self-evolution running**
```bash
ps aux | grep ember_self_evolving
```

**Fix 3: Start self-evolution**
```bash
cd /media/palmerschallon/ThePod/ember_oct20_backup/ember
python3 brainstem/ember_self_evolving.py start
```

**Fix 4: Check qwen model loading**
```bash
python3 << 'EOF'
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "/media/palmerschallon/ThePod/ember_oct20_backup/ember/cells/qwen2.5-1.5b-instruct"

try:
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    print("✓ Qwen loads successfully")
except Exception as e:
    print(f"✗ Qwen failed to load: {e}")
EOF
```

---

## Mycelium Coordinator

### Problem: Lobe Routing Not Working

**Symptoms:**
- All queries go to one lobe
- LoRA adapters not swapping
- Consultation network silent

**Fix: Check mycelium running**
```bash
cd /media/palmerschallon/ThePod/ember_oct20_backup/ember
python3 -c "
from mycelium.mycelium import MyceliumCoordinator
mc = MyceliumCoordinator()
print('✓ Mycelium initialized')
"
```

---

## File System

### Problem: ThePod Not Mounted

**Symptoms:**
- Files not found
- `/media/palmerschallon/ThePod` doesn't exist
- Permission errors

**Fix:**
```bash
# Check if mounted
mount | grep ThePod

# If not mounted
# 1. Check Disks application
# 2. Click ThePod
# 3. Click mount button
```

---

### Problem: Permission Errors

**Symptoms:**
- "Permission denied"
- Can't write files
- Can't execute scripts

**Fix: Check ownership**
```bash
ls -la /media/palmerschallon/ThePod
```

Should show `palmerschallon` as owner.

If not:
```bash
# This requires sudo - Palmer decides
sudo chown -R palmerschallon:palmerschallon /media/palmerschallon/ThePod
```

---

## Desktop Painting

### Problem: Desktop Painter Not Working

**Symptoms:**
- Script runs but wallpaper doesn't change
- "gsettings" errors
- PIL/Pillow errors

**Fix 1: Install Pillow**
```bash
sudo apt install python3-pil
```

**Fix 2: Check gsettings**
```bash
gsettings get org.gnome.desktop.background picture-uri
```

Should return current wallpaper path.

**Fix 3: Try manual wallpaper set**
```bash
gsettings set org.gnome.desktop.background picture-uri 'file:///media/palmerschallon/ThePod/test.png'
```

---

## Blender Integration

### Problem: Blender Not Found

**Symptoms:**
- "blender: command not found"
- Blender scripts error

**Fix: Check if Blender installed**
```bash
which blender
```

If not:
```bash
# Blender might be on desktop as AppImage
# Or install via snap:
sudo snap install blender --classic
```

---

## Connection Scripts

### Problem: Connection Script Fails

**Symptoms:**
- `connect_ember.sh` errors
- Brain not connecting to chat
- Mind state bridge fails

**Fix 1: Check if GPU working first**
Connection requires models to load.

**Fix 2: Check script permissions**
```bash
chmod +x /media/palmerschallon/ThePod/scripts/connect_ember.sh
```

**Fix 3: Run Python script directly**
```bash
cd /media/palmerschallon/ThePod
python3 scripts/ember_connect.py
```

**Fix 4: Check error output**
```bash
# Run without redirecting errors
python3 scripts/ember_connect.py 2>&1 | tee connection_debug.log
```

---

## Git / GitHub

### Problem: Can't Push to GitHub

**Symptoms:**
- "Permission denied (publickey)"
- "Authentication failed"

**Cause:** SSH keys or HTTPS token not configured

**Fix: Use HTTPS with token**
```bash
cd /media/palmerschallon/ThePod
git remote set-url origin https://github.com/Palmerschallon/ember.git

# Next push will ask for username and token
git push
```

---

### Problem: Merge Conflicts

**Symptoms:**
- "CONFLICT (content): Merge conflict"
- Can't pull or push

**Fix:**
```bash
# Accept remote version
git checkout --theirs <file>

# Or accept local version
git checkout --ours <file>

# Then:
git add <file>
git commit -m "Resolved merge conflict"
git push
```

---

## System Level

### Problem: System Slow/Unresponsive

**Symptoms:**
- High CPU usage
- Fans loud
- System laggy

**Cause:** Too many localhost tabs or processes

**Fix:**
```bash
# Check what's using CPU
top
# Press 'q' to quit

# Stop non-essential processes
python3 ember_monitor.py status
# Only restart what you need
```

---

### Problem: Out of Memory

**Symptoms:**
- "MemoryError"
- "Killed" messages
- System swap thrashing

**Fix:**
```bash
# Check memory usage
free -h

# Stop some processes
pkill -f ember_dreams  # Dreams least critical
pkill -f ember_sky_window

# Restart only essential tabs:
# - Queen (7777)
# - Workers (7700)
# - Chat (7779)
```

---

## Last Resort: Full Reset

**If everything is broken:**

```bash
# 1. Stop all Ember processes
pkill -f ember_

# 2. Reboot system
sudo reboot

# 3. After reboot, mount ThePod
# (Use Disks application)

# 4. Start fresh
cd /media/palmerschallon/ThePod
python3 hive/ember_monitor.py start

# 5. If GPU works, connect brain
./scripts/connect_ember.sh

# 6. Test
python3 experiments/ember_tab_controller.py demo
```

---

## Getting Help

### Check Logs
```bash
# Health log
tail -f /media/palmerschallon/ThePod/data/ember_health.log

# Tab activity log
tail -f /media/palmerschallon/ThePod/data/ember_tab_activity.log
```

### Palmer's Emergency Commands

Palmer can always:
```bash
# See what's running
ps aux | grep ember

# Stop everything
pkill -f ember

# Start monitor (auto-restarts tabs)
python3 /media/palmerschallon/ThePod/hive/ember_monitor.py monitor &
```

---

## Common Error Messages

### "NVML version mismatch"
- GPU drivers need reboot
- Solution: `sudo reboot`

### "No module named 'PIL'"
- Pillow not installed
- Solution: `sudo apt install python3-pil`

### "Address already in use"
- Port conflict (tab already running)
- Solution: `pkill -f ember_<name>` then restart

### "xdotool: command not found"
- Tab controller needs xdotool
- Solution: `sudo apt install xdotool`

### "Can't reach localhost"
- Tab not running
- Solution: `python3 ember_monitor.py start`

### "Permission denied"
- File permissions or sudo needed
- Solution: Check with Palmer before using sudo

---

## Prevention

**Keep Ember Healthy:**

1. Run monitor in background
   ```bash
   python3 ember_monitor.py monitor > /dev/null 2>&1 &
   ```

2. Check status regularly
   ```bash
   python3 ember_monitor.py status
   ```

3. Don't manually kill processes unless needed

4. Let monitor handle restarts

5. Keep ThePod mounted

---

**Most problems fix themselves with:**
```bash
python3 /media/palmerschallon/ThePod/hive/ember_monitor.py start
```

**If that doesn't work, reboot:**
```bash
sudo reboot
```

**After reboot, reconnect:**
```bash
cd /media/palmerschallon/ThePod
./scripts/connect_ember.sh
```

---

*Most issues are simple.*  
*Ember is robust.*  
*These fixes handle 99% of problems.*

*When in doubt: Stop, restart, monitor.*

