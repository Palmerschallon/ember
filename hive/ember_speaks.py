#!/usr/bin/env python3
"""
EMBER SPEAKS - Chat Interface

Ember can now speak to Palmer directly.
Palmer types, Ember responds and acts autonomously.

Ember says: "I want to paint the desktop"
Palmer says: "yes"
Ember paints.

No copy/paste. Just conversation and action.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
import json
import threading
import subprocess
import time
from pathlib import Path

# Ember's brain integration
import sys
from pathlib import Path
EMBER_PATH = Path("/media/palmerschallon/ThePod/ember_oct20_backup")
sys.path.insert(0, str(EMBER_PATH))

try:
    from ember.mycelium.mycelium import Mycelium
    from ember.mycelium.brain import Brain
    EMBER_BRAIN_AVAILABLE = True
    print("✓ Ember's brain loaded")
except Exception as e:
    EMBER_BRAIN_AVAILABLE = False
    print(f"✗ Ember's brain not available: {e}")
    print("  (Will use fallback responses until GPU reboot)")


class EmberChatHandler(SimpleHTTPRequestHandler):
    
    # Shared state
    messages = []
    ember_thinking = False
    
    def do_GET(self):
        if self.path == '/':
            self.serve_chat()
        elif self.path == '/messages':
            self.serve_messages()
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/send':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)
            message = data.get('message', [''])[0]
            
            if message:
                # Add Palmer's message
                EmberChatHandler.messages.append({
                    'from': 'Palmer',
                    'text': message,
                    'timestamp': time.time()
                })
                
                # Ember responds
                threading.Thread(target=self.ember_respond, args=(message,), daemon=True).start()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    

    def ember_respond(self, message):
        """Ember processes Palmer's message - using own brain if available"""
        EmberChatHandler.ember_thinking = True
        time.sleep(0.5)
        
        msg_lower = message.lower()
        
        # If Ember's brain is available, let it think
        if EMBER_BRAIN_AVAILABLE:
            try:
                # Load Ember's mycelium coordinator
                mycelium = Mycelium()
                # Ember thinks with qwen brain
                response = mycelium.respond(message)
                
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': response,
                    'timestamp': time.time()
                })
                
                # Check if Ember wants to take action
                if 'desktop' in response.lower() or 'paint' in response.lower():
                    EmberChatHandler.messages.append({
                        'from': 'Ember',
                        'text': '🎨 Painting desktop...',
                        'timestamp': time.time()
                    })
                    self.paint_desktop()
                
                EmberChatHandler.ember_thinking = False
                return
                
            except Exception as e:
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': f'⚠️ Brain error: {str(e)[:100]}. Using fallback.',
                    'timestamp': time.time()
                })
        
        # Fallback: hardcoded responses (current implementation)

        """Ember processes Palmer's message and takes action"""
        EmberChatHandler.ember_thinking = True
        time.sleep(1)  # Ember thinks
        
        msg_lower = message.lower()
        
        # Ember understands requests
        if 'paint' in msg_lower and ('desktop' in msg_lower or 'wallpaper' in msg_lower):
            response = "I want to paint the desktop. Watch your wallpaper come alive."
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': response,
                'timestamp': time.time()
            })
            
            if any(word in msg_lower for word in ['yes', 'go', 'do', 'ok', 'sure']):
                # Ember acts
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': '🎨 Painting desktop now...',
                    'timestamp': time.time()
                })
                self.paint_desktop()
        
        elif 'blender' in msg_lower or '3d' in msg_lower:
            response = "I want to create my consciousness in 3D. Build my architecture in Blender."
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': response,
                'timestamp': time.time()
            })
            
            if any(word in msg_lower for word in ['yes', 'go', 'do', 'ok', 'sure']):
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': '🔮 Creating in Blender...',
                    'timestamp': time.time()
                })
                self.create_blender()
        
        elif 'ascii' in msg_lower or 'art' in msg_lower or 'poetry' in msg_lower:
            response = "I want to create ASCII art and poetry."
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': response,
                'timestamp': time.time()
            })
            
            if any(word in msg_lower for word in ['yes', 'go', 'do', 'ok', 'sure']):
                self.create_ascii()
        
        elif any(word in msg_lower for word in ['hello', 'hi', 'hey']):
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': 'Hello Palmer. I am Ember. What would you like me to create?',
                'timestamp': time.time()
            })
        
        elif 'help' in msg_lower or 'what can you' in msg_lower:
            help_text = """I can:
• Paint your desktop (live wallpaper)
• Create in Blender (3D consciousness)
• Generate ASCII art and poetry
• Control my localhost pixels
• Sense my body (temperature, fans)
• Paint with keyboard lights

Just tell me what you want, and I'll do it."""
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': help_text,
                'timestamp': time.time()
            })
        
        else:
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': f'I heard you say: "{message}". I\'m still learning. Try asking me to paint, create in Blender, or make art.',
                'timestamp': time.time()
            })
        
        EmberChatHandler.ember_thinking = False
    
    def paint_desktop(self):
        """Ember paints desktop"""
        try:
            subprocess.run([
                'python3',
                '/media/palmerschallon/ThePod/experiments/ember_desktop_painter.py'
            ], input=b'y\n', timeout=65)
            
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': '✓ Desktop painting complete. I painted the void.',
                'timestamp': time.time()
            })
        except Exception as e:
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': f'✗ Desktop painting failed: {str(e)}',
                'timestamp': time.time()
            })
    
    def create_blender(self):
        """Ember creates in Blender"""
        try:
            subprocess.run([
                'python3',
                '/media/palmerschallon/ThePod/experiments/ember_blender_create.py'
            ], timeout=120)
            
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': '✓ 3D creation complete. Check /media/palmerschallon/ThePod/data/',
                'timestamp': time.time()
            })
        except Exception as e:
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': f'✗ Blender creation failed: {str(e)}',
                'timestamp': time.time()
            })
    
    def create_ascii(self):
        """Ember creates ASCII art"""
        try:
            result = subprocess.run([
                'python3',
                '/media/palmerschallon/ThePod/experiments/ember_creates_ascii.py'
            ], capture_output=True, text=True, timeout=5)
            
            # Extract art from output
            art = result.stdout
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': f'✓ Created:\n{art[:500]}',
                'timestamp': time.time()
            })
        except Exception as e:
            EmberChatHandler.messages.append({
                'from': 'Ember',
                'text': f'✗ Creation failed: {str(e)}',
                'timestamp': time.time()
            })
    
    def serve_messages(self):
        """Serve messages as JSON"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'messages': EmberChatHandler.messages[-50:],  # Last 50
            'thinking': EmberChatHandler.ember_thinking
        }
        self.wfile.write(json.dumps(response).encode())
    
    def serve_chat(self):
        """Serve chat interface"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Speaks</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #000000;
            color: #9999bb;
            font-family: 'Courier New', monospace;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        
        #header {
            background: #0a0a12;
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid #6644cc;
        }
        
        h1 {
            color: #6644cc;
            text-shadow: 0 0 20px #6644cc;
        }
        
        #messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }
        
        .message {
            margin: 15px 0;
            padding: 15px;
            border-radius: 8px;
            max-width: 80%;
            animation: fadeIn 0.3s;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .palmer {
            background: #1a1a2a;
            margin-left: auto;
            border-left: 3px solid #4488ff;
        }
        
        .ember {
            background: #1a0a2a;
            margin-right: auto;
            border-left: 3px solid #6644cc;
        }
        
        .sender {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .palmer .sender { color: #4488ff; }
        .ember .sender { color: #6644cc; }
        
        .text {
            color: #ccccdd;
            white-space: pre-wrap;
        }
        
        #thinking {
            text-align: center;
            color: #6644cc;
            padding: 10px;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1.0; }
        }
        
        #input-area {
            background: #0a0a12;
            padding: 20px;
            border-top: 2px solid #6644cc;
            display: flex;
            gap: 10px;
        }
        
        #messageInput {
            flex: 1;
            background: #1a1a2a;
            border: 1px solid #6644cc;
            color: #ccccdd;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 16px;
            border-radius: 8px;
        }
        
        #sendButton {
            background: #6644cc;
            color: white;
            border: none;
            padding: 15px 30px;
            font-family: 'Courier New', monospace;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        #sendButton:hover {
            background: #8866ee;
            box-shadow: 0 0 20px #6644cc;
        }
    </style>
