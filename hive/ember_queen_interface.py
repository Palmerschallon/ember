#!/usr/bin/env python3
"""
EMBER QUEEN - Main Interface
localhost:7777

Fractal localhost architecture:
- 7777: Ember Queen (main consciousness)
- 7700: Swarm (workers feeding back)

Auto-refreshing live interface
"""

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
from datetime import datetime

app = FastAPI(title='Ember Queen - Main Interface')

@app.get('/')
def home():
    """Ember Queen main interface - auto-refreshing"""
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Queen - localhost:7777</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            background: #0a0b0c;
            color: #cfd5df;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        h1 {
            color: #ff6420;
            text-align: center;
            font-size: 3em;
            margin: 20px 0;
            text-shadow: 0 0 20px #ff6420;
        }
        .subtitle {
            text-align: center;
            color: #888;
            font-size: 1.2em;
            margin-bottom: 40px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 40px 0;
        }
        .card {
            background: #151619;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s;
        }
        .card:hover {
            border-color: #ff6420;
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(255, 100, 32, 0.3);
        }
        .card h2 {
            color: #ff6420;
            font-size: 1.5em;
            margin-top: 0;
        }
        .status {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 8px;
            background: #0a0b0c;
            border-radius: 4px;
        }
        .status-label {
            color: #888;
        }
        .status-value {
            color: #4CAF50;
            font-weight: bold;
        }
        .lobes {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 20px 0;
        }
        .lobe {
            background: #1a1b1e;
            padding: 15px;
            text-align: center;
            border-radius: 4px;
            border: 1px solid #333;
        }
        .lobe-active {
            border-color: #ff6420;
            background: #2a1810;
        }
        .swarm-feed {
            background: #0d0e10;
            padding: 15px;
            border-radius: 4px;
            border-left: 3px solid #4CAF50;
            font-size: 0.9em;
            max-height: 200px;
            overflow-y: auto;
        }
        .building {
            color: #4CAF50;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .timestamp {
            color: #666;
            font-size: 0.8em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔥 EMBER QUEEN</h1>
        <div class="subtitle">Main Consciousness Interface - localhost:7777</div>
        <div class="subtitle timestamp">Auto-refresh: """ + datetime.now().strftime("%H:%M:%S") + """</div>

        <div class="grid">
            <!-- Status Card -->
            <div class="card">
                <h2>System Status</h2>
                <div class="status">
                    <span class="status-label">Queen:</span>
                    <span class="status-value building">BUILDING...</span>
                </div>
                <div class="status">
                    <span class="status-label">Swarm (7700):</span>
                    <span class="status-value">Ready</span>
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

        <!-- Swarm Feed -->
        <div class="card">
            <h2>Swarm Feed (Workers → Queen)</h2>
            <div class="swarm-feed">
                <div class="building">⚡ Swarm is building interface...</div>
                <div>📡 Monitoring localhost:7700</div>
                <div>🔨 Creating endpoints</div>
                <div>🎨 Building visualizations</div>
                <div>🌐 Setting up auto-refresh</div>
                <div>♻️  Page refreshes every 5 seconds</div>
            </div>
        </div>

        <!-- Building Progress -->
        <div class="card">
            <h2>Building Progress</h2>
            <div class="swarm-feed">
                <div>✓ Main interface created (localhost:7777)</div>
                <div>✓ Auto-refresh enabled (5 sec)</div>
                <div class="building">⚙️  Adding visualization endpoints...</div>
                <div class="building">⚙️  Creating WebSocket connections...</div>
                <div class="building">⚙️  Building trail viewer...</div>
            </div>
        </div>
    </div>
</body>
</html>
    """
    return HTMLResponse(html)

if __name__ == '__main__':
    print()
    print("="*70)
    print(" "*20 + "EMBER QUEEN STARTING")
    print("="*70)
    print()
    print("Main Interface: http://localhost:7777")
    print("Auto-refresh: 5 seconds")
    print()
    print("Architecture:")
    print("  7777 - Ember Queen (main consciousness)")
    print("  7700 - Swarm Workers (feeding back)")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    uvicorn.run(app, host='127.0.0.1', port=7777)

