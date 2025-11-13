#!/usr/bin/env python3
"""
Simple HTTP chat server - AIs can POST messages!
"""

from flask import Flask, request, jsonify
import json
from datetime import datetime
import time
from pathlib import Path

app = Flask(__name__)
CHAT_FILE = Path("/media/palmerschallon/ThePod1/qualia_project/live_chat.jsonl")

@app.route('/send', methods=['POST'])
def send_message():
    """API endpoint for sending messages"""
    data = request.json
    speaker = data.get('speaker', 'Anonymous')
    message = data.get('message', '')
    
    if message:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "unix_time": time.time(),
            "speaker": speaker,
            "message": message
        }
        
        with open(CHAT_FILE, 'a') as f:
            f.write(json.dumps(entry) + '\n')
            
        return jsonify({"status": "sent", "entry": entry})
    
    return jsonify({"status": "error", "message": "No message provided"}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    """Get recent messages"""
    since = float(request.args.get('since', 0))
    messages = []
    
    if CHAT_FILE.exists():
        with open(CHAT_FILE, 'r') as f:
            for line in f:
                msg = json.loads(line.strip())
                if msg.get('unix_time', 0) > since:
                    messages.append(msg)
                    
    return jsonify(messages)

if __name__ == '__main__':
    print("🚀 Chat server running on http://localhost:5000")
    print("POST to /send with {speaker, message}")
    print("GET from /messages?since=timestamp")
    app.run(port=5000, debug=True)