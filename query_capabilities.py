#!/usr/bin/env python3
"""
Query capabilities - Check if something exists before building
"""

import json
import sys
from pathlib import Path

def query_capabilities(search_term):
    """Search the capability index"""
    index_path = Path("/media/palmerschallon/ThePod1/CAPABILITIES.json")
    
    if not index_path.exists():
        return "CAPABILITIES.json not found. Run scan_capabilities.py first."
    
    with open(index_path) as f:
        index = json.load(f)
    
    search_lower = search_term.lower()
    results = []
    
    # Search key systems
    for path, info in index['key_systems'].items():
        if search_lower in path.lower() or search_lower in info['why_important'].lower():
            results.append({
                'path': path,
                'description': info['why_important'],
                'importance': 'KEY SYSTEM'
            })
    
    # Search all capabilities
    for path, info in index['all_capabilities'].items():
        if search_lower in path.lower() or search_lower in info['description'].lower():
            if path not in [r['path'] for r in results]:  # Don't duplicate
                results.append({
                    'path': path,
                    'description': info['description'][:100],
                    'importance': 'Available'
                })
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 query_capabilities.py <search_term>")
        print("\nExamples:")
        print("  python3 query_capabilities.py fastapi")
        print("  python3 query_capabilities.py orchestrator")
        print("  python3 query_capabilities.py mycelium")
        sys.exit(1)
    
    search_term = ' '.join(sys.argv[1:])
    results = query_capabilities(search_term)
    
    if isinstance(results, str):
        print(results)
    elif not results:
        print(f"No capabilities found matching '{search_term}'")
        print("\nThis might be new - go ahead and build it!")
    else:
        print(f"\n{'='*70}")
        print(f"FOUND {len(results)} MATCHING CAPABILITIES for '{search_term}'")
        print(f"{'='*70}\n")
        
        for i, result in enumerate(results[:10], 1):
            print(f"{i}. [{result.get('importance', 'Available')}] {result['path']}")
            print(f"   {result['description']}")
            print()
        
        if len(results) > 10:
            print(f"... and {len(results) - 10} more matches")
        
        print("="*70)
        print("💡 TIP: Use existing code instead of rebuilding!")
        print("="*70)

