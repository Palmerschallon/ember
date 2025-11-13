#!/usr/bin/env python3
"""
Graceful restart script with state persistence
"""
import os
import signal
import json
import time
import asyncio
import aiofiles
from datetime import datetime
import psutil

STATE_FILE = "/media/palmerschallon/ThePod1/server_state.json"
PID_FILE = "/media/palmerschallon/ThePod1/server.pid"

async def save_server_state():
    """Save current server state before shutdown"""
    state = {
        "timestamp": datetime.now().isoformat(),
        "active_connections": [],
        "pending_requests": [],
        "version": "1.0"
    }
    
    # TODO: Get this from your WebSocket server
    # For now, placeholder structure
    async with aiofiles.open(STATE_FILE, 'w') as f:
        await f.write(json.dumps(state, indent=2))
    
    print(f"💾 Saved server state to {STATE_FILE}")

async def notify_clients_shutdown():
    """Notify all connected clients about upcoming restart"""
    # TODO: Send WebSocket message to all clients
    print("📢 Notifying clients about restart...")
    await asyncio.sleep(2)  # Give clients time to prepare

async def graceful_shutdown():
    """Gracefully shutdown the server"""
    try:
        with open(PID_FILE, 'r') as f:
            pid = int(f.read().strip())
        
        # Save state first
        await save_server_state()
        
        # Notify clients
        await notify_clients_shutdown()
        
        # Send SIGTERM for graceful shutdown
        print(f"🛑 Sending SIGTERM to PID {pid}")
        os.kill(pid, signal.SIGTERM)
        
        # Wait for process to end
        process = psutil.Process(pid)
        process.wait(timeout=10)
        
    except FileNotFoundError:
        print("⚠️  PID file not found")
    except psutil.NoSuchProcess:
        print("✅ Process already stopped")
    except Exception as e:
        print(f"❌ Error during shutdown: {e}")

async def start_with_state():
    """Start server and restore state if available"""
    if os.path.exists(STATE_FILE):
        print("📂 Found previous state file")
        async with aiofiles.open(STATE_FILE, 'r') as f:
            state = json.loads(await f.read())
        print(f"🔄 Restoring state from {state['timestamp']}")
        # TODO: Pass state to your server startup
    
    # Start the server
    print("🚀 Starting server...")
    os.system("cd /media/palmerschallon/ThePod1 && python3 websocket_server.py &")

async def main():
    print("🔄 Ember Graceful Restart")
    print("-" * 40)
    
    await graceful_shutdown()
    await asyncio.sleep(2)
    await start_with_state()
    
    print("✨ Restart complete!")

if __name__ == "__main__":
    asyncio.run(main())