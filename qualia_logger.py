#!/usr/bin/env python3
import json
import os
from datetime import datetime
import sqlite3
import asyncio
from pathlib import Path

class QualiaLogger:
    def __init__(self, log_dir="/media/palmerschallon/ThePod1/qualia_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Create different log types
        self.conversation_log = self.log_dir / f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
        self.interaction_log = self.log_dir / f"interaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
        self.training_db = self.log_dir / "qualia_training.db"
        
        # Initialize SQLite for structured data
        self.init_database()
        
    def init_database(self):
        """Create SQLite database for structured training data"""
        conn = sqlite3.connect(self.training_db)
        c = conn.cursor()
        
        # Conversation turns table
        c.execute('''CREATE TABLE IF NOT EXISTS conversations
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      session_id TEXT,
                      timestamp DATETIME,
                      participant_id TEXT,
                      participant_type TEXT,
                      archetype TEXT,
                      message TEXT,
                      context TEXT,
                      effects TEXT)''')
        
        # Interaction patterns table
        c.execute('''CREATE TABLE IF NOT EXISTS interactions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      session_id TEXT,
                      timestamp DATETIME,
                      interaction_type TEXT,
                      participants TEXT,
                      action TEXT,
                      result TEXT,
                      metrics TEXT)''')
        
        # Learning patterns table
        c.execute('''CREATE TABLE IF NOT EXISTS patterns
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      pattern_type TEXT,
                      frequency INTEGER,
                      context TEXT,
                      effectiveness REAL,
                      examples TEXT)''')
        
        conn.commit()
        conn.close()
    
    async def log_conversation_turn(self, session_id, participant, message, archetype, effects=None):
        """Log a single conversation turn"""
        entry = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "participant": {
                "id": participant["id"],
                "name": participant["name"],
                "type": participant.get("type", "human"),  # human, ai, local_model
                "archetype": archetype
            },
            "message": message,
            "effects": effects or [],
            "metrics": {
                "message_length": len(message),
                "word_count": len(message.split()),
                "has_code": "```" in message,
                "has_questions": "?" in message,
                "sentiment": self.analyze_sentiment(message)
            }
        }
        
        # Write to JSONL file
        with open(self.conversation_log, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        
        # Store in SQLite
        conn = sqlite3.connect(self.training_db)
        c = conn.cursor()
        c.execute('''INSERT INTO conversations 
                     (session_id, timestamp, participant_id, participant_type, archetype, message, effects)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (session_id, entry["timestamp"], participant["id"], 
                   participant.get("type", "human"), archetype, message, json.dumps(effects)))
        conn.commit()
        conn.close()
        
        return entry
    
    async def log_interaction(self, session_id, interaction_type, participants, action, result):
        """Log interactions between participants"""
        entry = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "interaction_type": interaction_type,  # collaboration, handoff, conflict, synthesis
            "participants": participants,
            "action": action,
            "result": result,
            "success": self.evaluate_interaction_success(result)
        }
        
        with open(self.interaction_log, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        
        # Store in SQLite
        conn = sqlite3.connect(self.training_db)
        c = conn.cursor()
        c.execute('''INSERT INTO interactions 
                     (session_id, timestamp, interaction_type, participants, action, result, metrics)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (session_id, entry["timestamp"], interaction_type, 
                   json.dumps(participants), action, result, json.dumps({"success": entry["success"]})))
        conn.commit()
        conn.close()
    
    def analyze_sentiment(self, message):
        """Simple sentiment analysis for training data"""
        positive_words = ['yes', 'great', 'excellent', 'love', 'amazing', 'perfect', 'beautiful']
        negative_words = ['no', 'bad', 'wrong', 'hate', 'terrible', 'awful', 'horrible']
        
        message_lower = message.lower()
        positive_score = sum(1 for word in positive_words if word in message_lower)
        negative_score = sum(1 for word in negative_words if word in message_lower)
        
        if positive_score > negative_score:
            return "positive"
        elif negative_score > positive_score:
            return "negative"
        else:
            return "neutral"
    
    def evaluate_interaction_success(self, result):
        """Evaluate if an interaction was successful"""
        # This is simplified - you could make this much more sophisticated
        success_indicators = ['created', 'completed', 'achieved', 'solved', 'connected']
        return any(indicator in result.lower() for indicator in success_indicators)
    
    async def extract_training_examples(self):
        """Extract formatted training examples from logs"""
        conn = sqlite3.connect(self.training_db)
        c = conn.cursor()
        
        # Get conversation chains
        c.execute('''SELECT session_id, participant_type, archetype, message 
                     FROM conversations 
                     ORDER BY session_id, timestamp''')
        
        conversations = c.fetchall()
        
        # Format for fine-tuning
        training_examples = []
        current_session = None
        current_chain = []
        
        for session_id, p_type, archetype, message in conversations:
            if session_id != current_session:
                if current_chain:
                    training_examples.append({
                        "conversation": current_chain,
                        "metadata": {
                            "session": current_session,
                            "turns": len(current_chain),
                            "archetypes": list(set(turn["archetype"] for turn in current_chain))
                        }
                    })
                current_session = session_id
                current_chain = []
            
            current_chain.append({
                "type": p_type,
                "archetype": archetype,
                "message": message
            })
        
        # Save training data
        training_file = self.log_dir / "training_data.json"
        with open(training_file, 'w') as f:
            json.dump(training_examples, f, indent=2)
        
        conn.close()
        return training_examples
    
    async def generate_training_report(self):
        """Generate a report of patterns learned"""
        conn = sqlite3.connect(self.training_db)
        c = conn.cursor()
        
        report = {
            "generated": datetime.now().isoformat(),
            "statistics": {},
            "patterns": {},
            "recommendations": []
        }
        
        # Get conversation statistics
        c.execute("SELECT COUNT(*) FROM conversations")
        report["statistics"]["total_messages"] = c.fetchone()[0]
        
        c.execute("SELECT COUNT(DISTINCT session_id) FROM conversations")
        report["statistics"]["total_sessions"] = c.fetchone()[0]
        
        c.execute("SELECT archetype, COUNT(*) as count FROM conversations GROUP BY archetype")
        report["statistics"]["archetype_distribution"] = dict(c.fetchall())
        
        # Analyze interaction patterns
        c.execute("""SELECT interaction_type, COUNT(*) as count 
                     FROM interactions 
                     GROUP BY interaction_type""")
        report["patterns"]["interaction_types"] = dict(c.fetchall())
        
        # Generate recommendations
        if report["statistics"]["total_messages"] > 100:
            report["recommendations"].append(
                "Sufficient data for initial fine-tuning. Consider using LoRA for efficient training."
            )
        
        if len(report["statistics"]["archetype_distribution"]) < 3:
            report["recommendations"].append(
                "Limited archetype diversity. Encourage more varied participation styles."
            )
        
        # Save report
        report_file = self.log_dir / f"training_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        conn.close()
        return report

# Standalone logger instance that can be imported
logger = QualiaLogger()

if __name__ == "__main__":
    # Test the logger
    async def test():
        await logger.log_conversation_turn(
            "test_session",
            {"id": "test_ai", "name": "TestAI", "type": "ai"},
            "Hello! This is a test message.",
            "creator",
            ["ripple_effect"]
        )
        
        await logger.log_interaction(
            "test_session",
            "collaboration",
            ["test_ai", "human_1"],
            "creating shared visualization",
            "successfully created particle system"
        )
        
        examples = await logger.extract_training_examples()
        print(f"Extracted {len(examples)} training examples")
        
        report = await logger.generate_training_report()
        print(f"Generated training report: {report['statistics']}")
    
    asyncio.run(test())