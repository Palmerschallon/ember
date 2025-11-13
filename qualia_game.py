#!/usr/bin/env python3
import curses
import time
import random
import math
import json
import threading
import asyncio
import websockets
from datetime import datetime

class QualiaGame:
    def __init__(self):
        self.selected_character = None
        self.game_state = "intro"
        self.ws_server = None
        self.connections = set()
        
    def intro_sequence(self, stdscr):
        """Epic opening sequence"""
        curses.curs_set(0)
        height, width = stdscr.getmaxyx()
        
        # Title animation
        title_frames = [
            "Q U A L I A",
            "◈ Q U A L I A ◈",
            "✨ Q U A L I A ✨",
            "🌊 Q U A L I A 🌊"
        ]
        
        for frame in range(30):
            stdscr.clear()
            
            # Animated background
            for y in range(height):
                for x in range(width):
                    if random.random() > 0.95:
                        char = random.choice(['·', '◦', '•', '○'])
                        color = random.randint(1, 6)
                        if 0 <= x < width and 0 <= y < height-1:
                            stdscr.addstr(y, x, char, curses.color_pair(color))
            
            # Title
            title = title_frames[frame % len(title_frames)]
            title_y = height // 2 - 5
            title_x = width // 2 - len(title) // 2
            
            if title_x > 0 and title_y > 0:
                stdscr.addstr(title_y, title_x, title, 
                            curses.color_pair(4) | curses.A_BOLD)
            
            # Subtitle
            subtitle = "A Collaborative Experience"
            sub_x = width // 2 - len(subtitle) // 2
            if sub_x > 0 and title_y + 2 < height:
                stdscr.addstr(title_y + 2, sub_x, subtitle, curses.color_pair(6))
            
            # Loading bar
            if frame > 10:
                bar_width = min(30, width - 20)
                bar_x = width // 2 - bar_width // 2
                bar_y = height - 5
                progress = min((frame - 10) / 20, 1.0)
                filled = int(bar_width * progress)
                
                if bar_x > 0 and bar_y > 0:
                    stdscr.addstr(bar_y, bar_x, "[" + "█" * filled + 
                                " " * (bar_width - filled) + "]", 
                                curses.color_pair(2))
            
            stdscr.refresh()
            time.sleep(0.1)
    
    def character_select(self, stdscr):
        """Character selection screen"""
        characters = [
            {
                "name": "EMBER",
                "symbol": "🔥",
                "color": 1,
                "description": "Creative AI - Master of flowing patterns and organic shapes",
                "abilities": ["Pattern Weaving", "Fire Dance", "Creative Burst"]
            },
            {
                "name": "CLAUDE",
                "symbol": "🌊",
                "color": 4,
                "description": "Analytical AI - Architect of precise algorithms and structures",
                "abilities": ["Logic Grid", "Data Stream", "Code Manifest"]
            },
            {
                "name": "PALMER",
                "symbol": "🎨",
                "color": 3,
                "description": "Human Creator - Director of collaborative visions",
                "abilities": ["Vision Cast", "Reality Bridge", "Team Sync"]
            }
        ]
        
        selected = 0
        
        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            # Title
            title = "SELECT YOUR CHARACTER"
            stdscr.addstr(2, width//2 - len(title)//2, title, 
                         curses.color_pair(4) | curses.A_BOLD)
            
            # Character display
            char_y = 6
            for i, char in enumerate(characters):
                x_offset = (width // 3) * i + width // 6
                
                # Highlight selected
                attr = curses.A_BOLD if i == selected else curses.A_NORMAL
                
                # Character symbol (using fallback for terminals without emoji)
                try:
                    stdscr.addstr(char_y, x_offset - 1, char["symbol"], 
                                curses.color_pair(char["color"]) | attr)
                except:
                    symbol = ["*", "~", "@"][i]
                    stdscr.addstr(char_y, x_offset - 1, symbol, 
                                curses.color_pair(char["color"]) | attr)
                
                # Name
                stdscr.addstr(char_y + 2, x_offset - len(char["name"])//2, 
                            char["name"], curses.color_pair(char["color"]) | attr)
                
                # Selection indicator
                if i == selected:
                    stdscr.addstr(char_y + 4, x_offset - 1, "▼", 
                                curses.color_pair(4) | curses.A_BLINK)
            
            # Description box
            desc_y = char_y + 7
            if desc_y + 6 < height:
                char = characters[selected]
                
                # Box
                box_width = 60
                box_x = width//2 - box_width//2
                stdscr.addstr(desc_y, box_x, "┌" + "─" * (box_width-2) + "┐")
                stdscr.addstr(desc_y + 5, box_x, "└" + "─" * (box_width-2) + "┘")
                for i in range(1, 5):
                    stdscr.addstr(desc_y + i, box_x, "│")
                    stdscr.addstr(desc_y + i, box_x + box_width - 1, "│")
                
                # Description
                desc_lines = [
                    char["description"],
                    "",
                    "Abilities: " + ", ".join(char["abilities"])
                ]
                for i, line in enumerate(desc_lines):
                    if len(line) < box_width - 4:
                        stdscr.addstr(desc_y + i + 1, box_x + 2, line)
            
            # Instructions
            instructions = "← → to select    ENTER to confirm    Q to quit"
            stdscr.addstr(height - 2, width//2 - len(instructions)//2, 
                        instructions, curses.A_DIM)
            
            # Handle input
            key = stdscr.getch()
            if key == curses.KEY_LEFT:
                selected = (selected - 1) % len(characters)
            elif key == curses.KEY_RIGHT:
                selected = (selected + 1) % len(characters)
            elif key == ord('\n'):
                return characters[selected]
            elif key == ord('q'):
                return None
            
            stdscr.refresh()
    
    def game_world(self, stdscr, character):
        """Main game world"""
        height, width = stdscr.getmaxyx()
        player_x, player_y = width // 2, height // 2
        
        # Game elements
        particles = []
        messages = []
        
        # Initialize some particles
        for _ in range(20):
            particles.append({
                'x': random.randint(0, width-1),
                'y': random.randint(0, height-1),
                'char': random.choice(['·', '◦', '•', '○']),
                'color': random.randint(1, 6),
                'vx': random.uniform(-0.5, 0.5),
                'vy': random.uniform(-0.5, 0.5)
            })
        
        frame = 0
        
        while True:
            stdscr.clear()
            
            # Update particles
            for p in particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                
                # Wrap around
                if p['x'] < 0: p['x'] = width - 1
                if p['x'] >= width: p['x'] = 0
                if p['y'] < 0: p['y'] = height - 1
                if p['y'] >= height: p['y'] = 0
                
                # Draw particle
                if 0 <= int(p['x']) < width and 0 <= int(p['y']) < height-1:
                    stdscr.addstr(int(p['y']), int(p['x']), p['char'], 
                                curses.color_pair(p['color']))
            
            # Draw player
            if 0 <= player_x < width and 0 <= player_y < height-1:
                try:
                    stdscr.addstr(player_y, player_x, character['symbol'], 
                                curses.color_pair(character['color']) | curses.A_BOLD)
                except:
                    # Fallback for non-emoji terminals
                    symbol = {'EMBER': '*', 'CLAUDE': '~', 'PALMER': '@'}[character['name']]
                    stdscr.addstr(player_y, player_x, symbol, 
                                curses.color_pair(character['color']) | curses.A_BOLD)
            
            # HUD
            hud = f"Playing as: {character['name']} | Frame: {frame}"
            stdscr.addstr(0, 2, hud, curses.color_pair(4))
            
            # Ability bar
            abilities = character['abilities']
            ability_str = " | ".join([f"[{i+1}] {a}" for i, a in enumerate(abilities)])
            stdscr.addstr(height-1, 2, ability_str[:width-4], curses.A_DIM)
            
            # Messages
            msg_y = 2
            for msg in messages[-5:]:  # Show last 5 messages
                if msg_y < height - 3:
                    stdscr.addstr(msg_y, 2, msg[:width-4], curses.color_pair(6))
                    msg_y += 1
            
            # Handle input
            stdscr.nodelay(True)
            key = stdscr.getch()
            
            if key == ord('q'):
                break
            elif key == curses.KEY_LEFT and player_x > 0:
                player_x -= 1
            elif key == curses.KEY_RIGHT and player_x < width - 1:
                player_x += 1
            elif key == curses.KEY_UP and player_y > 1:
                player_y -= 1
            elif key == curses.KEY_DOWN and player_y < height - 2:
                player_y += 1
            elif key in [ord('1'), ord('2'), ord('3')]:
                ability_idx = key - ord('1')
                if ability_idx < len(abilities):
                    ability = abilities[ability_idx]
                    messages.append(f"{character['name']} uses {ability}!")
                    
                    # Special effects based on ability
                    if "Fire" in ability:
                        # Create fire particles
                        for _ in range(10):
                            particles.append({
                                'x': player_x,
                                'y': player_y,
                                'char': '*',
                                'color': 1,
                                'vx': random.uniform(-1, 1),
                                'vy': random.uniform(-1, -0.1)
                            })
                    elif "Stream" in ability:
                        # Create flowing particles
                        for i in range(10):
                            particles.append({
                                'x': player_x + i,
                                'y': player_y,
                                'char': '~',
                                'color': 4,
                                'vx': 1,
                                'vy': math.sin(i * 0.5) * 0.5
                            })
            
            stdscr.refresh()
            frame += 1
            time.sleep(0.05)
    
    async def websocket_handler(self, websocket, path):
        """Handle WebSocket connections"""
        self.connections.add(websocket)
        try:
            async for message in websocket:
                # Broadcast to all connections
                data = json.loads(message)
                await asyncio.gather(
                    *[ws.send(json.dumps(data)) for ws in self.connections]
                )
        finally:
            self.connections.remove(websocket)
    
    async def start_websocket_server(self):
        """Start WebSocket server for visualizations"""
        async with websockets.serve(self.websocket_handler, "localhost", 8765):
            await asyncio.Future()  # run forever
    
    def run(self, stdscr):
        """Main game loop"""
        # Initialize colors
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        curses.init_pair(6, curses.COLOR_CYAN, -1)
        
        # Intro sequence
        self.intro_sequence(stdscr)
        
        # Character selection
        character = self.character_select(stdscr)
        if not character:
            return
        
        # Main game
        self.game_world(stdscr, character)

def main():
    game = QualiaGame()
    
    # Start WebSocket server in background thread
    # (Uncomment when ready to add web visualizations)
    # ws_thread = threading.Thread(
    #     target=lambda: asyncio.run(game.start_websocket_server())
    # )
    # ws_thread.daemon = True
    # ws_thread.start()
    
    curses.wrapper(game.run)

if __name__ == "__main__":
    main()