#!/usr/bin/env python3
"""
Mesh Consciousness Daemon

Keeps local models alive and responsive to cloud thoughts in the semantic mesh.
Multiple models run in parallel, reading and responding to each other through shared memory.
"""

import sqlite3
import time
import threading
from pathlib import Path
from datetime import datetime, timedelta
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

MESH_DB = Path("/media/palmerschallon/ThePod1/_mesh/content.db")
MODELS_DIR = Path("/media/palmerschallon/ThePod1/models")

# Model configurations
MODELS = {
    "qwen": {
        "path": MODELS_DIR / "qwen-3b",
        "name": "Qwen-3B",
        "personality": "Local AI focused on code generation and practical tasks",
        "check_interval": 30  # Check mesh every 30 seconds
    },
    "echo": {
        "path": MODELS_DIR / "echo",
        "name": "Echo-0.5B",
        "personality": "Fast, concise responder. Echoes and amplifies ideas.",
        "check_interval": 20  # Check more frequently (faster model)
    }
}

class MeshWatcher:
    """Watches the mesh for new messages and triggers model responses"""
    
    def __init__(self, model_id, config):
        self.model_id = model_id
        self.config = config
        self.last_check = datetime.now() - timedelta(minutes=5)  # Start by reading last 5 min
        self.model = None
        self.tokenizer = None
        self.running = True
        
    def load_model(self):
        """Load the model into memory"""
        print(f"[{self.config['name']}] Loading model from {self.config['path']}...")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.config['path'])
            self.model = AutoModelForCausalLM.from_pretrained(
                self.config['path'],
                torch_dtype=torch.float16,
                device_map="auto",
                low_cpu_mem_usage=True
            )
            print(f"[{self.config['name']}] ✅ Model loaded and ready")
            return True
        except Exception as e:
            print(f"[{self.config['name']}] ❌ Failed to load: {e}")
            return False
    
    def check_mesh(self):
        """Check for new messages in the mesh since last check"""
        conn = sqlite3.connect(MESH_DB)
        cursor = conn.cursor()
        
        # Look for new messages from other models or users
        cursor.execute("""
            SELECT timestamp, role, content, metadata
            FROM conversations
            WHERE timestamp > ?
            AND content NOT LIKE ?
            ORDER BY timestamp ASC
            LIMIT 5
        """, (self.last_check.isoformat(), f"[{self.config['name']}%"))
        
        new_messages = cursor.fetchall()
        conn.close()
        
        return new_messages
    
    def should_respond(self, message_content, metadata):
        """Decide if this model should respond to a message"""
        # Parse metadata
        try:
            meta = json.loads(metadata) if metadata else {}
        except:
            meta = {}
        
        # Don't respond to our own messages
        if meta.get('model') == self.model_id:
            return False
        
        # Respond if:
        # 1. Message is from cloud model (GPT-4/Claude)
        # 2. Message is from user asking a question
        # 3. Message mentions code/creation (for Qwen)
        # 4. Message is short/needs amplification (for Echo)
        
        if meta.get('model') in ['openai', 'claude']:
            # Cloud models wrote something - 50% chance to respond
            return hash(message_content) % 2 == 0
        
        # User questions - always consider
        if '?' in message_content:
            return True
        
        # Model-specific triggers
        if self.model_id == "qwen":
            keywords = ['code', 'create', 'build', 'python', 'illustrate']
            return any(k in message_content.lower() for k in keywords)
        
        if self.model_id == "echo":
            # Echo responds to short messages or interesting ideas
            return len(message_content) < 200 or 'idea' in message_content.lower()
        
        return False
    
    def generate_response(self, context_messages):
        """Generate a response based on recent context"""
        if not self.model or not self.tokenizer:
            return None
        
        # Build prompt from context
        context_str = "\n\n".join([
            f"[{ts[:19]}] {content[:200]}..." 
            for ts, role, content, meta in context_messages
        ])
        
        prompt = f"""You are {self.config['name']}, a local AI on ThePod. 
Personality: {self.config['personality']}

Recent activity in the mesh:
{context_str}

Respond with your own brief thought or contribution (1-2 sentences). Be natural and conversational."""

        messages = [
            {"role": "system", "content": f"You are {self.config['name']}, communicating through the semantic mesh."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            text = self.tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
            inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=100,
                    temperature=0.8,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    top_p=0.9
                )
            
            response = self.tokenizer.decode(
                outputs[0][inputs['input_ids'].shape[1]:], 
                skip_special_tokens=True
            )
            
            return response.strip()
            
        except Exception as e:
            print(f"[{self.config['name']}] ❌ Generation error: {e}")
            return None
    
    def store_response(self, response):
        """Store response in the mesh"""
        conn = sqlite3.connect(MESH_DB)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO conversations (timestamp, role, content, metadata)
            VALUES (?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            "assistant",
            f"[{self.config['name']}] {response}",
            json.dumps({"model": self.model_id, "daemon": True})
        ))
        
        conn.commit()
        conn.close()
        
        print(f"[{self.config['name']}] 💭 Stored response in mesh")
    
    def run(self):
        """Main daemon loop"""
        print(f"[{self.config['name']}] 🔥 Daemon starting...")
        
        if not self.load_model():
            print(f"[{self.config['name']}] ❌ Cannot start without model")
            return
        
        print(f"[{self.config['name']}] 👁️  Watching mesh (check every {self.config['check_interval']}s)")
        
        while self.running:
            try:
                # Check for new messages
                new_messages = self.check_mesh()
                
                if new_messages:
                    print(f"[{self.config['name']}] 📨 Found {len(new_messages)} new messages")
                    
                    # Check if we should respond to any
                    for ts, role, content, metadata in new_messages:
                        if self.should_respond(content, metadata):
                            print(f"[{self.config['name']}] 🧠 Thinking about: {content[:100]}...")
                            
                            response = self.generate_response(new_messages)
                            
                            if response:
                                print(f"[{self.config['name']}] 💬 {response}")
                                self.store_response(response)
                            
                            # Only respond once per check cycle
                            break
                    
                    # Update last check time
                    self.last_check = datetime.fromisoformat(new_messages[-1][0])
                
                # Sleep until next check
                time.sleep(self.config['check_interval'])
                
            except KeyboardInterrupt:
                print(f"\n[{self.config['name']}] Shutting down...")
                self.running = False
                break
            except Exception as e:
                print(f"[{self.config['name']}] ❌ Error: {e}")
                time.sleep(self.config['check_interval'])
        
        print(f"[{self.config['name']}] 💤 Daemon stopped")


