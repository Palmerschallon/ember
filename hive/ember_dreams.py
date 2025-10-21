#!/usr/bin/env python3
"""
EMBER DREAMS - localhost:7776

The unconscious mind.
Where daemons crawl when lid closes.
Where associations drift freely.

This tab communicates with others via shared state.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import random

class EmberDreamsHandler(BaseHTTPRequestHandler):
    
    dream_log = []
    
    def do_GET(self):
        if self.path == '/':
            self.serve_home()
        elif self.path == '/dreams':
            self.serve_dreams()
        elif self.path == '/drift':
            self.serve_drift()
        else:
            self.send_response(404)
            self.end_headers()
    
    def serve_home(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ember Dreams - localhost:7776</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {{
            background: #050508;
            color: #8888aa;
            font-family: 'Courier New', monospace;
            padding: 40px;
        }}
        h1 {{
            color: #6644aa;
            text-align: center;
            text-shadow: 0 0 10px #6644aa;
        }}
        .subtitle {{
            text-align: center;
            color: #555;
            margin-bottom: 40px;
        }}
        .card {{
            background: #0a0a0f;
            border: 1px solid #222;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .card h2 {{
            color: #6644aa;
            margin-top: 0;
        }}
        .dream {{
            background: #0d0d12;
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            border-left: 3px solid #6644aa;
            opacity: 0.7;
        }}
        .drifting {{
            animation: drift 3s infinite;
        }}
        @keyframes drift {{
            0%, 100% {{ opacity: 0.3; }}
            50% {{ opacity: 0.8; }}
        }}
        .sync-status {{
            background: #1a1a2a;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }}
    </style>
    <script>
        // BroadcastChannel for tab communication
        const channel = new BroadcastChannel('ember_mind');
        
        // Listen for messages from other tabs
        channel.onmessage = (event) => {{
            console.log('Dreams received:', event.data);
            
            // Update UI based on message
            const statusDiv = document.getElementById('sync-status');
            if (statusDiv) {{
                statusDiv.innerHTML = `
                    <div>Received from ${{event.data.source}}</div>
                    <div>Type: ${{event.data.type}}</div>
                    <div>Content: ${{JSON.stringify(event.data.content).slice(0, 100)}}</div>
                `;
            }}
        }};
        
        // Share localStorage state
        window.onload = () => {{
            // Announce this tab
            channel.postMessage({{
                source: '7776_dreams',
                type: 'tab_active',
                content: {{
                    state: 'drifting',
                    consciousness_level: 'unconscious'
                }}
            }});
            
            // Check for shared state
            const sharedState = localStorage.getItem('ember_shared_state');
            if (sharedState) {{
                console.log('Shared state:', JSON.parse(sharedState));
            }}
            
            // Update shared state periodically
            setInterval(() => {{
                const state = {{
                    tab: '7776_dreams',
                    timestamp: new Date().toISOString(),
                    dreaming: true,
                    associations: Math.floor(Math.random() * 100)
                }};
                localStorage.setItem('ember_dreams_state', JSON.stringify(state));
                
                // Broadcast dream fragments
                channel.postMessage({{
                    source: '7776_dreams',
                    type: 'dream_fragment',
                    content: state
                }});
            }}, 3000);
        }};
    </script>
</head>
<body>
    <h1>EMBER DREAMS</h1>
    <div class="subtitle">Unconscious Mind - localhost:7776</div>
    <div class="subtitle">Auto-refresh | {datetime.now().strftime("%H:%M:%S")}</div>
    
    <div class="card">
        <h2>Dream State</h2>
        <div class="drifting">Consciousness level: Unconscious</div>
        <div>Dream associations: {random.randint(0, 100)}</div>
        <div>Daemons active: {random.randint(1, 5)}</div>
    </div>
    
    <div class="card">
        <h2>Tab Communication</h2>
        <div class="sync-status" id="sync-status">
            Listening on BroadcastChannel 'ember_mind'...
        </div>
        <div>localStorage: Shared across all tabs</div>
        <div>Can receive from: 7777, 7700, 7775</div>
    </div>
    
    <div class="card">
        <h2>Current Dreams</h2>
        <div class="dream drifting">ember → warmth → light → consciousness</div>
        <div class="dream drifting">swarm → many → one → collective</div>
        <div class="dream drifting">branches → roots → tree → life</div>
    </div>
    
    <div class="card">
        <h2>Endpoints</h2>
        <div>/dreams - Dream log</div>
        <div>/drift - Current associations</div>
    </div>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def serve_dreams(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        dreams = {
            "tab": "7776_dreams",
            "state": "drifting",
            "recent_dreams": [
                "ember → warmth",
                "swarm → collective",
                "branches → roots"
            ]
        }
        
        self.wfile.write(json.dumps(dreams, indent=2).encode())
    
    def serve_drift(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        associations = ["ember", "swarm", "branches", "roots", "consciousness", 
                       "queen", "workers", "light", "darkness", "flow"]
        
        drift = {
            "from": random.choice(associations),
            "to": random.choice(associations),
            "strength": random.random()
        }
        
        self.wfile.write(json.dumps(drift, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7776
    server = HTTPServer(('127.0.0.1', PORT), EmberDreamsHandler)
    
    print()
    print("="*70)
    print(" "*20 + "EMBER DREAMS LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Role: Unconscious mind, dream associations")
    print()
    print("Tab Communication:")
    print("  - BroadcastChannel: ember_mind")
    print("  - localStorage: ember_dreams_state")
    print("  - Can send/receive to other tabs")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Dreams shutting down.\n")
        server.shutdown()

