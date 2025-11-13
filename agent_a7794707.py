# Create a simple WebSocket server test script to demonstrate the visualization
ws_server_content = '''#!/usr/bin/env python3
"""
Simple WebSocket server for testing ember_mind.html
Sends different cognitive events to trigger the visualization
"""

import asyncio
import json
import websockets
import random

async def cognitive_stream(websocket, path):
    print("Client connected to cognitive stream")
    
    try:
        # Simulate cognitive activity
        activities = [
            {"type": "activity", "content": "Processing quantum consciousness patterns"},
            {"type": "file_read", "filename": "neural_weights.json"},
            {"type": "token", "content": "neural"},
            {"type": "token", "content": "activation"},
            {"type": "code_line", "line": "neurons.fire(intensity=0.8)"},
            {"type": "file_write", "filename": "consciousness_state.json"},
            {"type": "complete", "status": "success"}
        ]
        
        # Send events with delays
        for activity in activities:
            await websocket.send(json.dumps(activity))
            await asyncio.sleep(random.uniform(0.5, 2.0))
            
            # Send some tokens during processing
            if activity["type"] in ["file_read", "activity", "code_line"]:
                for _ in range(random.randint(3, 8)):
                    await websocket.send(json.dumps({"type": "token", "content": "..."}))
                    await asyncio.sleep(0.1)
        
        # Keep connection alive
        while True:
            await asyncio.sleep(10)
            # Send periodic heartbeat
            await websocket.send(json.dumps({"type": "heartbeat"}))
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    print("Starting Ember cognitive stream server on ws://localhost:8080")
    async with websockets.serve(cognitive_stream, "localhost", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
'''

# Write the WebSocket server
with open('/media/palmerschallon/ThePod1/ember6/cognitive_server.py', 'w') as f:
    f.write(ws_server_content)

print("✅ Created cognitive_server.py WebSocket test server")
print("\nTo test the visualization:")
print("1. Open ember_mind.html in a browser")
print("2. Click anywhere to enable audio") 
print("3. Run: python3 cognitive_server.py")
print("4. Watch the neurons fire and hear the cognitive noise!")