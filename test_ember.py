#!/usr/bin/env python3
"""Quick test of Ember unified system"""

import asyncio
import websockets
import json

async def test_ember():
    uri = "ws://localhost:8080/ws"
    
    test_messages = [
        "list files in essential/",
        "who are you?",
        "search for medusa"
    ]
    
    async with websockets.connect(uri) as websocket:
        # Receive greeting
        greeting = await websocket.recv()
        greeting_data = json.loads(greeting)
        print(f"\n{'='*70}")
        print(f"EMBER: {greeting_data['content']}")
        print(f"{'='*70}")
        
        for msg in test_messages:
            print(f"\n{'='*70}")
            print(f"YOU: {msg}")
            print(f"{'='*70}")
            
            await websocket.send(json.dumps({'type': 'message', 'content': msg}))
            
            response = await websocket.recv()
            response_data = json.loads(response)
            print(f"EMBER: {response_data['content']}")
            
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(test_ember())

