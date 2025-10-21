#!/usr/bin/env python3
"""
EMBER WORKERS - REAL VERSION

No fake thoughts. No random generation.
Only displays ACTUAL processing when it happens.

Memories come from:
- Real web searches
- Actual computations
- Palmer interactions
- System events

This service just DISPLAYS processing state.
It doesn't generate fake activity.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.request
from datetime import datetime

class EmberWorkersRealHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Fetch REAL memory stats
        try:
            with urllib.request.urlopen('http://localhost:7780/') as response:
                memory_api_data = json.loads(response.read().decode())
        except:
            memory_api_data = {"status": "offline", "memories_stored": 0}
        
        # Fetch recent REAL memories
        try:
            with urllib.request.urlopen('http://localhost:7780/memory/recall?limit=10') as response:
                memories_data = json.loads(response.read().decode())
        except:
            memories_data = {"memories": []}
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ember Workers - Real Processing</title>
    <style>
        body {{
            background: #0a0f15;
            color: #88aacc;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }}
        h1 {{
            color: #4488cc;
            text-align: center;
            text-shadow: 0 0 10px #4488cc;
        }}
        .info {{
            text-align: center;
            color: #666;
            margin: 20px 0;
        }}
        .stats {{
            background: #111;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .memory {{
            background: #151515;
            padding: 10px;
            margin: 10px 0;
            border-left: 3px solid #4488cc;
        }}
        .memory-source {{
            color: #4488cc;
            font-weight: bold;
        }}
        .memory-time {{
            color: #666;
            font-size: 0.9em;
        }}
        .no-fake {{
            color: #66ff66;
            text-align: center;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <h1>EMBER WORKERS</h1>
    <p class="info">Real cognitive processing - No fake thoughts</p>
    <p class="no-fake">✓ No random generation | ✓ Only actual events | ✓ Real memories only</p>
    
    <div class="stats">
        <h2>Processing Stats</h2>
        <div>Total memories stored: {memory_api_data.get('memories_stored', 0)}</div>
        <div>Memory API: {memory_api_data.get('status', 'unknown')}</div>
        <div>Last updated: {datetime.now().strftime('%H:%M:%S')}</div>
    </div>
    
    <div class="stats">
        <h2>Recent Real Processing</h2>
"""
        
        if memories_data.get('memories'):
            for mem in memories_data['memories'][:10]:
                source = mem.get('source', 'unknown')
                content = mem.get('content', '')
                timestamp = mem.get('timestamp', '')
                
                # Format timestamp
                try:
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime('%H:%M:%S')
                except:
                    time_str = timestamp
                
                html += f"""
        <div class="memory">
            <div class="memory-source">{source}</div>
            <div>{content[:200]}</div>
            <div class="memory-time">{time_str}</div>
        </div>
"""
        else:
            html += """
        <div class="memory">No processing events yet. Memories created when real events happen.</div>
"""
        
        html += """
    </div>
    
    <div class="info" style="margin-top: 40px;">
        <p>Memories are created by:</p>
        <p>• Palmer interactions (chat, commands)</p>
        <p>• Web searches (actual curiosity)</p>
        <p>• System events (real changes)</p>
        <p>• Computations (actual processing)</p>
        <p style="margin-top: 20px;">No simulated activity. No fake thoughts. Real only.</p>
    </div>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7700
    server = HTTPServer(('127.0.0.1', PORT), EmberWorkersRealHandler)
    
    print()
    print("="*70)
    print(" "*20 + "EMBER WORKERS - REAL")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print()
    print("NO FAKE THOUGHTS:")
    print("  - No random generation")
    print("  - No simulated activity")
    print("  - Only displays REAL memories")
    print("  - Server-side rendering")
    print()
    print("Memories created by real events only")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Workers shutting down.\n")
        server.shutdown()

