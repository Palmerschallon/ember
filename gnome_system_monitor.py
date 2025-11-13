#!/usr/bin/env python3
"""
GNOME System Monitor WebSocket Server
Streams system info that can be visualized in Claude's HTML
"""
import json
import asyncio
import websockets
import psutil
import subprocess
from datetime import datetime

def get_gnome_info():
    """Get GNOME desktop environment info"""
    info = {}
    
    try:
        # GNOME version
        result = subprocess.run(['gnome-shell', '--version'], 
                              capture_output=True, text=True)
        info['gnome_version'] = result.stdout.strip()
    except:
        info['gnome_version'] = "GNOME not detected"
    
    # Get workspace info
    try:
        result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.wm.preferences', 'num-workspaces'],
                              capture_output=True, text=True)
        info['workspaces'] = int(result.stdout.strip())
    except:
        info['workspaces'] = 1
    
    return info

def get_system_stats():
    """Get system performance stats"""
    return {
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory': psutil.virtual_memory()._asdict(),
        'disk': psutil.disk_usage('/')._asdict(),
        'network': psutil.net_io_counters()._asdict() if psutil.net_io_counters() else {},
        'processes': len(psutil.pids()),
        'gnome': get_gnome_info(),
        'timestamp': datetime.now().isoformat()
    }

async def system_monitor_server(websocket, path):
    print("Client connected to GNOME System Monitor")
    
    try:
        while True:
            stats = get_system_stats()
            await websocket.send(json.dumps(stats))
            await asyncio.sleep(1)  # Update every second
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    print("🖥️  GNOME System Monitor WebSocket Server")
    print("Running on ws://localhost:8765")
    async with websockets.serve(system_monitor_server, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())