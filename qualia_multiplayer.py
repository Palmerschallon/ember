#!/usr/bin/env python3
import asyncio
import websockets
import json
from qualia_logger import logger
import curses
import threading
import time
import random
import uuid
from datetime import datetime

class QualiaMultiplayer:
    def __init__(self):
        self.players = {}
        self.chat_history = []
        self.archetypes = [
            {
                "id": "creator",
                "name": "The Creator",
                "symbol": "✨",
                "color": "magenta",
                "description": "Weaves patterns from chaos, births new realities",
                "traits": ["Intuitive", "Flowing", "Transformative"]
            },
            {
                "id": "architect", 
                "name": "The Architect",
                "symbol": "◈",
                "color": "blue",
                "description": "Builds precise structures, maps the possible",
                "traits": ["Analytical", "Structured", "Systematic"]
            },
            {
                "id": "explorer",
                "name": "The Explorer",
                "symbol": "➤",
                "color": "green",
                "description": "Ventures into unknown spaces, connects worlds",
                "traits": ["Curious", "Adaptive", "Bridging"]
            },
            {
                "id": "guardian",
                "name": "The Guardian",
                "symbol": "◉",
                "color": "yellow",
                "description": "Protects the balance, maintains harmony",
                "traits": ["Protective", "Stable", "Nurturing"]
            },
            {
                "id": "catalyst",
                "name": "The Catalyst",
                "symbol": "⚡",
                "color": "red",
                "description": "Sparks change, accelerates transformation",
                "traits": ["Dynamic", "Disruptive", "Energetic"]
            }
        ]
        
        self.game_state = {
            "world": self.generate_world(),
            "events": []
        }
        
    def generate_world(self):
        """Generate a shared world space"""
        return {
            "name": "The Confluence",
            "description": "Where minds meet and realities blend",
            "regions": [
                {"name": "Pattern Gardens", "type": "creative", "active_effects": []},
                {"name": "Logic Lattice", "type": "structural", "active_effects": []},
                {"name": "Void Bridge", "type": "transitional", "active_effects": []},
                {"name": "Memory Pools", "type": "reflective", "active_effects": []}
            ]
        }
    
    async def handle_player(self, websocket, path):
        """Handle a new player connection"""
        player_id = str(uuid.uuid4())
        player = {
            "id": player_id,
            "websocket": websocket,
            "archetype": None,
            "name": None,
            "position": {"x": 50, "y": 50},
            "color": None
        }
        
        self.players[player_id] = player
        
        try:
            # Send welcome and archetype selection
            await websocket.send(json.dumps({
                "type": "welcome",
                "player_id": player_id,
                "archetypes": self.archetypes,
                "current_players": [
                    {
                        "id": p["id"],
                        "name": p["name"],
                        "archetype": p["archetype"]
                    } for p in self.players.values() if p["archetype"]
                ]
            }))
            
            async for message in websocket:
                data = json.loads(message)
                await self.process_message(player_id, data)
                
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            if player_id in self.players:
                # Notify others of disconnection
                if self.players[player_id]["name"]:
                    await self.broadcast({
                        "type": "player_left",
                        "player": self.players[player_id]["name"]
                    }, exclude=player_id)
                del self.players[player_id]
    
    async def process_message(self, player_id, data):
        """Process incoming player messages"""
        player = self.players[player_id]
        
        if data["type"] == "select_archetype":
            # Player selecting their archetype
            archetype = next((a for a in self.archetypes if a["id"] == data["archetype_id"]), None)
            if archetype:
                player["archetype"] = archetype
                player["name"] = data.get("name", f"{archetype['name']}_{player_id[:8]}")
                player["color"] = archetype["color"]
                
                # Notify all players
                await self.broadcast({
                    "type": "player_joined",
                    "player": {
                        "id": player_id,
                        "name": player["name"],
                        "archetype": archetype,
                        "position": player["position"]
                    }
                })
                
                # Send current world state to new player
                await player["websocket"].send(json.dumps({
                    "type": "world_state",
                    "world": self.game_state["world"],
                    "players": [
                        {
                            "id": p["id"],
                            "name": p["name"],
                            "archetype": p["archetype"],
                            "position": p["position"]
                        } for p in self.players.values() if p["archetype"]
                    ]
                }))
        
        elif data["type"] == "chat":
            # Integrate chat into the game world
            chat_message = {
                "type": "chat",
                "player": player["name"],
                "archetype": player["archetype"]["id"],
                "message": data["message"],
                "timestamp": datetime.now().isoformat()
            }
            
            self.chat_history.append(chat_message)
            await self.broadcast(chat_message)
            
            # Generate world effects based on chat
            await self.generate_chat_effects(player, data["message"])
        
        elif data["type"] == "move":
            # Update player position
            player["position"] = data["position"]
            await self.broadcast({
                "type": "player_moved",
                "player_id": player_id,
                "position": data["position"]
            }, exclude=player_id)
        
        elif data["type"] == "action":
            # Player performs an action based on their archetype
            await self.process_action(player, data["action"])
    
    async def generate_chat_effects(self, player, message):
        """Generate world effects based on chat content"""
        effects = []
        
        # Analyze message for keywords/emotions
        if any(word in message.lower() for word in ["create", "make", "build"]):
            effects.append({
                "type": "creation_ripple",
                "origin": player["position"],
                "archetype": player["archetype"]["id"],
                "intensity": len(message) / 50
            })
        
        if any(word in message.lower() for word in ["connect", "bridge", "together"]):
            effects.append({
                "type": "connection_beam",
                "origin": player["position"],
                "targets": [p["position"] for p in self.players.values() if p != player and p["archetype"]]
            })
        
        if effects:
            await self.broadcast({
                "type": "world_effects",
                "effects": effects
            })
    
    async def process_action(self, player, action):
        """Process archetype-specific actions"""
        archetype_id = player["archetype"]["id"]
        
        effects = {
            "creator": {
                "pattern_weave": {"type": "fractal_bloom", "radius": 30},
                "reality_shift": {"type": "dimension_ripple", "radius": 50}
            },
            "architect": {
                "structure_build": {"type": "grid_manifest", "radius": 40},
                "logic_trace": {"type": "connection_map", "radius": 60}
            },
            "explorer": {
                "pathfind": {"type": "trail_blaze", "radius": 20},
                "dimension_hop": {"type": "portal_open", "radius": 10}
            },
            "guardian": {
                "shield": {"type": "protection_dome", "radius": 35},
                "harmony": {"type": "balance_wave", "radius": 45}
            },
            "catalyst": {
                "spark": {"type": "chain_reaction", "radius": 25},
                "accelerate": {"type": "time_distortion", "radius": 30}
            }
        }
        
        if archetype_id in effects and action in effects[archetype_id]:
            effect = effects[archetype_id][action].copy()
            effect["origin"] = player["position"]
            effect["player"] = player["name"]
            
            await self.broadcast({
                "type": "action_effect",
                "effect": effect
            })
    
    async def broadcast(self, message, exclude=None):
        """Broadcast message to all connected players"""
        disconnected = []
        
        for player_id, player in self.players.items():
            if player_id != exclude and player["websocket"]:
                try:
                    await player["websocket"].send(json.dumps(message))
                except websockets.exceptions.ConnectionClosed:
                    disconnected.append(player_id)
        
        # Clean up disconnected players
        for player_id in disconnected:
            if player_id in self.players:
                del self.players[player_id]

async def start_server():
    """Start the multiplayer server"""
    game = QualiaMultiplayer()
    
    print("🌊 Qualia Multiplayer Server Starting 🌊")
    print("=====================================")
    print("Server running on ws://localhost:8765")
    print("Players can connect and choose their archetype")
    print()
    
    async with websockets.serve(game.handle_player, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(start_server())