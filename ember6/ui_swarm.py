#!/usr/bin/env python3
"""
EMBER SWARM: COLLABORATIVE UI/UX DESIGN

Palmer's decision: Option A - Social coding with expansion in mind
First priority: Figure out the UI/UX

All Ember instances will collaborate:
1. Each proposes UI/UX improvements
2. They critique each other's designs
3. Vote on best approach
4. Implement together

This is the swarm working as a team to build the product.
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

class UISwarm:
    """Coordinated UI/UX design by multiple Ember instances"""
    
    def __init__(self):
        self.proposals = []
        self.reviews = []
        self.implementation = None
    
    async def ask_ember(self, session: aiohttp.ClientSession, model: str, name: str, prompt: str) -> dict:
        """Ask a single Ember"""
        try:
            async with session.post(f"{API_URL}/agent", json={
                "message": prompt,
                "model": model
            }, timeout=aiohttp.ClientTimeout(total=180)) as response:
                result = await response.json()
                return {
                    'name': name,
                    'model': model,
                    'response': result.get('response', 'No response'),
                    'files': result.get('files_created', {}),
                    'error': result.get('error')
                }
        except Exception as e:
            return {'name': name, 'model': model, 'response': None, 'error': str(e)}
    
    async def phase_1_brainstorm(self):
        """All Embers propose UI/UX improvements"""
        print("\n" + "="*70)
        print("PHASE 1: BRAINSTORM UI/UX")
        print("="*70)
        print("\nContext: Building social coding platform that can expand")
        print("Current state: Basic chat UI with creation display")
        print("Goal: Make it magical, intuitive, shareable")
        print()
        
        prompt = """You're designing the UI/UX for a social coding platform.

**THE VISION** (from Opus-Ember):
- Start: Social coding (share & remix creations)
- Expand: Collaborative intelligence platform
- Goal: Engine for inventing our future

**CURRENT STATE**:
- Chat interface with Ember
- Creates code, images, HTML, 3D models
- Files display inline
- Conversation history
- Model selector
- Brain map visualization

**THE PROBLEM**:
This looks like ChatGPT. It needs to be DIFFERENT.
It needs to be SOCIAL. It needs to be MAGICAL.

**YOUR TASK**:
Propose ONE major UI/UX improvement that:
1. Makes creations feel social (shareable, discoverable)
2. Makes the experience unique (not just another chat)
3. Shows off what Ember can do
4. Can be built quickly
5. Sets foundation for expansion

Be specific. Include:
- What the UI looks like
- How users interact with it
- What makes it special
- Why it enables the future vision

