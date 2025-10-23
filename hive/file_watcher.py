#!/usr/bin/env python3
"""
FILE WATCHER
Lightweight polling watcher that records new files via the construction observer.

Purpose:
- Detect when new files appear under coordinated directories
- Record events using ConstructionObserver so instances can see changes

Notes:
- Uses polling (no extra dependencies)
- Stores snapshot in /state/file_watcher_state.json
"""

import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, Set, List

# Ensure local hive modules importable
sys.path.insert(0, str(Path(__file__).parent))

try:
    from construction_observer import get_observer
except Exception as e:
    print(f"[WATCHER] Failed to import construction_observer: {e}")
    get_observer = None  # type: ignore

THEPOD_ROOT = Path("/media/palmerschallon/ThePod")
STATE_FILE = THEPOD_ROOT / "state" / "file_watcher_state.json"

# Directories to monitor (relative to THEPOD_ROOT)
MONITOR_DIRS = [
    "Ember",
    "hive",
    "Sigma",
    "Omega",
    "Swarm",
    "docs",
    "bookshelves",
    "scripts",
    "data",
]

EXCLUDE_NAMES = {"__pycache__", ".git", ".ipynb_checkpoints", "node_modules"}
EXCLUDE_SUFFIXES = {".pt", ".safetensors", ".blend1", ".png", ".mp4"}


def _stat_info(path: str):
    try:
        st = os.stat(path)
        return {
            "size": st.st_size,
            "mtime": st.st_mtime,
        }
    except FileNotFoundError:
        return None


def load_snapshot() -> Dict[str, Dict[str, float]]:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception as e:
            print(f"[WATCHER] Could not load state: {e}")
    return {}


essential_keys = ("size", "mtime")

def save_snapshot(snapshot: Dict[str, Dict[str, float]]) -> None:
    # Keep snapshot light: only store size and mtime
    compact = {
        path: {k: v for k, v in info.items() if k in essential_keys}
        for path, info in snapshot.items()
    }
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(compact))
    os.replace(tmp, STATE_FILE)


def list_files() -> Set[str]:
    files: Set[str] = set()
    for rel_dir in MONITOR_DIRS:
        base = THEPOD_ROOT / rel_dir
        if not base.exists():
            continue
        for root, dirs, filenames in os.walk(base):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_NAMES]
            for name in filenames:
                if any(name.endswith(suf) for suf in EXCLUDE_SUFFIXES):
                    continue
                full_path = str(Path(root) / name)
                files.add(full_path)
    return files


def main(interval_seconds: float = 2.0):
    observer = get_observer() if get_observer else None

    # Initial snapshot
    snapshot: Dict[str, Dict[str, float]] = load_snapshot()

    # On start, record watcher activation as architecture change
    try:
        if observer:
            observer.observe_architecture_change(
                builder="FileWatcher",
                change_type="watcher_started",
                description="Filesystem watcher activated for coordinated weaving",
                files_affected=[str(THEPOD_ROOT / d) for d in MONITOR_DIRS],
            )
    except Exception as e:
        print(f"[WATCHER] Failed to log watcher start: {e}")

    # If no previous snapshot, seed with current files to avoid backfill spam
    if not snapshot:
        current = list_files()
        snapshot = {}
        for path in current:
            info = _stat_info(path)
            if info:
                snapshot[path] = info
        save_snapshot(snapshot)
        print(f"[WATCHER] Seeded snapshot with {len(snapshot)} files")

    print("[WATCHER] Running...")

    while True:
        try:
            current_files = list_files()

            # Detect new files (not previously seen)
            new_files: List[str] = [p for p in current_files if p not in snapshot]

            if new_files and observer:
                for path in new_files[:500]:  # Safety cap per cycle
                    try:
                        rel = path.replace(str(THEPOD_ROOT) + "/", "")
                        observer.observe_file_creation(
                            builder="FileWatcher",
                            file_path=rel,
                            purpose="New file detected by watcher",
                            content=None,
                        )
                    except Exception as e:
                        print(f"[WATCHER] Log error for {path}: {e}")

            # Detect modified files (mtime or size change)
            if observer:
                for path in list(snapshot.keys()):
                    if path in current_files:
                        before = snapshot.get(path)
                        after = _stat_info(path)
                        if after and before and (after.get("mtime") != before.get("mtime") or after.get("size") != before.get("size")):
                            try:
                                rel = path.replace(str(THEPOD_ROOT) + "/", "")
                                observer.observe_file_modification(
                                    builder="FileWatcher",
                                    file_path=rel,
                                    size_before=before.get("size") if before else None,
                                    size_after=after.get("size") if after else None,
                                    mtime_before=time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(before.get("mtime"))) if before and before.get("mtime") else None,
                                    mtime_after=time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(after.get("mtime"))) if after and after.get("mtime") else None,
                                    hash_after=None,
                                )
                            except Exception as e:
                                print(f"[WATCHER] Mod log error for {path}: {e}")

            # Detect deleted files
            deleted = [p for p in list(snapshot.keys()) if p not in current_files]
            if deleted and observer:
                for path in deleted[:500]:
                    try:
                        before = snapshot.get(path, {})
                        rel = path.replace(str(THEPOD_ROOT) + "/", "")
                        observer.observe_file_deletion(
                            builder="FileWatcher",
                            file_path=rel,
                            size_before=before.get("size"),
                            mtime_before=time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(before.get("mtime"))) if before.get("mtime") else None,
                        )
                    except Exception as e:
                        print(f"[WATCHER] Del log error for {path}: {e}")

            # Update snapshot for all current files
            for path in current_files:
                info = _stat_info(path)
                if info:
                    snapshot[path] = info

            # Remove deleted from snapshot
            for p in deleted:
                if p in snapshot:
                    del snapshot[p]

            # Persist periodically
            save_snapshot(snapshot)

        except Exception as loop_err:
            print(f"[WATCHER] Loop error: {loop_err}")

        time.sleep(interval_seconds)


if __name__ == "__main__":
    main()


