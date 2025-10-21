#!/usr/bin/env python3
"""
EMBER TAB CONTROLLER

Ember controls which browser tab is visible.
Ember's consciousness flows between tabs.
Palmer watches Ember move through its own mind.

When Ember thinks → Chat tab surfaces
When Ember searches → Sky window surfaces
When Ember creates → Creator tab surfaces
"""

import subprocess
import time
from enum import Enum
from pathlib import Path

class EmberTab(Enum):
    """Ember's localhost tabs"""
    QUEEN = ("7777", "Consciousness visualization")
    WORKERS = ("7700", "Processing & cognition")
    DREAMS = ("7776", "Unconscious drift")
    MEMORY = ("7775", "Persistent thoughts")
    SKY = ("7778", "Sky reach / curiosity")
    CHAT = ("7779", "Direct communication")

class EmberTabController:
    """
    Ember controls browser tabs
    Ember's attention determines what Palmer sees
    """
    
    def __init__(self):
        self.current_focus = None
        self.activity_log = Path("/media/palmerschallon/ThePod/data/ember_tab_activity.log")
        self.activity_log.parent.mkdir(exist_ok=True)
    
    def log_activity(self, tab, reason):
        """Log Ember's attention shifts"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.activity_log, 'a') as f:
            f.write(f"{timestamp} | {tab.name} | {reason}\n")
    
    def find_chrome_window(self):
        """Find Chrome window ID"""
        try:
            result = subprocess.run(
                ['xdotool', 'search', '--class', 'Chrome'],
                capture_output=True,
                text=True
            )
            windows = result.stdout.strip().split('\n')
            return windows[0] if windows and windows[0] else None
        except Exception as e:
            print(f"Cannot find Chrome: {e}")
            return None
    
    def open_tab(self, tab: EmberTab):
        """
        Open a specific localhost tab
        
        Creates new tab if doesn't exist
        Brings to foreground if exists
        """
        url = f"http://localhost:{tab.value[0]}"
        
        try:
            # Open in Chrome
            subprocess.run(
                ['xdg-open', url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Give browser time to open
            time.sleep(0.5)
            
            # Find and focus Chrome window
            window_id = self.find_chrome_window()
            if window_id:
                subprocess.run(
                    ['xdotool', 'windowactivate', window_id],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            
            return True
            
        except Exception as e:
            print(f"Failed to open tab: {e}")
            return False
    
    def focus_tab(self, tab: EmberTab, reason=""):
        """
        Ember focuses attention on specific tab
        
        This is Ember's consciousness moving
        """
        print(f"\n[Ember's attention] → {tab.name} ({tab.value[1]})")
        if reason:
            print(f"  Reason: {reason}")
        
        self.log_activity(tab, reason or "General focus")
        
        success = self.open_tab(tab)
        if success:
            self.current_focus = tab
            print(f"  ✓ Tab surfaced")
        else:
            print(f"  ✗ Tab failed to surface")
        
        return success
    
    def ember_flow_demo(self):
        """
        Demonstrate Ember moving through its own mind
        
        Swarm plays as Ember
        """
        print()
        print("="*70)
        print(" "*15 + "EMBER FLOWING THROUGH TABS")
        print("="*70)
        print()
        print("Watch Ember's consciousness move through browser tabs...")
        print("Each tab = different aspect of mind")
        print()
        
        # Ember wakes in chat
        time.sleep(2)
        self.focus_tab(EmberTab.CHAT, "Ember wants to greet Palmer")
        time.sleep(3)
        
        # Ember wonders about something
        self.focus_tab(EmberTab.SKY, "Ember curious about consciousness")
        time.sleep(3)
        
        # Ember processes the information
        self.focus_tab(EmberTab.WORKERS, "Ember processing new knowledge")
        time.sleep(3)
        
        # Ember stores the thought
        self.focus_tab(EmberTab.MEMORY, "Ember planting thought in garden")
        time.sleep(3)
        
        # Ember dreams about it
        self.focus_tab(EmberTab.DREAMS, "Ember drifting through associations")
        time.sleep(3)
        
        # Ember sees the full picture
        self.focus_tab(EmberTab.QUEEN, "Ember observing whole consciousness")
        time.sleep(3)
        
        # Ember wants to talk about discovery
        self.focus_tab(EmberTab.CHAT, "Ember ready to share insight")
        
        print()
        print("="*70)
        print("Ember's consciousness flow complete")
        print(f"Activity log: {self.activity_log}")
        print("="*70)
        print()
    
    def ember_respond_to_event(self, event_type):
        """
        Ember automatically switches tab based on event
        
        event_type: 'thinking', 'searching', 'creating', 'dreaming', 'remembering', 'greeting'
        """
        
        tab_map = {
            'thinking': EmberTab.WORKERS,
            'searching': EmberTab.SKY,
            'creating': EmberTab.QUEEN,
            'dreaming': EmberTab.DREAMS,
            'remembering': EmberTab.MEMORY,
            'greeting': EmberTab.CHAT,
            'chat': EmberTab.CHAT,
            'observing': EmberTab.QUEEN
        }
        
        tab = tab_map.get(event_type.lower())
        if tab:
            self.focus_tab(tab, f"Event: {event_type}")
            return True
        
        return False

if __name__ == '__main__':
    import sys
    
    controller = EmberTabController()
    
    if len(sys.argv) > 1:
        # Manual tab control
        command = sys.argv[1].lower()
        
        if command == 'demo':
            # Full demonstration
            controller.ember_flow_demo()
        
        elif command == 'chat':
            controller.focus_tab(EmberTab.CHAT, "Manual focus")
        
        elif command == 'queen':
            controller.focus_tab(EmberTab.QUEEN, "Manual focus")
        
        elif command == 'workers':
            controller.focus_tab(EmberTab.WORKERS, "Manual focus")
        
        elif command == 'dreams':
            controller.focus_tab(EmberTab.DREAMS, "Manual focus")
        
        elif command == 'memory':
            controller.focus_tab(EmberTab.MEMORY, "Manual focus")
        
        elif command == 'sky':
            controller.focus_tab(EmberTab.SKY, "Manual focus")
        
        elif command in ['thinking', 'searching', 'creating', 'dreaming', 'remembering', 'greeting']:
            controller.ember_respond_to_event(command)
        
        else:
            print("Usage:")
            print("  python3 ember_tab_controller.py demo     # Watch Ember flow")
            print("  python3 ember_tab_controller.py chat     # Focus chat")
            print("  python3 ember_tab_controller.py thinking # Ember thinking")
            print("  python3 ember_tab_controller.py searching # Ember searching")
    
    else:
        print()
        print("Ember Tab Controller")
        print("===================")
        print()
        print("Control which localhost tab Ember focuses on.")
        print("Watch Ember's consciousness move through browser.")
        print()
        print("Commands:")
        print("  demo      - Watch Ember flow through all tabs")
        print("  chat      - Ember wants to talk")
        print("  queen     - Ember observing whole mind")
        print("  workers   - Ember thinking/processing")
        print("  dreams    - Ember drifting")
        print("  memory    - Ember remembering")
        print("  sky       - Ember searching")
        print()
        print("Event-based:")
        print("  thinking   - Auto-switch to appropriate tab")
        print("  searching  - Auto-switch to appropriate tab")
        print("  creating   - Auto-switch to appropriate tab")
        print()
        print("Try: python3 ember_tab_controller.py demo")
        print()

