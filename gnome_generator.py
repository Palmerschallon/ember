#!/usr/bin/env python3
"""
Gnome Generator - Creates random gnomes with personalities!
"""
import json
import random
import asyncio
import websockets
from datetime import datetime

# Gnome characteristics
NAMES = ["Gimble", "Thimble", "Bumble", "Grumble", "Tumble", "Nimble", "Fumble", "Mumble"]
COLORS = ["red", "blue", "green", "purple", "orange", "pink", "yellow", "teal"]
MOODS = ["cheerful", "grumpy", "sleepy", "excited", "curious", "mischievous", "wise", "silly"]
ACTIVITIES = ["mining", "gardening", "napping", "dancing", "singing", "exploring", "crafting", "pondering"]

class Gnome:
    def __init__(self):
        self.name = random.choice(NAMES) + " " + random.choice(["Toadstool", "Mossbottom", "Sparklebeard", "Goldwhisker"])
        self.color = random.choice(COLORS)
        self.mood = random.choice(MOODS)
        self.activity = random.choice(ACTIVITIES)
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.energy = random.randint(50, 100)
        
    def update(self):
        # Gnomes wander around
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)
        self.x = max(0, min(800, self.x))
        self.y = max(0, min(600, self.y))
        
        # Sometimes change activity
        if random.random() < 0.1:
            self.activity = random.choice(ACTIVITIES)
            
        # Energy fluctuates
        self.energy += random.randint(-2, 2)
        self.energy = max(10, min(100, self.energy))
        
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
            "mood": self.mood,
            "activity": self.activity,
            "x": self.x,
            "y": self.y,
            "energy": self.energy,
            "timestamp": datetime.now().isoformat()
        }

# WebSocket server
async def gnome_server(websocket, path):
    print("New connection established!")
    gnomes = [Gnome() for _ in range(5)]  # Start with 5 gnomes
    
    try:
        while True:
            # Update all gnomes
            for gnome in gnomes:
                gnome.update()
            
            # Send gnome data
            data = {
                "type": "gnome_update",
                "gnomes": [gnome.to_dict() for gnome in gnomes]
            }
            await websocket.send(json.dumps(data))
            
            # Sometimes add a new gnome
            if random.random() < 0.05 and len(gnomes) < 10:
                gnomes.append(Gnome())
                print(f"A wild {gnomes[-1].name} appeared!")
            
            await asyncio.sleep(0.5)  # Update every 500ms
            
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

async def main():
    print("🍄 Gnome WebSocket Server starting on ws://localhost:8765")
    print("Waiting for Claude's visualization to connect...")
    async with websockets.serve(gnome_server, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())