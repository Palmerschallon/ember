# EMBER USER EXPERIENCE

## Before (Complex)

```
User downloads zip
  ↓
Reads which file???
  ↓
Installs dependencies manually
  ↓
Starts ember_chat.py (web server)
  ↓
Opens another terminal
  ↓
Runs talk_to_ember.py (client)
  ↓
Confused: "Why web server for local chat?"
  ↓
Maybe it works?
```

---

## After (Simple)

```
User downloads zip
  ↓
Opens README.md (right there in the folder)
  ↓
Sees: "Run ./setup.sh"
  ↓
./setup.sh
  ├─ Checks Python ✓
  ├─ Installs dependencies ✓
  ├─ Checks for model (guides download if needed)
  └─ "Ready to go!"
  ↓
python3 ember.py
  ↓
Ember loads. They talk. Done.
```

---

## Three Interfaces, Three Use Cases

### 1. ember.py - **Default** (Simple Chat)
**Use case:** "I just want to talk to Ember"
- No web server
- Direct model loading
- Clean, simple output
- Tools work inline

```bash
python3 ember.py
```

### 2. ember_three_windows.py - **Power User** (Visualization)
**Use case:** "I want to see what Ember is doing"
- Adaptive layout (full/split/triple)
- Real-time visualizations
- Tool execution visible
- Expression window shows metrics

```bash
python3 ember_three_windows.py
```

### 3. _legacy/ember_chat.py - **Web/API** (Server Mode)
**Use case:** "I want web UI or multiple clients"
- Flask web server
- Browser interface at localhost:8080
- Multiple clients can connect
- API endpoints for status/memory

```bash
cd _legacy && python3 ember_chat.py
# Then open http://localhost:8080
```

---

## The Distribution Package

```
ember-vX.X.zip
  │
  ├─ README.md              ← "Start here! 2 steps."
  ├─ GET_STARTED.md         ← "Deep dive and philosophy"
  ├─ setup.sh               ← "One-click setup"
  │
  ├─ ember.py               ← ⭐ "Most users run this"
  ├─ ember_three_windows.py ← "Power users run this"
  ├─ talk_to_ember.py       ← "Alternative simple interface"
  │
  ├─ _legacy/               ← Advanced tools
  │   ├─ ember_chat.py      ← Web server
  │   ├─ ember_cli.py       ← Mesh queries
  │   ├─ ember_expression.py
  │   ├─ intake_system.py
  │   └─ visual_forager.py
  │
  ├─ _mesh/                 ← Semantic mesh storage
  ├─ bookshelves/           ← Ember's expressions
  ├─ _intake/               ← Drop files here to feed Ember
  └─ _archive_old/
      └─ models/            ← (empty - user downloads model)
```

**User downloads → README → setup.sh → ember.py → Done**

---

## What Makes This Simple

### 1. Clear Entry Point
**README.md** is the first file they see. It says exactly what to do.

### 2. Automated Setup
**setup.sh** handles everything:
- Dependency installation
- Directory creation
- Model verification (with instructions if missing)
- GPU detection
- Permission setup

### 3. One Command to Run
```bash
python3 ember.py
```
Not two terminals. Not a web server. Just Ember.

### 4. Progressive Complexity
- Want simple? → `ember.py`
- Want pretty? → `ember_three_windows.py`  
- Want advanced? → Read GET_STARTED.md for mesh, expressions, intake

### 5. No Magic Paths
Everything relative to ThePod1. Works anywhere you unzip it.

---

## The Key Insight

Palmer's question: **"Why web socket if not on web?"**

Answer: **You don't need one.**

- `ember.py` loads the model directly
- No Flask. No web server. No HTTP.
- Just Python → Model → Chat

The web server (`ember_chat.py`) is for:
- Browser interface (some people prefer that)
- Multiple clients
- API access
- Running Ember as a service

But most users? **They just want to talk.**

So `ember.py` is the default. Simple. Direct. Fast.

---

## For Palmer to Test

### Test 1: The Basic Experience
```bash
python3 ember.py
```
- Does it feel natural?
- Is tool execution visible but not intrusive?
- Are ellipses reasonable (some OK, not excessive)?

### Test 2: The Visual Experience
```bash
python3 ember_three_windows.py
```
- Does layout adapt based on what Ember is doing?
- Are visualizations helpful or distracting?
- Does it show the "three modes of expression"?

### Test 3: The Distribution
```bash
# Pretend you're a new user
less README.md
./setup.sh
python3 ember.py
```
- Is it clear what to do?
- Does setup.sh guide well?
- Could your mom use this? (ultimate test)

---

**If these work, Ember is ready to share. 🔥**

