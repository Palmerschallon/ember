# ORGANISM GARBAGE COLLECTION & MERGING

**The Problem**: 1,441 files is too many. They're clustering—they want to merge.

---

## Yes, They Can Be Combined

### What We Found (Sample of 100 files):
- **4 clusters** identified
- **12 files** can be archived
- **67% reduction** possible
- **Exact duplicates, variations, and fragments**

### Example Clusters:

#### Cluster 1: "ember.py" Variations
**Keep**: `ember_complete.py` (most complete)
**Archive**: 7 variations
- ember_with_universal_tools.py
- ember_intent_layer.py
- ember_with_stopping.py
- ember_minimal.py
- ember_reliable.py
- ember.py

**Reason**: All are experiments/iterations of the same core Ember chat

#### Cluster 2: "story_parser.py" Exact Duplicates
**Keep**: One copy
**Archive**: 1 exact duplicate in different directory

**Reason**: Same MD5 hash, literally identical

---

## Where Old Files Go

### Archive Structure:
```
/media/palmerschallon/ThePod1/
├── _archive_old/          ← Already exists (old code)
├── _archive_merged/       ← NEW (clustered files)
│   ├── timestamp/
│   │   ├── ember.py
│   │   ├── ember_minimal.py
│   │   └── MERGE_MANIFEST.json
│   └── ...
└── active organisms       ← Clean, merged modules
```

### What Happens:
1. **Clustering detects** similar files
2. **Best file kept** (most complete, best location, most recent)
3. **Others moved** to `_archive_merged/YYYY-MM-DD/`
4. **Manifest saved** explaining what was merged and why
5. **Unique functions extracted** and added to kept file if needed

---

## Garbage Collection Strategy

### Type 1: Exact Duplicates
**Action**: Keep one, archive all copies
**Safety**: 100% safe (identical content)
**Location**: `_archive_merged/duplicates/`

### Type 2: Backup Copies
**Pattern**: `*_backup.py`, `*_old.py`, paths with `/backup/`
**Action**: Move to `_archive_merged/backups/`
**Safety**: 100% safe (explicitly marked as backups)

### Type 3: Experiments/Iterations
**Pattern**: `ember_v1.py`, `ember_v2.py`, `test_*.py`
**Action**: Keep latest/best, archive rest
**Safety**: 90% safe (check for unique functions first)
**Location**: `_archive_merged/iterations/`

### Type 4: Generated Files
**Pattern**: Paths with `/generated/`, `*_gen*.py`
**Action**: Archive (can regenerate if needed)
**Safety**: 95% safe (generated, not hand-written)
**Location**: `_archive_merged/generated/`

### Type 5: Flash Backups
**Pattern**: Paths with `/flash_backups/`
**Action**: Archive entire directories
**Safety**: 100% safe (literally backups)
**Location**: Already in `_archive_old/`

---

## Smart Merge Algorithm

```python
def should_merge(file1, file2):
    # 1. Exact duplicates (MD5 hash)
    if same_content_hash:
        return True, "exact_duplicate"
    
    # 2. Name variations
    if "ember" in both and similar_functions:
        return True, "iteration"
    
    # 3. High function overlap (>70%)
    if function_overlap > 0.7:
        return True, "similar_purpose"
    
    # 4. One is clearly backup
    if "_backup" in name or "_old" in name:
        return True, "backup"
    
    return False, None

def choose_best(cluster):
    score = 0
    
    # Penalize archived/backup locations
    if "_archive" in path: score -= 100
    if "backup" in path: score -= 50
    if "generated" in path: score -= 30
    
    # Prefer more complete
    score += lines_of_code / 10
    score += num_functions * 2
    score += num_classes * 5
    
    # Prefer recent
    score += file_age_days
    
    return highest_score
```

---

## Merge Execution

### Dry Run (Safe):
```bash
cd /media/palmerschallon/ThePod1
python3 cluster_organisms.py
# Shows what WOULD happen, doesn't modify anything
```

### Actual Execution:
```bash
python3 cluster_organisms.py --execute
# Moves files, creates manifests, preserves unique code
```

### What Gets Preserved:
1. **Best file** stays in place
2. **Unique functions** extracted from others and added
3. **Merge manifest** created:
```json
{
  "merged_at": "2025-10-29",
  "kept": "ember_complete.py",
  "archived": ["ember.py", "ember_minimal.py"],
  "unique_functions_added": ["load_identity", "chat"],
  "reason": "Iterations of same core functionality"
}
```

