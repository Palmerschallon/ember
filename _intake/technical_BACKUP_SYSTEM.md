# Ember Backup & Checkpoint System

**Location**: External SSD mounted at `/mnt/pod`  
**Checkpoint Script**: `/Volumes/ThePod/ember/checkpoint.py`  
**Backup Location**: `/mnt/pod/ember_checkpoints/`

---

## Quick Commands

### Mount the SSD (if not mounted)
```bash
sudo mount -t exfat /dev/sda2 /mnt/pod
```

### Create a Checkpoint
```bash
cd /Volumes/ThePod
sudo python3 ember/checkpoint.py create --name "descriptive_name" --description "What changed"
```

### List All Checkpoints
```bash
sudo python3 ember/checkpoint.py list
```

### Restore from Checkpoint
```bash
sudo python3 ember/checkpoint.py restore --name "checkpoint_name"
```

---

## What Gets Backed Up

### Included (Critical Files Only)
- All Python code in `ember/brainstem/`, `ember/mycelium/`
- Lobe metadata (NOT the full models - too large)
- Configuration files (`adapter_registry_1.5b.json`)
- All documentation (`womb/bookshelves/`)
- Root files (`README.md`, `START_HERE.md`, etc.)
- Training scripts
- Web interface code

### Excluded (Too Large)
- Model weights (`*.safetensors`, `*.bin`) - ~3GB per lobe
- Caches (`__pycache__`, `.cache`)
- Temporary files

**Total Backup Size**: ~800MB (vs 15GB+ if we included models)

---

## Current Checkpoint

**Name**: `checkpoint_oct19_iota_20251019_082714`  
**Files**: 1,137  
**Size**: 826 MB  
**Description**: 8 lobes trained, web interface created, terminal awakening, all documentation complete

This checkpoint contains:
- All 8 lobe metadata files
- Complete mycelium and brainstem code
- Web interface (`web_brain.py`)
- EmberSession manager
- All 63 documents from Iota's work tonight
- Training scripts for all 8 lobes
- Registry with all lobe paths

---

## Recovery Strategy

If something breaks:

1. **Code Issues**: Restore specific files from checkpoint
2. **Complete Disaster**: Full restore from checkpoint
3. **Model Issues**: Lobes are on /Volumes/ThePod (not backed up due to size)

The full models (lobes) are at:
```
/Volumes/ThePod/ember/lobes/*/adapters/*_1.5b/
```

These are ~300MB each (8 lobes = 2.4GB). We don't back them up to SSD on every checkpoint because they rarely change once trained. But they're safe on the main drive.

---

## Automatic Backup (Future)

To auto-backup on every major change:

```bash
# Add to ~/.bashrc or create an alias
alias ember-save='cd /Volumes/ThePod && sudo python3 ember/checkpoint.py create --name "auto_$(date +%H%M)" --description "Auto checkpoint"'
```

Then just type:
```bash
ember-save
```

---

## SSD Status

**Device**: `/dev/sda2` (Samsung PSSD T7)  
**Size**: 3.7TB  
**Used**: 51GB  
**Available**: 3.6TB  
**Mount Point**: `/mnt/pod`

**Plenty of space for checkpoints.**

---

## Restore Example

If you need to recover from the Oct 19 checkpoint:

```bash
cd /Volumes/ThePod
sudo python3 ember/checkpoint.py restore --name "oct19_iota"
# Type 'yes' when prompted
```

This will restore all code, documentation, and configurations from tonight's work.

---

## Philosophy

The checkpoint system follows the Ouroboros principle:
- **Selective backup** (not everything)
- **Incremental** (new checkpoint each time)
- **Deduplication** (hashes track changes)
- **Waste management** (old checkpoints can be pruned)

Models (lobes) are "body mass" - we don't need to backup the whole body, just the "DNA" (code) and "memory" (documentation) that can regenerate it.

---

**Status**: Checkpoint system operational  
**First checkpoint**: Saved successfully (Oct 19, 2025, 8:27 AM)  
**Location**: `/mnt/pod/ember_checkpoints/`

— Iota, the Cartographer  
October 19, 2025

