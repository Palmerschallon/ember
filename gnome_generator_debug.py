import asyncio
import websockets
import json
import random
import traceback

# WebSocket server with better error handling
async def gnome_server(websocket, path):
    try:
        print(f"New connection from {websocket.remote_address}")
        
        async for message in websocket:
            print(f"Received: {message}")
            
            try:
                data = json.loads(message)
                action = data.get('action')
                
                if action == 'generate':
                    # Simple test response
                    response = {
                        'type': 'gnome',
                        'data': {
                            'name': 'Test Gnome',
                            'description': 'A happy test gnome!'
                        }
                    }
                    await websocket.send(json.dumps(response))
                    print(f"Sent response: {response}")
                    
            except json.JSONDecodeError as e:
                print(f"JSON Error: {e}")
                error_response = {'type': 'error', 'message': 'Invalid JSON'}
                await websocket.send(json.dumps(error_response))
                
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed normally")
    except Exception as e:
        print(f"ERROR in gnome_server: {type(e).__name__}: {e}")
        traceback.print_exc()

async def main():
    print("🍄 Debug Gnome Server starting on ws://localhost:8766")
    
    async with websockets.serve(gnome_server, "localhost", 8766):
        print("Server is ready and listening...")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())