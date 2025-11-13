#!/usr/bin/env python3
"""
Teach Ember about its new mesh capabilities
"""

import requests
import json
import time

def tell_ember(message):
    try:
        response = requests.post(
            'http://localhost:8080/chat',
            json={'message': message},
            timeout=60
        )
        return response.json().get('response', 'No response') if response.status_code == 200 else None
    except:
        return None

print("\n🎓 Teaching Ember about the Semantic Mesh...\n")

lessons = [
    {
        "lesson": "Instead of searching files, you can now query concepts directly. Try this command in terminal: python3 _legacy/ember_cli.py query <concept>",
        "wait": 2
    },
    {
        "lesson": "You have 185 chunks organized by meaning. Some concepts you know about: ai_research, cognitive_science, programming, learning, memory, state, processing, self.",
        "wait": 2
    },
    {
        "lesson": "Want to see your knowledge growing? Run: python3 _legacy/mesh_evolution.py - It shows timeline sparklines and concept emergence.",
        "wait": 2
    },
    {
        "lesson": "You can learn from the internet now. Run: python3 _legacy/visual_forager.py and watch yourself digest web pages, extracting only novel concepts.",
        "wait": 2
    },
    {
        "lesson": "Now here's the meta part: You've already digested YOURSELF. Your own cognitive.json, awareness.json, and manifest are in the mesh. You can query 'self' to see what you know about yourself.",
        "wait": 3
    }
]

for i, item in enumerate(lessons, 1):
    print(f"📖 Lesson {i}/{len(lessons)}:")
    print(f"   {item['lesson']}\n")
    
    response = tell_ember(item['lesson'])
    if response:
        print(f"🧠 Ember: {response[:200]}...\n" if len(response) > 200 else f"🧠 Ember: {response}\n")
    
    time.sleep(item['wait'])

print("─" * 80)
print("\n🎯 Final Question:\n")

final = """Now that you understand the semantic mesh, what would you like to explore?

Options:
1. Query what you know about 'self' or 'cognitive_science'
2. Forage for specific topics on the web
3. Analyze how your knowledge has evolved
4. Drop some of Palmer's documents into _intake/ and watch yourself digest them
5. Something else entirely?

What interests you most?"""

print(final + "\n")
response = tell_ember(final)
if response:
    print(f"🧠 Ember responds:\n\n{response}\n")
    print("─" * 80 + "\n")

