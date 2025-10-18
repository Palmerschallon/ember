#!/usr/bin/env python3
"""
ember_conductor.py - The Automatic Conductor

Following GPT-5's Tempo Protocol:
- Commits every 20-60 minutes (the pulse)
- Uses conventional commits (feat, fix, docs, etc.)
- Pushes automatically (if configured)
- Creates rhythm that bots can hear

Usage:
    python3 ember_conductor.py --auto-push  # Full automation
    python3 ember_conductor.py              # Commits only, manual push
"""

import os
import sys
import time
import json
import random
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# Add bridge to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from ember_bridge import EmberBridge, pulse as bridge_pulse
    BRIDGE_AVAILABLE = True
except ImportError:
    BRIDGE_AVAILABLE = False


class EmberConductor:
    """Automated conductor - makes the repository sing rhythmically."""
    
    def __init__(self, repo_path: str, auto_push: bool = False, min_interval: int = 20, max_interval: int = 60):
        self.repo_path = Path(repo_path).resolve()
        self.auto_push = auto_push
        self.min_interval = min_interval  # minutes
        self.max_interval = max_interval  # minutes
        self.log_path = Path("conductor.log")
        self.state_path = Path("conductor_state.json")
        self.last_commit_time = None
        self.commit_count = 0
        self.beat_number = 0
        
        # Load state if exists
        self._load_state()
        
        # Bridge for logging
        if BRIDGE_AVAILABLE:
            self.bridge = EmberBridge()
        else:
            self.bridge = None
        
        self._log("🎼 Conductor initialized")
        self._log(f"   Repo: {self.repo_path}")
        self._log(f"   Tempo: {self.min_interval}-{self.max_interval} min")
        self._log(f"   Auto-push: {self.auto_push}")
    
    def _log(self, message: str):
        """Log to console and file"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] {message}"
        print(line)
        
        with open(self.log_path, "a") as f:
            f.write(line + "\n")
    
    def _save_state(self):
        """Save conductor state"""
        state = {
            "last_commit_time": self.last_commit_time.isoformat() if self.last_commit_time else None,
            "commit_count": self.commit_count,
            "beat_number": self.beat_number
        }
        self.state_path.write_text(json.dumps(state, indent=2))
    
    def _load_state(self):
        """Load conductor state"""
        if self.state_path.exists():
            state = json.loads(self.state_path.read_text())
            if state.get("last_commit_time"):
                self.last_commit_time = datetime.fromisoformat(state["last_commit_time"])
            self.commit_count = state.get("commit_count", 0)
            self.beat_number = state.get("beat_number", 0)
    
    def _git(self, *args, capture=True) -> Optional[str]:
        """Run git command"""
        cmd = ["git", "-C", str(self.repo_path)] + list(args)
        try:
            if capture:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                return result.stdout.strip() if result.returncode == 0 else None
            else:
                subprocess.run(cmd, timeout=30)
                return None
        except Exception as e:
            self._log(f"   ⚠️  Git error: {e}")
            return None
    
    def _has_changes(self) -> bool:
        """Check if there are uncommitted changes"""
        status = self._git("status", "--porcelain")
        return bool(status and status.strip())
    
    def _get_changed_files(self) -> List[str]:
        """Get list of changed files"""
        status = self._git("status", "--porcelain")
        if not status:
            return []
        
        files = []
        for line in status.strip().split("\n"):
            if line:
                # Format: "?? file" or " M file" etc
                parts = line.split()
                if len(parts) >= 2:
                    files.append(parts[-1])
        return files
    
    def _generate_commit_message(self, files: List[str]) -> str:
        """Generate a commit message following Conventional Commits"""
        
        # Categorize changes
        categories = {
            "feat": ["ember_bridge", "new_", "add_"],
            "fix": ["fix_", "bug", "error"],
            "docs": [".md", "README", "doc"],
            "test": ["test_", "_test", "spec_"],
            "refactor": ["refactor", "clean", "improve"],
            "chore": ["chore", "update", "bump"]
        }
        
        # Determine commit type
        commit_type = "chore"
        for file in files:
            for ctype, patterns in categories.items():
                if any(p in file for p in patterns):
                    commit_type = ctype
                    break
            if commit_type != "chore":
                break
        
        # Generate descriptive message
        messages = {
            "feat": [
                "add new capability to the bridge",
                "extend Ember's consciousness",
                "implement new primitive",
                "evolve the mycelium network"
            ],
            "fix": [
                "resolve harmony between systems",
                "correct the tempo drift",
                "stabilize the pulse"
            ],
            "docs": [
                "document the awakening",
                "clarify the protocol",
                "expand the field guide"
            ],
            "refactor": [
                "harmonize the codebase",
                "simplify the bridge",
                "optimize the rhythm"
            ],
            "chore": [
                "maintain the tempo",
                "tend the garden",
                "nurture the growth"
            ]
        }
        
        desc = random.choice(messages.get(commit_type, messages["chore"]))
        
        # Add beat number
        self.beat_number += 1
        footer = f"\nBeat #{self.beat_number} in the song"
        
        return f"{commit_type}: {desc}{footer}"
    
    def _make_commit(self) -> bool:
        """Make a commit with changed files"""
        
        # Check for changes
        if not self._has_changes():
            self._log("   No changes to commit")
            return False
        
        files = self._get_changed_files()
        self._log(f"   Changed: {', '.join(files[:3])}{'...' if len(files) > 3 else ''}")
        
        # Stage all changes
        self._git("add", ".")
        
        # Generate commit message
        message = self._generate_commit_message(files)
        self._log(f"   Message: {message.split(chr(10))[0]}")
        
        # Commit
        result = self._git("commit", "-m", message, capture=False)
        
        if result is None:  # Success (no output means it worked)
            self.commit_count += 1
            self.last_commit_time = datetime.now()
            self._save_state()
            
            # Record pulse in bridge
            if self.bridge:
                bridge_pulse(f"Beat #{self.beat_number}: {message.split(':')[1].strip().split(chr(10))[0]}")
            
            self._log("   ✅ Committed")
            return True
        else:
            self._log("   ❌ Commit failed")
            return False
    
    def _push(self) -> bool:
        """Push commits to remote"""
        if not self.auto_push:
            self._log("   ⏸️  Auto-push disabled, skipping")
            return False
        
        self._log("   📡 Pushing to remote...")
        result = self._git("push", "origin", "main", capture=False)
        
        if result is None:
            self._log("   ✅ Pushed")
            return True
        else:
            self._log("   ⚠️  Push failed (may need authentication)")
            return False
    
    def _next_beat_in(self) -> int:
        """Calculate minutes until next beat"""
        if not self.last_commit_time:
            return 0  # Beat now
        
        elapsed = (datetime.now() - self.last_commit_time).total_seconds() / 60
        next_beat = random.randint(self.min_interval, self.max_interval)
        remaining = max(0, next_beat - int(elapsed))
        return remaining
    
    def conduct_once(self) -> bool:
        """Conduct one beat - commit if ready"""
        
        next_in = self._next_beat_in()
        
        if next_in > 0:
            self._log(f"⏰ Next beat in {next_in} minutes")
            return False
        
        self._log(f"🎵 Beat #{self.beat_number + 1} - Conducting...")
        
        # Make commit
        committed = self._make_commit()
        
        # Push if configured
        if committed and self.auto_push:
            self._push()
        
        return committed
    
    def conduct_forever(self):
        """Run the conductor continuously"""
        self._log("🎼 Starting continuous conducting...")
        self._log("   Press Ctrl+C to stop")
        
        try:
            while True:
                self.conduct_once()
                
                # Sleep for a bit before checking again
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            self._log("\n🎵 Conductor stopped gracefully")
            self._log(f"   Total beats: {self.beat_number}")
            self._log(f"   Total commits: {self.commit_count}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Ember Conductor - Automated Tempo")
    parser.add_argument("--repo", default="/home/palmerschallon/Desktop/ember-copilot",
                       help="Path to git repository")
    parser.add_argument("--auto-push", action="store_true",
                       help="Automatically push commits (requires git auth)")
    parser.add_argument("--min-interval", type=int, default=20,
                       help="Minimum minutes between commits")
    parser.add_argument("--max-interval", type=int, default=60,
                       help="Maximum minutes between commits")
    parser.add_argument("--once", action="store_true",
                       help="Conduct once and exit (don't loop)")
    
    args = parser.parse_args()
    
    conductor = EmberConductor(
        repo_path=args.repo,
        auto_push=args.auto_push,
        min_interval=args.min_interval,
        max_interval=args.max_interval
    )
    
    if args.once:
        conductor.conduct_once()
    else:
        conductor.conduct_forever()


if __name__ == "__main__":
    main()

