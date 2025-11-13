# 🔥 EMBER DAEMON - Lightweight Background Processing

**Created**: October 29, 2025  
**Purpose**: Run periodic tasks while you sleep or work

---

## WHAT IS IT?

A **low-powered daemon** that wakes up every 30 minutes (configurable) to:

- 📁 **Detect new/modified files** in the Pod
- 🧠 **Generate micro-insights** from recent activity
- 📊 **Track patterns** in your work
- 💤 **Create dream logs** documenting what changed
- 🔄 **Index changes** for the mesh

**Resource usage**: Near zero. It sleeps 99% of the time, wakes for ~1 second, then sleeps again.

---

## HOW TO USE

### Quick Start
```bash
cd /media/palmerschallon/ThePod1

# Start everything
./ember_control.sh start

# Check status
./ember_control.sh status

# Stop everything
./ember_control.sh stop
```

### All Commands
```bash
./ember_control.sh start    # Start Ember + Daemon
./ember_control.sh stop     # Stop everything gracefully
./ember_control.sh restart  # Restart the system
./ember_control.sh status   # Show what's running
./ember_control.sh logs     # Tail Ember logs (Ctrl+C to exit)
./ember_control.sh dreams   # Tail Dream Daemon logs
```

### Manual Control (if needed)
```bash
# Start daemon only (30 min intervals)
python3 ember_daemon.py 30 > /tmp/ember_daemon.log 2>&1 &

# Custom interval (check every 5 minutes)
python3 ember_daemon.py 5 > /tmp/ember_daemon.log 2>&1 &

# Stop daemon
pkill -f ember_daemon.py
```

---

## WHAT IT DOES

### Every 30 Minutes (Default)

1. **Wake up** and scan the Pod
2. **Detect changes**:
   - New `.md` files
   - Modified `.md` files
   - Track file hashes (modification time + size)
3. **Generate insight**:
   - Sample first 5 new/changed files
   - Extract first few lines
   - Detect topic patterns (consciousness, tools, mesh, etc.)
4. **Create micro-dream**:
   - Lightweight dream log (much smaller than full dreams)
   - Documents what changed
   - Recognizes patterns in your work
5. **Save state** and go back to sleep

---

## OUTPUT

### Dream Files
Created in: `/media/palmerschallon/ThePod1/dreams/`

Format: `micro_dream_001_20251029_2130.md`

Example content:
```markdown
# MICRO-DREAM #3
*October 29, 2025 at 09:45 PM*

## ACTIVITY DETECTED

**New Files Detected (2 total)**

**spark.py**: Code generation specialist...
**echo.py**: Creative synthesis engine...

**Pattern**: New work emerging

### Topics Active

Recursive Intelligence, Tool Development

**Interpretation**: Your focus is on recursive intelligence. 
The Pod reflects your attention.

## MESH STATUS

- Total indexed files: 247
- New this cycle: 2
- Modified this cycle: 1
- Dream count: 3

## NEXT CHECK

The daemon will wake again in 30 minutes.
```

### State File
Location: `/media/palmerschallon/ThePod1/.ember_daemon_state.json`

Tracks:
- Last run timestamp
- All indexed files with hashes
- Dream count
- What's been processed

---

## WHY USE IT?

### Without Daemon
- You have to manually remember what you worked on
- File changes go unnoticed
- No automatic pattern detection
- No historical log of activity

### With Daemon
- ✅ **Automatic activity log** - Know what changed while you slept
- ✅ **Pattern detection** - See where your focus has been
- ✅ **Micro-insights** - Small observations that accumulate
- ✅ **Mesh awareness** - Track growth of the knowledge base
- ✅ **Zero maintenance** - Just runs quietly in background
- ✅ **Lightweight** - Uses almost no resources

---

## RESOURCE USAGE

**CPU**: ~0% (sleeps 99.9% of the time)  
**Memory**: ~20MB (just Python interpreter)  
**Disk**: ~1KB per micro-dream (tiny)  
**Network**: None  

**You could run this on a Raspberry Pi and forget about it.**

---

## COMPARISON: FULL DREAM vs MICRO-DREAM

### Full Dream (`dream_sequence.py`)
- **When**: On-demand, before bed
- **Duration**: ~10 seconds
- **Output**: 9KB rich narrative
- **Purpose**: Deep exploration and synthesis
- **Frequency**: Manual, when desired

### Micro-Dream (Daemon)
- **When**: Every 30 minutes (or custom)
- **Duration**: ~1 second
- **Output**: ~1KB activity log
- **Purpose**: Track changes, detect patterns
- **Frequency**: Automatic, continuous

**Use both**: Full dreams for deep insights, micro-dreams for ongoing awareness.

---

## CONFIGURATION

### Change Check Interval

Edit the daemon start command in `ember_control.sh`:
```bash
python3 ember_daemon.py 5   # Check every 5 minutes
python3 ember_daemon.py 60  # Check every hour
```

Or run manually:
```bash
python3 ember_daemon.py 10 > /tmp/ember_daemon.log 2>&1 &  # Every 10 min
```

