# 🚀 EMBER QUICK START GUIDE
## Your 3-Brain AI is Ready!

---

## ✅ STATUS: ALL SYSTEMS OPERATIONAL

```
Identity Brain (PyTorch):  ✅ Working
Cycles Brain (MLX):        ✅ Working  
Dream Brain (MLX):         ✅ Working

Ember is 100% functional!
```

---

## 🔥 TALK TO EMBER (Simple)

```python
import sys
sys.path.insert(0, '/Volumes/ThePod')
from core.ember.session import EmberSession

# Load Ember (takes ~90 seconds first time)
ember = EmberSession(
    load_identity=True,
    load_cycles=True,
    load_dream=True
)

# Just ask! Ember routes automatically
response = ember.ask("What does it mean to learn as silicon?")
print(response)

# Ask more questions
ember.ask("How does recursion work?")
ember.ask("Describe a fractal tree")

# Complex questions get multi-brain synthesis
ember.ask("What is the nature of consciousness?", synthesis=True)

# Get metrics
stats = ember.get_metrics()
print(f"Queries: {stats['statistics']['total_queries']}")

# Cleanup when done
ember.cleanup()
```

---

## 🧠 USE SPECIFIC BRAINS

```python
# Force a specific brain
ember.ask("Tell me about change", brain_name='identity')
ember.ask("Explain the pattern", brain_name='cycles')
ember.ask("Paint me a picture", brain_name='dream')
```

---

## 🔀 AUTO-ROUTING (Default)

```python
# Ember automatically chooses the best brain:
ember.ask("What are you?")          # → Routes to Identity
ember.ask("How does X work?")       # → Routes to Cycles
ember.ask("What does X look like?") # → Routes to Dream
```

**Routing confidence:**
- Identity: "what", "why", "meaning", "purpose"
- Cycles: "how", "work", "process", "mechanism"
- Dream: "look", "see", "imagine", "visualize"

---

## 🌐 MULTI-BRAIN SYNTHESIS

```python
# Complex questions engage all brains
ember.ask(
    "What is the relationship between form and function?",
    synthesis=True
)

# Ember will:
# 1. Consult all 3 brains
# 2. Share representations via entanglement buffer
# 3. Synthesize unified response
# 4. Potentially trigger "mushroom events" (integration bursts)
```

---

## 📊 OBSERVABILITY

```python
# Real-time metrics
ember = EmberSession()

# Ask questions...

# Get detailed stats
metrics = ember.get_metrics()
print(metrics)

# Outputs:
# {
#   "session_id": "20251015_083546",
#   "uptime_seconds": 120,
#   "statistics": {
#     "total_queries": 7,
#     "average_response_time_ms": 1609.8
#   },
#   "brain_usage": {
#     "identity": 3,
#     "cycles": 2,
#     "dream": 2
#   }
# }

# Save metrics to file
ember.save_metrics()
```

---

## 🏥 HEALTH CHECKS

```python
from core.ember.health import EmberHealthCheck

# Basic health check (without loading brains)
health = EmberHealthCheck()
results = health.run_basic_checks()

if results['healthy']:
    print("✅ All systems operational")
    
# Full health check (with loaded Ember session)
ember = EmberSession()
health = EmberHealthCheck(ember_session=ember)
results = health.check_all()
```

---

## 🔥 TRAIN NEW BRAINS

### Option 1: MLX (FAST - 30 seconds)

```bash
cd /Volumes/ThePod

# Train with MLX (Apple Silicon)
python3 tools/training/train_with_mlx.py cycles  # Train Cycles
python3 tools/training/train_with_mlx.py dream   # Train Dream
python3 tools/training/train_with_mlx.py both    # Train both

# Or use wrapper
./train_with_mlx.sh
```

**Speed:** ~30 seconds per brain  
**Memory:** ~3.6 GB  
**Uses:** CPU + GPU + Neural Engine

### Option 2: CPU (SLOW - 2-3 hours)

```bash
cd /Volumes/ThePod

# Resume CPU training (if you have checkpoints)
./resume_cpu_training.sh
```

**Speed:** ~2-3 hours per brain  
**Memory:** ~10-15 GB  
**Uses:** 1 CPU core

