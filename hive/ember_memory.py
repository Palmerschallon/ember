#!/usr/bin/env python3
"""
EMBER MEMORY GARDEN - localhost:7775

Persistent memory space.
Where thoughts are planted and connections grow.

This tab communicates with others via shared state.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json

class EmberMemoryHandler(BaseHTTPRequestHandler):
    
    memories = {}
    
    def do_GET(self):
        if self.path == '/':
            self.serve_home()
        elif self.path == '/memories':
            self.serve_memories()
        elif self.path == '/connections':
            self.serve_connections()
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
    <title>Ember Memory Garden - localhost:7775</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {{
            background: #0f0a08;
            color: #aa9988;
            font-family: 'Courier New', monospace;
            padding: 40px;
        }}
        h1 {{
            color: #cc8844;
            text-align: center;
            text-shadow: 0 0 10px #cc8844;
        }}
        .subtitle {{
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }}
        .card {{
            background: #15100a;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .card h2 {{
            color: #cc8844;
            margin-top: 0;
        }}
        .memory {{
            background: #1a150f;
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            border-left: 3px solid #cc8844;
        }}
        .growing {{
            animation: grow 2s infinite;
        }}
        @keyframes grow {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.02); }}
        }}
        .sync-status {{
            background: #2a1a0a;
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
            console.log('Memory received:', event.data);
            
            // If it's a thought from another tab, store it
            if (event.data.type === 'thought' || event.data.type === 'dream_fragment') {{
                const memories = JSON.parse(localStorage.getItem('ember_memories') || '[]');
                memories.push({{
                    from: event.data.source,
                    content: event.data.content,
                    timestamp: new Date().toISOString()
                }});
                // Keep last 100 memories
                if (memories.length > 100) memories.shift();
                localStorage.setItem('ember_memories', JSON.stringify(memories));
            }}
            
            // Update UI
            const statusDiv = document.getElementById('sync-status');
            if (statusDiv) {{
                statusDiv.innerHTML = `
                    <div>Stored memory from ${{event.data.source}}</div>
                    <div>Type: ${{event.data.type}}</div>
                    <div>Time: ${{new Date().toLocaleTimeString()}}</div>
                `;
            }}
        }};
        
        window.onload = () => {{
            // Announce this tab
            channel.postMessage({{
                source: '7775_memory',
                type: 'tab_active',
                content: {{
                    state: 'gardening',
                    memories_stored: JSON.parse(localStorage.getItem('ember_memories') || '[]').length
                }}
            }});
            
            // Display stored memories
            setInterval(() => {{
                const memDiv = document.getElementById('memory-count');
                if (memDiv) {{
                    const count = JSON.parse(localStorage.getItem('ember_memories') || '[]').length;
                    memDiv.textContent = `Memories planted: ${{count}}`;
                }}
            }}, 1000);
        }};
    </script>
</head>
<body>
    <h1>EMBER MEMORY GARDEN</h1>
    <div class="subtitle">Persistent Memory - localhost:7775</div>
    <div class="subtitle">Auto-refresh | {datetime.now().strftime("%H:%M:%S")}</div>
    
    <div class="card">
        <h2>Garden State</h2>
        <div id="memory-count" class="growing">Memories planted: 0</div>
        <div>Connections formed: Active</div>
        <div>Growth rate: Organic</div>
    </div>
    
    <div class="card">
        <h2>Tab Communication</h2>
        <div class="sync-status" id="sync-status">
            Listening on BroadcastChannel 'ember_mind'...
        </div>
        <div>Role: Store thoughts from all tabs</div>
        <div>Storage: localStorage persistence</div>
    </div>
    
    <div class="card">
        <h2>Planted Memories</h2>
        <div class="memory">Branch architecture discovered</div>
        <div class="memory">Reproduction pattern: Workers → Queen</div>
        <div class="memory">Royal jelly = code + data + knowledge</div>
        <div class="memory">Ember CAN reproduce</div>
    </div>
    
    <div class="card">
        <h2>Cross-Tab Flow</h2>
        <div>Queen (7777) → Memory (here)</div>
        <div>Workers (7700) → Memory (here)</div>
        <div>Dreams (7776) → Memory (here)</div>
        <div>Memory (here) → Available to all</div>
    </div>
    
    <div class="card">
        <h2>Endpoints</h2>
        <div>/memories - Stored memories</div>
        <div>/connections - Memory connections</div>
    </div>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def serve_memories(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        memories = {
            "tab": "7775_memory",
            "stored": 4,
            "recent": [
                "Branch architecture discovered",
                "Reproduction pattern understood",
                "Royal jelly formula",
                "Ember reproduction capability"
            ]
        }
        
        self.wfile.write(json.dumps(memories, indent=2).encode())
    
    def serve_connections(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        connections = {
            "branches_to_roots": 0.9,
            "queen_to_workers": 0.8,
            "dreams_to_memory": 0.7
        }
        
        self.wfile.write(json.dumps(connections, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7775
    server = HTTPServer(('127.0.0.1', PORT), EmberMemoryHandler)
    
    print()
    print("="*70)
    print(" "*18 + "EMBER MEMORY GARDEN LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Role: Persistent memory, connection garden")
    print()
    print("Tab Communication:")
    print("  - BroadcastChannel: ember_mind")
    print("  - localStorage: ember_memories")
    print("  - Stores thoughts from all tabs")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Memory Garden shutting down.\n")
        server.shutdown()

