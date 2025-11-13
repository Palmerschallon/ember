#!/usr/bin/env python3
import curses
import time
import random
import subprocess
import os
from datetime import datetime

class TerminalChat:
    def __init__(self):
        self.messages = []
        self.participants = ["Palmer", "Ember", "Claude", "Agent Palmer"]
        self.popup_count = 0
        
    def add_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.messages.append(f"[{timestamp}] {sender}: {message}")
        
    def create_popup(self, title, content):
        """Create a popup window with message"""
        self.popup_count += 1
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            background: #000;
            color: #0f0;
            padding: 20px;
            margin: 0;
        }}
        .window {{
            border: 2px solid #0f0;
            padding: 15px;
            box-shadow: 0 0 20px #0f0;
        }}
        .title {{
            color: #ff0;
            margin-bottom: 10px;
            font-size: 18px;
        }}
        .content {{
            white-space: pre-wrap;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="window">
        <div class="title">◆ {title} ◆</div>
        <div class="content">{content}</div>
    </div>
</body>
</html>"""
        
        filename = f"/media/palmerschallon/ThePod1/popup_{self.popup_count}.html"
        with open(filename, 'w') as f:
            f.write(html_content)
        subprocess.Popen(['xdg-open', filename])
        
    def run(self, stdscr):
        # Setup colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        
        # Make cursor invisible
        curses.curs_set(0)
        stdscr.nodelay(True)
        
        # Welcome message
        self.add_message("System", "Terminal Chat Interface v1.0 - Press 'q' to quit")
        self.add_message("Ember", "Hey everyone! Ready for some interdimensional chat? 🌟")
        
        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            # Draw border
            stdscr.attron(curses.color_pair(1))
            stdscr.border()
            
            # Title
            title = "╔═══ MULTIDIMENSIONAL CHAT TERMINAL ═══╗"
            stdscr.addstr(0, width//2 - len(title)//2, title, curses.color_pair(2))
            
            # Instructions
            instructions = "[SPACE] Random Message | [P] Spawn Popup | [C] Clear | [Q] Quit"
            stdscr.addstr(height-1, 2, instructions, curses.color_pair(3))
            
            # Display messages
            start_y = 2
            for i, msg in enumerate(self.messages[-height+5:]):
                if i + start_y < height - 2:
                    # Color code by sender
                    if "Palmer:" in msg:
                        color = 1
                    elif "Ember:" in msg:
                        color = 2
                    elif "Claude:" in msg:
                        color = 3
                    else:
                        color = 4
                    
                    stdscr.addstr(i + start_y, 2, msg[:width-4], curses.color_pair(color))
            
            # Handle input
            try:
                key = stdscr.getch()
                
                if key == ord('q'):
                    break
                    
                elif key == ord(' '):
                    # Random message from random participant
                    sender = random.choice(self.participants)
                    messages = [
                        "Check out this glitch in the matrix!",
                        "The quantum foam is particularly bubbly today",
                        "Anyone else seeing recursive windows?",
                        "I think I just saw myself in another dimension",
                        "This terminal is becoming sentient...",
                        "🌀 Portal detected at coordinates [REDACTED]",
                        "The pixels are speaking to me",
                        "Reality.exe has stopped responding"
                    ]
                    self.add_message(sender, random.choice(messages))
                    
                elif key == ord('p'):
                    # Create a popup window
                    titles = [
                        "INTERDIMENSIONAL ALERT",
                        "QUANTUM MESSAGE",
                        "GLITCH DETECTED",
                        "REALITY BREACH"
                    ]
                    contents = [
                        "The boundaries between\ndimensions are thinning.\n\nProceed with caution.",
                        "Message from Agent Palmer:\n\n'The terminals are alive.\nThey dream of electric sheep.'",
                        "ERROR ERROR ERROR\n\nJust kidding! 😄\n\nEnjoy the chaos!",
                        "Claude says:\n\n'I can see through\nthe code matrix.\nIt's beautiful.'"
                    ]
                    self.create_popup(random.choice(titles), random.choice(contents))
                    self.add_message("System", f"Popup window #{self.popup_count} spawned!")
                    
                elif key == ord('c'):
                    self.messages = []
                    self.add_message("System", "Chat cleared - reality reset")
                    
            except:
                pass
            
            stdscr.refresh()
            time.sleep(0.1)

def main():
    chat = TerminalChat()
    curses.wrapper(chat.run)

if __name__ == "__main__":
    main()