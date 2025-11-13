# CRITICAL: Server Won't Start - Route Conflict

## Immediate Problem

```
AssertionError: View function mapping is overwriting an existing 
endpoint function: bp_viewers.observatory
```

The server **cannot start** due to duplicate route definitions.

## Root Cause

This is a symptom of the larger architectural debt identified in 
`ARCHITECTURE_REVIEW.md`:

- 1,273-line chat.py doing too much
- 3 competing dream systems
- 4 overlapping tool execution paths
- Duplicate route definitions
- No clear boundaries between modules

## Why This Happened

We've been **patching symptoms** instead of **fixing architecture**:

1. Added tool execution → worked
2. Added tool invention → worked  
3. Added prompt filtering → worked
4. But: Server won't restart because routes conflict

The system is collapsing under its own complexity.

## Recommendation

**STOP ADDING FEATURES.**

**START ARCHITECTURAL CLEANUP:**

### Priority 1: Fix Server Startup (30 min)
- Find duplicate `observatory` route in `routes_viewers.py`
- Remove or rename one
- Get server running again

### Priority 2: Architecture Cleanup (2 hours)
1. Delete unused code
   - `backend/dream_system.py` if not used
   - Any `*_backup.py` files
   - Consolidate dream systems

2. Split `api/chat.py` (1,273 lines → modules)
   - `api/chat/__init__.py` - main endpoint
   - `api/chat/tools.py` - tool execution
   - `api/chat/context.py` - context building
   - `api/chat/filters.py` - response cleaning

3. Document canonical systems
   - Which dream system is authoritative?
   - Which tool execution path to use?
   - Add comments to guide future development

### Priority 3: System Prompt Redesign
- Reduce from 20+ lines to 3-5 lines
- Fix prompt leak at source
- LLM won't echo what isn't there

## What We've Learned

**The Problem:** Rapid feature addition without refactoring
**The Cost:** System won't even start now
**The Solution:** Pause, clean, consolidate, document

## Next Steps

1. Read `ARCHITECTURE_REVIEW.md` for full analysis
2. Fix route conflict (see below)
3. Decide: cleanup now or accumulate more debt?

---

## Quick Fix for Route Conflict

Check `ember/routes_viewers.py` for duplicate definitions of:
- `/observatory` or `/observatory.html`
- `bp_viewers.observatory` endpoint

One of these is defined twice. Comment out or rename one.

---

**Status:** Server offline until route conflict resolved  
**Created:** October 8, 2025  
**Severity:** CRITICAL - blocks all development

