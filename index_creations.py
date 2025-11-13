#!/usr/bin/env python3
"""Index Ember's creations into the semantic mesh"""

import sqlite3
import os
from pathlib import Path
from datetime import datetime

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
MESH_DB = THEPOD_PATH / "_mesh" / "content.db"
CREATIONS_DIR = THEPOD_PATH / "ember5" / "creations"

def index_creations():
    """Add all creation files to the mesh"""
    conn = sqlite3.connect(MESH_DB)
    cursor = conn.cursor()
    
    indexed = 0
    for file_path in sorted(CREATIONS_DIR.glob("*.py")):
        # Check if already indexed
        cursor.execute("SELECT content_hash FROM files WHERE current_path = ?", (str(file_path),))
        if cursor.fetchone():
            continue
        
        # Read file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract metadata from filename (timestamp)
        filename = file_path.stem
        if filename.startswith("2025"):
            timestamp_str = "_".join(filename.split("_")[:2])
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d_%H_%M_%S")
            except:
                timestamp = datetime.fromtimestamp(file_path.stat().st_mtime)
        else:
            timestamp = datetime.fromtimestamp(file_path.stat().st_mtime)
        
        # Detect what type of creation it is
        tags = []
        if "matplotlib" in content or "plt." in content:
            tags.append("visualization")
        if "animation" in content.lower() or "FuncAnimation" in content:
            tags.append("animation")
        if "fractal" in content.lower() or "mandelbrot" in content.lower() or "julia" in content.lower():
            tags.append("fractal")
        if "3d" in content.lower() or "Axes3D" in content:
            tags.append("3d")
        if "spiral" in content.lower():
            tags.append("spiral")
        
        # Insert into files table
        import hashlib
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        
        cursor.execute("""
            INSERT INTO files (content_hash, current_path, file_name, file_size, indexed_at, full_content, content_preview)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            content_hash,
            str(file_path),
            file_path.name,
            len(content),
            timestamp.timestamp(),
            content,
            content[:500]
        ))
        
        # Extract key concepts and add to concepts table
        concepts = []
        lines = content.split('\n')
        for line in lines[:10]:  # First 10 lines usually have imports/comments
            if 'import' in line:
                parts = line.split()
                if 'import' in parts:
                    idx = parts.index('import')
                    if idx + 1 < len(parts):
                        module = parts[idx + 1].split('.')[0]
                        concepts.append(module)
        
        # Add tags as concepts
        concepts.extend(tags)
        
        for concept in set(concepts):
            cursor.execute("""
                INSERT INTO concepts (content_hash, concept, relevance)
                VALUES (?, ?, ?)
            """, (content_hash, concept, 0.8))
        
        indexed += 1
        print(f"✅ Indexed: {file_path.name}")
        print(f"   Tags: {', '.join(tags) if tags else 'general'}")
        print(f"   Concepts: {', '.join(set(concepts))}")
    
    conn.commit()
    conn.close()
    
    print(f"\n📊 Indexed {indexed} new creations into the mesh")
    return indexed

if __name__ == "__main__":
    index_creations()