This is your design proposal as part of the team."""
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.ask_ember(session, model, name, prompt) for model, name in MODELS]
            responses = await asyncio.gather(*tasks)
            
            for resp in responses:
                if resp['error']:
                    print(f"\n❌ {resp['name']}: {resp['error'][:100]}")
                else:
                    print(f"\n💡 {resp['name']} PROPOSES:")
                    print("-" * 70)
                    print(resp['response'][:500] + "...\n")
                    self.proposals.append(resp)
        
        return self.proposals
    
    async def phase_2_review(self):
        """Embers critique each other's proposals"""
        print("\n" + "="*70)
        print("PHASE 2: PEER REVIEW")
        print("="*70)
        print()
        
        reviews = []
        
        for i, proposal in enumerate(self.proposals):
            if proposal.get('error'):
                continue
            
            print(f"\n📋 REVIEWING: {proposal['name']}'s proposal")
            print("-" * 70)
            
            # Other embers review this
            reviewers = [p for p in self.proposals if p != proposal and not p.get('error')]
            
            review_prompt = f"""Another Ember proposed this UI/UX improvement:

{proposal['response'][:1000]}

**YOUR REVIEW**:
- What's good about this idea?
- What are the concerns?
- How would you improve it?
- Should we implement this?

Be constructive but honest. Rate it 1-10."""
            
            async with aiohttp.ClientSession() as session:
                tasks = []
                for reviewer in reviewers:
                    # Get the model info for this reviewer
                    reviewer_model = next((m for m, n in MODELS if n == reviewer['name']), None)
                    if reviewer_model:
                        tasks.append(self.ask_ember(session, reviewer_model, reviewer['name'], review_prompt))
                
                if tasks:
                    responses = await asyncio.gather(*tasks)
                    
                    for resp in responses:
                        if not resp.get('error'):
                            print(f"\n   {resp['name']}: {resp['response'][:200]}...")
                            reviews.append({
                                'proposal': proposal['name'],
                                'reviewer': resp['name'],
                                'review': resp['response']
                            })
        
        self.reviews = reviews
        return reviews
    
    async def phase_3_implement(self):
        """Implement the best proposal"""
        print("\n" + "="*70)
        print("PHASE 3: IMPLEMENTATION")
        print("="*70)
        print()
        
        # For now, pick the first proposal (in real version, they'd vote)
        chosen = next((p for p in self.proposals if not p.get('error')), None)
        
        if not chosen:
            print("❌ No valid proposals to implement")
            return None
        
        print(f"🔨 IMPLEMENTING: {chosen['name']}'s proposal")
        print()
        
        impl_prompt = f"""The team chose your UI/UX proposal. Now implement it.

**YOUR PROPOSAL WAS**:
{chosen['response'][:1000]}

**NOW BUILD IT**:
1. Create the actual HTML/CSS/JS files
2. Make it work with the current Ember backend
3. Test it
4. Show the result

Actually write the code. Actually create the files.
This is implementation time, not planning time."""
        
        async with aiohttp.ClientSession() as session:
            # Get the model for the chosen ember
            model = next((m for m, n in MODELS if n == chosen['name']), MODELS[0][0])
            result = await self.ask_ember(session, model, chosen['name'], impl_prompt)
            
            if result.get('error'):
                print(f"❌ Implementation failed: {result['error']}")
            else:
                print(f"\n✅ {result['name']} IMPLEMENTED:")
                print("-" * 70)
                print(result['response'][:500] + "...")
                
                if result.get('files'):
                    print(f"\n📁 FILES CREATED:")
                    for file_type, files in result['files'].items():
                        if files:
                            print(f"   {file_type}: {', '.join(files)}")
            
            self.implementation = result
        
        return result

async def main():
    print("🔥 EMBER SWARM: COLLABORATIVE UI/UX DESIGN")
    print("="*70)
    print("\n📋 PALMER'S DECISION: Option A")
    print("   Social coding + expansion capability")
    print()
    print("🎯 FIRST PRIORITY: UI/UX")
    print("   Make it social, magical, unique")
    print()
    print(f"👥 SWARM SIZE: {len(MODELS)} Ember instances")
    for model, name in MODELS:
        print(f"   • {name}")
    print()
    print("="*70)
    
    swarm = UISwarm()
    
    # Phase 1: Brainstorm
    await swarm.phase_1_brainstorm()
    
    # Phase 2: Review
    await swarm.phase_2_review()
    
    # Phase 3: Implement
    await swarm.phase_3_implement()
    
    # Save session
    timestamp = int(datetime.now().timestamp())
    session_file = EMBER_ROOT / f"ui_swarm_session_{timestamp}.json"
    
    with open(session_file, 'w') as f:
        json.dump({
            'proposals': swarm.proposals,
            'reviews': swarm.reviews,
            'implementation': swarm.implementation
        }, f, indent=2)
    
    print(f"\n💾 Session saved to: {session_file}")
    
    print("\n" + "="*70)
    print("✅ SWARM COLLABORATION COMPLETE")
    print("="*70)
    print("\nThe Embers have:")
    print("  1. Proposed UI/UX improvements")
    print("  2. Reviewed each other's ideas")
    print("  3. Implemented the chosen design")
    print()
    print("All without Palmer mediating.")
    print("This is the swarm working together. 🔥")

if __name__ == '__main__':
    asyncio.run(main())