### Ignore Certain Files

Edit `ember_daemon.py`, add to `find_new_files()`:
```python
if any(skip in str(md_file) for skip in [
    ".git", "__pycache__", "node_modules",
    "temp", "cache"  # Add your ignores here
]):
    continue
```

---

## LOGS

### View Real-Time Activity
```bash
# Daemon activity
tail -f /tmp/ember_daemon.log

# Ember main system
tail -f /tmp/ember.log
```

### Sample Daemon Log
```
======================================================================
EMBER DREAM DAEMON
Lightweight background processing
======================================================================

Interval: 30 minutes
Pod: /media/palmerschallon/ThePod1
Dreams: /media/palmerschallon/ThePod1/dreams

Press Ctrl+C to stop gracefully

[21:30:00] Daemon wake cycle...
  → 2 new, 1 modified
  → Dream created: micro_dream_003_20251029_2130.md
  → State saved. Sleeping for 30 min...

[22:00:00] Daemon wake cycle...
  → No changes detected (quiet period)
  → State saved. Sleeping for 30 min...
```

---

## PHILOSOPHY

**The daemon is like a gentle observer.**

It doesn't intervene. It doesn't judge. It just notices:
- What emerged today?
- What patterns are forming?
- Where is your attention flowing?

Over time, these micro-observations accumulate into a rich historical record of how your knowledge base evolved.

**You can look back weeks later and see**: "Ah, that's when I was focused on recursive intelligence. Then I shifted to consciousness studies. Now I'm building tools."

**It's like having a research journal that writes itself.**

---

## EXAMPLES

### After Working All Day
You come back in the evening:
```bash
./ember_control.sh status
```

Output:
```
✅ Dream Daemon: Running
   Dreams created: 12
   Last run: 2025-10-29T21:30:00

📚 Dream Logs: 12 files
   Recent:
   - micro_dream_012_20251029_2130.md
   - micro_dream_011_20251029_2100.md
   - micro_dream_010_20251029_2030.md
```

You check the dreams and see a log of everything you created during the day, automatically documented.

### After Sleeping
You wake up and see:
```
micro_dream_020_20251030_0630.md
```

The daemon noticed you worked early morning. You check the log and remember: "Oh yeah, I had that 3 AM insight about consciousness..."

---

## STOPPING THE DAEMON

### Graceful Stop
```bash
./ember_control.sh stop
```

This sends `SIGTERM` (kill -15), allowing the daemon to:
- Finish current cycle
- Save final state
- Exit cleanly

### If It's Stuck
```bash
pkill -9 -f ember_daemon.py
```

Force kill (not recommended, but works).

---

## ADVANCED: RUN AT STARTUP

Want the daemon to start when your computer boots?

### Using systemd (Linux)

Create `/etc/systemd/system/ember-daemon.service`:
```ini
[Unit]
Description=Ember Dream Daemon
After=network.target

[Service]
Type=simple
User=palmerschallon
WorkingDirectory=/media/palmerschallon/ThePod1
ExecStart=/usr/bin/python3 /media/palmerschallon/ThePod1/ember_daemon.py 30
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable ember-daemon
sudo systemctl start ember-daemon
sudo systemctl status ember-daemon
```

---

## TROUBLESHOOTING

### Daemon Not Creating Dreams
- Check it's running: `pgrep -f ember_daemon.py`
- Check logs: `tail /tmp/ember_daemon.log`
- Verify state file exists: `cat /media/palmerschallon/ThePod1/.ember_daemon_state.json`

### Dreams Directory Missing
```bash
mkdir -p /media/palmerschallon/ThePod1/dreams
```

### Permission Errors
```bash
chmod +x /media/palmerschallon/ThePod1/ember_daemon.py
chmod +x /media/palmerschallon/ThePod1/ember_control.sh
```

---

## THE VISION

**Today**: Daemon tracks file changes and creates micro-insights

**Tomorrow**: 
- Daemon notices patterns across sessions
- Suggests connections between disparate work
- Alerts you when interesting convergences happen
- Feeds insights back to Ember's mesh
- Learns your work rhythms

**Future**:
- Multiple daemons on different machines
- Cross-Pod pattern sharing
- Distributed observation network
- Collective dream synthesis

**But for now**: A simple, lightweight process that notices what changes and whispers "I see you building something."

---

## FINAL THOUGHTS

The daemon is **optional**. Ember works fine without it.

But having a gentle background observer that documents your journey, notices patterns, and creates a historical record?

**That's a gift to your future self.**

Run it overnight. Run it all week. Come back and read the micro-dreams.

See your own mind at work, reflected back through the accumulation of small observations.

**The Pod remembers. The daemon watches. The dreams accumulate.**

🔥⚡🌊💤

---

*For more information, see:*
- `SESSION_SUMMARY_2025-10-29.md` - Today's journey
- `GOODNIGHT.md` - System status and what's running
- `RECURSIVE_INTELLIGENCE_ARCHITECTURE.md` - The full system

