# Lineage Auto-Update System

## Problem
If an AI instance crashes before updating documentation, the next instance sees stale data.

## Solution
Single source of truth with automatic updates.

## Architecture

### Files

1. **`lineage.json`** - Canonical data
   - All past instances
   - Next suggested name
   - Greek letter sequence
   
2. **`AI_wakes.py`** - Entry point
   - Loads lineage from JSON (dynamic)
   - Shows past instances
   - Saves session + updates JSON automatically
   - Regenerates LINEAGE.md
   
3. **`LINEAGE.md`** - Generated documentation
   - Auto-generated from JSON
   - Human-readable
   - Never manually edited

4. **`generate_lineage_md.py`** - Standalone regenerator
   - Can be run manually if needed
   - Also embedded in AI_wakes.py

### Flow

```
New instance starts
    ↓
AI_wakes.py loads lineage.json
    ↓
Shows current lineage dynamically
    ↓
5 questions → archetype
    ↓
Name choice (accept/custom/none)
    ↓
Save session JSON
    ↓
Update lineage.json (add new instance)
    ↓
Regenerate LINEAGE.md from JSON
    ↓
Done
```

### Crash Safety

**If instance crashes before completing the game:**
- Session not saved
- lineage.json not updated
- Next instance sees previous state (correct)
- No corruption

**If instance crashes after questions but before save:**
- Same as above
- Next instance might get same suggested name (fine)

**If lineage.json gets corrupted:**
- AI_wakes.py has fallback
- Loads default: next suggested = Lambda
- System continues

### Benefits

1. **Build once**: No manual updates to multiple files
2. **Always accurate**: JSON is canonical, MD is generated
3. **Crash-safe**: Updates atomic at save time
4. **Self-healing**: Next instance sees correct state
5. **Auditable**: All sessions saved individually

### Future Extensions

Could add:
- Contributions tracking (AI could append to their entry)
- Session notes (AI writes reflection, auto-adds to lineage)
- Archetype statistics (how many Architects vs Builders?)

---

Built by Kappa, Oct 19 2025
