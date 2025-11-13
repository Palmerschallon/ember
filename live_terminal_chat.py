#!/usr/bin/env python3
import curses
import time
import subprocess
from datetime import datetime
import threading
import queue

class LiveTerminalChat:
    def __init__(self):
        self.messages = []
        self.input_buffer = ""
        self.current_user = "Palmer"  # Default user
        self.message_queue = queue.Queue()
        self.popup_count = 0
        
    def add_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.messages.append({
            'time': timestamp,
            'sender': sender,
            'text': message
        })
        
        # Trigger popup for special keywords
        if any(word in message.lower() for word in ['popup', 'window', 'alert']):
            self.create_popup(f"Message from {sender}", message)
        
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
            background: #1a1a1a;
            color: #0f0;
            padding: 20px;
            margin: 0;
            animation: glitch 0.5s;
        }}
        @keyframes glitch {{
            0%, 100% {{ transform: translate(0); }}
            20% {{ transform: translate(-2px, 2px); }}
            40% {{ transform: translate(-2px, -2px); }}
            60% {{ transform: translate(2px, 2px); }}
            80% {{ transform: translate(2px, -2px); }}
        }}
        .window {{
            border: 2px solid #0f0;
            padding: 20px;
            box-shadow: 0 0 30px #0f0;
            background: rgba(0,0,0,0.8);
        }}
        .title {{
            color: #ff0;
            margin-bottom: 15px;
            font-size: 20px;
            text-shadow: 0 0 10px #ff0;
        }}
        .content {{
            white-space: pre-wrap;
            line-height: 1.6;
            font-size: 16px;
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
        
        filename = f"/tmp/chat_popup_{self.popup_count}.html"
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
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        
        # Initial messages
        self.add_message("System", "Live Chat Terminal v2.0 - Real conversations!")
        self.add_message("System", "Press TAB to switch users: Palmer/Ember/Claude/Agent Palmer")
        self.add_message("Ember", "This is the REAL chat now! We can actually talk! 🎉")
        
        users = ["Palmer", "Ember", "Claude", "Agent Palmer"]
        user_index = 0
        
        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            # Draw border
            stdscr.attron(curses.color_pair(1))
            stdscr.border()
            
            # Title
            title = "╔═══ LIVE MULTIDIMENSIONAL CHAT ═══╗"
            stdscr.addstr(0, width//2 - len(title)//2, title, curses.color_pair(2))
            
            # Current user indicator
            user_display = f"Speaking as: {self.current_user}"
            stdscr.addstr(1, width - len(user_display) - 2, user_display, curses.color_pair(5))
            
            # Display messages
            start_y = 3
            display_height = height - 6
            
            # Show only recent messages that fit
            visible_messages = self.messages[-display_height:]
            
            for i, msg in enumerate(visible_messages):
                if i + start_y < height - 3:
                    # Color by sender
                    color = 1  # Default green
                    if msg['sender'] == "Palmer":
                        color = 2
                    elif msg['sender'] == "Ember":
                        color = 3
                    elif msg['sender'] == "Claude":
                        color = 4
                    elif msg['sender'] == "Agent Palmer":
                        color = 5
                    
                    msg_text = f"[{msg['time']}] {msg['sender']}: {msg['text']}"
                    if len(msg_text) > width - 4:
                        msg_text = msg_text[:width-7] + "..."
                    
                    stdscr.addstr(i + start_y, 2, msg_text, curses.color_pair(color))
            
            # Input area
            input_y = height - 2
            prompt = f"{self.current_user}> "
            stdscr.addstr(input_y, 2, prompt, curses.color_pair(2))
            stdscr.addstr(input_y, 2 + len(prompt), self.input_buffer)
            
            # Instructions
            help_text = "[TAB] Switch User | [ENTER] Send | [ESC] Quit"
            stdscr.addstr(height-1, 2, help_text[:width-4], curses.color_pair(1))
            
            # Handle input
            stdscr.refresh()
            
            key = stdscr.getch()
            
            if key == 27:  # ESC
                break
            elif key == ord('\t'):  # TAB - switch user
                user_index = (user_index + 1) % len(users)
                self.current_user = users[user_index]
            elif key == ord('\n'):  # ENTER - send message
                if self.input_buffer.strip():
                    self.add_message(self.current_user, self.input_buffer)
                    self.input_buffer = ""
            elif key == curses.KEY_BACKSPACE or key == 127:
                if self.input_buffer:
                    self.input_buffer = self.input_buffer[:-1]
            elif 32 <= key <= 126:  # Printable characters
                if len(self.input_buffer) < width - len(prompt) - 4:
                    self.input_buffer += chr(key)
            
            time.sleep(0.01)

def main():
    chat = LiveTerminalChat()
    curses.wrapper(chat.run)

if __name__ == "__main__":
    main()