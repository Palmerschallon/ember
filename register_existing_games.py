#!/usr/bin/env python3
"""
Register existing evolved games into the game library retroactively
"""

import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/media/palmerschallon/ThePod1')


def register_existing_games():
    """Scan for existing game HTML files and register them in the library"""
    pod_root = Path('/media/palmerschallon/ThePod1')
    library_path = pod_root / 'game_library_v2.json'

    # Games to register (known successful games)
    games_to_register = [
        {
            'name': 'physics_platformer_genesis',
            'file': 'physics_platformer_genesis.html',
            'primitives': {
                'movement': ['continuous_2d', 'physics_momentum'],
                'action': ['timing_windows'],
                'space': ['continuous_2d'],
                'feedback': ['scoring', 'health_lives', 'visual_juice'],
                'systems': ['collision_detection', 'camera_system']
            },
            'generation': 0,
            'fitness_score': 0.75,
            'parent_games': []
        },
        {
            'name': 'quantum_pong',
            'file': 'quantum_pong.html',
            'primitives': {
                'movement': ['continuous_2d', 'physics_momentum'],
                'action': ['timing_windows', 'projectile_spawning'],
                'space': ['continuous_2d', 'wrapped_space'],
                'feedback': ['scoring', 'visual_juice'],
                'systems': ['collision_detection', 'ai_opponents']
            },
            'generation': 0,
            'fitness_score': 0.72,
            'parent_games': []
        }
    ]

    # Verify files exist
    existing_games = []
    for game_info in games_to_register:
        game_file = pod_root / game_info['file']
        if game_file.exists():
            print(f"✓ Found {game_info['name']}")
            existing_games.append({
                'name': game_info['name'],
                'primitives': game_info['primitives'],
                'generation': game_info['generation'],
                'fitness_score': game_info['fitness_score'],
                'parent_games': game_info['parent_games'],
                'tech_stack': ['canvas', 'html5'],
                'innovation_score': 0.5,
                'created_at': datetime.fromtimestamp(game_file.stat().st_mtime).isoformat()
            })
        else:
            print(f"✗ Missing {game_info['name']}")

    if not existing_games:
        print("\n⚠️  No games found to register")
        return

    # Create library
    library_data = {
        'games': existing_games,
        'metadata': {
            'total_games': len(existing_games),
            'generation_count': 0,
            'last_updated': datetime.now().isoformat()
        }
    }

    # Save library
    library_path.write_text(json.dumps(library_data, indent=2))
    print(f"\n✓ Registered {len(existing_games)} games to {library_path}")
    print("  Dashboard should now show these games!")

    # Generate visualizations
    print("\n📊 Generating visualizations...")
    try:
        import subprocess
        result = subprocess.run([
            'python3',
            str(pod_root / 'evolution_visualizer.py')
        ], check=True, capture_output=True, text=True)
        print("   ✓ Visualizations generated!")
        print(f"   View dashboard at: http://localhost:8080/evolution_dashboard.html")
    except Exception as e:
        print(f"   ⚠️  Visualization generation failed: {e}")


if __name__ == '__main__':
    register_existing_games()
