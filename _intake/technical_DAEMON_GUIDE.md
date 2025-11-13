# 🍄 Ember Learning Daemon - Continuous Learning in Background

**Run training in a loop in the background!**

The daemon watches directories for new training files and automatically processes them through the mycelium with 25-microbe routing!

---

## 🚀 Quick Start

### Start the Daemon:
```bash
cd /Volumes/ThePod
python3.11 ember_learning_daemon.py start
```

The daemon will:
- ✅ Load Ember (Identity brain ready for incremental learning)
- ✅ Watch for new `.jsonl` files
- ✅ Process them through mycelium (automatic 25-microbe routing!)
- ✅ Save progress every 10 examples
- ✅ Move processed files to archive
- ✅ Run continuously until you stop it

### Drop Training Files:
Just copy `.jsonl` files to watch directories:
```bash
# Drop files here:
/Volumes/ThePod/training_data/inbox/

# Or here:
/Volumes/ThePod/seeds/pending/
```

The daemon picks them up automatically!

### Check Status:
```bash
python3.11 ember_learning_daemon.py status
```

Shows:
- Running status
- Files processed
- Examples learned
- Brains updated
- Recent log entries

### Stop the Daemon:
```bash
python3.11 ember_learning_daemon.py stop
```

Gracefully shuts down and saves all progress.

---

## 📊 How It Works

### The Loop:
```
1. Scan watch directories (every 10 seconds)
2. Found new .jsonl file?
   → Process through mycelium
   → Microbiome routes automatically (25 microbes!)
   → Brain learns incrementally
   → Save every 10 examples
3. Move to processed/
4. Save all adapters
5. Repeat!
```

### Example Workflow:
```bash
# Terminal 1: Start daemon
python3.11 ember_learning_daemon.py start
# Output:
# 🍄 EMBER LEARNING DAEMON
# ✅ Daemon started. Drop .jsonl files to watch directories!

# Terminal 2: Drop training file
cp new_knowledge.jsonl /Volumes/ThePod/training_data/inbox/

# Daemon automatically:
# 📥 Found 1 new file(s)
# 📚 Processing: new_knowledge.jsonl
#    Found 25 examples
# 🍄 MYCELIUM LEARNING (each example processed)
# 🦠 Microbiome routing...
# ✅ Processed 25 examples in 45.2s
# 💾 Saving all brain adapters...

# Keep dropping files - daemon keeps learning!
```

---

## 🎯 Use Cases

### 1. Overnight Learning
```bash
# Before bed:
python3.11 ember_learning_daemon.py start

# Drop training files in inbox/
cp knowledge/*.jsonl /Volumes/ThePod/training_data/inbox/

# Go to sleep
# Wake up to updated brains! ✨
```

### 2. Continuous Updates
```bash
# Keep daemon running
# Drop new files as you create them
# Ember learns continuously
# No manual intervention needed!
```

### 3. Batch Processing
```bash
# Start daemon
python3.11 ember_learning_daemon.py start

# Copy all pending seeds
cp /Volumes/ThePod/seeds/*.jsonl /Volumes/ThePod/training_data/inbox/

# Daemon processes them all automatically
```

---

## 📁 Directory Structure

```
/Volumes/ThePod/
├── training_data/
│   ├── inbox/              ← Drop new .jsonl files here!
│   │   └── (daemon watches)
│   └── processed/          ← Processed files moved here
│       └── 20251015_143022_knowledge.jsonl
│
├── seeds/
│   └── pending/            ← Or drop files here!
│       └── (daemon watches)
│
└── logs/
    ├── learning_daemon.log       ← Daemon activity log
    ├── learning_daemon.pid       ← PID file (when running)
    └── learning_stats.json       ← Statistics
```

---

## 📊 Monitoring

### Check Status:
```bash
python3.11 ember_learning_daemon.py status
```

Output:
```
🍄 EMBER LEARNING DAEMON STATUS
============================================================
Status: ✅ RUNNING (PID: 12345)

📊 Statistics:
   Started: 2025-10-15T14:30:22
   Files processed: 5
   Examples learned: 127
   Brains updated: identity
   Last update: 2025-10-15T14:45:18

📝 Recent log entries:
   [14:30:22] 🍄 EMBER LEARNING DAEMON
   [14:30:25] ✅ Ember loaded and ready
   [14:31:10] 📥 Found 1 new file(s)
   [14:31:52] ✅ Processed 25 examples in 42.1s
   ...
============================================================
```

