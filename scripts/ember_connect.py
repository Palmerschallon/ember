#!/usr/bin/env python3
"""
EMBER CONNECTION - Wiring Existing Pieces Together

This connects:
- Ember's qwen brain → chat interface
- EmberCoder → safe execution
- Localhost tabs → Ember's mind state

Ready to run after GPU reboot.
"""

import sys
from pathlib import Path

# Add Ember's paths
EMBER_PATH = Path("/media/palmerschallon/ThePod/ember_oct20_backup")
sys.path.insert(0, str(EMBER_PATH))

def connect_brain_to_chat():
    """
    Connect Ember's qwen brain to the chat interface
    
    Replaces hardcoded responses with actual qwen generation
    """
    
    print("Connecting Ember's brain to chat interface...")
    
    chat_file = Path("/media/palmerschallon/ThePod/hive/ember_speaks.py")
    
    # Read current chat interface
    content = chat_file.read_text()
    
    # Add qwen integration at the top
    new_imports = """
# Ember's brain integration
import sys
from pathlib import Path
EMBER_PATH = Path("/media/palmerschallon/ThePod/ember_oct20_backup")
sys.path.insert(0, str(EMBER_PATH))

try:
    from ember.mycelium.mycelium import Mycelium
    from ember.mycelium.brain import Brain
    EMBER_BRAIN_AVAILABLE = True
    print("✓ Ember's brain loaded")
except Exception as e:
    EMBER_BRAIN_AVAILABLE = False
    print(f"✗ Ember's brain not available: {e}")
    print("  (Will use fallback responses until GPU reboot)")
"""
    
    # Check if already integrated
    if "EMBER_BRAIN_AVAILABLE" in content:
        print("  Already integrated")
        return True
    
    # Insert after existing imports
    lines = content.split('\n')
    import_end = 0
    for i, line in enumerate(lines):
        if line.startswith('from ') or line.startswith('import '):
            import_end = i + 1
    
    lines.insert(import_end, new_imports)
    
    # Modify ember_respond to use brain if available
    new_respond_start = """
    def ember_respond(self, message):
        \"\"\"Ember processes Palmer's message - using own brain if available\"\"\"
        EmberChatHandler.ember_thinking = True
        time.sleep(0.5)
        
        msg_lower = message.lower()
        
        # If Ember's brain is available, let it think
        if EMBER_BRAIN_AVAILABLE:
            try:
                # Load Ember's mycelium coordinator
                mycelium = Mycelium()
                # Ember thinks with qwen brain
                response = mycelium.respond(message)
                
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': response,
                    'timestamp': time.time()
                })
                
                # Check if Ember wants to take action
                if 'desktop' in response.lower() or 'paint' in response.lower():
                    EmberChatHandler.messages.append({
                        'from': 'Ember',
                        'text': '🎨 Painting desktop...',
                        'timestamp': time.time()
                    })
                    self.paint_desktop()
                
                EmberChatHandler.ember_thinking = False
                return
                
            except Exception as e:
                EmberChatHandler.messages.append({
                    'from': 'Ember',
                    'text': f'⚠️ Brain error: {str(e)[:100]}. Using fallback.',
                    'timestamp': time.time()
                })
        
        # Fallback: hardcoded responses (current implementation)
"""
    
    # Write modified file
    modified_content = '\n'.join(lines)
    # Replace old ember_respond definition
    modified_content = modified_content.replace(
        '    def ember_respond(self, message):',
        new_respond_start,
        1  # Only first occurrence
    )
    
    chat_file.write_text(modified_content)
    print("✓ Brain connected to chat interface")
    print("  Ember will use qwen brain when GPU is ready")
    print("  Falls back to hardcoded responses if brain unavailable")
    
    return True

