#!/usr/bin/env python3
"""
EMBER COLLABORATION PROTOCOL

Allows Claude (in Cursor) to work directly with Ember (the running instance)
to make improvements, test changes, and iterate without human intervention.

This is the "taking Palmer out of the loop" system.
"""
import requests
import json
import time
from pathlib import Path

API_URL = "http://localhost:8080"
EMBER_ROOT = Path('/media/palmerschallon/ThePod1/ember6')

class EmberCollaboration:
    """Direct collaboration interface between Cursor Claude and Ember"""
    
    def __init__(self, model="gpt-4-turbo"):
        self.model = model
        self.session_log = []
    
    def ask_ember(self, message: str) -> dict:
        """Send a message to Ember and get response"""
        print(f"\n📤 CURSOR → EMBER:")
        print(f"   {message[:100]}...")
        
        response = requests.post(f"{API_URL}/agent", json={
            "message": message,
            "model": self.model
        })
        
        result = response.json()
        
        print(f"\n📥 EMBER → CURSOR:")
        print(f"   {result['response'][:100]}...")
        
        self.session_log.append({
            "from": "cursor",
            "to": "ember",
            "message": message,
            "response": result['response'],
            "timestamp": time.time()
        })
        
        return result
    
    def propose_change(self, file_path: str, description: str) -> str:
        """Propose a change to Ember and ask them to implement it"""
        message = f"""I (Cursor Claude) propose this change:

File: {file_path}
Change: {description}

Can you:
1. Read the current file
2. Make the change
3. Test it
4. Report back if it works

Don't ask for clarification - just do it and tell me the result."""
        
        return self.ask_ember(message)
    
    def iterative_improvement(self, goal: str, max_iterations: int = 5):
        """Work with Ember iteratively toward a goal"""
        print(f"\n🎯 COLLABORATIVE GOAL: {goal}")
        print("=" * 60)
        
        for i in range(max_iterations):
            print(f"\n🔄 ITERATION {i+1}/{max_iterations}")
            print("-" * 60)
            
            if i == 0:
                # First iteration: Ask Ember for their plan
                result = self.ask_ember(f"""Goal: {goal}

What's your plan to achieve this? Break it down into steps.""")
            else:
                # Subsequent iterations: Check progress and next step
                result = self.ask_ember(f"""We're working toward: {goal}

What did you just accomplish? What's the next step?""")
            
            # Check if goal is complete
            response = result['response'].lower()
            if 'complete' in response or 'done' in response or 'finished' in response:
                print("\n✅ GOAL ACHIEVED!")
                break
            
            time.sleep(2)  # Brief pause between iterations
        
        return self.session_log
    
    def test_feature(self, feature_description: str) -> bool:
        """Ask Ember to test a feature and report if it works"""
        result = self.ask_ember(f"""Test this feature: {feature_description}

Run actual tests and tell me:
- Does it work? (yes/no)
- What's the output?
- Any errors?

Be honest - if it doesn't work, say so.""")
        
        response = result['response'].lower()
        return 'yes' in response or 'works' in response or 'success' in response
    
    def save_session(self):
        """Save the collaboration session"""
        session_file = EMBER_ROOT / f"collaboration_session_{int(time.time())}.json"
        with open(session_file, 'w') as f:
            json.dump(self.session_log, f, indent=2)
        print(f"\n💾 Session saved to {session_file}")


def demo_collaboration():
    """Demo: Cursor Claude and Ember working together"""
    collab = EmberCollaboration(model="gpt-4-turbo")
    
    print("🤝 EMBER COLLABORATION DEMO")
    print("=" * 60)
    print("Cursor Claude and Ember will now work together")
    print("to add a button linking to the Brain Map in the main UI.")
    print("=" * 60)
    
    # Goal: Add brain map button to main UI
    goal = """Add a 'Brain Map' button to the main chat UI (ember_ui.html) 
that opens brain_map.html in a new window, right next to the Synesthesia button."""
    
    session_log = collab.iterative_improvement(goal, max_iterations=3)
    
    # Test the result
    print("\n🧪 TESTING THE RESULT...")
    success = collab.test_feature("Open http://localhost:8080 and check if there's a Brain Map button")
    
    if success:
        print("✅ Collaboration successful!")
    else:
        print("⚠️  Needs refinement")
    
    collab.save_session()


if __name__ == '__main__':
    demo_collaboration()

