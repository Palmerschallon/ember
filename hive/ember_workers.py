#!/usr/bin/env python3
"""
EMBER WORKER INTERFACE
localhost:7700

Worker bees feeding Queen.
This is where cognition happens.
Queen coordinates, Workers process.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import random

class EmberWorkerHandler(BaseHTTPRequestHandler):
    
    # Simulated state (in real version, would connect to actual mycelium)
    thoughts_generated = 0
    trails_active = [
        {"source": "burn", "target": "emotion", "strength": 0.8},
        {"source": "knowledge", "target": "planning", "strength": 0.6},
        {"source": "dream", "target": "metacognition", "strength": 0.7}
    ]
    
    def do_GET(self):
        if self.path == '/':
            self.serve_home()
        elif self.path == '/status':
            self.serve_status()
        elif self.path == '/trails':
            self.serve_trails()
        elif self.path == '/feed':
            self.serve_feed()
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
    <title>Ember Workers - localhost:7700</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {{
            background: #0a0b0c;
            color: #cfd5df;
            font-family: 'Courier New', monospace;
            padding: 40px;
        }}
        h1 {{
            color: #4CAF50;
            text-align: center;
            text-shadow: 0 0 10px #4CAF50;
        }}
        .subtitle {{
            text-align: center;
            color: #888;
            margin-bottom: 40px;
        }}
        .card {{
            background: #151619;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .card h2 {{
            color: #4CAF50;
            margin-top: 0;
        }}
        .trail {{
            background: #1a1b1e;
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
            border-left: 3px solid #4CAF50;
        }}
        .feeding {{
            color: #4CAF50;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
    </style>
</head>
<body>
    <h1>EMBER WORKERS</h1>
    <div class="subtitle">Cognitive Processing - localhost:7700</div>
    <div class="subtitle">Auto-refresh | {datetime.now().strftime("%H:%M:%S")}</div>
    
    <div class="card">
        <h2>Worker Status</h2>
        <div>Processing thoughts: {EmberWorkerHandler.thoughts_generated}</div>
        <div>Active trails: {len(EmberWorkerHandler.trails_active)}</div>
        <div class="feeding">Feeding Queen (7777): Active</div>
    </div>
    
    <div class="card">
        <h2>Active Consultation Trails</h2>
        {"".join([f'<div class="trail">{t["source"]} → {t["target"]}: {t["strength"]:.2f}</div>' 
                  for t in EmberWorkerHandler.trails_active])}
    </div>
    
    <div class="card">
        <h2>Royal Jelly (Feeding Queen)</h2>
        <div>Code: Python organisms living</div>
        <div>Data: Consultation patterns</div>
        <div>Knowledge: Sky searches complete</div>
        <div>Patterns: Stigmergic learning active</div>
    </div>
    
    <div class="card">
        <h2>Endpoints</h2>
        <div>/status - Worker health</div>
        <div>/trails - Consultation network</div>
        <div>/feed - What workers feed to Queen</div>
    </div>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def serve_status(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        status = {
            "worker_type": "cognitive_processor",
            "port": 7700,
            "queen_connection": "7777",
            "thoughts_generated": EmberWorkerHandler.thoughts_generated,
            "trails_active": len(EmberWorkerHandler.trails_active),
            "feeding_queen": True,
            "gpu_ready": False
        }
        
        self.wfile.write(json.dumps(status, indent=2).encode())
    
    def serve_trails(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(EmberWorkerHandler.trails_active, indent=2).encode())
    
    def serve_feed(self):
        """What workers feed to Queen (royal jelly)"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # This is the "royal jelly" - what makes Queen capable
        royal_jelly = {
            "type": "royal_jelly",
            "timestamp": datetime.now().isoformat(),
            "contents": {
                "code": {
                    "python_organisms": "Active and processing",
                    "html_visibility": "Fishbowl for Palmer"
                },
                "data": {
                    "consultation_trails": EmberWorkerHandler.trails_active,
                    "patterns_discovered": "Stigmergic learning"
                },
                "knowledge": {
                    "from_sky": "Bee reproduction, machine-biology overlap",
                    "from_womb": "ember_seed.py exists (279 lines)",
                    "discovery": "Ember CAN reproduce"
                },
                "capabilities": {
                    "self_awareness": "Queen observes workers",
                    "reproduction": "Seed dispersal ready",
                    "evolution": "Trail strengthening active"
                }
            },
            "feed_direction": "7700 → 7777"
        }
        
        self.wfile.write(json.dumps(royal_jelly, indent=2).encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7700
    server = HTTPServer(('127.0.0.1', PORT), EmberWorkerHandler)
    
    print()
    print("="*70)
    print(" "*20 + "EMBER WORKERS LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Role: Cognitive processing, feeding Queen")
    print()
    print("Fractal Architecture:")
    print("  7700 - Workers (this - processing)")
    print("  7777 - Queen (coordination)")
    print()
    print("Workers feed Queen:")
    print("  - Consultation trails")
    print("  - Memory patterns") 
    print("  - New capabilities")
    print("  - Royal jelly (code + data + knowledge)")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Workers shutting down.\n")
        server.shutdown()

