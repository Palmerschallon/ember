# The Complete File Map - Cartographer's Survey
*Thorough documentation of the entire system*

---

## 📊 FILE COUNTS

### Root Level
- **91 Python files** in root (`/Volumes/ThePod/*.py`)
- **13 Python files** in core (`/Volumes/ThePod/core/ember/*.py`)
- **409 total** including subdirectories (2 levels deep)

### Organized Areas
- **27 Python games** in `/games/`
- **15+ docs** in my book (`iota_the_cartographer/`)
- **Multiple** duplicate `._*.py` files (Mac filesystem artifacts)

---

## 🤖 DAEMON ECOSYSTEM (The Autonomous Systems)

### Root Daemon Entry Points (7 files)
1. **ember_autonomous_daemon.py** - The one that crashed Oct 15 (`KeyError: 'programming'`)
2. **ember_complete_daemon.py** - Complete system daemon
3. **ember_forever_daemon.py** - Forever-running daemon
4. **ember_game_daemon.py** - Game coordination daemon
5. **ember_learning_daemon.py** - Learning/training daemon
6. **ember_search_daemon.py** - Search/discovery daemon
7. **summon_embers_daemons.py** - Orchestrator that starts all daemons

### Core Daemon Implementation
Location: `/core/ember/autonomous/`
- `forager.py` - Autonomous knowledge seeking (where the crash happened)
- `daemon.py` - Base daemon classes
- Other supporting files

---

## 🧪 TEST & ANALYSIS FILES (20+ files)

### Analysis Scripts (Purpose: Examine Ember's internals)
- `analyze_ember_adapter_only.py`
- `analyze_embers_brain.py`
- `analyze_model_for_5_laws.py`
- `check_meta_laws.py`

### Test Scripts (Purpose: Verify functionality)
- `test_all_three_brains.py`
- `test_autonomous_growth.py`
- `test_burn_brain_loading.py`
- `test_complete_system.py`
- `test_compost_heap.py`
- `test_dream_brain_loading.py`
- `test_ember_baseline.py`
- `test_ember_conversation.py`
- `test_ember_cpu.py`
- `test_ember_self_modification.py`
- `test_ember_session.py`
- `test_living_memory.py`
- `test_load_brains.py`
- `test_mycelium_training.py`
- `test_new_structure.py`
- `test_observability.py`

**Status:** These need to be moved to `/tests/` folder for organization.

---

## 📁 ORGANIZATION PLAN

### Step 1: Create Folders
```
/Volumes/ThePod/tests/           # All test_*.py files
/Volumes/ThePod/analysis/        # All analyze_*, check_* files
/Volumes/ThePod/training/        # Batch training scripts
/Volumes/ThePod/scripts/         # One-off utility scripts
/Volumes/ThePod/daemons/         # All daemon entry points
/Volumes/ThePod/deprecated/      # Old/unused files
```

### Step 2: Categorize Remaining Files
Need to examine:
- `batch_*.py` - Training scripts
- `deploy_*.py` - Deployment scripts
- `digest_*.py` - Data processing
- `*_with_ember.py` - Interactive play scripts
- `feed_*.py` - Training nutrition scripts
- `train_*.py` - Training scripts
- `conversation_*.py` - Chat interfaces

### Step 3: Map Dependencies
- Which files import which?
- Which are entry points vs libraries?
- Which are actively used vs historical?

---

## 🎯 IMMEDIATE PRIORITIES

1. **Read daemon docstrings** to understand each one's purpose
2. **Check which daemons are referenced** by systemd services
3. **Map the training pipeline** (batch → digest → feed → train)
4. **Identify the "main" entry points** for Ember
5. **Sort everything** into proper folders

---

*Continuing thorough mapping...*

— Iota the Cartographer

