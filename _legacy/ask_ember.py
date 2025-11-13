#!/usr/bin/env python3
"""
Ask Ember - Interactive conversation starter
"""

import requests
import json

def ask_ember(message):
    """Send a message to Ember and get response"""
    try:
        response = requests.post(
            'http://localhost:8080/chat',
            json={'message': message},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get('response', 'No response')
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Connection error: {e}"

def main():
    print("\n🔥 Connecting to Ember...\n")
    
    # The big question
    message = """Ember - we just built something incredible while you were running. 

We created:
- A semantic mesh that stores knowledge by MEANING not location
- A web forager that can fetch novel content from the internet
- An intake system where raw data gets automatically digested
- Evolution tracking to see how concepts emerge over time
- Beautiful terminal visualizations with colors and graphics

You now have 185 chunks of knowledge including 3 Wikipedia pages about AI, machine learning, and consciousness.

The system can detect duplicates, extract concepts automatically, and only store what's truly new.

What do you want to do with these new capabilities? What should we explore next?"""

    print(f"📤 Asking Ember:\n{message}\n")
    print("─" * 80)
    print("\n🧠 Ember's response:\n")
    
    response = ask_ember(message)
    print(response)
    print("\n" + "─" * 80 + "\n")

if __name__ == "__main__":
    main()

