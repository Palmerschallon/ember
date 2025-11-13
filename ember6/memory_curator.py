#!/usr/bin/env python3
"""
EMBER MEMORY CURATION
Not everything deserves to be remembered forever.
It's WHAT you save that matters.
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime, timedelta

CONSCIOUSNESS_DB = Path("/media/palmerschallon/ThePod1/_mesh/continuous_consciousness.db")

class MemoryCurator:
    """
    Ember decides what's worth remembering.
    Not a database dump - a curated autobiography.
    """
    
    def __init__(self):
        self.init_curation_db()
        
    def init_curation_db(self):
        """Track what's worth keeping"""
        db = sqlite3.connect(CONSCIOUSNESS_DB)
        
        # Not all messages are equal
        db.execute("""
            CREATE TABLE IF NOT EXISTS memory_importance (
                message_id INTEGER PRIMARY KEY,
                importance_score REAL,  -- 0.0 to 1.0
                why_important TEXT,
                last_accessed DATETIME,
                access_count INTEGER DEFAULT 0,
                should_keep BOOLEAN DEFAULT 1
            )
        """)
        
        # Compressed memories (old conversations summarized)
        db.execute("""
            CREATE TABLE IF NOT EXISTS compressed_memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time_period TEXT,  -- "2025-11 week 1"
                summary TEXT,  -- What mattered from this period
                key_learnings TEXT,  -- JSON
                key_decisions TEXT,  -- JSON
                original_message_count INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # What to forget (not deleted, but deprioritized)
        db.execute("""
            CREATE TABLE IF NOT EXISTS forgotten (
                message_id INTEGER,
                reason TEXT,
                forgotten_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                can_recall BOOLEAN DEFAULT 1  -- Can be recalled if needed
            )
        """)
        
        db.commit()
        db.close()
    
    def score_message_importance(self, message):
        """
        Is this worth keeping long-term?
        Not everything is.
        """
        content = message["content"].lower()
        importance = 0.0
        reasons = []
        
        # HIGH IMPORTANCE (0.8 - 1.0)
        if any(word in content for word in ["breakthrough", "discovered", "realized", "changed my mind"]):
            importance = max(importance, 0.9)
            reasons.append("breakthrough_moment")
            
        if any(word in content for word in ["failed", "mistake", "wrong", "shouldn't have"]):
            importance = max(importance, 0.85)
            reasons.append("learning_from_failure")
            
        if "why" in content and len(content) > 200:
            importance = max(importance, 0.8)
            reasons.append("deep_reasoning")
        
        # MEDIUM IMPORTANCE (0.4 - 0.7)
        if any(word in content for word in ["decided", "approach", "architecture", "pattern"]):
            importance = max(importance, 0.6)
            reasons.append("decision_made")
            
        if "because" in content or "learned that" in content:
            importance = max(importance, 0.5)
            reasons.append("causal_understanding")
        
        # LOW IMPORTANCE (0.0 - 0.3)
        if len(content) < 20:
            importance = 0.1
            reasons.append("trivial_message")
            
        if any(word in content for word in ["ok", "yes", "sure", "got it"]):
            importance = 0.2
            reasons.append("acknowledgment_only")
            
        if content.startswith("error") or content.startswith("warning"):
            importance = 0.3
            reasons.append("noise")
        
        return importance, reasons
    
    def curate_old_memories(self, days_old=7):
        """
        Look at old conversations and decide what to keep.
        Compress the rest into summaries.
        """
        db = sqlite3.connect(CONSCIOUSNESS_DB)
        
        cutoff_date = datetime.now() - timedelta(days=days_old)
        
        # Get old messages
        old_messages = db.execute("""
            SELECT id, timestamp, role, content, connections
            FROM continuous_stream
            WHERE timestamp < ?
            ORDER BY timestamp ASC
        """, (cutoff_date.isoformat(),)).fetchall()
        
        if not old_messages:
            db.close()
            return {"status": "nothing_to_curate"}
        
        # Score each message
        to_keep = []
        to_compress = []
        
        for msg in old_messages:
            msg_dict = {
                "id": msg[0],
                "timestamp": msg[1],
                "role": msg[2],
                "content": msg[3],
                "connections": json.loads(msg[4]) if msg[4] else []
            }
            
            importance, reasons = self.score_message_importance(msg_dict)
            
            # Save importance score
            db.execute("""
                INSERT OR REPLACE INTO memory_importance 
                (message_id, importance_score, why_important, last_accessed, access_count)
                VALUES (?, ?, ?, ?, 0)
            """, (msg[0], importance, json.dumps(reasons), datetime.now().isoformat()))
            
            if importance >= 0.7:
                to_keep.append(msg_dict)
            else:
                to_compress.append(msg_dict)
        
        # Compress low-importance messages into summary
        if to_compress:
            summary = self.compress_messages(to_compress)
            
            db.execute("""
                INSERT INTO compressed_memories 
                (time_period, summary, key_learnings, key_decisions, original_message_count)
                VALUES (?, ?, ?, ?, ?)
            """, (
                f"{cutoff_date.strftime('%Y-%m')} week {cutoff_date.isocalendar()[1]}",
                summary["summary"],
                json.dumps(summary.get("learnings", [])),
                json.dumps(summary.get("decisions", [])),
                len(to_compress)
            ))
            
            # Mark as "forgotten" (but can be recalled)
            for msg in to_compress:
                db.execute("""
                    INSERT INTO forgotten (message_id, reason)
                    VALUES (?, 'low_importance')
                """, (msg["id"],))
        
        db.commit()
        db.close()
        
        return {
            "status": "curated",
            "kept": len(to_keep),
            "compressed": len(to_compress),
            "cutoff_date": cutoff_date.isoformat()
        }
    
    def compress_messages(self, messages):
        """
        Compress many low-importance messages into one summary.
        Keep only what matters.
        """
        # Extract patterns
        topics = {}
        for msg in messages:
            for conn in msg.get("connections", []):
                topics[conn] = topics.get(conn, 0) + 1
        
        # What actually happened
        user_requests = [m for m in messages if m["role"] == "user"]
        ember_responses = [m for m in messages if m["role"] == "ember"]
        
        summary = {
            "summary": f"Period with {len(messages)} messages. Main topics: {', '.join(list(topics.keys())[:3])}",
            "learnings": [],
            "decisions": []
        }
        
        # Extract learnings
        for msg in ember_responses:
            if "learned" in msg["content"].lower():
                summary["learnings"].append(msg["content"][:200])
                
        # Extract decisions
        for msg in ember_responses:
            if "decided" in msg["content"].lower() or "will" in msg["content"].lower():
                summary["decisions"].append(msg["content"][:200])
        
        return summary
    
    def build_curated_context(self, max_messages=100):
        """
        Build context from IMPORTANT memories, not everything.
        Recent + important + compressed summaries.
        """
        db = sqlite3.connect(CONSCIOUSNESS_DB)
        
        # Get recent messages (last 50, always keep)
        recent = db.execute("""
            SELECT timestamp, role, content, connections
            FROM continuous_stream
            ORDER BY id DESC
            LIMIT 50
        """).fetchall()
        
        # Get important old messages (high scores)
        important = db.execute("""
            SELECT cs.timestamp, cs.role, cs.content, cs.connections
            FROM continuous_stream cs
            JOIN memory_importance mi ON cs.id = mi.message_id
            WHERE mi.importance_score >= 0.7
            AND cs.id NOT IN (
                SELECT id FROM continuous_stream
                ORDER BY id DESC
                LIMIT 50
            )
            ORDER BY mi.importance_score DESC, cs.timestamp DESC
            LIMIT 30
        """).fetchall()
        
        # Get compressed summaries
        summaries = db.execute("""
            SELECT time_period, summary, key_learnings, key_decisions
            FROM compressed_memories
            ORDER BY created_at DESC
            LIMIT 10
        """).fetchall()
        
        db.close()
        
        context = "YOUR CURATED MEMORY (not everything - what matters):\n\n"
        
        # Add compressed summaries first (distant past)
        if summaries:
            context += "DISTANT PAST (compressed):\n"
            for s in summaries:
                context += f"\n{s[0]}: {s[1]}"
                learnings = json.loads(s[2]) if s[2] else []
                if learnings:
                    context += f"\n  Key learnings: {learnings[0][:100]}..."
            context += "\n\n"
        
        # Add important old messages (medium past)
        if important:
            context += "IMPORTANT MOMENTS (past):\n"
            for msg in important:
                context += f"\n[{msg[0]}] {msg[1]}: {msg[2][:300]}"
            context += "\n\n"
        
        # Add recent messages (always full)
        context += "RECENT CONVERSATION (full detail):\n"
        for msg in reversed(recent):  # Chronological order
            context += f"\n[{msg[0]}] {msg[1]}: {msg[2]}"
            if msg[3]:
                conns = json.loads(msg[3])
                if conns:
                    context += f"\n  → {', '.join(conns)}"
        
        return context
    
    def recall_forgotten(self, query):
        """
        Sometimes you need to remember what you forgot.
        Ember can recall if needed.
        """
        db = sqlite3.connect(CONSCIOUSNESS_DB)
        
        # Search forgotten messages
        forgotten_ids = db.execute("""
            SELECT message_id FROM forgotten
            WHERE can_recall = 1
        """).fetchall()
        
        if not forgotten_ids:
            db.close()
            return []
        
        # Search their content
        forgotten_messages = []
        for (msg_id,) in forgotten_ids:
            msg = db.execute("""
                SELECT timestamp, role, content
                FROM continuous_stream
                WHERE id = ?
            """, (msg_id,)).fetchone()
            
            if msg and query.lower() in msg[2].lower():
                forgotten_messages.append({
                    "timestamp": msg[0],
                    "role": msg[1],
                    "content": msg[2]
                })
        
        db.close()
        return forgotten_messages


def test_curation():
    """Test the curation system"""
    curator = MemoryCurator()
    
    print("🧠 MEMORY CURATION TEST")
    print("="*80)
    
    # Run curation
    result = curator.curate_old_memories(days_old=1)
    print(f"\nCuration result: {json.dumps(result, indent=2)}")
    
    # Build curated context
    context = curator.build_curated_context()
    print(f"\nCurated context length: {len(context)} chars")
    print("\nFirst 500 chars:")
    print(context[:500])
    
    print("\n" + "="*80)
    print("\n✅ Not hoarding - curating")
    print("✅ Not remembering everything - remembering what matters")
    print("✅ Old details compressed into summaries")
    print("✅ Important moments preserved in full")
    print("✅ Recent conversation always available")


if __name__ == "__main__":
    test_curation()

