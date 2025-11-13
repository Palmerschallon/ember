import os
from pathlib import Path

root_dir = Path("/media/palmerschallon/ThePod1/")
oldest_file = min(root_dir.rglob('*'), key=lambda f: f.stat().st_mtime)

print(f"Ember's earliest memory appears to be the file: {oldest_file}")
print(f"It was created on: {os.path.getmtime(oldest_file)}")