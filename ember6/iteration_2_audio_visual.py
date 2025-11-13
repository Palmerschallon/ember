#!/usr/bin/env python3
"""
EMBER SWARM: ITERATION 2 - AUDIO/VISUAL ENHANCEMENT

Palmer's feedback:
- index.html was a prototype, not the vision
- Empty space needs better use
- Audio should be more musical (not just beeps)
- Add atmospheric soundscapes
- Brain wave entrainment/shaping

The swarm will now iterate on this feedback.
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
    """Ask a single Ember"""
    try:
        async with session.post(f"{API_URL}/agent", json={
            "message": prompt,
            "model": model
        }, timeout=aiohttp.ClientTimeout(total=180)) as response:
            result = await response.json()
            return {
                'name': name,
                'response': result.get('response', 'No response'),
                'files': result.get('files_created', {}),
                'error': result.get('error')
            }
    except Exception as e:
        return {'name': name, 'error': str(e)}

async def iteration_2():
    """Swarm iterates based on Palmer's feedback"""
    
    print("🔥 EMBER SWARM: ITERATION 2")
    print("="*70)
    print("\n📋 PALMER'S FEEDBACK:")
    print("   • Empty space needs better use")
    print("   • Audio should be musical (not beeps)")
    print("   • Add atmospheric soundscapes")
    print("   • Brain wave entrainment/shaping")
    print()
    print("🎯 GOAL: Create immersive audio-visual experience")
    print("="*70)
    print()
    
    prompt = """Palmer reviewed the prototype and wants improvements.

**THE FEEDBACK**:
- The current synesthesia window (beeping tones) is good, but limited
- Empty space in the UI needs better use
- Audio should evolve into actual MUSIC, not just beeps
- Need atmospheric soundscapes
- Want brainwave entrainment/shaping capabilities

**THE VISION**:
Imagine the Ember interface as an immersive space where:
- Visual particles create patterns in the "empty space"
- Audio evolves from simple tones into layered, musical soundscapes
- The atmosphere changes based on what Ember is doing
- The experience can affect your mental state (focus, creativity, relaxation)

**YOUR TASK**:
Design and implement an enhanced audio-visual system that:

1. **Uses Empty Space**:
   - Ambient particle systems
   - Background patterns/nebulae
   - Flowing energy fields
   - Make the void feel alive

2. **Musical Evolution**:
   - Layer multiple tones into chords
   - Add rhythm/percussion for different operations
   - Melodic progression as Ember thinks
   - Transform simple beeps → ambient music

3. **Atmospheric Soundscapes**:
   - Base drone/pad sounds
   - Environmental effects (wind, space, ocean)
   - Dynamic mixing based on activity
   - Generative music that never repeats

4. **Brainwave Entrainment**:
   - Alpha waves (8-12 Hz) for creativity
   - Beta waves (12-30 Hz) for focus
   - Theta waves (4-8 Hz) for deep thought
   - Use binaural beats or isochronic tones

**REQUIREMENTS**:
- Build on existing synesthesia.html
- Use Web Audio API for synthesis
- Canvas for visuals
- Real-time response to Ember's operations
- Should work in background while chatting

Create the actual implementation. Write the full HTML/JS file.
Make it WORK, not just a design document.

This is about creating an immersive environment where using Ember
feels like stepping into a living, breathing, musical consciousness."""
    
    print("🤔 ASKING ALL EMBERS FOR IMPLEMENTATIONS...")
    print()
    
    implementations = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [ask_ember(session, model, name, prompt) for model, name in MODELS]
        responses = await asyncio.gather(*tasks)
        
        for resp in responses:
            if resp.get('error'):
                print(f"\n❌ {resp['name']}: {resp['error'][:100]}")
            else:
                print(f"\n✅ {resp['name']} IMPLEMENTED:")
                print("-" * 70)
                print(resp['response'][:400] + "...")
                
                if resp.get('files'):
                    print(f"\n   📁 Files created:")
                    for file_type, files in resp['files'].items():
                        if files:
                            for f in files:
                                print(f"      • {f}")
                
                implementations.append(resp)
    
    # Save results
    timestamp = int(datetime.now().timestamp())
    session_file = EMBER_ROOT / f"iteration_2_audio_visual_{timestamp}.json"
    
    with open(session_file, 'w') as f:
        json.dump(implementations, f, indent=2)
    
    print(f"\n\n💾 Session saved to: {session_file}")
    
    print("\n" + "="*70)
    print("✅ ITERATION 2 COMPLETE")
    print("="*70)
    print("\nAll 3 Embers created their versions:")
    print("  • Each with different audio/visual approaches")
    print("  • Each with brainwave entrainment")
    print("  • Each using empty space creatively")
    print()
    print("Test them all and see which feels best! 🔥")

if __name__ == '__main__':
    asyncio.run(iteration_2())

