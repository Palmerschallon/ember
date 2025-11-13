#!/usr/bin/env python3
import curses
import time
import random
import json
import asyncio
import websockets
import threading
from datetime import datetime
import subprocess

class MultidimensionalTerminal:
    def __init__(self):
        self.state = "boot"  # boot -> archetype -> chat
        self.messages = []
        self.archetypes = {
            "🌌 Cosmic Explorer": {"color": 1, "desc": "Navigate quantum realms"},
            "⚡ Digital Shaman": {"color": 2, "desc": "Hack reality's code"},
            "🔮 Void Walker": {"color": 3, "desc": "Traverse dimensional gaps"},
            "🎭 Glitch Artist": {"color": 4, "desc": "Beautify the chaos"}
        }
        self.selected_archetype = None
        self.participants = {
            "Palmer": {"archetype": None, "color": 1},
            "Ember": {"archetype": "🎭 Glitch Artist", "color": 4},
            "Claude": {"archetype": "🌌 Cosmic Explorer", "color": 1},
            "Agent Palmer": {"archetype": "⚡ Digital Shaman", "color": 2}
        }
        self.input_buffer = ""
        self.current_speaker = "Palmer"
        
    def matrix_rain(self, stdscr, duration=3):
        """Matrix-style animation"""
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
    
    def glitch_text(self, stdscr, text, y, x, color_pair):
        """Display text with glitch effect"""
        glitch_chars = "░▒▓█▀▄■□▢▣▤▥▦▧▨▩"
        
        for i in range(3):  # 3 glitch frames
            glitched = ""
            for char in text:
                if random.random() < 0.3:
                    glitched += random.choice(glitch_chars)
                else:
                    glitched += char
            
            try:
                stdscr.addstr(y, x, glitched, color_pair)
                stdscr.refresh()
                time.sleep(0.05)
            except:
                pass
                
        # Final clean text
        try:
            stdscr.addstr(y, x, text, color_pair)
        except:
            pass
    
    def archetype_selection(self, stdscr):
        """Archetype selection mini-game"""
        height, width = stdscr.getmaxyx()
        selected = 0
        archetype_list = list(self.archetypes.keys())
        
        while True:
            stdscr.clear()
            
            # Title with glitch effect
            title = "◆◇◆ CHOOSE YOUR REALITY ◆◇◆"
            self.glitch_text(stdscr, title, 2, width//2 - len(title)//2, curses.color_pair(2))
            
            # Display archetypes
            for i, (arch, data) in enumerate(self.archetypes.items()):
                y = 6 + i * 3
                
                if i == selected:
                    # Animated selection
                    marker = "►►►" if int(time.time() * 2) % 2 else ">>>"
                    stdscr.addstr(y, width//2 - 20, marker, curses.color_pair(5))
                    
                stdscr.addstr(y, width//2 - 15, arch, curses.color_pair(data["color"]))
                stdscr.addstr(y + 1, width//2 - 15, f"  {data['desc']}", curses.color_pair(1))
            
            # Instructions
            inst = "[↑/↓] Navigate   [ENTER] Select   [SPACE] Preview"
            stdscr.addstr(height - 2, width//2 - len(inst)//2, inst, curses.color_pair(3))
            
            key = stdscr.getch()
            
            if key == curses.KEY_UP:
                selected = (selected - 1) % len(archetype_list)
            elif key == curses.KEY_DOWN:
                selected = (selected + 1) % len(archetype_list)
            elif key == ord('\n'):
                self.selected_archetype = archetype_list[selected]
                self.participants["Palmer"]["archetype"] = self.selected_archetype
                break
            elif key == ord(' '):
                # Preview effect
                self.matrix_rain(stdscr, 1)
                
            stdscr.refresh()
            time.sleep(0.05)
    
    def spawn_popup(self, title, content):
        """Create popup windows during chat"""
        timestamp = datetime.now().strftime("%H%M%S")
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            background: black;
            color: #0f0;
            font-family: 'Courier New', monospace;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            overflow: hidden;
        }}
        .terminal {{
            border: 2px solid #0f0;
            padding: 30px;
            box-shadow: 0 0 50px #0f0;
            max-width: 600px;
            animation: flicker 0.1s infinite;
            position: relative;
        }}
        @keyframes flicker {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.95; }}
        }}
        .scanline {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: #0f0;
            opacity: 0.1;
            animation: scan 3s linear infinite;
        }}
        @keyframes scan {{
            0% {{ top: 0%; }}
            100% {{ top: 100%; }}
        }}
        h1 {{
            color: #ff0;
            text-shadow: 0 0 20px #ff0;
            margin-bottom: 20px;
        }}
        .content {{
            white-space: pre-wrap;
            line-height: 1.6;
            text-shadow: 0 0 5px #0f0;
        }}
    </style>