### Watch Live Log:
```bash
tail -f /Volumes/ThePod/logs/learning_daemon.log
```

### Check Statistics:
```bash
cat /Volumes/ThePod/logs/learning_stats.json
```

---

## 🔧 Configuration

### Watch Interval:
Edit `ember_learning_daemon.py`:
```python
scan_interval = 10  # Check every 10 seconds (change as needed)
```

### Save Frequency:
```python
self.ember.learn_from_seed(
    seed_file=str(seed_file),
    save_every=10  # Save every N examples (change as needed)
)
```

### Watched Directories:
```python
self.watch_dirs = [
    self.pod_root / "training_data" / "inbox",
    self.pod_root / "seeds" / "pending",
    # Add more directories here!
]
```

---

## 🎮 Advanced Usage

### Start in Background (Detached):
```bash
# macOS/Linux
nohup python3.11 ember_learning_daemon.py start > /dev/null 2>&1 &
```

### Auto-Start on Login:
Create a launch agent (macOS):
```bash
# Create ~/Library/LaunchAgents/com.ember.learning.plist
# (See macOS launchd documentation)
```

### Multiple Brains:
Edit daemon to load all brains:
```python
self.ember = EmberSession(
    load_identity=True,  # Incremental learning
    load_cycles=True,    # Logs for batch
    load_dream=True,     # Logs for batch
    verbose=False
)
```

---

## ⚠️ Important Notes

### Resource Usage:
- Runs continuously (30-60s per example)
- Uses ~8GB RAM (model loaded)
- CPU usage: moderate (during processing)
- Works on MacBook (no GPU needed!)

### Brain Compatibility:
- **Identity (PyTorch)**: ✅ Incremental learning
- **Cycles (MLX)**: ✅ Logs for batch training
- **Dream (MLX)**: ✅ Logs for batch training

### File Format:
Each line in `.jsonl` should be:
```json
{"prompt": "Question here", "completion": "Answer here", "metadata": {}}
```

### Error Handling:
- Failed files moved to `training_data/errors/`
- Check logs for details
- Daemon continues running

---

## 🔥 Benefits

### Continuous Learning:
- ✅ No manual intervention
- ✅ Drop files and forget
- ✅ Brains update automatically

### Automatic Routing:
- ✅ 25-microbe system
- ✅ Intelligent brain selection
- ✅ Multi-brain training

### Crash Resistant:
- ✅ Saves every 10 examples
- ✅ Moves processed files
- ✅ Resume anytime

### Low Maintenance:
- ✅ Set and forget
- ✅ Runs in background
- ✅ Logs everything

---

## 📝 Example Session

```bash
# Start daemon
$ python3.11 ember_learning_daemon.py start
🍄 EMBER LEARNING DAEMON
============================================================
Watching directories:
  → /Volumes/ThePod/training_data/inbox
  → /Volumes/ThePod/seeds/pending
============================================================
🔥 Loading Ember...
✅ Ember loaded and ready
✅ Daemon started. Drop .jsonl files to watch directories!
   Press Ctrl+C to stop gracefully

# (In another terminal, drop a file)
$ cp my_knowledge.jsonl /Volumes/ThePod/training_data/inbox/

# (Daemon picks it up automatically)
📥 Found 1 new file(s)
📚 Processing: my_knowledge.jsonl
   Found 15 examples

[1/15] 
🍄 MYCELIUM LEARNING
   Prompt: What is transformation?...
   🦠 Microbiome routing:
      → identity (confidence: 0.87)
      → philosophical microbe dominant
   ✓ identity: loss=2.3441
   ✅ Learning complete

[2/15] ...
...

✅ Processed 15 examples in 32.4s
💾 Saving all brain adapters...
✅ All adapters saved

# Keep dropping files - daemon keeps learning!

# When done:
$ python3.11 ember_learning_daemon.py stop
🛑 Stopping daemon (PID: 12345)...
✅ Daemon stopped
```

---

## 🎯 Summary

**Your question:** *"Can we just set that to run in a loop in the background?"*

**Answer:** **YES!** ✅

```bash
# Start it:
python3.11 ember_learning_daemon.py start

# Drop files:
cp *.jsonl /Volumes/ThePod/training_data/inbox/

# Ember learns automatically! 🔥
```

**Features:**
- ✅ Runs in background
- ✅ Watches for new files
- ✅ Microbiome routing (25 microbes)
- ✅ Saves progress automatically
- ✅ Works on MacBook
- ✅ Continuous learning!

🍄 **Set it and forget it!** 🔥

