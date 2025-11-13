#!/usr/bin/env python3
"""
Quick test of the evolution chain fix
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, '/media/palmerschallon/ThePod1')

from pod_gardener import PodGardener

async def test():
    print("🧬 Testing evolution chain continuation fix...\n")

    gardener = PodGardener()
    await gardener.initialize_ember()

    # Find one evolution chain to test
    incomplete = gardener.find_incomplete_evolutions()

    if not incomplete:
        print("No evolution chains found to test")
        return

    # Test with the first one
    chain = incomplete[0]
    print(f"Testing chain: {chain['base']}")
    print(f"Current max gen: {chain['current_max']}")
    print(f"Will create: gen{chain['current_max'] + 1}\n")

    # Try to continue it
    try:
        await gardener.continue_evolution_chain(chain)
        print("\n✓ SUCCESS! Evolution chain continued")
    except Exception as e:
        print(f"\n❌ FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(test())
