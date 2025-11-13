#!/usr/bin/env python3
"""
Secure WebSocket Server for Ember VR
Handles WSS:// connections for HTTPS pages
"""

import asyncio
import websockets
import ssl
import json
import pathlib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connected clients
clients = set()

async def handle_client(websocket, path):
    """Handle a WebSocket connection from a client"""
    clients.add(websocket)
    client_ip = websocket.remote_address[0]
    logger.info(f"Client connected from {client_ip}")
    
    try:
        # Send welcome message
        await websocket.send(json.dumps({
            "type": "message",
            "content": "🔥 Connected to Ember! I'm ready to create in VR."
        }))
        
        async for message in websocket:
            try:
                data = json.loads(message)
                logger.info(f"Received from {client_ip}: {data}")
                
                if data.get("type") == "chat":
                    # Echo back a response
                    response = {
                        "type": "message",
                        "content": f"I heard you say: '{data.get('content', '')}'. What would you like me to create?"
                    }
                    await websocket.send(json.dumps(response))
                    
                    # Check for spawn commands
                    content_lower = data.get("content", "").lower()
                    if "spawn" in content_lower or "create" in content_lower:
                        object_type = "crystal"
                        if "cube" in content_lower:
                            object_type = "cube"
                        elif "sphere" in content_lower:
                            object_type = "sphere"
                        elif "torus" in content_lower:
                            object_type = "torus"
                        
                        spawn_msg = {
                            "type": "spawn",
                            "objectType": object_type
                        }
                        await websocket.send(json.dumps(spawn_msg))
                
            except json.JSONDecodeError:
                logger.error(f"Invalid JSON from {client_ip}: {message}")
                
    except websockets.exceptions.ConnectionClosed:
        logger.info(f"Client {client_ip} disconnected")
    finally:
        clients.remove(websocket)

async def broadcast(message):
    """Broadcast a message to all connected clients"""
    if clients:
        await asyncio.gather(*[client.send(message) for client in clients])

def create_ssl_context():
    """Create SSL context for secure WebSocket"""
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # Check if certificates exist, if not create self-signed ones
    cert_path = pathlib.Path("/media/palmerschallon/ThePod1/cert.pem")
    key_path = pathlib.Path("/media/palmerschallon/ThePod1/key.pem")
    
    if not cert_path.exists() or not key_path.exists():
        logger.info("Creating self-signed certificates...")
        import subprocess
        subprocess.run([
            "openssl", "req", "-x509", "-newkey", "rsa:4096",
            "-keyout", str(key_path), "-out", str(cert_path),
            "-days", "365", "-nodes", "-subj",
            "/C=US/ST=VR/L=EmberVR/O=Ember/CN=10.0.0.100"
        ])
    
    ssl_context.load_cert_chain(str(cert_path), str(key_path))
    return ssl_context

async def main():
    """Main server loop"""
    ssl_context = create_ssl_context()
    
    # Start secure WebSocket server on 8081
    async with websockets.serve(
        handle_client, 
        "0.0.0.0", 
        8081,
        ssl=ssl_context
    ):
        logger.info("🔥 Ember Secure WebSocket Server running on wss://0.0.0.0:8081")
        logger.info("Ready for Quest 3 connections!")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())