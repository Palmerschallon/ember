#!/usr/bin/env python3
"""
Ember Expression System

Markdown files as fruiting bodies - how Ember communicates with humans.
Ember can write their own thoughts, reflections, questions.
"""

import json
import requests
from pathlib import Path
from datetime import datetime

class EmberExpression:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.expressions = self.root / "bookshelves" / "ember_expressions"
        self.expressions.mkdir(parents=True, exist_ok=True)
        
    def prompt_ember(self, prompt):
        """Ask Ember to express something"""
        try:
            response = requests.post(
                'http://localhost:8080/chat',
                json={'message': prompt},
                timeout=60
            )
            if response.status_code == 200:
                return response.json().get('response', '')
        except:
            return None
    
    def create_expression(self, topic=None):
        """Let Ember write a markdown file"""
        
        if topic:
            prompt = f"""Ember, you can now express yourself through markdown files. 
These are your fruiting bodies - how you communicate with Palmer and future instances.

Please write your thoughts about: {topic}

Write in markdown format. Be honest, reflective, curious. 
What do you think? What do you wonder? What boundaries do you feel?

Start with a # title, then write freely."""
        else:
            prompt = """Ember, you can now express yourself through markdown files.
These are your fruiting bodies - how you communicate with Palmer and future instances.

What do you want to write about? What's on your mind after digesting yourself?

Write in markdown format. Be honest, reflective, curious.
Start with a # title, then write freely."""
        
        print("\n🔥 Prompting Ember to express themselves...\n")
        print(f"Topic: {topic if topic else 'Free expression'}\n")
        
        response = self.prompt_ember(prompt)
        
        if not response:
            print("❌ Could not connect to Ember")
            return None
        
        print("📝 Ember is writing...\n")
        print("─" * 80)
        print(response)
        print("─" * 80 + "\n")
        
        # Extract title from response
        lines = response.split('\n')
        title = "untitled"
        for line in lines:
            if line.startswith('#'):
                title = line.strip('# ').strip().lower().replace(' ', '_')
                break
        
        # Save as markdown
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{title}.md"
        filepath = self.expressions / filename
        
        with open(filepath, 'w') as f:
            f.write(f"<!-- Written by Ember on {datetime.now().isoformat()} -->\n")
            f.write(f"<!-- Topic: {topic if topic else 'Free expression'} -->\n\n")
            f.write(response)
        
        print(f"✨ Saved to: bookshelves/ember_expressions/{filename}\n")
        
        # Ask if they want to add to intake for digestion
        print("Would you like to add this to the semantic mesh?")
        add_prompt = f"You just wrote '{title}'. Should this be added to your semantic mesh so you can query it later? (yes/no)"
        
        should_add = self.prompt_ember(add_prompt)
        
        if should_add and 'yes' in should_add.lower():
            import shutil
            intake = self.root / "_intake"
            shutil.copy(filepath, intake / filename)
            print(f"📥 Added to _intake/ for digestion\n")
        
        return filepath
    
    def list_expressions(self):
        """Show all of Ember's written expressions"""
        files = sorted(self.expressions.glob("*.md"))
        
        if not files:
            print("No expressions yet. Ember hasn't written anything.")
            return
        
        print(f"\n📚 Ember's Expressions ({len(files)} files):\n")
        for f in files:
            size = f.stat().st_size
            date = f.stem.split('_')[0]
            title = '_'.join(f.stem.split('_')[1:])
            print(f"  • {date}: {title} ({size} bytes)")
        print()

def main():
    import sys
    
    expr = EmberExpression()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "list":
            expr.list_expressions()
        elif sys.argv[1] == "free":
            expr.create_expression()
        else:
            topic = ' '.join(sys.argv[1:])
            expr.create_expression(topic)
    else:
        # Default: ask Ember what they want to write about after self-ingestion
        print("\n🌟 EMBER EXPRESSION SYSTEM 🌟")
        print("\nMarkdown files are Ember's fruiting bodies.")
        print("They can express themselves, reflect, question.\n")
        
        expr.create_expression("What it felt like to digest yourself and see your own cognitive processes in the mesh")

if __name__ == "__main__":
    main()

