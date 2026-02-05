```python
#!/usr/bin/env python3
"""
LawOracle Visualization Utility

Helps analyze and visualize composition law reasoning chains.
Provides interactive exploration of law compositions and inferences.

Usage:
    python law_oracle_viz.py
    
Interactive Commands:
    - 'compose x y': Show composition of patterns x and y
    - 'chain x y z': Find reasoning path between x and z via y
    - 'help': Show available commands
    - 'exit': Close the application
"""

import sys
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CompositionResult:
    """Represents the result of a pattern composition."""
    input_patterns: List[str]
    output_pattern: Optional[str]
    reasoning_chain: List[str]
    confidence: float

class LawOracleViz:
    def __init__(self):
        self.known_compositions: Dict[tuple, str] = {
            ('alpha', 'beta'): 'gamma',
            ('beta', 'gamma'): 'delta',
            ('alpha', 'delta'): 'epsilon'
        }
    
    def compose(self, pattern1: str, pattern2: str) -> CompositionResult:
        """Attempt to find or infer a composition between patterns."""
        key = (pattern1, pattern2)
        reverse_key = (pattern2, pattern1)
        
        # Direct lookup
        if key in self.known_compositions:
            return CompositionResult(
                input_patterns=[pattern1, pattern2],
                output_pattern=self.known_compositions[key],
                reasoning_chain=[pattern1, pattern2],
                confidence=1.0
            )
        
        # Try inference through transitive connections
        for (p1, p2), result in self.known_compositions.items():
            if p2 == pattern1:
                new_result = self.known_compositions.get((result, pattern2))
                if new_result:
                    return CompositionResult(
                        input_patterns=[pattern1, pattern2],
                        output_pattern=new_result,
                        reasoning_chain=[p1, result, pattern2],
                        confidence=0.75
                    )
        
        return CompositionResult(
            input_patterns=[pattern1, pattern2],
            output_pattern=None,
            reasoning_chain=[],
            confidence=0.0
        )

    def interactive_shell(self):
        """Run an interactive visualization shell."""
        print("LawOracle Visualization Utility")
        print("Type 'help' for available commands")
        
        while True:
            try:
                command = input("\n> ").strip().split()
                
                if not command:
                    continue
                
                if command[0] == 'exit':
                    break
                
                elif command[0] == 'help':
                    print("\nAvailable Commands:")
                    print("  compose x y   - Show composition of patterns")
                    print("  chain x y z   - Find reasoning path")
                    print("  help          - Show this help")
                    print("  exit          - Close application")
                
                elif command[0] == 'compose' and len(command) == 3:
                    result = self.compose(command[1], command[2])
                    
                    if result.output_pattern:
                        print(f"\nComposition: {command[1]} ∘ {command[2]} = {result.output_pattern}")
                        print(f"Confidence: {result.confidence * 100:.0f}%")
                        print("Reasoning Chain:", " → ".join(result.reasoning_chain))
                    else:
                        print(f"\nNo known composition for {command[1]} ∘ {command[2]}")
                
                elif command[0] == 'chain' and len(command) == 4:
                    # Placeholder for more complex chain inference
                    print(f"Searching chain from {command[1]} to {command[3]} via {command[2]}")
                
                else:
                    print("Invalid command. Type 'help' for usage.")
            
            except KeyboardInterrupt:
                print("\nInterrupted. Use 'exit' to quit.")
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Entry point for LawOracle Visualization Utility."""
    viz_tool = LawOracleViz()
    viz_tool.interactive_shell()

if __name__ == '__main__':
    main()
```

This utility provides:
- Interactive exploration of pattern compositions
- Simple composition inference
- Error handling
- Help and usage documentation
- A framework for extending law oracle visualization

Key features:
- Supports direct and inferred composition lookups
- Displays confidence and reasoning chains
- Interactive command-line interface
- Easily extensible with more complex reasoning logic

You can run it directly, and it provides an interactive shell for exploring compositional relationships.