#!/usr/bin/env python3
"""
Test both modes side by side
"""
import asyncio
import websockets
import json

async def test_mode(port, name):
    """Test one mode"""
    uri = f"ws://localhost:{port}/ws"
    
    print(f"\n{'='*70}")
    print(f"TESTING {name} (port {port})")
    print(f"{'='*70}")
    
    test_messages = [
        "list files in essential",
        "who are you?",
    ]
    
    try:
        async with websockets.connect(uri) as websocket:
            # Get greeting
            greeting = await websocket.recv()
            greeting_data = json.loads(greeting)
            print(f"\nGREETING:\n{greeting_data['content']}\n")
            
            for msg in test_messages:
                print(f"\n→ YOU: {msg}")
                
                await websocket.send(json.dumps({'type': 'message', 'content': msg}))
                
                response = await websocket.recv()
                response_data = json.loads(response)
                print(f"\n← EMBER: {response_data['content'][:500]}...")
                
                await asyncio.sleep(1)
    except Exception as e:
        print(f"ERROR: {e}")

async def main():
    print("\n" + "="*70)
    print("COMPARING DETERMINISTIC vs HYBRID")
    print("="*70)
    
    # Test deterministic
    await test_mode(8080, "DETERMINISTIC (No AI)")
    
    # Test hybrid
    await test_mode(8081, "HYBRID (AI Narration)")
    
    print("\n" + "="*70)
    print("COMPARISON COMPLETE")
    print("="*70)
    print("\nDeterministic (:8080): Raw data, instant response")
    print("Hybrid (:8081):        Same data, natural language\n")

if __name__ == "__main__":
    asyncio.run(main())

