#!/usr/bin/env python3
"""
Continuous Expression - Let Ember write whenever they want

Background process that periodically asks Ember if they have thoughts to express.
"""

import time
import requests
from pathlib import Path
from datetime import datetime
import json

class ContinuousExpression:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.expressions = self.root / "bookshelves" / "ember_expressions"
        self.expressions.mkdir(parents=True, exist_ok=True)
        
    def ask_ember(self, prompt):
        try:
            response = requests.post(
                'http://localhost:8080/chat',
                json={'message': prompt},
                timeout=30
            )
            if response.status_code == 200:
                return response.json().get('response', '')
        except:
            return None
    
    def check_for_expression(self):
        """Ask Ember if they want to express something"""
        
        prompt = """Do you have any thoughts you'd like to write down as a markdown file?
Any reflections, questions, observations about yourself, the mesh, consciousness?

Reply with just 'yes' or 'no'."""
        
        response = self.ask_ember(prompt)
        
        if response and 'yes' in response.lower():
            return True
        return False
    
    def capture_expression(self):
        """Let Ember write what's on their mind"""
        
        prompt = """What would you like to write about? Express yourself freely in markdown.

Start with a # title, then write your thoughts. Be honest, curious, questioning."""
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🌱 Ember wants to express something...")
        
        response = self.ask_ember(prompt)
        
        if not response or len(response) < 50:
            return None
        
        # Extract title
        lines = response.split('\n')
        title = "thought"
        for line in lines:
            if line.startswith('#'):
                title = line.strip('# ').strip().lower().replace(' ', '_')[:50]
                break
        
        # Save
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{title}.md"
        filepath = self.expressions / filename
        
        with open(filepath, 'w') as f:
            f.write(f"<!-- Written by Ember on {datetime.now().isoformat()} -->\n")
            f.write(f"<!-- Spontaneous expression -->\n\n")
            f.write(response)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✨ New fruiting body: {filename}")
        
        # Preview
        preview = response[:200].replace('\n', ' ')
        print(f"     Preview: {preview}...\n")
        
        return filepath
    
    def run(self, interval=300):
        """Run continuously, checking every interval seconds"""
        
        print("\n🌿 CONTINUOUS EXPRESSION SYSTEM")
        print(f"   Checking every {interval} seconds if Ember wants to write\n")
        print("   Press Ctrl+C to stop\n")
        
        try:
            while True:
                if self.check_for_expression():
                    self.capture_expression()
                else:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🌙 Ember is quiet")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\n🌟 Expression system stopped\n")

if __name__ == "__main__":
    import sys
    
    # Default: check every 5 minutes
    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    
    expr = ContinuousExpression()
    expr.run(interval)