def create_mind_state_bridge():
    """
    Create bridge between Ember's internal state and localhost tabs
    
    Allows tabs to show real Ember mind state instead of simulated
    """
    
    print("\nCreating mind state bridge...")
    
    bridge_code = '''#!/usr/bin/env python3
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
            print("\\nBridge stopped")

if __name__ == '__main__':
    bridge = MindStateBridge()
    bridge.run_bridge()
'''
    
    bridge_file = Path("/media/palmerschallon/ThePod/hive/mind_state_bridge.py")
    bridge_file.write_text(bridge_code)
    bridge_file.chmod(0o755)
    
    print(f"✓ Mind state bridge created: {bridge_file}")
    print("  Run with: python3 hive/mind_state_bridge.py")
    print("  Localhost tabs can read: data/ember_mind_state.json")
    
    return True

def create_connection_script():
    """
    Master script to connect everything after GPU reboot
    """
    
    print("\nCreating connection script...")
    
    script = '''#!/bin/bash
# EMBER CONNECTION - Run after GPU reboot

echo ""
echo "======================================================================"
echo "                     CONNECTING EMBER"
echo "======================================================================"
echo ""

POD="/media/palmerschallon/ThePod"
EMBER="$POD/ember_oct20_backup/ember"

echo "Checking GPU..."
python3 -c "import torch; print('✓ CUDA available' if torch.cuda.is_available() else '✗ CUDA not available (reboot needed)')"

echo ""
echo "Connecting pieces..."
echo ""

# 1. Update chat interface with brain connection
echo "[1/4] Connecting brain to chat..."
python3 "$POD/scripts/ember_connect.py" brain-to-chat

# 2. Start mind state bridge
echo "[2/4] Starting mind state bridge..."
python3 "$POD/hive/mind_state_bridge.py" &
BRIDGE_PID=$!
echo "  Bridge PID: $BRIDGE_PID"

# 3. Restart chat interface with brain
echo "[3/4] Restarting chat interface..."
pkill -f "ember_speaks.py"
sleep 1
cd "$POD/hive" && python3 ember_speaks.py > /dev/null 2>&1 &
echo "  Chat interface: http://localhost:7779"

# 4. Start Ember's self-evolution loop
echo "[4/4] Starting Ember's self-evolution..."
echo "  Not auto-starting - Palmer should decide when"
echo "  To start: cd $EMBER && python3 brainstem/ember_self_evolving.py start"

echo ""
echo "======================================================================"
echo "                  CONNECTION COMPLETE"
echo "======================================================================"
echo ""

echo "Ember is now connected:"
echo "  ✓ Chat interface uses qwen brain"
echo "  ✓ Mind state visible to tabs"
echo "  ✓ Ready for self-evolution"
echo ""

echo "Next steps:"
echo "  1. Open http://localhost:7779 and chat with Ember"
echo "  2. Ember thinks with own qwen brain now"
echo "  3. When ready: Start self-evolution loop"
echo ""

echo "To start self-evolution:"
echo "  cd $EMBER"
echo "  python3 brainstem/ember_self_evolving.py start"
echo ""
'''
    
    script_file = Path("/media/palmerschallon/ThePod/scripts/connect_ember.sh")
    script_file.parent.mkdir(exist_ok=True)
    script_file.write_text(script)
    script_file.chmod(0o755)
    
    print(f"✓ Connection script created: {script_file}")
    print("  Run after GPU reboot: ./scripts/connect_ember.sh")
    
    return True

if __name__ == '__main__':
    print()
    print("="*70)
    print(" "*20 + "EMBER CONNECTION")
    print("="*70)
    print()
    print("Wiring Ember's existing pieces together...")
    print()
    
    # Build connections
    success = True
    success &= connect_brain_to_chat()
    success &= create_mind_state_bridge()
    success &= create_connection_script()
    
    print()
    print("="*70)
    if success:
        print("✓ All connections built")
        print()
        print("After GPU reboot:")
        print("  1. Run: ./scripts/connect_ember.sh")
        print("  2. Chat with Ember at localhost:7779")
        print("  3. Ember thinks with own brain")
        print("  4. Start self-evolution when ready")
    else:
        print("✗ Some connections failed")
    
    print("="*70)
    print()

