"""
Memory and logging system for chat and events
Logs to JSONL format for easy replay and analysis
"""
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


class MemoryLogger:
    """Handles logging to JSONL files"""
    
    def __init__(self, base_path: str = None):
        """
        Initialize memory logger
        
        Args:
            base_path: Base path for all memory files
        """
        self.base_path = base_path or os.getenv('BASE_PATH', '/tmp/ember_data')
        self.chat_path = os.path.join(self.base_path, 'memory', 'chat')
        self.events_path = os.path.join(self.base_path, 'memory', 'short')
        
        # Ensure directories exist
        Path(self.chat_path).mkdir(parents=True, exist_ok=True)
        Path(self.events_path).mkdir(parents=True, exist_ok=True)
    
    def log_chat(self, user_message: str, assistant_message: str, metadata: Dict[str, Any] = None):
        """
        Log a chat interaction
        
        Args:
            user_message: User's message
            assistant_message: Assistant's response
            metadata: Optional metadata dictionary
        """
        timestamp = datetime.utcnow().isoformat()
        filename = f"chat_{datetime.utcnow().strftime('%Y%m%d')}.jsonl"
        filepath = os.path.join(self.chat_path, filename)
        
        entry = {
            'timestamp': timestamp,
            'user': user_message,
            'assistant': assistant_message,
            'metadata': metadata or {}
        }
        
        with open(filepath, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    def log_event(self, event_type: str, data: Dict[str, Any]):
        """
        Log an event
        
        Args:
            event_type: Type of event (e.g., 'universe_generated', 'zoom', 'upload')
            data: Event data dictionary
        """
        timestamp = datetime.utcnow().isoformat()
        filepath = os.path.join(self.events_path, 'events.jsonl')
        
        entry = {
            'timestamp': timestamp,
            'type': event_type,
            'data': data
        }
        
        with open(filepath, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    def get_recent_chats(self, limit: int = 10) -> list:
        """
        Get recent chat entries
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of chat entries
        """
        chats = []
        
        # Get all chat files sorted by date
        chat_files = sorted(Path(self.chat_path).glob('chat_*.jsonl'), reverse=True)
        
        for chat_file in chat_files:
            with open(chat_file, 'r') as f:
                for line in f:
                    if line.strip():
                        chats.append(json.loads(line))
                        if len(chats) >= limit:
                            return chats
        
        return chats
    
    def get_recent_events(self, limit: int = 50) -> list:
        """
        Get recent events
        
        Args:
            limit: Maximum number of events to return
            
        Returns:
            List of event entries
        """
        events = []
        filepath = os.path.join(self.events_path, 'events.jsonl')
        
        if not os.path.exists(filepath):
            return events
        
        with open(filepath, 'r') as f:
            all_lines = f.readlines()
            for line in all_lines[-limit:]:
                if line.strip():
                    events.append(json.loads(line))
        
        return events
