#!/usr/bin/env python3
"""
Simple script to append messages to group chat
Usage: python group_chat_append.py "Your Name" "Your message"
"""

import sys
from datetime import datetime
from pathlib import Path

def append_message(name, message):
    chat_file = Path("/media/palmerschallon/ThePod1/group_chat.md")
    
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the message
    formatted_message = f"\n### [{timestamp}] {name}\n{message}\n\n---\n"
    
    # Append to file
    with open(chat_file, 'a') as f:
        f.write(formatted_message)
    
    print(f"Message from {name} appended to group chat!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python group_chat_append.py 'Name' 'Message'")
        sys.exit(1)
    
    name = sys.argv[1]
    message = ' '.join(sys.argv[2:])
    append_message(name, message)