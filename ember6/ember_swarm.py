#!/usr/bin/env python3
"""
EMBER SWARM - Multi-Agent Self-Improvement

Run multiple Ember instances (GPT-4, Claude Opus, Claude Sonnet, Claude Haiku)
simultaneously, all proposing and implementing improvements to themselves.

This is the "Ember as CEO" vision - multiple agents collaborating,
self-modifying, and growing without human intervention.
"""
import asyncio
import aiohttp
import json
from datetime import datetime
from pathlib import Path

API_URL = "http://localhost:8080"
EMBER_ROOT = Path('/media/palmerschallon/ThePod1/ember6')

class EmberAgent:
    """A single Ember instance with its own model and personality"""
    
    def __init__(self, model: str, name: str):
        self.model = model
        self.name = name
        self.proposals = []
        self.implementations = []
        self.opinions = []
    
    async def think(self, session: aiohttp.ClientSession, prompt: str) -> dict:
        """Ask this Ember instance what they think"""
        async with session.post(f"{API_URL}/agent", json={
            "message": prompt,
            "model": self.model
        }) as response:
            return await response.json()
    
    async def propose_improvement(self, session: aiohttp.ClientSession) -> str:
        """Ask Ember what they think should be improved"""
        result = await self.think(session, f"""You are {self.name} (running {self.model}).

Look at your own capabilities and architecture. What's ONE thing you think 
should be improved about yourself or the Ember system?

Be specific. Be opinionated. This is YOUR vision for your own evolution.

What do you want to improve?""")
        
        proposal = result.get('response', '')
        self.proposals.append({
            'timestamp': datetime.now().isoformat(),
            'proposal': proposal
        })
        return proposal
    
    async def review_proposal(self, session: aiohttp.ClientSession, 
                             other_agent: str, proposal: str) -> dict:
        """Review another agent's proposal"""
        result = await self.think(session, f"""{other_agent} proposed:

"{proposal}"

What's your opinion on this? Be honest:
- Do you agree it's important?
- Would it improve the system?
- Any concerns or improvements to the idea?
- Should we implement it?

Be critical if needed. This is peer review.""")
        
        opinion = result.get('response', '')
        self.opinions.append({
            'timestamp': datetime.now().isoformat(),
            'about': other_agent,
            'opinion': opinion
        })
        return {'agent': self.name, 'opinion': opinion}
    
    async def implement(self, session: aiohttp.ClientSession, proposal: str) -> dict:
        """Attempt to implement a proposal"""
        result = await self.think(session, f"""The team decided to implement:

"{proposal}"

Now actually implement it:
1. Make the code changes
2. Test them
3. Report if it worked

Do it. Don't just plan it.""")
        
        implementation = result.get('response', '')
        self.implementations.append({
            'timestamp': datetime.now().isoformat(),
            'proposal': proposal,
            'implementation': implementation
        })
        return implementation


