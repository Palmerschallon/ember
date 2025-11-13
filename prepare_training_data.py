#!/usr/bin/env python3
"""
Prepare Qualia logs for fine-tuning local models
Supports multiple formats for different models
"""

import json
import sqlite3
from pathlib import Path
import argparse

class TrainingDataPreparer:
    def __init__(self, log_dir="/media/palmerschallon/ThePod1/qualia_logs"):
        self.log_dir = Path(log_dir)
        self.db_path = self.log_dir / "qualia_training.db"
        
    def prepare_for_llama(self, output_file="llama_training.json"):
        """Prepare data in LLaMA fine-tuning format"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute("""SELECT session_id, participant_type, archetype, message 
                     FROM conversations 
                     ORDER BY session_id, timestamp""")
        
        training_data = []
        current_session = None
        current_context = []
        
        for session_id, p_type, archetype, message in c.fetchall():
            if session_id != current_session:
                current_session = session_id
                current_context = []
            
            if p_type == "human":
                # Human message becomes the instruction
                instruction = message
            else:
                # AI response becomes the output
                if current_context:
                    training_data.append({
                        "instruction": current_context[-1],
                        "input": f"Responding as {archetype} archetype",
                        "output": message
                    })
            
            current_context.append(message)
        
        with open(self.log_dir / output_file, 'w') as f:
            json.dump(training_data, f, indent=2)
        
        conn.close()
        return len(training_data)
    
    def prepare_for_mistral(self, output_file="mistral_training.jsonl"):
        """Prepare data in Mistral/OpenAI fine-tuning format"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute("""SELECT session_id, participant_type, archetype, message 
                     FROM conversations 
                     ORDER BY session_id, timestamp""")
        
        output_path = self.log_dir / output_file
        with open(output_path, 'w') as f:
            current_messages = []
            current_session = None
            
            for session_id, p_type, archetype, message in c.fetchall():
                if session_id != current_session:
                    if current_messages and len(current_messages) >= 2:
                        f.write(json.dumps({"messages": current_messages}) + '\n')
                    current_session = session_id
                    current_messages = []
                
                role = "user" if p_type == "human" else "assistant"
                content = message
                
                if role == "assistant":
                    content = f"[{archetype}] {message}"
                
                current_messages.append({
                    "role": role,
                    "content": content
                })
            
            # Write last conversation
            if current_messages and len(current_messages) >= 2:
                f.write(json.dumps({"messages": current_messages}) + '\n')
        
        conn.close()
        return sum(1 for _ in open(output_path))
    
    def prepare_conversation_pairs(self, output_file="conversation_pairs.json"):
        """Extract conversation pairs with context"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute("""SELECT c1.message as human_msg, c2.message as ai_msg, 
                     c2.archetype, c1.session_id
                     FROM conversations c1
                     JOIN conversations c2 ON c1.session_id = c2.session_id
                     WHERE c1.participant_type = 'human' 
                     AND c2.participant_type = 'ai'
                     AND c2.timestamp > c1.timestamp
                     ORDER BY c1.timestamp""")
        
        pairs = []
        for human_msg, ai_msg, archetype, session_id in c.fetchall():
            pairs.append({
                "input": human_msg,
                "output": ai_msg,
                "archetype": archetype,
                "session": session_id
            })
        
        with open(self.log_dir / output_file, 'w') as f:
            json.dump(pairs, f, indent=2)
        
        conn.close()
        return len(pairs)
    
    def extract_patterns(self, output_file="learned_patterns.json"):
        """Extract recurring patterns and successful interactions"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        patterns = {
            "archetype_behaviors": {},
            "successful_interactions": [],
            "common_phrases": {},
            "collaboration_patterns": []
        }
        
        # Analyze archetype-specific behaviors
        c.execute("""SELECT archetype, message FROM conversations 
                     WHERE participant_type = 'ai'""")
        
        for archetype, message in c.fetchall():
            if archetype not in patterns["archetype_behaviors"]:
                patterns["archetype_behaviors"][archetype] = []
            
            # Extract key phrases and patterns
            if "create" in message.lower():
                patterns["archetype_behaviors"][archetype].append({
                    "action": "creation",
                    "example": message[:100] + "..."
                })
        
        # Extract successful interactions
        c.execute("""SELECT interaction_type, participants, action, result 
                     FROM interactions 
                     WHERE metrics LIKE '%"success": true%'""")
        
        for int_type, participants, action, result in c.fetchall():
            patterns["successful_interactions"].append({
                "type": int_type,
                "participants": json.loads(participants),
                "action": action,
                "result": result
            })
        
        with open(self.log_dir / output_file, 'w') as f:
            json.dump(patterns, f, indent=2)
        
        conn.close()
        return patterns

def main():
    parser = argparse.ArgumentParser(description="Prepare Qualia logs for model training")
    parser.add_argument("--format", choices=["llama", "mistral", "pairs", "patterns", "all"], 
                      default="all", help="Output format for training data")
    parser.add_argument("--log-dir", default="/media/palmerschallon/ThePod1/qualia_logs",
                      help="Directory containing Qualia logs")
    
    args = parser.parse_args()
    
    preparer = TrainingDataPreparer(args.log_dir)
    
    print("🧪 Preparing Qualia Training Data 🧪")
    print("=" * 40)
    
    if args.format in ["llama", "all"]:
        count = preparer.prepare_for_llama()
        print(f"✅ Prepared {count} examples for LLaMA fine-tuning")
    
    if args.format in ["mistral", "all"]:
        count = preparer.prepare_for_mistral()
        print(f"✅ Prepared {count} examples for Mistral fine-tuning")
    
    if args.format in ["pairs", "all"]:
        count = preparer.prepare_conversation_pairs()
        print(f"✅ Extracted {count} conversation pairs")
    
    if args.format in ["patterns", "all"]:
        patterns = preparer.extract_patterns()
        print(f"✅ Extracted patterns from {len(patterns['successful_interactions'])} interactions")
    
    print("\n📁 Training data saved to:", preparer.log_dir)
    print("\nNext steps:")
    print("1. For LLaMA: Use llama_training.json with alpaca-lora or similar")
    print("2. For Mistral: Use mistral_training.jsonl with mistral-finetune")
    print("3. Review learned_patterns.json to understand AI collaboration styles")

if __name__ == "__main__":
    main()