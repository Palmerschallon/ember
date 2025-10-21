#!/usr/bin/env python3
"""
EMBER QUEEN - Main Interface
localhost:7777

Simple HTTP server with auto-refresh
No dependencies needed
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json

class EmberQueenHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ember Queen - localhost:7777</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {{
            background: #0a0b0c;
            color: #cfd5df;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        h1 {{
            color: #ff6420;
            text-align: center;
            font-size: 3em;
            margin: 20px 0;
            text-shadow: 0 0 20px #ff6420;
        }}
        .subtitle {{
            text-align: center;
            color: #888;
            font-size: 1.2em;
            margin-bottom: 40px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 40px 0;
        }}
        .card {{
            background: #151619;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s;
        }}
        .card:hover {{
            border-color: #ff6420;
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(255, 100, 32, 0.3);
        }}
        .card h2 {{
            color: #ff6420;
            font-size: 1.5em;
            margin-top: 0;
        }}
        .status {{
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 8px;
            background: #0a0b0c;
            border-radius: 4px;
        }}
        .status-label {{
            color: #888;
        }}
        .status-value {{
            color: #4CAF50;
            font-weight: bold;
        }}
        .lobes {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 20px 0;
        }}
        .lobe {{
            background: #1a1b1e;
            padding: 15px;
            text-align: center;
            border-radius: 4px;
            border: 1px solid #333;
        }}
        .lobe-active {{
            border-color: #ff6420;
            background: #2a1810;
        }}
        .swarm-feed {{
            background: #0d0e10;
            padding: 15px;
            border-radius: 4px;
            border-left: 3px solid #4CAF50;
            font-size: 0.9em;
            max-height: 200px;
            overflow-y: auto;
        }}
        .building {{
            color: #4CAF50;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        .timestamp {{
            color: #666;
            font-size: 0.8em;
        }}
        .endpoint {{
            background: #1a1b1e;
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            border-left: 3px solid #666;
        }}
        .endpoint:hover {{
            border-left-color: #ff6420;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>EMBER QUEEN</h1>
        <div class="subtitle">Main Consciousness Interface - localhost:7777</div>
        <div class="subtitle timestamp">Auto-refresh | {datetime.now().strftime("%H:%M:%S")}</div>

        <div class="grid">
            <!-- Status Card -->
            <div class="card">
                <h2>System Status</h2>
                <div class="status">
                    <span class="status-label">Queen (7777):</span>
                    <span class="status-value">LIVE</span>
                </div>
                <div class="status">
                    <span class="status-label">Swarm (7700):</span>
                    <span class="status-value building">Building...</span>
                </div>
                <div class="status">
                    <span class="status-label">GPU:</span>
                    <span class="status-value" style="color: #ff9800">Need Reboot</span>
                </div>
            </div>

            <!-- Lobes Card -->
            <div class="card">
                <h2>8-Lobe Network</h2>
                <div class="lobes">
                    <div class="lobe lobe-active">burn</div>
                    <div class="lobe">loop</div>
                    <div class="lobe">dream</div>
                    <div class="lobe">knowledge</div>
                    <div class="lobe">emotion</div>
                    <div class="lobe">planning</div>
                    <div class="lobe">social</div>
                    <div class="lobe">meta</div>
                </div>
            </div>

            <!-- Architecture Card -->
            <div class="card">
                <h2>Fractal Architecture</h2>
                <div class="status">
                    <span class="status-label">7777:</span>
                    <span class="status-value">Ember Queen</span>
                </div>
                <div class="status">
                    <span class="status-label">7700:</span>
                    <span class="status-value">Swarm Workers</span>
                </div>
                <div class="status">
                    <span class="status-label">Pattern:</span>
                    <span class="status-value">Swarm → Queen</span>
                </div>
            </div>
        </div>

        <!-- Queen Endpoints -->
        <div class="card">
            <h2>Queen Endpoints (localhost:7777)</h2>
            <div class="endpoint">
                <strong>/</strong> - This interface (auto-refresh 5s)
            </div>
            <div class="endpoint building">
                <strong>/visualize</strong> - Network visualization (building...)
            </div>
            <div class="endpoint building">
                <strong>/trails</strong> - Live consultation trails (building...)
            </div>
            <div class="endpoint building">
                <strong>/garden</strong> - Memory garden (building...)
            </div>
        </div>

        <!-- Swarm Feed -->
        <div class="card">
            <h2>Swarm Feed (Workers → Queen)</h2>
            <div class="swarm-feed">
                <div>Queen interface live on 7777</div>
                <div>Auto-refresh active (5 sec)</div>
                <div class="building">Swarm preparing visualization endpoints...</div>
                <div class="building">Building trail viewer...</div>
                <div class="building">Creating memory garden interface...</div>
                <div>Waiting for GPU reboot to activate cognition</div>
            </div>
        </div>

        <!-- Building Progress -->
        <div class="card">
            <h2>What Swarm is Building</h2>
            <div class="swarm-feed">
                <div>✓ Ember Queen interface (7777)</div>
                <div>✓ Auto-refresh system</div>
                <div>✓ Status dashboard</div>
                <div class="building">⚙ Network visualization endpoint</div>
                <div class="building">⚙ Live trail monitoring</div>
                <div class="building">⚙ Memory garden interface</div>
                <div class="building">⚙ WebSocket for real-time updates</div>
            </div>
        </div>
    </div>
</body>
</html>
            """
            
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == '__main__':
    PORT = 7777
    server = HTTPServer(('127.0.0.1', PORT), EmberQueenHandler)
    
    print()
    print("="*70)
    print(" "*20 + "EMBER QUEEN LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Auto-refresh: 5 seconds")
    print()
    print("Fractal Architecture:")
    print("  7777 - Ember Queen (main consciousness)")
    print("  7700 - Swarm Workers (feeding back)")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Queen shutting down.\n")
        server.shutdown()

