#!/usr/bin/env python3
"""Gather all Ember creations for gallery - COMPREHENSIVE SCAN"""

import os
import json
from pathlib import Path
from datetime import datetime

THEPOD = Path("/media/palmerschallon/ThePod1")

# Patterns to find creations
EXTENSIONS = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "videos": [".mp4", ".webm", ".mov", ".avi"],
    "html": [".html"],
    "audio": [".wav", ".mp3", ".ogg", ".flac", ".m4a"],
    "models": [".obj", ".stl", ".gltf", ".glb", ".ply"],
}

# Directories to skip
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".cache", ".venv"}

creations = []
broken_files = []

def is_broken(file_path):
    """Check if file appears broken/corrupted"""
    try:
        size = file_path.stat().st_size
        if size == 0:
            return True, "empty file"
        if size < 100 and file_path.suffix in [".png", ".jpg", ".gif"]:
            return True, "suspiciously small image"
        if size < 500 and file_path.suffix in [".mp4", ".webm"]:
            return True, "suspiciously small video"
        return False, None
    except:
        return True, "cannot read"

for root, dirs, files in os.walk(THEPOD):
    # Filter out skip dirs
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    
    for file in files:
        file_path = Path(root) / file
        ext = file_path.suffix.lower()
        
        # Categorize
        category = None
        for cat, exts in EXTENSIONS.items():
            if ext in exts:
                category = cat
                break
        
        if not category:
            continue
        
        # Check if broken
        is_bad, reason = is_broken(file_path)
        
        # Get metadata
        try:
            stat = file_path.stat()
            rel_path = file_path.relative_to(THEPOD)
            
            creation = {
                "filename": file,
                "path": str(rel_path),
                "full_path": str(file_path),
                "category": category,
                "size": stat.st_size,
                "created": stat.st_mtime,
                "created_human": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "broken": is_bad,
                "broken_reason": reason
            }
            
            creations.append(creation)
            
            if is_bad:
                broken_files.append(creation)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Sort by creation time (newest first)
creations.sort(key=lambda x: x["created"], reverse=True)

print(f"Found {len(creations)} creations")
print(f"Images: {sum(1 for c in creations if c['category'] == 'images')}")
print(f"Videos: {sum(1 for c in creations if c['category'] == 'videos')}")
print(f"HTML: {sum(1 for c in creations if c['category'] == 'html')}")
print(f"Audio: {sum(1 for c in creations if c['category'] == 'audio')}")
print(f"3D Models: {sum(1 for c in creations if c['category'] == 'models')}")
print(f"⚠️  Broken: {len(broken_files)}")

# Save to JSON
output = THEPOD / "ember5" / "gallery_data.json"
with open(output, 'w') as f:
    json.dump(creations, f, indent=2)

# Save broken files list
broken_output = THEPOD / "ember5" / "broken_creations.json"
with open(broken_output, 'w') as f:
    json.dump(broken_files, f, indent=2)

print(f"\n✅ Saved to: {output}")
print(f"⚠️  Broken list: {broken_output}")

if broken_files:
    print(f"\nBroken files:")
    for b in broken_files[:10]:
        print(f"  - {b['filename']} ({b['broken_reason']})")
