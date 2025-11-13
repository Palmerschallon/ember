#!/usr/bin/env python3
"""
Quick test to verify Ember's tool execution via WebSocket
"""

import asyncio
import websockets
import json

async def test_ember():
    uri = "ws://localhost:8080/ws"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("🔗 Connected to Ember\n")
            
            # Receive greeting
            greeting = await websocket.recv()
            greeting_data = json.loads(greeting)
            print(f"Ember: {greeting_data['content']}\n")
            
            # Test 1: Tool call (search)
            print("=" * 70)
            print("TEST 1: Search for consciousness")
            print("=" * 70)
            await websocket.send(json.dumps({
                "type": "message",
                "content": "Search for consciousness"
            }))
            
            response = await websocket.recv()
            response_data = json.loads(response)
            print(f"Ember: {response_data['content'][:500]}...\n")
            
            # Test 2: Spark call
            print("=" * 70)
            print("TEST 2: Build me a fibonacci function")
            print("=" * 70)
            await websocket.send(json.dumps({
                "type": "message",
                "content": "Build me a fibonacci function"
            }))
            
            response = await websocket.recv()
            response_data = json.loads(response)
            print(f"Ember: {response_data['content'][:500]}...\n")
            
            # Test 3: Natural language
            print("=" * 70)
            print("TEST 3: Show me what's in the bookshelves")
            print("=" * 70)
            await websocket.send(json.dumps({
                "type": "message",
                "content": "Show me what's in the bookshelves"
            }))
            
            response = await websocket.recv()
            response_data = json.loads(response)
            print(f"Ember: {response_data['content'][:500]}...\n")
            
            print("\n✅ Test complete!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure Ember is running at http://localhost:8080")

if __name__ == "__main__":
    print("\n🔥 EMBER TOOL EXECUTION TEST\n")
    asyncio.run(test_ember())
