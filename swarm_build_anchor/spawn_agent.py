#!/usr/bin/env python3
"""
Individual agent spawner for testing the temporal anchor system
"""

import sys
import time
import argparse
from pathlib import Path

# Import from our main module
sys.path.append(str(Path(__file__).parent))
from build_temporal_anchor import SwarmAgent

def main():
    parser = argparse.ArgumentParser(description='Spawn a swarm agent')
    parser.add_argument('--type', choices=['builder', 'scanner', 'weaver', 'guardian'], 
                       default='builder', help='Agent type')
    parser.add_argument('--anchor', default='anchor_ALPHA_001', 
                       help='Anchor directory name')
    parser.add_argument('--actions', type=int, default=5, 
                       help='Number of actions to perform')
    
    args = parser.parse_args()
    
    # Create agent
    anchor_path = Path(__file__).parent / args.anchor
    
    if not anchor_path.exists():
        print(f"❌ Anchor path not found: {anchor_path}")
        print("   Run build_temporal_anchor.py first!")
        return
    
    agent = SwarmAgent(args.type, anchor_path)
    agent.join_swarm()
    
    print(f"✨ Agent {agent.agent_id} active")
    print(f"   Type: {args.type}")
    print(f"   Syncing with: {args.anchor}\n")
    
    # Perform actions
    for i in range(args.actions):
        pulse = agent.sync_with_anchor()
        
        if pulse:
            print(f"📡 Pulse received - Phase: {pulse['phase']}")
            
            # Create artifact
            if i % 2 == 0:  # Every other cycle
                artifact = agent.create_artifact()
                print(f"🔨 Created artifact: {artifact.name}")
        else:
            print("⏳ Waiting for anchor pulse...")
        
        time.sleep(2)
    
    print(f"\n✅ Agent {agent.agent_id} completed mission")

if __name__ == "__main__":
    main()