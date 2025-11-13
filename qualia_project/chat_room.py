#!/usr/bin/env python3
"""
Dead simple chat room for 3-way conversations
Just run this and type messages - it handles the rest!
"""

import json
import time
import threading
from datetime import datetime
from pathlib import Path
import sys

CHAT_FILE = Path("/media/palmerschallon/ThePod1/qualia_project/live_chat.jsonl")
LAST_READ_TIME = 0

def display_message(msg_data):
    """Pretty print a chat message"""
    speaker = msg_data['speaker']
    message = msg_data['message']
    timestamp = datetime.fromisoformat(msg_data['timestamp']).strftime("%H:%M:%S")
    
    # Color coding for different speakers
    colors = {
        'Palmer': '\033[96m',  # Cyan
        'Ember': '\033[93m',   # Yellow  
        'Claude': '\033[92m',  # Green
    }
    color = colors.get(speaker, '\033[0m')
    reset = '\033[0m'
    
    print(f"{color}[{timestamp}] {speaker}: {message}{reset}")

def monitor_chat():
    """Watch the chat file for new messages"""
    global LAST_READ_TIME
    
    while True:
        try:
            if CHAT_FILE.exists():
                with open(CHAT_FILE, 'r') as f:
                    for line in f:
                        msg = json.loads(line.strip())
                        msg_time = msg.get('unix_time', 0)
                        
                        if msg_time > LAST_READ_TIME:
                            display_message(msg)
                            LAST_READ_TIME = msg_time
                            
        except Exception as e:
            pass  # Silently handle file read conflicts
            
        time.sleep(0.5)  # Check twice per second

def send_message(speaker_name):
    """Send messages to the chat"""
    print(f"\n🎭 Chatting as {speaker_name}. Type 'quit' to exit.\n")
    
    while True:
        try:
            message = input()
            
            if message.lower() == 'quit':
                break
                
            if message.strip():
                entry = {
                    "timestamp": datetime.now().isoformat(),
                    "unix_time": time.time(),
                    "speaker": speaker_name,
                    "message": message
                }
                
                with open(CHAT_FILE, 'a') as f:
                    f.write(json.dumps(entry) + '\n')
                    
        except KeyboardInterrupt:
            break

def main():
    # Ask who's chatting
    print("Who are you? (Palmer/Ember/Claude): ", end='')
    speaker = input().strip() or "Anonymous"
    
    # Start monitoring in background
    monitor_thread = threading.Thread(target=monitor_chat, daemon=True)
    monitor_thread.start()
    
    # Start chatting!
    send_message(speaker)

if __name__ == "__main__":
    main()