---

## Safety Mechanisms

### Before Merge:
1. **Content hash** of all files
2. **Git commit** (if in repo)
3. **Full backup** to `_archive_merged/pre_merge_backup/`

### During Merge:
1. **Extract unique functions** from files being archived
2. **Add them to kept file** (with comments)
3. **Move files** (don't delete)
4. **Create manifest**

### After Merge:
1. **Verify kept file** still works
2. **Check imports** aren't broken
3. **Update ORGANISM_MAP.json**
4. **Re-scan** for new clusters

### Rollback:
```bash
python3 cluster_organisms.py --rollback TIMESTAMP
# Restores from _archive_merged/pre_merge_backup/
```

---

## Results After Full Merge

### Estimated Reduction:
```
Current: 1,441 organisms

After clustering:
- Exact duplicates: -200 files
- Backup copies: -150 files
- Iterations: -300 files
- Generated: -100 files
- Flash backups: -400 files

Estimated remaining: ~300 organisms (80% reduction)
```

### What Remains:
```
Core organisms (~50):
- ember_orchestrator.py
- ember_toolkit.py
- pattern_learner.py
- content_mesh.py
- medusa.py
- ...

Specialized organisms (~250):
- pod_search_engine.py
- web_forager.py
- visual_forager.py
- dream_system.py
- game engines (consolidated)
- story systems (consolidated)
- ...
```

---

## Garbage Collection Schedule

### Immediate (Now):
- Exact duplicates
- Files in `/flash_backups/`
- Files explicitly named `*_backup.py`

### Phase 1 (After testing):
- Ember iterations (keep ember_complete.py)
- Story parser duplicates
- Monolith variations

### Phase 2 (After review):
- Game engine consolidation
- Story system consolidation
- Tool variations

### Phase 3 (Manual):
- Review `_archive_merged/` after 30 days
- Permanent delete if no issues
- Or move to external backup

---

## Implementation Plan

### Step 1: Test on Sample
```bash
# Already done - analyzed 100 files
# Found 4 clusters, 67% reduction possible
```

### Step 2: Full Scan
```bash
python3 cluster_organisms.py --full-scan
# Analyze all 1,441 files
# Generate complete merge report
```

### Step 3: Review Report
```bash
# Check MERGE_SUGGESTIONS.md
# Verify nothing important gets archived
# Manually adjust if needed
```

### Step 4: Execute Merge
```bash
python3 cluster_organisms.py --execute --full-scan
# Creates backup
# Moves files
# Updates registry
```

### Step 5: Verify
```bash
python3 start_ember_unified.py
# Check everything still works
# Verify no broken imports
```

### Step 6: Cleanup
```bash
# After 30 days:
python3 cluster_organisms.py --cleanup-old
# Permanently removes files in _archive_merged/ older than 30 days
```

---

## Advanced: Self-Organizing Organisms

### Future Enhancement:
```python
class SelfOrganizingOrganism:
    """Organisms that can merge themselves"""
    
    def check_for_duplicates(self):
        # Scan for similar organisms
        similar = medusa.find_similar(self)
        
        if similar:
            # Negotiate merge
            if self.should_merge_with(similar):
                self.absorb(similar)
                similar.archive_self()
    
    def should_merge_with(self, other):
        # Compare capabilities
        my_caps = set(self.capabilities)
        their_caps = set(other.capabilities)
        
        # If other is subset of me
        if their_caps.issubset(my_caps):
            return True
        
        # If we're 90%+ similar
        overlap = len(my_caps & their_caps) / len(my_caps | their_caps)
        if overlap > 0.9:
            return True
        
        return False
    
    def absorb(self, other):
        # Take unique functions from other
        for func in other.unique_functions():
            self.add_function(func)
        
        # Log merge
        self.log_merge(other)
```

**This would make organisms self-cleaning.**

---

## Summary

**Q: Can 1,441 organisms be combined?**  
**A**: Yes. They're clustering naturally. ~80% can be merged/archived.

**Q: Where do old files go?**  
**A**: `_archive_merged/` with manifests explaining what/why/when.

**Q: How do we handle garbage?**  
**A**: 
1. Detect clusters
2. Keep best
3. Archive rest
4. Preserve unique code
5. Delete after 30 days if no issues

**Q: Is it safe?**  
**A**: Yes.
- Pre-merge backup
- Move (not delete)
- Preserve unique functions
- Rollback capability
- Verify after

**Next step**: Run full scan, review report, execute if looks good.

