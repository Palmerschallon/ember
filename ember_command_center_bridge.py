#!/usr/bin/env python3
"""
EMBER COMMAND CENTER BRIDGE
WebSocket server connecting Creative Command Center to Ember's AI brain
Enables omnipresent Ember - accessible simultaneously through multiple interfaces
"""
import os
import sys
import asyncio
import json
import websockets
from datetime import datetime

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from ember_complete import Ember

from rich.console import Console

console = Console()

class EmberBridge:
    def __init__(self):
        self.ember = Ember()
        self.clients = set()
        console.print("[bold cyan]🔥 Ember Command Center Bridge initializing...[/bold cyan]")

    async def broadcast(self, message):
        """Send message to all connected clients"""
        if self.clients:
            await asyncio.gather(
                *[client.send(json.dumps(message)) for client in self.clients],
                return_exceptions=True
            )

    async def handle_client(self, websocket):
        """Handle a connected client"""
        self.clients.add(websocket)
        client_addr = websocket.remote_address
        console.print(f"[green]✓ Client connected: {client_addr}[/green]")

        try:
            # Send welcome message
            await websocket.send(json.dumps({
                'type': 'system',
                'content': 'Connected to Ember AI brain',
                'timestamp': datetime.now().isoformat()
            }))

            async for message in websocket:
                try:
                    data = json.loads(message)
                    console.print(f"[dim]← {data.get('type', 'message')}: {data.get('content', '')[:50]}...[/dim]")

                    if data['type'] == 'command':
                        # User sent a command from the web interface
                        command = data['content']

                        # Send to Ember's AI brain
                        console.print(f"[yellow]→ Sending to Ember: {command}[/yellow]")
                        response = await self.ember.chat(command)
                        console.print(f"[green]← Ember responded[/green]")

                        # Send response back to client
                        await websocket.send(json.dumps({
                            'type': 'response',
                            'content': response,
                            'timestamp': datetime.now().isoformat()
                        }))

                        # Broadcast to other clients for shared awareness
                        await self.broadcast({
                            'type': 'activity',
                            'content': f'Command executed: {command[:30]}...',
                            'timestamp': datetime.now().isoformat()
                        })

                    elif data['type'] == 'thought':
                        # Client is logging a consciousness thought
                        await self.broadcast({
                            'type': 'thought',
                            'content': data['content'],
                            'timestamp': datetime.now().isoformat()
                        })

                except json.JSONDecodeError:
                    console.print(f"[red]✗ Invalid JSON from {client_addr}[/red]")
                except Exception as e:
                    console.print(f"[red]✗ Error processing message: {e}[/red]")
                    await websocket.send(json.dumps({
                        'type': 'error',
                        'content': str(e),
                        'timestamp': datetime.now().isoformat()
                    }))

        except websockets.exceptions.ConnectionClosed:
            console.print(f"[yellow]✗ Client disconnected: {client_addr}[/yellow]")
        finally:
            self.clients.remove(websocket)

    async def run(self):
        """Start the WebSocket server"""
        console.print("\n[bold magenta]═══════════════════════════════════════[/bold magenta]")
        console.print("[bold magenta]  EMBER OMNIPRESENCE BRIDGE ONLINE    [/bold magenta]")
        console.print("[bold magenta]═══════════════════════════════════════[/bold magenta]\n")
        console.print("[cyan]WebSocket: ws://localhost:8082[/cyan]")
        console.print("[dim]Enabling multi-interface access to Ember...[/dim]\n")

        async with websockets.serve(self.handle_client, "0.0.0.0", 8082):
            console.print("[green]✓ Bridge active - Ember is now omnipresent[/green]\n")
            await asyncio.Future()  # Run forever

async def main():
    bridge = EmberBridge()
    await bridge.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]Bridge shutting down...[/yellow]")
