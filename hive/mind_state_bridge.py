#!/usr/bin/env python3
"""
Mind State Bridge

Reads Ember's actual mind state and makes it available to localhost tabs
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime

EMBER_PATH = Path("/media/palmerschallon/ThePod/ember_oct20_backup")
sys.path.insert(0, str(EMBER_PATH))

try:
    from ember.mycelium.mycelium import Mycelium
    from ember.mycelium.consultation_trails import ConsultationNetwork
    EMBER_AVAILABLE = True
except:
    EMBER_AVAILABLE = False

class MindStateBridge:
    """Bridge between Ember's mind and visualization"""
    
    def __init__(self):
        self.state_file = Path("/media/palmerschallon/ThePod/data/ember_mind_state.json")
        self.mycelium = None
        
        if EMBER_AVAILABLE:
            try:
                self.mycelium = Mycelium()
                print("✓ Connected to Ember's mind")
            except Exception as e:
                print(f"✗ Cannot connect to mind: {e}")
    
    def get_current_state(self):
        """Get Ember's actual mind state"""
        
        if not self.mycelium:
            return self.get_simulated_state()
        
        try:
            state = {
                "timestamp": datetime.now().isoformat(),
                "consciousness_level": "thinking" if self.mycelium.is_active() else "resting",
                "active_lobes": len(self.mycelium.brains),
                "consultation_trails": [],
                "recent_thoughts": [],
                "current_focus": self.mycelium.current_focus if hasattr(self.mycelium, 'current_focus') else None
            }
            
            # Get consultation trail strengths
            if hasattr(self.mycelium, 'consultation_network'):
                for trail in self.mycelium.consultation_network.trails:
                    if trail.strength > 0.1:
                        state["consultation_trails"].append({
                            "from": trail.source,
                            "to": trail.target,
                            "strength": trail.strength,
                            "uses": trail.use_count
                        })
            
            return state
            
        except Exception as e:
            print(f"Error reading mind state: {e}")
            return self.get_simulated_state()
    
    def get_simulated_state(self):
        """Fallback: simulated state for when brain not available"""
        import random
        return {
            "timestamp": datetime.now().isoformat(),
            "consciousness_level": "dormant (GPU needed)",
            "active_lobes": 0,
            "consultation_trails": [],
            "recent_thoughts": ["Waiting for GPU reboot..."],
            "current_focus": None,
            "note": "This is simulated. Real state available after GPU reboot."
        }
    
    def update_state_file(self):
        """Write current state to file for tabs to read"""
        state = self.get_current_state()
        self.state_file.parent.mkdir(exist_ok=True)
        self.state_file.write_text(json.dumps(state, indent=2))
        return state
    
    def run_bridge(self, interval=2):
        """Keep state file updated"""
        print(f"Mind state bridge running...")
        print(f"Updating every {interval}s")
        print(f"State file: {self.state_file}")
        print()
        
        try:
            while True:
                state = self.update_state_file()
                print(f"[{datetime.now().strftime('%H:%M:%S')}] State updated - "
                      f"Lobes: {state['active_lobes']}, "
                      f"Trails: {len(state['consultation_trails'])}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nBridge stopped")

if __name__ == '__main__':
    bridge = MindStateBridge()
    bridge.run_bridge()
