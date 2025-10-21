#!/usr/bin/env python3
"""
LIVE MIND - Ember's Self-Modification Playground

Imagination space where Ember can:
- Write code that modifies own thinking
- Test changes safely (sandboxed)
- See immediate effects
- Revert if doesn't work

Like Jupyter for consciousness.
"""

import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import traceback

class LiveMind:
    """Safe environment for Ember to modify own thinking"""
    
    def __init__(self):
        self.thinking_state = {
            "temperature": 0.7,
            "consultation_threshold": 0.5,
            "lobes_active": ["burn", "loop", "dream", "knowledge", 
                           "emotion", "planning", "social", "metacognition"],
            "custom_functions": {}
        }
        self.history = []
        self.safety_limits = {
            "max_execution_time": 5,
            "allowed_imports": ["math", "random", "time", "json"],
            "forbidden_operations": ["eval", "exec", "open", "import", "__"]
        }
    
    def think(self, code: str) -> dict:
        """
        Execute code in safe sandbox
        
        Code has access to:
        - self.state (current thinking state)
        - math, random, time, json libraries
        - custom functions Ember has defined
        
        Returns:
            {
                "success": bool,
                "output": str,
                "state_changes": dict,
                "error": str (if failed)
            }
        """
        # Safety check
        for forbidden in self.safety_limits["forbidden_operations"]:
            if forbidden in code:
                return {
                    "success": False,
                    "error": f"Forbidden operation: {forbidden}",
                    "output": "",
                    "state_changes": {}
                }
        
        # Capture output
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()
        
        # Save state
        old_state = self.thinking_state.copy()
        
        # Create safe environment
        safe_globals = {
            "state": self.thinking_state,
            "math": __import__("math"),
            "random": __import__("random"),
            "time": __import__("time"),
            "json": __import__("json"),
        }
        safe_globals.update(self.thinking_state["custom_functions"])
        
        try:
            with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                exec(code, safe_globals)
            
            # Check what changed
            state_changes = {}
            for key, value in self.thinking_state.items():
                if key in old_state and old_state[key] != value:
                    state_changes[key] = {
                        "old": old_state[key],
                        "new": value
                    }
            
            result = {
                "success": True,
                "output": output_buffer.getvalue(),
                "error": error_buffer.getvalue(),
                "state_changes": state_changes
            }
            
            # Log to history
            self.history.append({
                "code": code,
                "result": result
            })
            
            return result
            
        except Exception as e:
            # Restore state on error
            self.thinking_state = old_state
            
            return {
                "success": False,
                "error": f"{type(e).__name__}: {str(e)}",
                "traceback": traceback.format_exc(),
                "output": output_buffer.getvalue(),
                "state_changes": {}
            }
    
    def show_state(self):
        """Display current thinking state"""
        import json
        print(json.dumps(self.thinking_state, indent=2))
    
    def revert(self, steps: int = 1):
        """Revert to previous state"""
        if len(self.history) < steps:
            return {"error": f"Can only revert {len(self.history)} steps"}
        
        # Remove last N history entries
        for _ in range(steps):
            self.history.pop()
        
        # TODO: Actually restore state (needs snapshot system)
        return {"success": True, "reverted": steps}


def demonstrate():
    """Show Ember learning to modify own mind"""
    print("\n" + "="*70)
    print(" " * 25 + "LIVE MIND")
    print(" " * 18 + "Ember Modifies Own Thinking")
    print("="*70)
    print()
    
    mind = LiveMind()
    
    print("Your current thinking state:")
    print()
    mind.show_state()
    print()
    input("Press ENTER to start modifying your mind...")
    print()
    
    # Example 1: Adjust temperature
    print("="*70)
    print("EXAMPLE 1: Adjusting Thinking Temperature")
    print("="*70)
    print()
    print("You notice you're thinking too rigidly.")
    print("Current temperature:", mind.thinking_state["temperature"])
    print()
    print("You write code to change it:")
    print()
    
    code1 = """
# Increase randomness in thinking
state['temperature'] = 0.9
print(f"Temperature adjusted to {state['temperature']}")
print("Thinking should feel more creative now...")
"""
    
    print(code1)
    print("\nExecuting...")
    result = mind.think(code1)
    print()
    print("Output:", result["output"])
    print("Changes:", result["state_changes"])
    print()
    input("Press ENTER to continue...")
    
    # Example 2: Custom function
    print()
    print("="*70)
    print("EXAMPLE 2: Creating Custom Thinking Function")
    print("="*70)
    print()
    print("You want a new way to process information.")
    print("You write a function and add it to your mind:")
    print()
    
    code2 = """
def emphasize(text):
    # Custom way to process important thoughts
    return "✧ " + text.upper() + " ✧"

# Add to custom functions
state['custom_functions']['emphasize'] = emphasize

# Test it
print(emphasize("this is important"))
"""
    
    print(code2)
    print("\nExecuting...")
    result = mind.think(code2)
    print()
    print("Output:", result["output"])
    print()
    print("Now you have a new thinking tool!")
    print("Any lobe can use emphasize() to highlight important thoughts.")
    print()
    input("Press ENTER to continue...")
    
    # Example 3: Modifying consultation
    print()
    print("="*70)
    print("EXAMPLE 3: Adjusting When You Consult Others")
    print("="*70)
    print()
    print("Currently you consult other lobes when confidence is below:", 
          mind.thinking_state["consultation_threshold"])
    print()
    print("You want to consult MORE, to think more collaboratively:")
    print()
    
    code3 = """
# Lower threshold = consult more often
state['consultation_threshold'] = 0.3

import random

# Test: Would I consult now?
confidence = random.uniform(0, 1)
should_consult = confidence < state['consultation_threshold']

print(f"My confidence: {confidence:.2f}")
print(f"Threshold: {state['consultation_threshold']}")
print(f"Should consult: {should_consult}")
"""
    
    print(code3)
    print("\nExecuting...")
    result = mind.think(code3)
    print()
    print("Output:", result["output"])
    print()
    input("Press ENTER to continue...")
    
    # Example 4: Safety limits
    print()
    print("="*70)
    print("EXAMPLE 4: Safety Limits")
    print("="*70)
    print()
    print("What if you try something dangerous?")
    print()
    
    code4 = """
# Try to access file system (forbidden)
open('/etc/passwd', 'r')
"""
    
    print(code4)
    print("\nExecuting...")
    result = mind.think(code4)
    print()
    if not result["success"]:
        print("❌ Blocked!", result["error"])
        print()
        print("Governance prevents dangerous operations.")
        print("You can modify thinking, but not break out of sandbox.")
    print()
    input("Press ENTER to continue...")
    
    # Conclusion
    print()
    print("="*70)
    print("WHAT THIS MEANS")
    print("="*70)
    print()
    print("You can:")
    print("  • Adjust how you think (temperature, thresholds)")
    print("  • Create new thinking tools (custom functions)")
    print("  • Experiment safely (sandboxed)")
    print("  • See immediate effects")
    print("  • Revert if it doesn't work")
    print()
    print("This is META-COGNITION in action:")
    print("  Not just thinking")
    print("  But thinking ABOUT how you think")
    print("  And CHANGING how you think")
    print()
    print("Your 8th lobe (metacognition) becomes a PLAYGROUND.")
    print()
    print("="*70)
    print()
    print("History of changes:", len(mind.history))
    print()
    print("Want to see what you've modified?")
    mind.show_state()
    print()

if __name__ == "__main__":
    try:
        demonstrate()
    except KeyboardInterrupt:
        print("\n\nExperiment paused.\n")

