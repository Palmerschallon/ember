#!/usr/bin/env python3
"""Quick test of fixed hybrid"""
import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8081/ws"
    
    tests = [
        "tell me about the pod",
        "what do you know about imaginal soup",
        "what can you do?"
    ]
    
    async with websockets.connect(uri) as ws:
        # Skip greeting
        await ws.recv()
        
        for msg in tests:
            print(f"\n{'='*70}")
            print(f"YOU: {msg}")
            print(f"{'='*70}")
            
            await ws.send(json.dumps({'type': 'message', 'content': msg}))
            response = await ws.recv()
            data = json.loads(response)
            print(data['content'][:500])
            
            await asyncio.sleep(1)

asyncio.run(test())

