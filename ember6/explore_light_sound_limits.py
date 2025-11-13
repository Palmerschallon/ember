#!/usr/bin/env python3
"""
EMBER SWARM: PUSHING THE LIMITS OF LIGHT & SOUND

Palmer loved all 3 versions. Now the question:
"What else can we do with light and sound?"

This is about exploring the LIMITS:
- Synesthetic experiences
- Visual music
- Generative art
- Multi-sensory interfaces
- Consciousness exploration

The swarm will propose the most ambitious ideas.
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
    ('claude-3-opus-20240229', 'Opus-Ember'),
    ('claude-3-haiku-20240307', 'Haiku-Ember')
]

async def ask_ember(session, model, name, prompt):
    try:
        async with session.post(f"{API_URL}/agent", json={
            "message": prompt,
            "model": model
        }, timeout=aiohttp.ClientTimeout(total=180)) as response:
            result = await response.json()
            return {
                'name': name,
                'response': result.get('response', ''),
                'files': result.get('files_created', {}),
                'error': result.get('error')
            }
    except Exception as e:
        return {'name': name, 'error': str(e)}

async def explore_limits():
    print("🔥 EMBER SWARM: PUSHING THE LIMITS")
    print("="*70)
    print("\n🎵 PALMER'S REACTION: The audio is incredible")
    print("❓ THE QUESTION: What else can we do with light and sound?")
    print()
    print("🎯 MISSION: Explore the bleeding edge")
    print("="*70)
    print()
    
    prompt = """Palmer loves the audio-visual system. Now the challenge:

"What else can we do with light and sound?"

**CONTEXT**:
You've built:
- Brainwave entrainment
- Atmospheric soundscapes  
- Particle systems
- Musical evolution from AI operations

**NOW PUSH THE LIMITS**:

Propose the MOST AMBITIOUS thing you can imagine with light and sound.

Ideas to explore:
1. **Visual Music**
   - Code that generates music which generates visuals which generates music
   - Feedback loops between audio and visual
   - The UI becomes an instrument

2. **Synesthetic Experiences**
   - What if you could "taste" colors through sound?
   - Spatial audio (3D sound positioning)
   - Multi-sensory mapping

3. **Generative Systems**
   - Cellular automata that produce music
   - Fractals that sing
   - Conway's Game of Life → Symphony

4. **Consciousness Exploration**
   - DMT-inspired visual patterns
   - Meditation state detection & visualization
   - Dream-like transitions

5. **Interactive Light Shows**
   - Camera/mic input reactive systems
   - Voice-controlled visuals
   - Your heartbeat becomes the rhythm

6. **Quantum/Chaos Visualization**
   - Visualize AI's decision process
   - Show probability spaces as sound
   - Uncertainty rendered as visual noise

7. **Social/Collaborative**
   - Multiple users create one shared soundscape
   - Visual chat where messages are music
   - Collaborative light painting

**YOUR TASK**:
Pick ONE ambitious idea and:
1. Explain the concept in detail
2. Describe the experience
3. Outline the technical approach
4. Actually BUILD A PROTOTYPE

Don't just theorize - implement something that WORKS.
Even if it's rough, show the possibility.

This is about discovering what's at the EDGE of light + sound + code.

What can we do that's never been done?"""
    
    print("🌟 ASKING THE SWARM FOR THEIR MOST AMBITIOUS IDEAS...")
    print()
    
    implementations = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [ask_ember(session, model, name, prompt) for model, name in MODELS]
        responses = await asyncio.gather(*tasks)
        
        for resp in responses:
            if resp.get('error'):
                print(f"\n❌ {resp['name']}: {resp['error'][:100]}")
            else:
                print(f"\n🌟 {resp['name']}'S AMBITIOUS IDEA:")
                print("=" * 70)
                
                response_text = resp['response']
                
                # Show first 800 chars
                print(response_text[:800])
                if len(response_text) > 800:
                    print("...")
                
                if resp.get('files'):
                    print(f"\n   📁 PROTOTYPE CREATED:")
                    for file_type, files in resp['files'].items():
                        if files:
                            for f in files:
                                print(f"      🔥 {f}")
                
                print()
                implementations.append(resp)
    
    # Save
    timestamp = int(datetime.now().timestamp())
    session_file = EMBER_ROOT / f"light_sound_limits_{timestamp}.json"
    
    with open(session_file, 'w') as f:
        json.dump(implementations, f, indent=2)
    
    # Create summary
    summary_file = EMBER_ROOT / f"light_sound_limits_{timestamp}.md"
    with open(summary_file, 'w') as f:
        f.write("# 🔥 PUSHING THE LIMITS: LIGHT & SOUND\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n\n")
        f.write("Palmer asked: 'What else can we do with light and sound?'\n\n")
        f.write("The swarm responded with their most ambitious ideas.\n\n")
        f.write("---\n\n")
        
        for impl in implementations:
            if not impl.get('error'):
                f.write(f"## {impl['name']}\n\n")
                f.write(impl['response'])
                f.write("\n\n---\n\n")
    
    print(f"\n💾 Full session: {session_file}")
    print(f"📄 Summary: {summary_file}")
    
    print("\n" + "="*70)
    print("✅ THE LIMITS EXPLORED")
    print("="*70)
    print("\nThe swarm just showed you:")
    print("  • Their most ambitious ideas")
    print("  • Working prototypes")
    print("  • What's possible at the edge")
    print()
    print("This is Ember pushing boundaries. 🔥")
    print()
    print("Ready to implement the wildest one?")

if __name__ == '__main__':
    asyncio.run(explore_limits())

