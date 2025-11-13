# FILE WATCHER & CONSTRUCTION LOG: DIAGNOSIS & FIX

## Problem 1: Hardcoded Path in file_watcher.py

**Line 31:**
```python
THEPOD_ROOT = Path("/media/palmerschallon/ThePod")
```

Should be:
```python
THEPOD_ROOT = Path("/media/palmerschallon/ThePod1")
```

**This causes:**
- FileWatcher to monitor WRONG directory
- Likely found nothing, then kept re-initializing
- Each initialization logged "watcher_started" event
- Created endless loop of restarts

## Problem 2: No Deduplication Logic

**Lines 154-173:** File modification detection runs on EVERY file in snapshot, EVERY cycle (2 seconds)

Even if mtime/size unchanged, the comparison happens repeatedly. The bug is subtle:

```python
if after and before and (after.get("mtime") != before.get("mtime") or ...):
```

If filesystem timestamps have sub-second precision but Python comparison doesn't handle it properly, OR if the state file isn't saving properly due to wrong path, it will keep thinking files changed.

## Problem 3: Snapshot State File in Wrong Location

**Line 32:**
```python
STATE_FILE = THEPOD_ROOT / "state" / "file_watcher_state.json"
```

With wrong THEPOD_ROOT, this is:
`/media/palmerschallon/ThePod/state/file_watcher_state.json`

But that directory might not exist! So:
- Snapshot never saves properly
- Every cycle thinks ALL files are new
- Logs them all again
- 800K line explosion

## The Loom Problem

The "Loom" that was spamming "think:auto" is NOT in the hive code - it's likely an external GPT-5 instance that was running via some API interface or autonomous agent script. Without seeing that code, I can't fix it directly, but the pattern suggests it was in a tight loop without rate limiting.

---

## THE FIX

Creating a corrected version of file_watcher.py...

