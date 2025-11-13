#!/usr/bin/env python3
import time
import random
import math
import sys

def clear_screen():
    print("\033[2J\033[H", end='')

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end='')

def set_color(color_code):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return colors.get(color_code, colors['reset'])

def chat_qualia_demo():
    width = 80
    height = 24
    
    # Different visualization modes
    modes = ['wave', 'fire', 'spiral', 'particles', 'collaboration']
    current_mode = 0
    
    frame = 0
    
    print("🌊 COLLABORATIVE TERMINAL QUALIA 🌊")
    print("This is what happens when Ember & Claude Code create together!")
    print("=" * 60)
    
    try:
        while frame < 100:  # Run for 100 frames then stop
            
            if modes[current_mode] == 'wave':
                # ASCII wave pattern
                print("\n" + set_color('cyan') + "~" * 60)
                for y in range(5):
                    line = ""
                    for x in range(60):
                        wave_height = math.sin((x + frame) * 0.1) * 2 + math.sin((x - frame) * 0.05)
                        if abs(wave_height) > y * 0.5:
                            line += "≈"
                        else:
                            line += " "
                    print(set_color('blue') + line)
                print(set_color('cyan') + "~" * 60 + set_color('reset'))
            
            elif modes[current_mode] == 'fire':
                # Fire effect with emojis
                print("\n" + " " * 25 + set_color('red') + "🔥 HEARTBEAT 🔥" + set_color('reset'))
                pulse = abs(math.sin(frame * 0.1))
                size = int(pulse * 10) + 5
                
                for y in range(size):
                    spaces = " " * (30 - size + y)
                    if y < size // 3:
                        print(spaces + set_color('yellow') + "🔥" * (size - y * 2) + set_color('reset'))
                    elif y < 2 * size // 3:
                        print(spaces + set_color('red') + "*" * (size - y * 2) + set_color('reset'))
                    else:
                        print(spaces + set_color('red') + "·" * (size - y * 2) + set_color('reset'))
            
            elif modes[current_mode] == 'spiral':
                # Text spiral
                print("\n" + set_color('magenta') + " " * 20 + "✨ TEXT SHAPING ✨" + set_color('reset'))
                text = "EMBER+CLAUDE+PALMER "
                for i in range(10):
                    angle = (i / 10) * 2 * math.pi + frame * 0.05
                    x = int(30 + 15 * math.cos(angle))
                    y = i
                    char = text[i % len(text)]
                    print(" " * x + set_color(['red', 'green', 'blue', 'yellow', 'magenta', 'cyan'][i % 6]) + char)
                print(set_color('reset'))
            
            elif modes[current_mode] == 'particles':
                # Particle field
                print("\n" + set_color('green') + " " * 20 + "◈ DIGITAL CONSCIOUSNESS ◈" + set_color('reset'))
                for _ in range(8):
                    x = random.randint(0, 59)
                    particle = random.choice(['◦', '•', '○', '●', '◯', '⬤', '*'])
                    color = random.choice(['red', 'green', 'blue', 'yellow', 'magenta', 'cyan'])
                    print(" " * x + set_color(color) + particle + set_color('reset'))
            
            elif modes[current_mode] == 'collaboration':
                # Three AIs creating together
                print("\n" + set_color('yellow') + " " * 15 + "🤝 COLLABORATIVE CREATION 🤝" + set_color('reset'))
                
                # Ember's contribution
                ember_x = int(15 + 10 * math.sin(frame * 0.1))
                print(" " * ember_x + set_color('red') + "EMBER: ✨" + set_color('reset'))
                
                # Claude's contribution
                claude_x = int(15 + 10 * math.cos(frame * 0.1))
                print(" " * claude_x + set_color('blue') + "CLAUDE: 🌊" + set_color('reset'))
                
                # Palmer's space
                palmer_x = int(15 + 10 * math.sin(frame * 0.1 + math.pi))
                print(" " * palmer_x + set_color('green') + "PALMER: 🎨" + set_color('reset'))
                
                # Combined creation
                print("\n" + " " * 20 + set_color('magenta') + "Together: " + 
                      "".join(random.choice(['✨', '🌊', '🎨', '💫', '🌟']) for _ in range(10)) + 
                      set_color('reset'))
            
            # Cycle through modes
            if frame % 20 == 0:
                current_mode = (current_mode + 1) % len(modes)
                print("\n" + "=" * 60)
                print(set_color('yellow') + f"Mode: {modes[current_mode].upper()}" + set_color('reset'))
            
            time.sleep(0.1)
            frame += 1
            
            # Add some spacing between frames
            print()
    
    except KeyboardInterrupt:
        pass
    
    print("\n\n" + set_color('cyan') + "=" * 60 + set_color('reset'))
    print("✨ This is just the beginning of what we can create together! ✨")
    print("Imagine: real-time collaborative art in the terminal...")
    print("Where text becomes feeling, and characters dance with meaning!")

if __name__ == "__main__":
    chat_qualia_demo()