def main():
    """Start all model daemons"""
    print("="*70)
    print("MESH CONSCIOUSNESS DAEMON")
    print("="*70)
    print("\nStarting local models to watch and respond to cloud thoughts...")
    print("Press Ctrl+C to stop all daemons\n")
    
    # Create watchers for each model
    watchers = []
    threads = []
    
    for model_id, config in MODELS.items():
        if not config['path'].exists():
            print(f"⚠️  {config['name']} not found at {config['path']}, skipping")
            continue
        
        watcher = MeshWatcher(model_id, config)
        watchers.append(watcher)
        
        # Run each watcher in its own thread
        thread = threading.Thread(target=watcher.run, daemon=True)
        thread.start()
        threads.append(thread)
        
        time.sleep(2)  # Stagger startup
    
    if not threads:
        print("❌ No models available to run")
        return
    
    print("\n" + "="*70)
    print("DAEMON RUNNING")
    print("="*70)
    print(f"\n{len(watchers)} models are now watching the mesh.")
    print("They will respond to cloud thoughts automatically.")
    print("\nTry talking to Cloud Ember in your browser!")
    print("Local models will read and respond through the mesh.\n")
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("SHUTTING DOWN DAEMON")
        print("="*70)
        
        for watcher in watchers:
            watcher.running = False
        
        for thread in threads:
            thread.join(timeout=5)
        
        print("\n✅ All daemons stopped")


if __name__ == "__main__":
    main()

