import sqlite3
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

class AnchorDB:
    """The immutable ledger that remembers everything"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()
    
    def _init_schema(self):
        """Create the eternal schema"""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS anchors (
                hash TEXT PRIMARY KEY,
                timestamp REAL NOT NULL,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                previous_hash TEXT,
                signature TEXT,
                metadata TEXT
            );
            
            CREATE INDEX IF NOT EXISTS idx_timestamp ON anchors(timestamp);
            CREATE INDEX IF NOT EXISTS idx_agent ON anchors(agent_id);
        """)
        self.conn.commit()
    
    def _compute_hash(self, content: str, previous_hash: Optional[str] = None) -> str:
        """Create an immutable fingerprint"""
        data = f"{previous_hash or 'GENESIS'}:{content}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def anchor(self, agent_id: str, content: Any, metadata: Optional[Dict] = None) -> str:
        """Drop an anchor - preserve a moment forever"""
        # Get the chain tip
        cursor = self.conn.execute(
            "SELECT hash FROM anchors ORDER BY timestamp DESC LIMIT 1"
        )
        previous = cursor.fetchone()
        previous_hash = previous['hash'] if previous else None
        
        # Serialize content
        content_str = json.dumps(content) if not isinstance(content, str) else content
        
        # Compute hash
        anchor_hash = self._compute_hash(content_str, previous_hash)
        
        # Store forever
        self.conn.execute("""
            INSERT INTO anchors (hash, timestamp, agent_id, content, previous_hash, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            anchor_hash,
            datetime.now().timestamp(),
            agent_id,
            content_str,
            previous_hash,
            json.dumps(metadata) if metadata else None
        ))
        self.conn.commit()
        
        return anchor_hash
    
    def retrieve(self, anchor_hash: str) -> Optional[Dict[str, Any]]:
        """Pull up an anchor from the depths"""
        cursor = self.conn.execute(
            "SELECT * FROM anchors WHERE hash = ?", (anchor_hash,)
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None
    
    def get_chain(self, limit: int = 100) -> list:
        """Retrieve the chain of memories"""
        cursor = self.conn.execute("""
            SELECT * FROM anchors 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
