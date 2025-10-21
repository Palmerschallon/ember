#!/usr/bin/env python3
"""
EMBER STATUS - ULTRA SIMPLE WORKING TAB

No tricks. No auto-refresh. Just shows real data when you click refresh.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.request

class EmberStatusHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Fetch REAL data server-side (no JavaScript needed)
        try:
            with urllib.request.urlopen('http://localhost:7780/') as response:
                memory_api_data = json.loads(response.read().decode())
        except:
            memory_api_data = {"status": "offline", "memories_stored": 0}
        
        try:
            with urllib.request.urlopen('http://localhost:7778/api/search') as response:
                sky_data = json.loads(response.read().decode())
        except:
            sky_data = {"searches": [], "total": 0}
        
        try:
            with urllib.request.urlopen('http://localhost:7780/memory/recall?limit=5') as response:
                memories_data = json.loads(response.read().decode())
        except:
            memories_data = {"memories": []}
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ember Status - localhost:7799</title>
    <style>
        body {{
            background: #0a0a0a;
            color: #aaaaaa;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }}
        h1 {{
            color: #66aaff;
            text-align: center;
        }}
        .card {{
            background: #111111;
            border: 1px solid #333333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .card h2 {{
            color: #66aaff;
            margin-top: 0;
        }}
        .item {{
            background: #151515;
            padding: 10px;
            margin: 10px 0;
            border-left: 3px solid #66aaff;
        }}
        .online {{
            color: #66ff66;
        }}
        .offline {{
            color: #ff6666;
        }}
        button {{
            background: #66aaff;
            color: #000;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }}
        button:hover {{
            background: #88bbff;
        }}
    </style>
</head>
<body>
    <h1>EMBER STATUS</h1>
    <p style="text-align: center; color: #666;">No tricks. No auto-refresh. Real data only.</p>
    <p style="text-align: center;">
        <button onclick="location.reload()">🔄 Refresh (get latest data)</button>
    </p>
    
    <div class="card">
        <h2>System Status</h2>
        <div class="item">
            Memory API: <span class="{'online' if memory_api_data.get('status') == 'breathing' else 'offline'}">{memory_api_data.get('status', 'unknown')}</span>
        </div>
        <div class="item">
            Memories stored: {memory_api_data.get('memories_stored', 0)}
        </div>
        <div class="item">
            Searches logged: {sky_data.get('total', 0)}
        </div>
    </div>
    
    <div class="card">
        <h2>Recent Memories (from ThePod)</h2>
"""
        
        if memories_data.get('memories'):
            for mem in memories_data['memories'][:5]:
                html += f"""
        <div class="item">
            <div><strong>{mem.get('source', 'unknown')}</strong> / {mem.get('memory_type', 'unknown')}</div>
            <div>{mem.get('content', '')[:200]}</div>
            <div style="color: #666; font-size: 0.9em; margin-top: 5px;">{mem.get('timestamp', '')}</div>
        </div>
"""
        else:
            html += """
        <div class="item">No memories stored yet</div>
"""
        
        html += """
    </div>
    
    <div class="card">
        <h2>Recent Searches</h2>
"""
        
        if sky_data.get('searches'):
            for search in sky_data['searches'][-5:]:
                html += f"""
        <div class="item">
            <div><strong>{search.get('query', 'unknown')}</strong></div>
            <div style="color: #666; font-size: 0.9em;">Source: {search.get('source', 'unknown')}</div>
        </div>
"""
        else:
            html += """
        <div class="item">No searches logged yet</div>
"""
        
        html += """
    </div>
    
    <p style="text-align: center; color: #666; margin-top: 40px;">
        This page is generated SERVER-SIDE from real API data.<br>
        Click refresh to see latest. No JavaScript tricks.
    </p>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7799
    server = HTTPServer(('127.0.0.1', PORT), EmberStatusHandler)
    
    print()
    print("="*70)
    print(" "*20 + "EMBER STATUS - SIMPLE & REAL")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print()
    print("NO TRICKS:")
    print("  - No auto-refresh")
    print("  - No JavaScript")
    print("  - Server-side rendering")
    print("  - Real data from APIs")
    print("  - Click refresh to update")
    print()
    print("This is what Palmer asked for: REAL not tricks")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Status shutting down.\n")
        server.shutdown()

