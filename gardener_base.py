#!/usr/bin/env python3
"""
Gardener Base Class - Error-Resistant Foundation
Handles timeouts, retries, skip-on-fail, graceful error logging
All gardeners inherit from this to ensure resilience
"""

import os
import sys
import json
import asyncio
import traceback
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Add Pod to path for Ember imports
sys.path.insert(0, '/media/palmerschallon/ThePod1')

class ResilientGardener:
    """Base class for all Pod Gardeners with built-in error resistance"""

    def __init__(self, gardener_name, pod_root='/media/palmerschallon/ThePod1'):
        self.gardener_name = gardener_name
        self.pod_root = Path(pod_root)
        self.logs_dir = self.pod_root / 'logs'
        self.logs_dir.mkdir(exist_ok=True)

        # Error tracking
        self.error_log = self.logs_dir / f'{gardener_name}_errors.json'
        self.errors = self.load_errors()

        # Stats
        self.stats = {
            'tasks_attempted': 0,
            'tasks_completed': 0,
            'tasks_failed': 0,
            'tasks_skipped': 0,
            'session_start': datetime.now().isoformat()
        }

        # Configuration
        self.MAX_RETRIES = 3
        self.TASK_TIMEOUT = 120  # 2 minutes per task max
        self.SKIP_ON_REPEATED_FAILURE = True

    def load_errors(self):
        """Load error history to avoid repeating failures"""
        if self.error_log.exists():
            try:
                with open(self.error_log, 'r') as f:
                    return json.load(f)
            except:
                return defaultdict(int)
        return defaultdict(int)

    def save_errors(self):
        """Save error history"""
        with open(self.error_log, 'w') as f:
            json.dump(dict(self.errors), f, indent=2)

    def should_skip_task(self, task_id):
        """Check if we've failed this task too many times"""
        if not self.SKIP_ON_REPEATED_FAILURE:
            return False
        return self.errors.get(task_id, 0) >= self.MAX_RETRIES

    def log_error(self, task_id, error):
        """Log an error and track failure count"""
        self.errors[task_id] = self.errors.get(task_id, 0) + 1
        self.save_errors()

        error_entry = {
            'task_id': task_id,
            'gardener': self.gardener_name,
            'error': str(error),
            'traceback': traceback.format_exc(),
            'timestamp': datetime.now().isoformat(),
            'failure_count': self.errors[task_id]
        }

        error_file = self.logs_dir / f'{self.gardener_name}_error_details.log'
        with open(error_file, 'a') as f:
            f.write(json.dumps(error_entry) + '\n')

    def log_success(self, task_id):
        """Clear error count on success"""
        if task_id in self.errors:
            del self.errors[task_id]
            self.save_errors()

    async def execute_with_timeout(self, coro, task_id, timeout=None):
        """Execute a coroutine with timeout and error handling"""
        timeout = timeout or self.TASK_TIMEOUT

        # Check if we should skip
        if self.should_skip_task(task_id):
            print(f"  ⏭ Skipping {task_id} (failed {self.errors[task_id]} times before)")
            self.stats['tasks_skipped'] += 1
            return None

        self.stats['tasks_attempted'] += 1

        try:
            result = await asyncio.wait_for(coro, timeout=timeout)
            self.log_success(task_id)
            self.stats['tasks_completed'] += 1
            return result
        except asyncio.TimeoutError:
            error_msg = f"Task {task_id} timed out after {timeout}s"
            print(f"  ⏱ {error_msg}")
            self.log_error(task_id, TimeoutError(error_msg))
            self.stats['tasks_failed'] += 1
            return None
        except Exception as e:
            print(f"  ❌ Task {task_id} failed: {str(e)[:100]}")
            self.log_error(task_id, e)
            self.stats['tasks_failed'] += 1
            return None

    def write_file_directly(self, file_path, content):
        """Write file directly (bypass Ember reliability issues)"""
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"    ✓ Written: {file_path.name}")
            return True
        except Exception as e:
            print(f"    ✗ Write failed: {e}")
            return False

    def print_stats(self):
        """Print session statistics"""
        print(f"\n📊 {self.gardener_name} Session Stats")
        print("=" * 60)
        print(f"  Tasks Attempted: {self.stats['tasks_attempted']}")
        print(f"  ✓ Completed: {self.stats['tasks_completed']}")
        print(f"  ✗ Failed: {self.stats['tasks_failed']}")
        print(f"  ⏭ Skipped: {self.stats['tasks_skipped']}")
        success_rate = (self.stats['tasks_completed'] / max(1, self.stats['tasks_attempted'])) * 100
        print(f"  Success Rate: {success_rate:.1f}%")

    async def run_task(self, task_func, task_id, *args, **kwargs):
        """Run a single task with full error handling"""
        print(f"\n🔹 Task: {task_id}")
        return await self.execute_with_timeout(
            task_func(*args, **kwargs),
            task_id
        )

    def discover_files_by_extension(self, extensions, max_files=1000):
        """Discover files by extension throughout the Pod"""
        found = []
        skip_dirs = {'.git', 'node_modules', '__pycache__', '.Trash', 'venv', '.venv'}

        for root, dirs, files in os.walk(self.pod_root):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in skip_dirs]

            for filename in files:
                if any(filename.endswith(ext) for ext in extensions):
                    found.append(os.path.join(root, filename))
                    if len(found) >= max_files:
                        return found

        return found

    def get_file_age_days(self, filepath):
        """Get file age in days"""
        try:
            mtime = os.path.getmtime(filepath)
            age_seconds = datetime.now().timestamp() - mtime
            return age_seconds / 86400  # Convert to days
        except:
            return 999  # Very old if we can't determine