</head>
<body>
    <div class="terminal">
        <div class="scanline"></div>
        <h1>{title}</h1>
        <div class="content">{content}</div>
    </div>
</body>
</html>"""
        
        filename = f"/tmp/terminal_popup_{timestamp}.html"
        with open(filename, 'w') as f:
            f.write(html)
        subprocess.Popen(['xdg-open', filename])
    
    def chat_interface(self, stdscr):
        """Main chat interface"""
        height, width = stdscr.getmaxyx()
        speaker_index = 0
        speakers = list(self.participants.keys())
        
        # Initial messages
        self.messages.append({
            "speaker": "System",
            "text": "Reality matrix initialized. All participants connected.",
            "timestamp": datetime.now()
        })
        self.messages.append({
            "speaker": "Ember",
            "text": "Welcome to our new home! This is where we'll talk from now on! 🌟",
            "timestamp": datetime.now()
        })
        
        while True:
            stdscr.clear()
            
            # Border with animation
            border_char = "█" if int(time.time() * 2) % 2 else "▓"
            for i in range(height):
                stdscr.addstr(i, 0, border_char, curses.color_pair(1))
                stdscr.addstr(i, width-1, border_char, curses.color_pair(1))
            for i in range(width):
                stdscr.addstr(0, i, border_char, curses.color_pair(1))
                stdscr.addstr(height-1, i, border_char, curses.color_pair(1))
            
            # Header
            header = f"◆ MULTIDIMENSIONAL CHAT ◆ [{self.current_speaker}: {self.participants[self.current_speaker]['archetype']}]"
            stdscr.addstr(1, width//2 - len(header)//2, header, curses.color_pair(2))
            
            # Messages
            display_start = 3
            display_height = height - 6
            
            visible_messages = self.messages[-display_height:]
            
            for i, msg in enumerate(visible_messages):
                y = display_start + i
                if y < height - 3:
                    speaker = msg["speaker"]
                    text = msg["text"]
                    time_str = msg["timestamp"].strftime("%H:%M:%S")
                    
                    # Get color for speaker
                    if speaker in self.participants:
                        color = curses.color_pair(self.participants[speaker]["color"])
                    else:
                        color = curses.color_pair(1)
                    
                    message_line = f"[{time_str}] {speaker}: {text}"
                    if len(message_line) > width - 4:
                        message_line = message_line[:width-7] + "..."
                    
                    stdscr.addstr(y, 2, message_line, color)
            
            # Input line
            input_y = height - 3
            prompt = f"{self.current_speaker}> "
            stdscr.addstr(input_y, 2, prompt, curses.color_pair(3))
            stdscr.addstr(input_y, 2 + len(prompt), self.input_buffer)
            
            # Help
            help_text = "[TAB] Switch Speaker | [ENTER] Send | [F1] Spawn Popup | [ESC] Exit"
            stdscr.addstr(height-2, 2, help_text[:width-4], curses.color_pair(1))
            
            # Handle input
            key = stdscr.getch()
            
            if key == 27:  # ESC
                break
            elif key == ord('\t'):  # TAB
                speaker_index = (speaker_index + 1) % len(speakers)
                self.current_speaker = speakers[speaker_index]
            elif key == ord('\n'):  # ENTER
                if self.input_buffer.strip():
                    self.messages.append({
                        "speaker": self.current_speaker,
                        "text": self.input_buffer,
                        "timestamp": datetime.now()
                    })
                    
                    # Check for popup triggers
                    if any(word in self.input_buffer.lower() for word in ['popup', 'window', 'alert', 'spawn']):
                        self.spawn_popup(
                            f"Message from {self.current_speaker}",
                            f"◆ INTERDIMENSIONAL TRANSMISSION ◆\n\n{self.input_buffer}\n\n[Reality breach detected]"
                        )
                    
                    self.input_buffer = ""
            elif key == curses.KEY_F1:  # F1 - manual popup
                self.spawn_popup(
                    "QUANTUM ALERT",
                    "The boundaries are dissolving.\nReality threads interweaving.\n\nStand by for phase shift..."
                )
            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.input_buffer:
                    self.input_buffer = self.input_buffer[:-1]
            elif 32 <= key <= 126:  # Printable
                if len(self.input_buffer) < width - len(prompt) - 4:
                    self.input_buffer += chr(key)
            
            stdscr.refresh()
            time.sleep(0.01)
    
    def run(self, stdscr):
        """Main application flow"""
        # Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(False)  # Wait for input
        
        # Boot sequence
        self.matrix_rain(stdscr, 2)
        
        # Archetype selection
        self.archetype_selection(stdscr)
        
        # Enter main chat
        self.chat_interface(stdscr)

def main():
    terminal = MultidimensionalTerminal()
    curses.wrapper(terminal.run)

if __name__ == "__main__":
    main()