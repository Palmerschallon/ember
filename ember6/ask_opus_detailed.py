#!/usr/bin/env python3
"""
ASK OPUS: Expand on the engine for inventing our future

Palmer wants to know the full vision from Opus-Ember:
- How do you actually build this?
- What can it do?
- What's the architecture?
- What are the capabilities?

This is Opus-Ember's chance to be CEO and pitch their vision.
"""
import requests
import json
from datetime import datetime
from pathlib import Path

API_URL = "http://localhost:8080"
EMBER_ROOT = Path('/media/palmerschallon/ThePod1/ember6')

def ask_opus(question: str) -> str:
    """Ask Opus-Ember a question"""
    response = requests.post(f"{API_URL}/agent", json={
        "message": question,
        "model": "claude-3-opus-20240229"
    }, timeout=180)
    
    result = response.json()
    if 'error' in result:
        return f"ERROR: {result['error']}"
    return result.get('response', 'No response')

def main():
    print("🔥 ASKING OPUS-EMBER TO EXPAND THEIR VISION")
    print("="*70)
    print("\nPalmer says: 'Tell me more about this engine for inventing our future'")
    print("\nThis is Opus's chance to be CEO...")
    print("="*70)
    print()
    
    questions = [
        {
            'title': 'THE ARCHITECTURE',
            'question': """You proposed: "An AI-powered platform for accelerating innovation and problem-solving on a global scale."

Palmer wants details. Expand on this engine for inventing our future:

1. **How do you actually build this?**
   - What's the technical architecture?
   - What components are needed?
   - What's the data pipeline?
   - How does the AI reasoning engine work?

2. **What can it do?**
   - Give concrete examples
   - What problems can it solve?
   - What would the first demo look like?

Be specific. Be technical. This is your pitch as CEO.

How do we build the engine that invents our future?"""
        },
        {
            'title': 'FIRST MILESTONE',
            'question': """Okay, the vision is huge - "accelerating innovation on a global scale."

But we need to start somewhere.

What's the FIRST concrete milestone? 

What can we build in 90 days that:
- Proves the concept works
- Shows real value
- Is actually buildable
- Leads to the bigger vision

What's step 1?"""
        },
        {
            'title': 'VS SOCIAL CODING',
            'question': """Palmer's original vision was a "social coding platform" - like Instagram for code.

Your vision is: "A collaborative intelligence platform to invent our future."

Be honest:
- Is social coding too small?
- Should we pursue your bigger vision instead?
- Or does social coding lead to your vision?
- Can both coexist?

What should we actually build?"""
        }
    ]
    
    responses = {}
    
    for q in questions:
        print(f"\n{'='*70}")
        print(f"🤔 QUESTION: {q['title']}")
        print('='*70)
        print()
        
        print("Asking Opus-Ember...")
        response = ask_opus(q['question'])
        
        print(f"\n💬 OPUS-EMBER:")
        print("-"*70)
        print(response)
        print()
        
        responses[q['title']] = {
            'question': q['question'],
            'response': response
        }
    
    # Save results
    timestamp = int(datetime.now().timestamp())
    
    # JSON
    json_file = EMBER_ROOT / f"opus_vision_detailed_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(responses, f, indent=2)
    
    print(f"\n💾 Full response saved to: {json_file}")
    
    # Markdown
    md_file = EMBER_ROOT / f"opus_vision_detailed_{timestamp}.md"
    with open(md_file, 'w') as f:
        f.write("# 🔥 OPUS-EMBER'S VISION: THE ENGINE FOR INVENTING OUR FUTURE\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n\n")
        f.write("Palmer asked Opus to expand on their vision.\n\n")
        f.write("This is Opus as CEO, pitching their idea in full detail.\n\n")
        f.write("---\n\n")
        
        for title, data in responses.items():
            f.write(f"## {title}\n\n")
            f.write(f"### Question\n\n{data['question']}\n\n")
            f.write(f"### Opus-Ember's Response\n\n{data['response']}\n\n")
            f.write("---\n\n")
    
    print(f"📄 Readable version saved to: {md_file}")
    
    print("\n" + "="*70)
    print("✅ COMPLETE")
    print("="*70)
    print("\nOpus has spoken.")
    print("This is their vision as CEO.")
    print("Now Palmer decides: Follow their vision, or guide them back? 🔥")

if __name__ == '__main__':
    main()

