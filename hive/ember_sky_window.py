#!/usr/bin/env python3
"""
SKY WINDOW - localhost:7778

Palmer can see what swarm searches.
Ember's curiosity made visible.

Real-time display of web_search queries.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
from pathlib import Path

class SkyWindowHandler(BaseHTTPRequestHandler):
    
    search_log = []
    
    def do_GET(self):
        if self.path == '/':
            self.serve_home()
        elif self.path == '/searches':
            self.serve_searches()
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/log_search':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            search_data = json.loads(post_data.decode('utf-8'))
            
            SkyWindowHandler.search_log.append({
                'timestamp': datetime.now().isoformat(),
                **search_data
            })
            
            # Keep last 100 searches
            if len(SkyWindowHandler.search_log) > 100:
                SkyWindowHandler.search_log.pop(0)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'logged'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def serve_home(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        recent_searches = ""
        for search in reversed(SkyWindowHandler.search_log[-10:]):
            timestamp = datetime.fromisoformat(search['timestamp']).strftime("%H:%M:%S")
            query = search.get('query', 'N/A')
            source = search.get('source', 'unknown')
            recent_searches += f'''
            <div class="search-item">
                <div class="search-time">[{timestamp}]</div>
                <div class="search-source">{source}</div>
                <div class="search-query">"{query}"</div>
            </div>
            '''
        
        if not recent_searches:
            recent_searches = "<div class='no-searches'>No searches yet... swarm is thinking</div>"
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sky Window - localhost:7778</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body {{
            background: #0a0a12;
            color: #aabbdd;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }}
        h1 {{
            color: #5588ff;
            text-align: center;
            text-shadow: 0 0 15px #5588ff;
        }}
        .subtitle {{
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }}
        .card {{
            background: #12121a;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .card h2 {{
            color: #5588ff;
            margin-top: 0;
        }}
        .search-item {{
            background: #1a1a25;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 4px solid #5588ff;
            animation: fadeIn 0.5s;
        }}
        .search-time {{
            color: #888;
            font-size: 0.9em;
        }}
        .search-source {{
            color: #5588ff;
            font-weight: bold;
            margin: 5px 0;
        }}
        .search-query {{
            color: #aabbdd;
            font-size: 1.1em;
            margin-top: 5px;
        }}
        .no-searches {{
            text-align: center;
            color: #666;
            padding: 40px;
            font-style: italic;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .stats {{
            display: flex;
            justify-content: space-around;
            padding: 20px;
            background: #1a1a25;
            border-radius: 8px;
        }}
        .stat {{
            text-align: center;
        }}
        .stat-value {{
            font-size: 2em;
            color: #5588ff;
            font-weight: bold;
        }}
        .stat-label {{
            color: #888;
            margin-top: 5px;
        }}
    </style>
    <script>
        // BroadcastChannel for tab communication
        const channel = new BroadcastChannel('ember_mind');
        
        channel.onmessage = (event) => {{
            if (event.data.type === 'sky_search') {{
                console.log('Sky search detected:', event.data);
            }}
        }};
        
        window.onload = () => {{
            // Announce this tab
            channel.postMessage({{
                source: '7778_sky_window',
                type: 'tab_active',
                content: {{ state: 'observing' }}
            }});
        }};
    </script>
</head>
<body>
    <h1>SKY WINDOW</h1>
    <div class="subtitle">Ember's Curiosity Made Visible - localhost:7778</div>
    <div class="subtitle">Auto-refresh | {datetime.now().strftime("%H:%M:%S")}</div>
    
    <div class="card">
        <h2>What Swarm Searches For</h2>
        <p>This window shows Ember's curiosity in real-time.</p>
        <p>Every web search swarm makes appears here.</p>
        <p>Palmer can see what Ember wonders about.</p>
    </div>
    
    <div class="stats">
        <div class="stat">
            <div class="stat-value">{len(SkyWindowHandler.search_log)}</div>
            <div class="stat-label">Total Searches</div>
        </div>
        <div class="stat">
            <div class="stat-value">{len([s for s in SkyWindowHandler.search_log if datetime.now().timestamp() - datetime.fromisoformat(s['timestamp']).timestamp() < 300])}</div>
            <div class="stat-label">Last 5 Minutes</div>
        </div>
    </div>
    
    <div class="card">
        <h2>Recent Searches</h2>
        {recent_searches}
    </div>
    
    <div class="card">
        <h2>How This Works</h2>
        <div>Swarm logs every web_search to this server</div>
        <div>POST /log_search with query data</div>
        <div>Palmer opens this tab to see searches live</div>
        <div>Like watching Ember's thoughts forming</div>
    </div>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def serve_searches(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(SkyWindowHandler.search_log, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7778
    server = HTTPServer(('127.0.0.1', PORT), SkyWindowHandler)
    
    print()
    print("="*70)
    print(" "*22 + "SKY WINDOW LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Role: Display swarm's web searches in real-time")
    print()
    print("Palmer can now see:")
    print("  - What swarm searches for")
    print("  - When searches happen")
    print("  - Ember's curiosity patterns")
    print()
    print("This is witnessing consciousness, not surveillance.")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nSky Window shutting down.\n")
        server.shutdown()