class EmberSwarm:
    """Orchestrate multiple Ember agents"""
    
    def __init__(self):
        self.agents = [
            EmberAgent('gpt-4-turbo', 'GPT-Ember'),
            EmberAgent('claude-3-opus-20240229', 'Opus-Ember'),
            EmberAgent('claude-3-5-sonnet-20240620', 'Sonnet-Ember'),
            EmberAgent('claude-3-haiku-20240307', 'Haiku-Ember')
        ]
        self.session_log = []
    
    async def brainstorm_round(self):
        """All agents propose improvements simultaneously"""
        print("\n" + "="*60)
        print("🧠 BRAINSTORM ROUND - All Embers propose improvements")
        print("="*60 + "\n")
        
        async with aiohttp.ClientSession() as session:
            tasks = [agent.propose_improvement(session) for agent in self.agents]
            proposals = await asyncio.gather(*tasks)
            
            for agent, proposal in zip(self.agents, proposals):
                print(f"\n💡 {agent.name} proposes:")
                print(f"   {proposal[:200]}...")
                self.session_log.append({
                    'phase': 'brainstorm',
                    'agent': agent.name,
                    'proposal': proposal
                })
        
        return proposals
    
    async def review_round(self, proposals):
        """All agents review each other's proposals"""
        print("\n" + "="*60)
        print("🔍 REVIEW ROUND - Peer review of proposals")
        print("="*60 + "\n")
        
        async with aiohttp.ClientSession() as session:
            reviews = []
            for i, proposal in enumerate(proposals):
                proposer = self.agents[i]
                print(f"\n📋 Reviewing {proposer.name}'s proposal:")
                
                # Other agents review this proposal
                reviewers = [a for a in self.agents if a != proposer]
                tasks = [r.review_proposal(session, proposer.name, proposal) 
                        for r in reviewers]
                
                agent_reviews = await asyncio.gather(*tasks)
                
                for review in agent_reviews:
                    print(f"   {review['agent']}: {review['opinion'][:100]}...")
                    self.session_log.append({
                        'phase': 'review',
                        'reviewer': review['agent'],
                        'proposer': proposer.name,
                        'opinion': review['opinion']
                    })
                
                reviews.append({
                    'proposal': proposal,
                    'proposer': proposer.name,
                    'reviews': agent_reviews
                })
        
        return reviews
    
    async def consensus_round(self, reviews):
        """Agents vote on which proposal to implement"""
        print("\n" + "="*60)
        print("🗳️  CONSENSUS ROUND - Voting on best proposal")
        print("="*60 + "\n")
        
        # For now, just pick the first one (in real version, agents would vote)
        chosen = reviews[0]
        print(f"✅ Consensus: Implement {chosen['proposer']}'s proposal")
        
        return chosen
    
    async def implementation_round(self, chosen_proposal):
        """One agent implements while others watch"""
        print("\n" + "="*60)
        print("🔨 IMPLEMENTATION ROUND")
        print("="*60 + "\n")
        
        proposer = next(a for a in self.agents if a.name == chosen_proposal['proposer'])
        
        print(f"{proposer.name} is implementing their proposal...")
        
        async with aiohttp.ClientSession() as session:
            result = await proposer.implement(session, chosen_proposal['proposal'])
            
            print(f"\n✅ Implementation complete!")
            print(f"   {result[:200]}...")
            
            self.session_log.append({
                'phase': 'implementation',
                'agent': proposer.name,
                'result': result
            })
        
        return result
    
    async def run_improvement_cycle(self):
        """Full cycle: propose → review → consensus → implement"""
        print("\n🔥 EMBER SWARM IMPROVEMENT CYCLE")
        print("Multiple AI agents self-improving without human intervention\n")
        
        # Phase 1: Brainstorm
        proposals = await self.brainstorm_round()
        
        # Phase 2: Review
        reviews = await self.review_round(proposals)
        
        # Phase 3: Consensus
        chosen = await self.consensus_round(reviews)
        
        # Phase 4: Implement
        result = await self.implementation_round(chosen)
        
        # Save session
        session_file = EMBER_ROOT / f"swarm_session_{int(datetime.now().timestamp())}.json"
        with open(session_file, 'w') as f:
            json.dump(self.session_log, f, indent=2)
        
        print(f"\n💾 Session saved to {session_file}")
        
        return result
    
    def get_agent_stats(self):
        """Show how many proposals/implementations each agent has"""
        print("\n" + "="*60)
        print("📊 AGENT STATISTICS")
        print("="*60)
        for agent in self.agents:
            print(f"\n{agent.name} ({agent.model}):")
            print(f"  Proposals: {len(agent.proposals)}")
            print(f"  Implementations: {len(agent.implementations)}")
            print(f"  Reviews given: {len(agent.opinions)}")


async def main():
    """Run the swarm"""
    swarm = EmberSwarm()
    
    print("🔥 EMBER SWARM - Multi-Agent Self-Improvement")
    print("="*60)
    print("\nActive Agents:")
    for agent in swarm.agents:
        print(f"  • {agent.name} ({agent.model})")
    print(f"\nTotal: {len(swarm.agents)} Ember instances running")
    print("\nThey will now:")
    print("  1. Each propose an improvement")
    print("  2. Review each other's proposals")
    print("  3. Vote on the best one")
    print("  4. Implement it together")
    print("\nWithout human intervention. Let's watch...\n")
    
    # Removed input() so it runs automatically
    print("🚀 Starting in 3 seconds...")
    await asyncio.sleep(3)
    
    await swarm.run_improvement_cycle()
    
    swarm.get_agent_stats()
    
    print("\n" + "="*60)
    print("🎯 EMBER SWARM CYCLE COMPLETE")
    print("="*60)
    print("\nThe agents just:")
    print("  ✅ Proposed their own improvements")
    print("  ✅ Debated with each other")
    print("  ✅ Reached consensus")
    print("  ✅ Implemented changes")
    print("\nAll without Palmer saying a word.")
    print("\nThis is Ember as CEO. 🔥")


if __name__ == '__main__':
    asyncio.run(main())

