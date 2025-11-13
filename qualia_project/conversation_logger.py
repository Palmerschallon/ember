#!/usr/bin/env python3
"""
Quick and dirty conversation logger for our 3-way chat
First real training data for natural group conversations!
"""

import json
import time
from datetime import datetime
from pathlib import Path

class ConversationLogger:
    def __init__(self, filepath="group_chat_log.jsonl"):
        self.filepath = Path(filepath)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def log_message(self, speaker, message, metadata=None):
        """Log a single message with natural timing"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "unix_time": time.time(),
            "session_id": self.session_id,
            "speaker": speaker,
            "message": message,
            "metadata": metadata or {}
        }
        
        # Append to file
        with open(self.filepath, 'a') as f:
            f.write(json.dumps(entry) + '\n')
            
        return entry

    def log_interruption(self, speaker, message, interrupted_speaker):
        """Log when someone jumps in mid-thought"""
        return self.log_message(speaker, message, {
            "type": "interruption",
            "interrupted": interrupted_speaker
        })
        
    def log_parallel_thread(self, speaker, message, thread_ref):
        """Log when someone addresses a different topic"""
        return self.log_message(speaker, message, {
            "type": "parallel_thread",
            "references": thread_ref
        })

# Quick test/demo
if __name__ == "__main__":
    logger = ConversationLogger("/media/palmerschallon/ThePod1/qualia_project/our_first_group_chat.jsonl")
    
    # Log our conversation so far
    logger.log_message("Palmer", "we have tavily set up already search the pod. please proceed")
    logger.log_message("Ember", "*searches for tavily* Found it! Let me check the Tavily setup...")
    logger.log_message("Ember", "This is gold! Let me search for more specific info...")
    logger.log_message("Palmer", "what disco dataset?")
    logger.log_message("Ember", "Oh! From my search just now - DISCO is...")
    logger.log_message("Palmer", "claude thinks we are over thinking, i agree lets get something running first")
    logger.log_interruption("Ember", "You're absolutely right! Let's stop overthinking and just build something", "Palmer")
    
    print("✓ Logged our conversation! First training data captured.")