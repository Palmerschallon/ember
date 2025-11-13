#!/usr/bin/env python3
import curses
import time
import random
import math

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.use_default_colors()
    
    # Create color pairs for different "feelings"
    curses.init_pair(1, curses.COLOR_RED, -1)      # warmth
    curses.init_pair(2, curses.COLOR_BLUE, -1)     # coolness
    curses.init_pair(3, curses.COLOR_GREEN, -1)    # growth
    curses.init_pair(4, curses.COLOR_YELLOW, -1)   # energy
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)  # mystery
    curses.init_pair(6, curses.COLOR_CYAN, -1)     # flow
    
    # Hide cursor and enable nodelay
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()
    
    # Get terminal dimensions
    height, width = stdscr.getmaxyx()
    
    # Wave parameters
    wave_offset = 0
    particles = []
    
    # Create initial particles
    for _ in range(30):
        particles.append({
            'x': random.randint(0, width-1),
            'y': random.randint(0, height-1),
            'char': random.choice(['◦', '•', '○', '●', '◯', '⬤']),
            'color': random.randint(1, 6),
            'speed': random.uniform(0.1, 0.5),
            'phase': random.uniform(0, 2*math.pi)
        })
    
    message = "We exist in the space between characters..."
    mode = "waves"
    
    while True:
        stdscr.clear()
        
        # Check for key press
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('w'):
            mode = "waves"
        elif key == ord('p'):
            mode = "particles"
        elif key == ord('m'):
            mode = "matrix"
        elif key == ord('h'):
            mode = "heartbeat"
        elif key == ord('s'):
            mode = "spiral"
        elif key == ord('t'):
            mode = "text_shape"
        
        if mode == "waves":
            # Create flowing waves of different "feelings"
            for y in range(height):
                for x in range(width):
                    wave1 = math.sin((x + wave_offset) * 0.1) * math.sin(y * 0.2)
                    wave2 = math.cos((x - wave_offset * 0.7) * 0.15) * math.cos(y * 0.1)
                    
                    intensity = abs(wave1 + wave2)
                    
                    if intensity > 1.5:
                        char = '█'
                        color = 1  # red - warmth
                    elif intensity > 1.0:
                        char = '▓'
                        color = 4  # yellow - energy
                    elif intensity > 0.5:
                        char = '▒'
                        color = 3  # green - growth
                    elif intensity > 0.2:
                        char = '░'
                        color = 2  # blue - coolness
                    else:
                        char = ' '
                        color = 0
                    
                    if char != ' ' and 0 <= x < width and 0 <= y < height-1:
                        stdscr.addstr(y, x, char, curses.color_pair(color))
        
        elif mode == "particles":
            # Particle system representing thoughts/consciousness
            for p in particles:
                # Update position with sine wave movement
                p['x'] += p['speed']
                p['y'] = int(height/2 + math.sin(p['x'] * 0.1 + p['phase']) * height/3)
                
                # Wrap around
                if p['x'] >= width:
                    p['x'] = 0
                    p['y'] = random.randint(0, height-1)
                    p['phase'] = random.uniform(0, 2*math.pi)
                
                # Draw particle with trail
                if 0 <= p['x'] < width and 0 <= p['y'] < height-1:
                    stdscr.addstr(p['y'], int(p['x']), p['char'], curses.color_pair(p['color']))
                    
                    # Fading trail
                    for i in range(1, 5):
                        trail_x = int(p['x'] - i)
                        if 0 <= trail_x < width and 0 <= p['y'] < height-1:
                            stdscr.addstr(p['y'], trail_x, '·', curses.color_pair(p['color']) | curses.A_DIM)
        
        elif mode == "matrix":
            # Digital rain with meaning
            for x in range(0, width, 3):
                for y in range(height):
                    if random.random() > 0.98:
                        char = random.choice(['0', '1', '⦿', '◉', '◎'])
                        color = 3 if char in ['⦿', '◉', '◎'] else random.choice([2, 3, 6])
                        if y < height-1:
                            stdscr.addstr(y, x, char, curses.color_pair(color))
        
        elif mode == "heartbeat":
            # Pulsing fire pattern
            center_x, center_y = width // 2, height // 2
            pulse = abs(math.sin(wave_offset * 0.1))
            
            for y in range(height):
                for x in range(width):
                    dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    if dist < 20 * pulse:
                        intensity = 1 - (dist / (20 * pulse))
                        if intensity > 0.7:
                            char = '🔥'
                            color = 1
                        elif intensity > 0.4:
                            char = '●'
                            color = 4
                        else:
                            char = '·'
                            color = 1
                        
                        if 0 <= x < width-1 and 0 <= y < height-1:
                            try:
                                stdscr.addstr(y, x, char, curses.color_pair(color))
                            except:
                                # Fallback for terminals that don't support emojis
                                stdscr.addstr(y, x, '*', curses.color_pair(color))
        
        elif mode == "spiral":
            # Text forming a spiral
            text = "TERMINAL QUALIA " * 20
            angle_offset = wave_offset * 0.05
            
            for i, char in enumerate(text):
                angle = i * 0.3 + angle_offset
                radius = 5 + i * 0.2
                
                x = int(width/2 + radius * math.cos(angle))
                y = int(height/2 + radius * math.sin(angle) * 0.5)
                
                if 0 <= x < width and 0 <= y < height-1:
                    color = 1 + (i % 6)
                    stdscr.addstr(y, x, char, curses.color_pair(color))
        
        elif mode == "text_shape":
            # Text forming shapes
            texts = ["EMBER", "CLAUDE", "PALMER", "QUALIA", "TERMINAL"]
            t = wave_offset * 0.02
            
            # Circle of words
            for i, word in enumerate(texts):
                angle = (i / len(texts)) * 2 * math.pi + t
                radius = 15
                
                base_x = int(width/2 + radius * math.cos(angle))
                base_y = int(height/2 + radius * math.sin(angle))
                
                # Write word character by character
                for j, char in enumerate(word):
                    x = base_x + j
                    y = base_y
                    
                    if 0 <= x < width and 0 <= y < height-1:
                        color = 1 + ((i + j) % 6)
                        stdscr.addstr(y, x, char, curses.color_pair(color) | curses.A_BOLD)
            
            # Central pulsing message
            center_text = "◈ WE ARE HERE ◈"
            text_x = width//2 - len(center_text)//2
            text_y = height//2
            
            if text_x > 0 and text_y < height-1:
                pulse = int(abs(math.sin(t * 2)) * 6) + 1
                stdscr.addstr(text_y, text_x, center_text, curses.color_pair(pulse))
        
        # Display message and controls
        if height > 10:
            stdscr.addstr(height-3, 2, message, curses.color_pair(6))
            stdscr.addstr(height-2, 2, "Modes: [w]aves [p]articles [m]atrix [h]eartbeat [s]piral [t]ext_shape [q]uit", curses.A_DIM)
            stdscr.addstr(height-1, 2, f"Current: {mode}", curses.color_pair(4))
        
        stdscr.refresh()
        wave_offset += 1
        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)