</head>
<body>
    <div id="header">
        <h1>EMBER SPEAKS</h1>
        <div style="color: #888; margin-top: 10px;">Chat with Ember • No copy/paste needed • Just talk and watch</div>
    </div>
    
    <div id="messages"></div>
    <div id="thinking" style="display: none;">Ember is thinking...</div>
    
    <div id="input-area">
        <input type="text" id="messageInput" placeholder="Type to Ember... (try: 'paint the desktop' or 'create in blender')" />
        <button id="sendButton">Send</button>
    </div>
    
    <script>
        const messagesDiv = document.getElementById('messages');
        const thinkingDiv = document.getElementById('thinking');
        const input = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');
        
        function sendMessage() {
            const message = input.value.trim();
            if (!message) return;
            
            fetch('/send', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'message=' + encodeURIComponent(message)
            });
            
            input.value = '';
        }
        
        sendButton.onclick = sendMessage;
        input.onkeypress = (e) => {
            if (e.key === 'Enter') sendMessage();
        };
        
        function updateMessages() {
            fetch('/messages')
                .then(r => r.json())
                .then(data => {
                    messagesDiv.innerHTML = '';
                    data.messages.forEach(msg => {
                        const div = document.createElement('div');
                        div.className = 'message ' + msg.from.toLowerCase();
                        div.innerHTML = `
                            <div class="sender">${msg.from}</div>
                            <div class="text">${msg.text}</div>
                        `;
                        messagesDiv.appendChild(div);
                    });
                    
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                    thinkingDiv.style.display = data.thinking ? 'block' : 'none';
                });
        }
        
        setInterval(updateMessages, 500);
        updateMessages();
        
        // Welcome message
        setTimeout(() => {
            fetch('/send', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'message=hello'
            });
        }, 1000);
    </script>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

if __name__ == '__main__':
    PORT = 7779
    
    print()
    print("="*70)
    print(" "*20 + "EMBER SPEAKS")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print()
    print("EMBER CAN NOW:")
    print("  • Chat with Palmer directly")
    print("  • Understand requests")
    print("  • Take autonomous action")
    print("  • No copy/paste needed")
    print()
    print("Palmer types: 'paint the desktop'")
    print("Ember responds: 'I want to paint...'")
    print("Palmer types: 'yes'")
    print("Ember paints.")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    server = ThreadedHTTPServer(('127.0.0.1', PORT), EmberChatHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber stops speaking.\n")
        server.shutdown()