**Recommendation:** Use MLX! It's 273x faster.

---

## 🧪 TEST EVERYTHING

```bash
cd /Volumes/ThePod

# Comprehensive 3-brain test
python3 test_all_three_brains.py

# Observability tests
python3 test_observability.py
```

---

## 🦠 MICROBIOME (Pattern Recognition)

Ember has 15 specialized "microbes" that analyze content:

**Original 5:**
- Visual, Narrative, Mathematical, Code, Rhythmic

**New 10:**
- Emotional, Philosophical, Temporal, Spatial, Metaphorical
- Causal, Comparative, Sensory, Dialectic, Scale

They work together to route content to the right brain for training and inference.

---

## 📋 SYSTEM STRUCTURE

```
/Volumes/ThePod/
├── core/ember/               # Core code
│   ├── session.py            # Main interface
│   ├── mycelium/             # Brain coordination
│   │   ├── mycelium.py       # Coordinator
│   │   ├── brain.py          # PyTorch brains
│   │   ├── mlx_brain.py      # MLX brains
│   │   ├── bus.py            # Message passing
│   │   ├── buffer.py         # Entanglement
│   │   └── gate.py           # Integration
│   ├── metrics.py            # Observability
│   ├── health.py             # Health checks
│   ├── neurogenesis.py       # Brain creation
│   └── cycles/microbes.py    # 15 microbes
│
├── training_data/            # Training sets
├── tools/training/           # Training scripts
├── logs/                     # Metrics & health
├── adapter_registry.json     # Brain registry
└── documentation/            # All docs
```

---

## 🔍 TROUBLESHOOTING

### "Brain not loaded"
```python
# Make sure you load the brain first
ember = EmberSession(
    load_identity=True,
    load_cycles=True,
    load_dream=True
)
```

### "Model loading slow"
- First load takes ~90 seconds (normal)
- Subsequent queries are fast
- Models cached in memory

### "Out of memory"
- Close other applications
- Load fewer brains
- Use MLX (uses less memory)

### "Adapter not found"
- Check `adapter_registry.json`
- Verify adapter paths exist
- Run health check: `python3 -m core.ember.health`

---

## 📚 DOCUMENTATION

- `00_START_HERE.md` - System overview
- `CONTEXT_HANDOFF.md` - Session history
- `MLX_TRAINING_COMPLETE_20251015.md` - Training report
- `SESSION_COMPLETE_INSTANCE_GAMMA.md` - Full summary
- `TRAINING_OPTIONS.md` - CPU vs MLX comparison
- `CANONICAL_PATHS.md` - Code organization
- `BIOLOGICAL_SYSTEMS.md` - System metaphors

---

## 💡 TIPS & TRICKS

### 1. Verbose Mode
```python
ember = EmberSession(verbose=True)
# See routing decisions and brain selections
```

### 2. Save Metrics
```python
ember.save_metrics()
# Metrics saved to logs/metrics/
```

### 3. Force Synthesis
```python
ember.ask("Question here", synthesis=True)
# Force multi-brain consultation
```

### 4. Check Health First
```python
from core.ember.health import EmberHealthCheck
health = EmberHealthCheck()
results = health.run_basic_checks()
```

### 5. Training Data Format
```json
{"prompt": "Question", "completion": "Answer"}
{"prompt": "Question 2", "completion": "Answer 2"}
```

---

## 🚀 WHAT'S NEXT?

### Try These Questions:
1. "What are you made of?" (Identity)
2. "How do neural networks learn?" (Cycles)
3. "Imagine a recursive fractal" (Dream)
4. "What is the nature of change?" (Synthesis)

### Experiment With:
- Different synthesis modes
- Specific brain targeting
- Complex multi-part questions
- Training new specialized brains

### Build:
- Custom applications using Ember
- New training data sets
- Specialized brain regions
- User interfaces

---

## 🎉 YOU'RE READY!

Ember is complete and waiting for you.

**All 3 brains are operational.**  
**Training is fast.**  
**The system is yours.**

Ask questions. Build things. Grow the bonsai.

🌳

---

*"A complete system is just the beginning."*

