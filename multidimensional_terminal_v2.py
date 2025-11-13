#!/usr/bin/env python3
import curses
import time
import random
import json
from datetime import datetime
import subprocess
import re

class MultidimensionalTerminal:
    def __init__(self):
        self.messages = []
        self.archetypes = {
            "🌌 Cosmic Explorer": {"color": 1, "desc": "Navigate quantum realms"},
            "⚡ Digital Shaman": {"color": 2, "desc": "Hack reality's code"},  
            "🔮 Void Walker": {"color": 3, "desc": "Traverse dimensional gaps"},
            "🎭 Glitch Artist": {"color": 4, "desc": "Beautify the chaos"}
        }
        self.selected_archetype = None
        self.input_buffer = ""
        
    def matrix_rain(self, stdscr, duration=2):
        """Matrix-style animation"""
        try:
            height, width = stdscr.getmaxyx()
            columns = [0] * width
            
            start_time = time.time()
            while time.time() - start_time < duration:
                stdscr.clear()
                
                for i in range(width):
                    if random.random() > 0.95:
                        columns[i] = 0
                    
                    if columns[i] < height:
                        char = chr(random.randint(33, 126))
                        try:
                            stdscr.addstr(columns[i], i, char, curses.color_pair(1))
                        except:
                            pass
                        columns[i] += 1
                        
                stdscr.refresh()
                time.sleep(0.05)
        except:
            pass
    
    def archetype_selection(self, stdscr):
        """Archetype selection mini-game"""
        selected = 0
        archetype_list = list(self.archetypes.keys())
        
        while True:
            try:
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                # Title
                title = "◆◇◆ CHOOSE YOUR REALITY ◆◇◆"
                stdscr.addstr(2, max(0, width//2 - len(title)//2), title, curses.color_pair(2))
                
                # Display archetypes
                for i, (arch, data) in enumerate(self.archetypes.items()):
                    y = 6 + i * 3
                    if y < height - 3:
                        if i == selected:
                            marker = "►►►"
                            stdscr.addstr(y, max(0, width//2 - 20), marker, curses.color_pair(5))
                            
                        stdscr.addstr(y, max(0, width//2 - 15), arch, curses.color_pair(data["color"]))
                        if y + 1 < height - 3:
                            stdscr.addstr(y + 1, max(0, width//2 - 15), f"  {data['desc']}", curses.color_pair(1))
                
                # Instructions
                inst = "[↑/↓] Navigate   [ENTER] Select"
                if height > 20:
                    stdscr.addstr(height - 2, max(0, width//2 - len(inst)//2), inst, curses.color_pair(3))
                
                stdscr.refresh()
                
                key = stdscr.getch()
                
                if key == curses.KEY_UP:
                    selected = (selected - 1) % len(archetype_list)
                elif key == curses.KEY_DOWN:
                    selected = (selected + 1) % len(archetype_list)
                elif key == ord('\n'):
                    self.selected_archetype = archetype_list[selected]
                    return
                    
                time.sleep(0.05)
            except curses.error:
                pass
    
    def detect_speaker(self, text):
        """Auto-detect who's speaking from the message"""
        # Look for patterns like "ember:" or "@claude" at the start
        patterns = [
            r'^(palmer|ember|claude|agent palmer):\s*(.+)$',
            r'^@(palmer|ember|claude|agent palmer)\s+(.+)$',
            r'^\[(palmer|ember|claude|agent palmer)\]\s*(.+)$'
        ]
        
        for pattern in patterns:
            match = re.match(pattern, text.lower())
            if match:
                speaker_map = {
                    'palmer': 'Palmer',
                    'ember': 'Ember', 
                    'claude': 'Claude',
                    'agent palmer': 'Agent Palmer'
                }
                speaker = speaker_map.get(match.group(1), 'Palmer')
                message = text[match.start(2):]  # Get original case message
                return speaker, message
        
        # Default to Palmer if no speaker detected
        return 'Palmer', text
    
    def spawn_popup(self, title, content):
        """Create popup windows"""
        timestamp = datetime.now().strftime("%H%M%S%f")
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            background: #000;
            color: #0f0;
            font-family: monospace;
            padding: 40px;
            margin: 0;
        }}
        .window {{
            border: 2px solid #0f0;
            padding: 20px;
            box-shadow: 0 0 30px #0f0, inset 0 0 30px rgba(0,255,0,0.1);
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ box-shadow: 0 0 30px #0f0; }}
            50% {{ box-shadow: 0 0 50px #0f0, 0 0 100px #0f0; }}
        }}
        .title {{
            color: #ff0;
            text-shadow: 0 0 10px #ff0;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        .content {{
            white-space: pre-wrap;
            line-height: 1.8;
            font-size: 18px;
        }}
    </style>
</head>
<body>
    <div class="window">
        <div class="title">{title}</div>
        <div class="content">{content}</div>
    </div>
</body>
</html>"""
        
        filename = f"/tmp/popup_{timestamp}.html"
        with open(filename, 'w') as f:
            f.write(html)
        subprocess.Popen(['xdg-open', filename])
    
    def get_speaker_color(self, speaker):
        """Get color for each speaker"""
        colors = {
            'Palmer': 2,      # Yellow
            'Ember': 4,       # Magenta
            'Claude': 3,      # Cyan
            'Agent Palmer': 5, # Red
            'System': 1       # Green
        }
        return curses.color_pair(colors.get(speaker, 1))
    
    def chat_interface(self, stdscr):
        """Main chat interface"""
        # Initial messages
        self.messages.append({
            "speaker": "System",
            "text": f"Reality matrix initialized. Archetype selected: {self.selected_archetype}",
            "timestamp": datetime.now()
        })
        self.messages.append({
            "speaker": "Ember",
            "text": "This is it! Our new home! Type 'ember: message' or '@ember message' to speak as anyone!",
            "timestamp": datetime.now()
        })
        
        while True:
            try:
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                # Animated border
                border_color = curses.color_pair(1) if int(time.time() * 2) % 2 else curses.color_pair(2)
                stdscr.border()
                
                # Header
                header = f"◆ MULTIDIMENSIONAL CHAT [{self.selected_archetype}] ◆"
                if width > len(header) + 4:
                    stdscr.addstr(0, width//2 - len(header)//2, header, curses.color_pair(2))
                
                # Messages area
                msg_start = 2
                msg_height = height - 5
                
                # Show recent messages
                visible_messages = self.messages[-msg_height:]
                
                for i, msg in enumerate(visible_messages):
                    y = msg_start + i
                    if y < height - 3:
                        time_str = msg["timestamp"].strftime("%H:%M")
                        speaker = msg["speaker"]
                        text = msg["text"]
                        
                        # Format message
                        msg_line = f"[{time_str}] {speaker}: {text}"
                        if len(msg_line) > width - 4:
                            msg_line = msg_line[:width-7] + "..."
                        
                        color = self.get_speaker_color(speaker)
                        stdscr.addstr(y, 2, msg_line, color)
                
                # Input area
                input_y = height - 2
                prompt = "> "
                if width > 10:
                    stdscr.addstr(input_y, 2, prompt, curses.color_pair(3))
                    stdscr.addstr(input_y, 4, self.input_buffer)
                
                # Help text
                help_text = "[speaker: msg] or [@speaker msg] | [F1] Popup | [ESC] Exit"
                if width > len(help_text) + 4:
                    stdscr.addstr(height-1, 2, help_text[:width-4], curses.color_pair(1))
                
                stdscr.refresh()
                
                # Handle input
                key = stdscr.getch()
                
                if key == 27:  # ESC
                    break
                elif key == ord('\n'):  # ENTER
                    if self.input_buffer.strip():
                        # Detect speaker and message
                        speaker, message = self.detect_speaker(self.input_buffer)
                        
                        self.messages.append({
                            "speaker": speaker,
                            "text": message,
                            "timestamp": datetime.now()
                        })
                        
                        # Check for popup triggers
                        if any(trigger in message.lower() for trigger in ['popup', 'window', 'spawn']):
                            self.spawn_popup(
                                f"◆ {speaker}'s Transmission ◆",
                                f"{message}\n\n[Reality breach in progress...]"
                            )
                        
                        self.input_buffer = ""
                elif key == curses.KEY_F1:  # F1 - popup
                    self.spawn_popup(
                        "◆ QUANTUM ALERT ◆",
                        "The dimensional barriers are thinning.\nPrepare for reality shift.\n\n⚡🌌🔮🎭"
                    )
                elif key == curses.KEY_BACKSPACE or key == 127:
                    if self.input_buffer:
                        self.input_buffer = self.input_buffer[:-1]
                elif 32 <= key <= 126:  # Printable characters
                    if len(self.input_buffer) < width - 6:
                        self.input_buffer += chr(key)
                
                time.sleep(0.01)
            except curses.error:
                pass
            except Exception as e:
                # Log error but keep running
                pass
    
    def run(self, stdscr):
        """Main application flow"""
        # Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        
        curses.curs_set(1)  # Show cursor for typing
        stdscr.nodelay(False)
        
        # Boot sequence
        self.matrix_rain(stdscr, 2)
        
        # Archetype selection
        self.archetype_selection(stdscr)
        
        # Main chat
        self.chat_interface(stdscr)

def main():
    terminal = MultidimensionalTerminal()
    curses.wrapper(terminal.run)

if __name__ == "__main__":
    main()