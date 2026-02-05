Here's a utility to monitor and analyze semantic changes in a content mesh:

```python
#!/usr/bin/env python3
"""
Content Mesh Evolution Analyzer

Monitors semantic changes in files over time by tracking:
- Content fingerprints
- Semantic drift
- File movement/modification patterns

Usage:
    python content_mesh_evolution.py /path/to/documents

Dependencies:
- sqlite3
- hashlib
- sentence_transformers
"""

import os
import sqlite3
import hashlib
import logging
from pathlib import Path
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np

class ContentMeshEvolutionAnalyzer:
    def __init__(self, root_path: str, db_path: str = None):
        """
        Initialize evolution analyzer for document corpus.

        Args:
            root_path (str): Root directory to monitor
            db_path (str, optional): Path to tracking database
        """
        self.root_path = Path(root_path)
        self.db_path = db_path or os.path.join(root_path, '_mesh_evolution.db')
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize embeddings model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Set up database
        self._initialize_database()
    
    def _initialize_database(self):
        """Create SQLite database schema for tracking document evolution."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS document_evolution (
                        file_path TEXT PRIMARY KEY,
                        content_hash TEXT,
                        semantic_embedding BLOB,
                        last_modified REAL,
                        semantic_drift REAL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            self.logger.error(f"Database initialization error: {e}")
    
    def compute_semantic_embedding(self, file_path: Path) -> np.ndarray:
        """
        Generate semantic embedding for a document.
        
        Args:
            file_path (Path): Path to document file
        
        Returns:
            np.ndarray: Semantic embedding vector
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                embedding = self.model.encode(content)
            return embedding
        except Exception as e:
            self.logger.warning(f"Could not compute embedding for {file_path}: {e}")
            return None
    
    def compute_semantic_drift(self, old_embedding: np.ndarray, new_embedding: np.ndarray) -> float:
        """
        Calculate semantic drift between two document embeddings.
        
        Args:
            old_embedding (np.ndarray): Previous document embedding
            new_embedding (np.ndarray): Current document embedding
        
        Returns:
            float: Semantic drift score (cosine distance)
        """
        if old_embedding is None or new_embedding is None:
            return 0.0
        
        return 1 - np.dot(old_embedding, new_embedding) / (
            np.linalg.norm(old_embedding) * np.linalg.norm(new_embedding)
        )
    
    def scan_documents(self):
        """
        Scan document corpus, track changes, compute semantic drifts.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                for file_path in self.root_path.rglob('*'):
                    if file_path.is_file():
                        self._process_document(file_path, conn)
        except Exception as e:
            self.logger.error(f"Document scanning error: {e}")
    
    def _process_document(self, file_path: Path, connection):
        """Process individual document for tracking."""
        cursor = connection.cursor()
        
        # Compute content hash
        with open(file_path, 'rb') as f:
            content_hash = hashlib.md5(f.read()).hexdigest()
        
        # Compute semantic embedding
        semantic_embedding = self.compute_semantic_embedding(file_path)
        
        # Check existing record
        cursor.execute(
            'SELECT semantic_embedding FROM document_evolution WHERE file_path = ?', 
            (str(file_path),)
        )
        existing_record = cursor.fetchone()
        
        if existing_record:
            old_embedding = np.frombuffer(existing_record[0])
            drift = self.compute_semantic_drift(old_embedding, semantic_embedding)
            
            cursor.execute('''
                UPDATE document_evolution 
                SET content_hash = ?, semantic_embedding = ?, semantic_drift = ?
                WHERE file_path = ?
            ''', (content_hash, semantic_embedding.tobytes(), drift, str(file_path)))
        else:
            cursor.execute('''
                INSERT INTO document_evolution 
                (file_path, content_hash, semantic_embedding, semantic_drift)
                VALUES (?, ?, ?, ?)
            ''', (str(file_path), content_hash, semantic_embedding.tobytes(), 0.0))
        
        connection.commit()

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python content_mesh_evolution.py /path/to/documents")
        sys.exit(1)
    
    analyzer = ContentMeshEvolutionAnalyzer(sys.argv[1])
    analyzer.scan_documents()

if __name__ == '__main__':
    main()
```

This utility does several key things:
1. Track document evolution
2. Compute semantic embeddings
3. Measure semantic drift
4. Persist tracking in SQLite
5. Robust error handling
6. Logging support
7. Command-line usability

It requires `sentence-transformers` and `numpy`. Install via:
```bash
pip install sentence-transformers numpy
```

Example usage:
```bash
python content_mesh_evolution.py /home/user/documents
```

The tool will track semantic changes, allowing you to understand how document content evolves over time.