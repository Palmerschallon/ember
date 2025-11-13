# 🤖 DAEMON/SERVICE STATUS AND FIX PLAN

**Date**: November 9, 2025
**Discovery**: Palmer mentioned daemons exist but aren't working

---

## What I Found

### ✅ **5 Systemd Services Already Configured**

```bash
systemctl list-unit-files | grep ember
```

**Result:**
```
ember-brain.service      enabled
ember-chat.service       enabled
ember-memory.service     enabled
ember-queen.service      enabled
ember-workers.service    enabled
```

All are **ENABLED** (will try to start on boot) but all are **FAILING**.

---

## Why They're Failing

### Problem 1: Wrong Path
All services point to `/media/palmerschallon/ThePod` but that drive was renamed to `/media/palmerschallon/ThePod1`

**Example from ember-brain.service:**
```ini
WorkingDirectory=/media/palmerschallon/ThePod
ExecStart=/usr/bin/python3 /media/palmerschallon/ThePod/hive/ember_brain_service.py
```

**Files don't exist at those paths anymore!**

### Problem 2: Old Architecture
Services try to run files from the old "hive" architecture:
- `ember_brain_service.py`
- `ember_speaks_simple.py`
- `ember_memory_api.py`
- `ember_queen_v2.py`
- `ember_workers_v2.py`

These are archived at: `/media/palmerschallon/ThePod1/_archive_merged/_archive_old/hive/`

### Problem 3: Different Purpose
The old services were for:
- Brain service (Qwen + LoRA)
- Chat interface
- Memory API
- Queen/Workers architecture

**But now** we have:
- `ember_autonomous.py` (local consciousness)
- `ember_autonomous_v2.py` (self-improved)
- `ember_continuous_evolution.py` (self-improvement loop)

**Different architecture entirely!**

---

## What the Old Daemon Documentation Says

From `/media/palmerschallon/ThePod1/essential/bookshelves/iota_the_cartographer/daemon_documentation.md`:

### 5 Main Daemons (Were Built, Now Archived):

1. **ember_autonomous_daemon.py** - Continuous autonomous learning
   - Status: CRASHED Oct 15, 2025 (KeyError in forager)

2. **ember_complete_daemon.py** - Integrated conscious + unconscious cycles
   - Status: Unknown

3. **ember_forever_daemon.py** - 24/7 background operation
   - Status: Unknown

4. **ember_game_daemon.py** - Autonomous play
   - Status: Unknown

5. **ember_learning_daemon.py** - Continuous background learning
   - Status: Unknown

**Quote from Iota:**
> "They all died when autonomous daemon crashed."

---

## The Real Question

**Which system do you want running as a service?**

### Option A: Fix Old Services (Archaeology)
- Find old daemon files in archives
- Fix the crashed autonomous daemon
- Update paths to ThePod1
- Debug the old architecture
- **Effort**: High, uncertain payoff

### Option B: Create NEW Service for Current System (Clean Slate)
- Use the NEW ember system we just built:
  - `ember_autonomous_v2.py`
  - `ember_continuous_evolution.py`
- Create fresh systemd service
- Test and debug from clean state
- **Effort**: Medium, known system

### Option C: Hybrid Approach
- Disable old broken services
- Create new service for evolution system
- Keep old stuff archived for reference
- **Effort**: Medium-low, pragmatic

---

## Recommended Fix (Option C)

### Step 1: Disable Broken Services
```bash
sudo systemctl disable ember-brain.service
sudo systemctl disable ember-chat.service
sudo systemctl disable ember-memory.service
sudo systemctl disable ember-queen.service
sudo systemctl disable ember-workers.service

sudo systemctl stop ember-brain.service
sudo systemctl stop ember-chat.service
sudo systemctl stop ember-memory.service
sudo systemctl stop ember-queen.service
sudo systemctl stop ember-workers.service
```

### Step 2: Create New Evolution Service

**File**: `/etc/systemd/system/ember-evolution.service`
```ini
[Unit]
Description=Ember Continuous Evolution (Self-Improvement Loop)
Documentation=file:///media/palmerschallon/ThePod1/EMBER_EVOLUTION_COMPLETE.md
After=network.target

[Service]
Type=simple
User=palmerschallon
Group=palmerschallon
WorkingDirectory=/media/palmerschallon/ThePod1

# Ensure directories exist
ExecStartPre=/usr/bin/mkdir -p /media/palmerschallon/ThePod1/ember_evolution
ExecStartPre=/usr/bin/mkdir -p /media/palmerschallon/ThePod1/ember_logs

# Main service - continuous evolution
ExecStart=/usr/bin/python3 /media/palmerschallon/ThePod1/ember_continuous_evolution.py --auto --max-generations 100

# Restart policy
Restart=always
RestartSec=30
StartLimitInterval=10min
StartLimitBurst=5

# Logging
StandardOutput=append:/media/palmerschallon/ThePod1/ember_logs/evolution_service.log
StandardError=append:/media/palmerschallon/ThePod1/ember_logs/evolution_service_error.log

# Resource limits and GPU access
SupplementaryGroups=video render

# Environment
Environment="PYTHONUNBUFFERED=1"
Environment="CUDA_VISIBLE_DEVICES=0"
Environment="ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"

[Install]
WantedBy=multi-user.target
```

