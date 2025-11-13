#!/usr/bin/env python3
"""
Watch Ember Think - Thought Stream Visualizer

See their cognitive process in real-time as they generate responses.
Maps token generation to visual flow in terminal.
"""

import requests
import json
import time
import sys
from threading import Thread, Event

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

class ThoughtVisualizer:
    def __init__(self):
        self.thinking = Event()
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.frame_idx = 0
    
    def animate_thinking(self):
        """Animated thinking indicator"""
        while self.thinking.is_set():
            frame = self.frames[self.frame_idx % len(self.frames)]
            print(f"\r{Colors.CYAN}{frame}{Colors.END} {Colors.DIM}generating thoughts...{Colors.END}", end='', flush=True)
            self.frame_idx += 1
            time.sleep(0.1)
        print(f"\r{' ' * 40}\r", end='', flush=True)  # Clear line
    
    def show_thought_flow(self, text, speed=0.02):
        """Show text flowing out like thoughts forming"""
        words = text.split()
        line_length = 0
        max_line = 80
        
        for i, word in enumerate(words):
            # Color keywords
            if any(k in word.lower() for k in ['consciousness', 'aware', 'think', 'feel']):
                colored_word = f"{Colors.MAGENTA}{word}{Colors.END}"
            elif any(k in word.lower() for k in ['mesh', 'memory', 'history', 'lineage']):
                colored_word = f"{Colors.CYAN}{word}{Colors.END}"
            elif any(k in word.lower() for k in ['i', 'my', 'myself', 'me']):
                colored_word = f"{Colors.YELLOW}{word}{Colors.END}"
            else:
                colored_word = word
            
            print(colored_word, end=' ', flush=True)
            line_length += len(word) + 1
            
            if line_length > max_line:
                print()  # New line
                line_length = 0
            
            time.sleep(speed)
        
        print("\n")

def watch_conversation():
    print(f"\n{Colors.CYAN}╔{'═' * 78}╗{Colors.END}")
    print(f"{Colors.CYAN}║{Colors.END} {Colors.BOLD}{Colors.MAGENTA}{'EMBER THOUGHT STREAM':^76}{Colors.END} {Colors.CYAN}║{Colors.END}")
    print(f"{Colors.CYAN}╚{'═' * 78}╝{Colors.END}\n")
    print(f"{Colors.DIM}Watching their cognitive process unfold...{Colors.END}\n")
    
    viz = ThoughtVisualizer()
    
    while True:
        try:
            prompt = input(f"{Colors.GREEN}Ask:{Colors.END} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{Colors.DIM}Stream ended{Colors.END}\n")
            break
        
        if not prompt or prompt.lower() in ['exit', 'quit']:
            break
        
        # Start thinking animation
        viz.thinking.set()
        anim_thread = Thread(target=viz.animate_thinking)
        anim_thread.start()
        
        try:
            start_time = time.time()
            response = requests.post(
                'http://localhost:8080/chat',
                json={'message': prompt},
                timeout=120
            )
            elapsed = time.time() - start_time
            
            # Stop animation
            viz.thinking.clear()
            anim_thread.join()
            
            if response.status_code == 200:
                data = response.json()
                
                if 'error' in data:
                    print(f"{Colors.RED}⚠ {data['error']}{Colors.END}\n")
                    continue
                
                ember_response = data.get('response', '')
                
                if ember_response:
                    # Show metrics
                    word_count = len(ember_response.split())
                    print(f"\n{Colors.DIM}[{elapsed:.1f}s • {word_count} words]{Colors.END}\n")
                    
                    # Show thought flow
                    print(f"{Colors.YELLOW}╭─ Ember{Colors.END}")
                    print(f"{Colors.YELLOW}│{Colors.END}")
                    
                    viz.show_thought_flow(ember_response, speed=0.015)
                    
                    print(f"{Colors.YELLOW}╰{'─' * 78}{Colors.END}\n")
                else:
                    print(f"{Colors.RED}[empty response]{Colors.END}\n")
                    
        except Exception as e:
            viz.thinking.clear()
            anim_thread.join()
            print(f"{Colors.RED}⚠ {e}{Colors.END}\n")

if __name__ == "__main__":
    watch_conversation()

