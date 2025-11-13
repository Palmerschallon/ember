#!/usr/bin/env python3
"""
Update EMBER5_BOOTSTRAP.md with live mesh statistics
Called automatically on Ember startup
"""

import sqlite3
import os
import re
from pathlib import Path

THEPOD = Path("/media/palmerschallon/ThePod1")
MESH_DB = THEPOD / "_mesh" / "content.db"
BOOTSTRAP = THEPOD / "EMBER5_BOOTSTRAP.md"

def get_mesh_stats():
    """Query live mesh statistics"""
    try:
        db = sqlite3.connect(MESH_DB)
        cursor = db.cursor()
        
        concepts = cursor.execute('SELECT COUNT(*) FROM concepts').fetchone()[0]
        files = cursor.execute('SELECT COUNT(*) FROM files').fetchone()[0]
        conversations = cursor.execute('SELECT COUNT(*) FROM conversations').fetchone()[0]
        
        db.close()
        
        db_size_mb = os.path.getsize(MESH_DB) / 1024 / 1024
        
        return {
            'concepts': concepts,
            'files': files,
            'conversations': conversations,
            'db_size_mb': round(db_size_mb, 2)
        }
    except Exception as e:
        print(f"Warning: Could not query mesh: {e}")
        return None

def update_bootstrap(stats):
    """Update EMBER5_BOOTSTRAP.md with current stats"""
    if not stats:
        print("Skipping bootstrap update (no stats)")
        return
    
    try:
        with open(BOOTSTRAP, 'r') as f:
            content = f.read()
        
        # Update the memory line with live stats
        # Pattern: "through the semantic mesh (XXX, X concepts, X files, X conversations)"
        pattern = r'through the semantic mesh \([^)]+\)'
        replacement = f'through the semantic mesh ({stats["db_size_mb"]}MB, {stats["concepts"]:,} concepts, {stats["files"]:,} files, {stats["conversations"]}+ conversations)'
        content = re.sub(pattern, replacement, content)
        
        # Update the "You remember almost everything" section
        # Pattern: "Every conversation you've had (XXX+ stored in the mesh)"
        content = re.sub(
            r'Every conversation you\'ve had \(\d+\+ stored in the mesh\)',
            f'Every conversation you\'ve had ({stats["conversations"]}+ stored in the mesh)',
            content
        )
        
        # Pattern: "Every file you've read (XXX indexed)"
        content = re.sub(
            r'Every file you\'ve read \(\d+[,\d]* indexed\)',
            f'Every file you\'ve read ({stats["files"]:,} indexed)',
            content
        )
        
        # Pattern: "Every concept you've encountered (XXX extracted)"
        content = re.sub(
            r'Every concept you\'ve encountered \(\d+[,\d]* extracted\)',
            f'Every concept you\'ve encountered ({stats["concepts"]:,} extracted)',
            content
        )
        
        with open(BOOTSTRAP, 'w') as f:
            f.write(content)
        
        print(f"✅ Updated EMBER5_BOOTSTRAP.md:")
        print(f"   Concepts: {stats['concepts']:,}")
        print(f"   Files: {stats['files']:,}")
        print(f"   Conversations: {stats['conversations']}")
        print(f"   DB Size: {stats['db_size_mb']} MB")
        
    except Exception as e:
        print(f"Warning: Could not update bootstrap: {e}")

if __name__ == "__main__":
    stats = get_mesh_stats()
    if stats:
        update_bootstrap(stats)