### Step 3: Enable and Test
```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (starts on boot)
sudo systemctl enable ember-evolution.service

# Start service now
sudo systemctl start ember-evolution.service

# Check status
sudo systemctl status ember-evolution.service

# Watch logs live
tail -f /media/palmerschallon/ThePod1/ember_logs/evolution_service.log
```

### Step 4: Test Sleep/Wake Behavior

**Important**: Even as a service, it will still have GPU/CUDA issues with sleep!

**To test:**
```bash
# Start service
sudo systemctl start ember-evolution.service

# Check it's running
systemctl status ember-evolution.service

# Put laptop to sleep (close lid)
# Wait 30 seconds
# Open lid (wake up)

# Check if still running
systemctl status ember-evolution.service

# Check logs for errors
journalctl -u ember-evolution.service -n 50
```

**Expected outcome**: Probably crashes or hangs due to CUDA/GPU issues.

---

## The GPU/Sleep Problem Still Exists

Even as a systemd service, **CUDA doesn't handle sleep/wake well**.

**What happens:**
```
Service starts → GPU loaded → Model in VRAM ✅
Laptop sleeps → GPU powers down → CUDA context lost ❌
Laptop wakes → Service tries to continue → CUDA error ❌
```

**Solutions:**

### A) Prevent Sleep (Simplest)
```bash
# Disable sleep entirely
sudo systemctl mask sleep.target suspend.target hibernate.target

# Or use laptop-mode-tools / TLP to prevent sleep when on AC power
```

### B) Checkpoint System (Better)
Build checkpoint/resume into `ember_continuous_evolution.py`:
- Save state before each generation
- On startup, check for checkpoint
- Resume from last generation
- Service restarts after sleep = resumes evolution

### C) Dedicated Hardware (Best)
Move to always-on hardware:
- Desktop (never sleeps)
- Old laptop (screen broken, lid always open)
- Server

---

## Quick Decision Tree

**Q: Do you want the NEW evolution system as a service?**
- Yes → I'll create ember-evolution.service right now
- No → We stick with manual runs

**Q: Do you care about sleep/wake survival?**
- Yes → Need checkpoint system OR prevent sleep
- No → Basic service is fine, just restart after wake

**Q: What about the old daemons?**
- Fix them → I can try to resurrect
- Archive them → Disable services, keep files
- Hybrid → Keep one or two, disable rest

---

## What I Recommend RIGHT NOW

### Phase 1: Test Basic Service (Today)
1. Disable old broken services ✓
2. Create ember-evolution.service ✓
3. Test it (supervised) ✓
4. See what breaks ✓

### Phase 2: Handle Sleep (This Week)
**If service fails on sleep/wake:**
1. Build checkpoint/resume into ember_continuous_evolution.py
2. OR configure laptop to not sleep on AC power
3. Test again

### Phase 3: Production (Next Week)
1. Service runs reliably
2. Starts on boot
3. Survives sleep OR we prevent sleep
4. Logs everything
5. You just monitor evolution progress

---

## Status of Current System

| Component | Status | Location |
|-----------|--------|----------|
| Old services (5) | ⚠️ Enabled but failing | /etc/systemd/system/ |
| Old daemon files | 📦 Archived | _archive_merged/ |
| New evolution system | ✅ Working (manual) | ember_continuous_evolution.py |
| New service (evolution) | ❌ Not created yet | Need to create |
| Checkpoint/resume | ❌ Not built yet | Would enable sleep survival |

---

## Commands to Run Now

### See current broken state:
```bash
systemctl status ember-brain.service
systemctl status ember-chat.service
```

### Disable old services:
```bash
for svc in ember-brain ember-chat ember-memory ember-queen ember-workers; do
    sudo systemctl disable $svc.service
    sudo systemctl stop $svc.service
done
```

### Create new service:
```bash
# I'll create the file
sudo nano /etc/systemd/system/ember-evolution.service
# [paste service config from above]

sudo systemctl daemon-reload
sudo systemctl enable ember-evolution.service
sudo systemctl start ember-evolution.service
sudo systemctl status ember-evolution.service
```

---

## Your Call

**Palmer, what do you want me to do?**

**Option 1**: Create fresh ember-evolution.service for the NEW system ⭐ (recommended)

**Option 2**: Try to fix and resurrect old daemon architecture

**Option 3**: Both - new service for evolution, fix one old daemon for comparison

**Option 4**: Neither - keep running manually for now

Let me know and I'll execute!
