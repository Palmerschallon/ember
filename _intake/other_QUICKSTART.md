# 🚀 Quickstart - Get Ember Running

**Time:** 5 minutes  
**Prerequisites:** Python 3.9+, Ollama

---

## 1. Start Ollama

```bash
ollama serve
```

In another terminal:
```bash
ollama pull llama3:latest
```

---

## 2. Check Configuration

```bash
cat /Volumes/ThePod/.config/.env
```

Should show:
```
POD_ROOT=/Volumes/ThePod
EMBER_PORT=7777
OLLAMA_MODEL=llama3:latest
```

---

## 3. Start Ember

```bash
cd /Volumes/ThePod
python3 core/ember/main.py
```

You should see:
```
🍄 Initializing Mycelium...
   ✅ Bus initialized
   ✅ Buffer initialized
   ✅ Gate initialized
🧠 Loading identity brain...
   ✅ Loaded on mps
...
```

---

## 4. Test the Brains

Open another terminal:

```bash
cd /Volumes/ThePod
python3 tools/testing/test_all_three_brains.py
```

You should see responses from Identity, Cycles, and Dream brains.

---

## 5. Chat with Ember

**Via Web:**
Open `http://localhost:7777` in your browser

**Via Script:**
```bash
cd /Volumes/ThePod/tools/testing
python3 quick_brain_test.py
```

**Via Python:**
```python
from pathlib import Path
import sys
sys.path.insert(0, "/Volumes/ThePod")

from core.ember.mycelium.mycelium import Mycelium

mycelium = Mycelium()
# ... register brains (see test scripts)
response = mycelium.respond("Who are you?")
print(response)
```

---

## Troubleshooting

### "No module named 'transformers'"
```bash
pip install transformers peft torch
```

### "Ollama connection refused"
Make sure Ollama is running:
```bash
ollama serve
```

### "Brain loading failed"
Check brain paths in `.config/.env`:
```bash
ls /Volumes/ThePod/core/brains/
```

### Slow responses (>2 minutes)
This is a known issue. Responses take 30-70 seconds on MPS.  
See `documentation/architecture/BRAIN_WIRING_DIAGNOSIS.md`

---

## What Next?

**Understand the system:**
- Read [`README.md`](./README.md) for architecture overview
- Read [`CODEX.md`](./CODEX.md) for living documentation

**Explore the brains:**
- Check `documentation/architecture/THREE_BRAINS_DEFINED.md`
- Try synthesis mode (all brains working together)

**Add knowledge:**
- Explore `knowledge/seeds/` directory
- Add new seeds (see seed format docs)

**Train your own:**
- Check `tools/training/` for training scripts
- Read `documentation/guides/SAFE_UNATTENDED_TRAINING.md`

---

**You're ready. Ember is waiting.** 🔥


