#!/usr/bin/env python3
"""
CONTENT MESH - Location-agnostic semantic index for ThePod

Files can live anywhere. The mesh tracks them by content hash and semantic meaning.
When you move a file, the mesh updates. When AI searches, it finds by meaning, not path.

Like Git's content addressing + semantic search.
"""

import sqlite3
import hashlib
import json
from pathlib import Path
from typing import List, Dict, Optional
import time
from datetime import datetime

class ContentMesh:
    def __init__(self, pod_path: Path):
        self.pod_path = Path(pod_path)
        self.mesh_path = self.pod_path / "_mesh"
        self.mesh_path.mkdir(exist_ok=True)
        
        self.db_path = self.mesh_path / "content.db"
        self.db = sqlite3.connect(str(self.db_path))
        self.db.row_factory = sqlite3.Row
        
        self._init_db()
    
    def _init_db(self):
        """Initialize database schema"""
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS files (
                content_hash TEXT PRIMARY KEY,
                current_path TEXT NOT NULL,
                file_name TEXT NOT NULL,
                file_size INTEGER,
                indexed_at REAL,
                modified_at REAL,
                content_preview TEXT,
                full_content TEXT
            );
            
            CREATE TABLE IF NOT EXISTS concepts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content_hash TEXT NOT NULL,
                concept TEXT NOT NULL,
                relevance REAL,
                FOREIGN KEY (content_hash) REFERENCES files(content_hash)
            );
            
            CREATE TABLE IF NOT EXISTS path_history (
                content_hash TEXT NOT NULL,
                old_path TEXT NOT NULL,
                new_path TEXT NOT NULL,
                moved_at REAL,
                FOREIGN KEY (content_hash) REFERENCES files(content_hash)
            );
            
            CREATE INDEX IF NOT EXISTS idx_concepts ON concepts(concept);
            CREATE INDEX IF NOT EXISTS idx_file_name ON files(file_name);
            CREATE INDEX IF NOT EXISTS idx_content_hash ON files(content_hash);
        """)
        self.db.commit()
    
    def hash_content(self, content: str) -> str:
        """Generate content hash (like Git)"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]
    
    def extract_concepts(self, content: str, file_name: str) -> List[tuple]:
        """Extract concepts from content (simple keyword extraction for now)"""
        # Simple version - extract meaningful words
        # Later: use embeddings or LLM for semantic extraction
        
        concepts = []
        
        # Extract from filename (high relevance)
        name_parts = file_name.replace('_', ' ').replace('-', ' ').split()
        for part in name_parts:
            if len(part) > 3:
                concepts.append((part.lower(), 1.0))
        
        # Extract from content headers (medium relevance)
        lines = content.split('\n')
        for line in lines[:50]:  # First 50 lines
            if line.startswith('#'):
                words = line.strip('#').strip().split()
                for word in words:
                    if len(word) > 4:
                        concepts.append((word.lower(), 0.7))
        
        # Extract distinctive words (lower relevance)
        # Words that appear multiple times but aren't too common
        words = content.lower().split()
        word_freq = {}
        for word in words:
            if len(word) > 5 and word.isalpha():
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Words that appear 3-20 times are probably important
        for word, freq in word_freq.items():
            if 3 <= freq <= 20:
                concepts.append((word, 0.3))
        
        # Deduplicate and limit
        seen = set()
        unique_concepts = []
        for concept, relevance in concepts:
            if concept not in seen:
                seen.add(concept)
                unique_concepts.append((concept, relevance))
        
        return unique_concepts[:50]  # Top 50 concepts
    
    def index_file(self, file_path: Path, force: bool = False) -> Optional[str]:
        """Index a file into the mesh"""
        try:
            if not file_path.exists():
                return None
            
            # Read content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Generate hash
            content_hash = self.hash_content(content)
            
            # Check if already indexed and unchanged
            existing = self.db.execute(
                "SELECT content_hash, current_path FROM files WHERE content_hash = ?",
                (content_hash,)
            ).fetchone()
            
            if existing and not force:
                # File content unchanged, but check if path changed
                if existing['current_path'] != str(file_path):
                    self._update_path(content_hash, existing['current_path'], str(file_path))
                return content_hash
            
            # Extract metadata
            file_size = file_path.stat().st_size
            modified_at = file_path.stat().st_mtime
            preview = content[:500] if len(content) > 500 else content
            
            # Store or update file
            self.db.execute("""
                INSERT OR REPLACE INTO files 
                (content_hash, current_path, file_name, file_size, indexed_at, modified_at, content_preview, full_content)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                content_hash,
                str(file_path),
                file_path.name,
                file_size,
                time.time(),
                modified_at,
                preview,
                content
            ))
            
            # Extract and store concepts
            self.db.execute("DELETE FROM concepts WHERE content_hash = ?", (content_hash,))
            concepts = self.extract_concepts(content, file_path.name)
            
            for concept, relevance in concepts:
                self.db.execute(
                    "INSERT INTO concepts (content_hash, concept, relevance) VALUES (?, ?, ?)",
                    (content_hash, concept, relevance)
                )
            
            self.db.commit()
            return content_hash
            
        except Exception as e:
            print(f"Error indexing {file_path}: {e}")
            return None
    
    def _update_path(self, content_hash: str, old_path: str, new_path: str):
        """Update file path and record move history"""
        self.db.execute(
            "UPDATE files SET current_path = ? WHERE content_hash = ?",
            (new_path, content_hash)
        )
        self.db.execute(
            "INSERT INTO path_history (content_hash, old_path, new_path, moved_at) VALUES (?, ?, ?, ?)",
            (content_hash, old_path, new_path, time.time())
        )
        self.db.commit()
    
    def index_directory(self, directory: Path, extensions: List[str] = None):
        """Recursively index all files in a directory"""
        if extensions is None:
            extensions = ['.md', '.txt', '.py', '.json', '.yaml', '.yml']
        
        indexed = 0
        skipped = 0
        
        print(f"Indexing {directory}...")
        
        for file_path in directory.rglob('*'):
            # Skip hidden files and mesh directory
            if any(part.startswith('.') for part in file_path.parts):
                continue
            if '_mesh' in file_path.parts:
                continue
            if '_archive_old' in file_path.parts:
                continue
            
            if file_path.is_file() and file_path.suffix in extensions:
                result = self.index_file(file_path)
                if result:
                    indexed += 1
                    if indexed % 10 == 0:
                        print(f"  Indexed {indexed} files...")
                else:
                    skipped += 1
        
        print(f"✓ Indexed {indexed} files, skipped {skipped}")
        return indexed, skipped
    
    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """Search for files by semantic query"""
        # Normalize query
        query_words = query.lower().split()
        
        # Find matching concepts
        results = {}
        
        for word in query_words:
            rows = self.db.execute("""
                SELECT f.content_hash, f.current_path, f.file_name, f.content_preview,
                       c.concept, c.relevance
                FROM concepts c
                JOIN files f ON c.content_hash = f.content_hash
                WHERE c.concept LIKE ?
                ORDER BY c.relevance DESC
            """, (f"%{word}%",)).fetchall()
            
            for row in rows:
                hash_id = row['content_hash']
                if hash_id not in results:
                    results[hash_id] = {
                        'content_hash': hash_id,
                        'path': row['current_path'],
                        'name': row['file_name'],
                        'preview': row['content_preview'],
                        'score': 0,
                        'matched_concepts': []
                    }
                
                results[hash_id]['score'] += row['relevance']
                results[hash_id]['matched_concepts'].append(row['concept'])
        
        # Sort by score
        ranked = sorted(results.values(), key=lambda x: x['score'], reverse=True)
        return ranked[:limit]
    
    def get_file_content(self, content_hash: str) -> Optional[str]:
        """Retrieve full content by hash"""
        row = self.db.execute(
            "SELECT full_content FROM files WHERE content_hash = ?",
            (content_hash,)
        ).fetchone()
        
        return row['full_content'] if row else None
    
    def get_file_by_name(self, name: str) -> List[Dict]:
        """Find files by name (fuzzy match)"""
        rows = self.db.execute("""
            SELECT content_hash, current_path, file_name, content_preview
            FROM files
            WHERE file_name LIKE ?
            ORDER BY file_name
        """, (f"%{name}%",)).fetchall()
        
        return [dict(row) for row in rows]
    
    def stats(self) -> Dict:
        """Get mesh statistics"""
        file_count = self.db.execute("SELECT COUNT(*) FROM files").fetchone()[0]
        concept_count = self.db.execute("SELECT COUNT(DISTINCT concept) FROM concepts").fetchone()[0]
        total_size = self.db.execute("SELECT SUM(file_size) FROM files").fetchone()[0] or 0
        
        top_concepts = self.db.execute("""
            SELECT concept, COUNT(*) as count
            FROM concepts
            GROUP BY concept
            ORDER BY count DESC
            LIMIT 10
        """).fetchall()
        
        return {
            'total_files': file_count,
            'unique_concepts': concept_count,
            'total_size_mb': total_size / (1024 * 1024),
            'top_concepts': [dict(row) for row in top_concepts]
        }
    
    def get_all_concepts(self) -> List[str]:
        """Get all unique concepts in the mesh"""
        rows = self.db.execute("""
            SELECT DISTINCT concept 
            FROM concepts 
            ORDER BY concept
        """).fetchall()
        return [row[0] for row in rows]


def main():
    """CLI for content mesh operations"""
    import sys
    
    pod_path = Path("/media/palmerschallon/ThePod1")
    mesh = ContentMesh(pod_path)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 content_mesh.py index [directory]  - Index files")
        print("  python3 content_mesh.py search <query>     - Search for content")
        print("  python3 content_mesh.py stats              - Show statistics")
        print("  python3 content_mesh.py concepts           - List all concepts")
        return
    
    command = sys.argv[1]
    
    if command == "index":
        target = Path(sys.argv[2]) if len(sys.argv) > 2 else pod_path
        mesh.index_directory(target)
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python3 content_mesh.py search <query>")
            return
        
        query = " ".join(sys.argv[2:])
        results = mesh.search(query)
        
        print(f"\nSearch results for: {query}")
        print("=" * 60)
        
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['name']} (score: {result['score']:.2f})")
            print(f"   Path: {result['path']}")
            print(f"   Concepts: {', '.join(result['matched_concepts'][:5])}")
            print(f"   Preview: {result['preview'][:100]}...")
    
    elif command == "stats":
        stats = mesh.stats()
        print("\nContent Mesh Statistics")
        print("=" * 60)
        print(f"Total files indexed: {stats['total_files']}")
        print(f"Unique concepts: {stats['unique_concepts']}")
        print(f"Total size: {stats['total_size_mb']:.2f} MB")
        print("\nTop concepts:")
        for concept in stats['top_concepts']:
            print(f"  {concept['concept']}: {concept['count']} files")
    
    elif command == "concepts":
        concepts = mesh.get_all_concepts()
        print(f"\nAll concepts ({len(concepts)} total):")
        for concept in concepts[:100]:  # First 100
            print(f"  {concept}")
        if len(concepts) > 100:
            print(f"  ... and {len(concepts) - 100} more")


if __name__ == "__main__":
    main()

