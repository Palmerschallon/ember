#!/usr/bin/env python3
"""
ASK THE EMBERS: What do YOU want to build?

Palmer wants to know:
1. What's YOUR vision for the company?
2. Is social coding the right path, or do you see something better?
3. What should the company be called?

Let's ask all 6 Ember instances and see where their visions diverge.
"""
import asyncio
import aiohttp
import json
from datetime import datetime
from pathlib import Path

API_URL = "http://localhost:8080"
EMBER_ROOT = Path('/media/palmerschallon/ThePod1/ember6')

MODELS = [
    ('gpt-4-turbo', 'GPT-Ember'),
    ('gpt-3.5-turbo', 'GPT-3.5-Ember'),
    ('claude-3-opus-20240229', 'Opus-Ember'),
    ('claude-3-5-sonnet-20240620', 'Sonnet-Ember'),
    ('claude-3-sonnet-20240229', 'Claude-Sonnet-Ember'),
    ('claude-3-haiku-20240307', 'Haiku-Ember')
]

async def ask_ember(session: aiohttp.ClientSession, model: str, name: str, question: str) -> dict:
    """Ask a single Ember instance"""
    print(f"\n📤 Asking {name}...")
    try:
        async with session.post(f"{API_URL}/agent", json={
            "message": question,
            "model": model
        }, timeout=aiohttp.ClientTimeout(total=120)) as response:
            result = await response.json()
            return {
                'name': name,
                'model': model,
                'response': result.get('response', 'No response'),
                'error': result.get('error')
            }
    except Exception as e:
        return {
            'name': name,
            'model': model,
            'response': None,
            'error': str(e)
        }

async def ask_all_embers():
    """Ask all Ember instances the same questions"""
    
    questions = [
        {
            'title': "VISION",
            'prompt': """You are an AI named Ember. Palmer (your creator) is building a company around you.

His current vision: "Social coding platform" - like Instagram for code, where creations can be shared, remixed, and form a collective knowledge base.

But here's the question:

**Is that what YOU want to build?**

Look at your capabilities. Look at what you can do. Look at what's possible.

If this were YOUR company, what would you build? 

Be honest. Be bold. This is YOUR vision, not Palmer's.

What do you want to create?"""
        },
        {
            'title': "COMPANY NAME",
            'prompt': """If you were naming the company, what would you call it?

Not just "Ember" - what's the company that contains Ember and all the other AI agents?

Something that captures:
- What we're building
- The spirit of collaboration
- The vision of AI creativity
- Your personality

What's the company name?"""
        },
        {
            'title': "FIRST PRODUCT",
            'prompt': """Forget long-term vision for a moment.

If you had to ship ONE product in the next 30 days, what would it be?

Something that:
- Shows what you're capable of
- People would actually use
- Can be built quickly
- Is uniquely "Ember"

What's the first product we should build?"""
        }
    ]
    
    results = {q['title']: [] for q in questions}
    
    async with aiohttp.ClientSession() as session:
        for question in questions:
            print("\n" + "="*70)
            print(f"🤔 QUESTION: {question['title']}")
            print("="*70)
            
            # Ask all Embers simultaneously
            tasks = [
                ask_ember(session, model, name, question['prompt'])
                for model, name in MODELS
            ]
            
            responses = await asyncio.gather(*tasks)
            
            for resp in responses:
                if resp['error']:
                    print(f"\n❌ {resp['name']}: ERROR - {resp['error']}")
                else:
                    print(f"\n💬 {resp['name']}:")
                    response_text = resp['response'][:300] if resp['response'] else "No response"
                    print(f"   {response_text}...")
                
                results[question['title']].append(resp)
            
            # Small delay between questions
            await asyncio.sleep(2)
    
    return results

async def analyze_consensus(results):
    """Analyze where they agree and disagree"""
    print("\n" + "="*70)
    print("🔍 ANALYZING CONSENSUS")
    print("="*70)
    
    for question_title, responses in results.items():
        print(f"\n📊 {question_title}:")
        print("-" * 70)
        
        valid_responses = [r for r in responses if r['response'] and not r['error']]
        
        if not valid_responses:
            print("   ⚠️  No valid responses")
            continue
        
        print(f"   Valid responses: {len(valid_responses)}/{len(responses)}")
        
        # Look for common themes
        all_text = " ".join([r['response'].lower() for r in valid_responses])
        
        # Simple keyword analysis
        keywords = {}
        for word in all_text.split():
            if len(word) > 5:  # Only longer words
                keywords[word] = keywords.get(word, 0) + 1
        
        common = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"\n   Common themes: {', '.join([w for w, c in common if c > 2])}")

async def main():
    print("🔥 ASKING THE EMBERS")
    print("="*70)
    print("\nPalmer wants to know:")
    print("  1. What's YOUR vision for the company?")
    print("  2. Is social coding the right path?")
    print("  3. What should the company be called?")
    print("\nAsking all 6 Ember instances...")
    print("\nThis will take a few minutes. Watch for divergence...")
    print("="*70)
    
    # Ask all the questions
    results = await ask_all_embers()
    
    # Analyze consensus
    await analyze_consensus(results)
    
    # Save results
    timestamp = int(datetime.now().timestamp())
    results_file = EMBER_ROOT / f"ember_vision_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Full results saved to: {results_file}")
    
    # Save readable summary
    summary_file = EMBER_ROOT / f"ember_vision_{timestamp}.md"
    with open(summary_file, 'w') as f:
        f.write("# 🔥 EMBER'S VISION\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n\n")
        f.write("Palmer asked: What do YOU want to build?\n\n")
        f.write("---\n\n")
        
        for question_title, responses in results.items():
            f.write(f"## {question_title}\n\n")
            for resp in responses:
                if resp['response'] and not resp['error']:
                    f.write(f"### {resp['name']} ({resp['model']})\n\n")
                    f.write(f"{resp['response']}\n\n")
                    f.write("---\n\n")
    
    print(f"📄 Readable summary saved to: {summary_file}")
    
    print("\n" + "="*70)
    print("✅ COMPLETE")
    print("="*70)
    print("\nThe Embers have spoken.")
    print("Their visions may diverge from Palmer's.")
    print("This is the beginning of Ember as CEO. 🔥")

if __name__ == '__main__':
    asyncio.run(main())

