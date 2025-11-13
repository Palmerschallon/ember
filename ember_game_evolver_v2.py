#!/usr/bin/env python3
"""
EMBER GAME EVOLVER V2 - PRIMITIVE-BASED EVOLUTION
==================================================
Advanced LLM-powered game evolution with:
- Game primitive library (movement, action, space, feedback, systems)
- Complex seed games (platformers, roguelikes, tower defense, etc.)
- Multi-tool asset pipeline (ImageMagick, SoX, Blender)
- Primitive-aware evolution prompts
- Asset generation and optimization

Evolution path: Complex seeds → Genre innovation → Indie-quality games
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import random
import subprocess

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener
from ember_complete import Ember


class GameGenome:
    """High-level semantic representation with primitives"""

    def __init__(self):
        # Primitive-based tracking
        self.primitives = {
            'movement': [],
            'action': [],
            'space': [],
            'feedback': [],
            'systems': [],
            'meta_primitives': []
        }

        # Legacy fields (backward compatible)
        self.core_mechanics = []
        self.systems = []
        self.complexity_features = []
        self.tech_stack = []

        # Evolution tracking
        self.generation = 0
        self.parent_games = []
        self.fitness_score = 0.0
        self.innovation_score = 0.0
        self.asset_manifest = {}  # Track generated assets

    def to_dict(self) -> Dict:
        return {
            'primitives': self.primitives,
            'core_mechanics': self.core_mechanics,
            'systems': self.systems,
            'complexity_features': self.complexity_features,
            'tech_stack': self.tech_stack,
            'generation': self.generation,
            'parent_games': self.parent_games,
            'fitness_score': self.fitness_score,
            'innovation_score': self.innovation_score,
            'asset_manifest': self.asset_manifest
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'GameGenome':
        genome = cls()
        genome.primitives = data.get('primitives', {
            'movement': [], 'action': [], 'space': [],
            'feedback': [], 'systems': [], 'meta_primitives': []
        })
        genome.core_mechanics = data.get('core_mechanics', [])
        genome.systems = data.get('systems', [])
        genome.complexity_features = data.get('complexity_features', [])
        genome.tech_stack = data.get('tech_stack', [])
        genome.generation = data.get('generation', 0)
        genome.parent_games = data.get('parent_games', [])
        genome.fitness_score = data.get('fitness_score', 0.0)
        genome.innovation_score = data.get('innovation_score', 0.0)
        genome.asset_manifest = data.get('asset_manifest', {})
        return genome


class AssetPipeline:
    """Generate and optimize game assets using creative tools"""

    def __init__(self, assets_dir: Path):
        self.assets_dir = assets_dir
        self.assets_dir.mkdir(exist_ok=True)

    def generate_sprite(self, description: str, name: str) -> Optional[str]:
        """Use ImageMagick to create a sprite"""
        try:
            output_path = self.assets_dir / f"{name}.png"

            # Simple geometric sprite generation
            # Example: colored circle with gradient
            cmd = [
                'convert', '-size', '64x64', 'xc:transparent',
                '-fill', f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}',
                '-draw', 'circle 32,32 32,4',
                str(output_path)
            ]

            subprocess.run(cmd, check=True, capture_output=True)
            return str(output_path.name)
        except Exception as e:
            print(f"    ⚠️ Sprite generation failed: {e}")
            return None

    def generate_sound(self, sound_type: str, name: str) -> Optional[str]:
        """Use SoX to synthesize sound effects"""
        try:
            output_path = self.assets_dir / f"{name}.wav"

            # Generate different sound types
            if sound_type == 'jump':
                cmd = ['sox', '-n', str(output_path), 'synth', '0.1', 'sine', '880', 'fade', '0', '0.1', '0.05']
            elif sound_type == 'explosion':
                cmd = ['sox', '-n', str(output_path), 'synth', '0.3', 'noise', 'fade', '0', '0.3', '0.1']
            elif sound_type == 'coin':
                cmd = ['sox', '-n', str(output_path), 'synth', '0.05', 'sine', '1320', 'fade', '0', '0.05', '0.02']
            else:
                cmd = ['sox', '-n', str(output_path), 'synth', '0.2', 'sine', '440']

            subprocess.run(cmd, check=True, capture_output=True)
            return str(output_path.name)
        except Exception as e:
            print(f"    ⚠️ Sound generation failed: {e}")
            return None

    def optimize_assets(self, game_dir: Path):
        """Compress and optimize all assets"""
        try:
            # Optimize PNGs
            for png in game_dir.glob('*.png'):
                subprocess.run(
                    ['convert', str(png), '-quality', '85', str(png)],
                    check=True, capture_output=True
                )
        except Exception as e:
            print(f"    ⚠️ Asset optimization failed: {e}")


class EmberGameEvolverV2(ResilientGardener):
    """Advanced LLM-powered game evolution with primitives"""

    def __init__(self):
        super().__init__('game_evolver_v2', pod_root='/media/palmerschallon/ThePod1')

        self.games_dir = self.pod_root / 'evolved_games'
        self.games_dir.mkdir(exist_ok=True)

        self.library_path = self.games_dir / 'game_library_v2.json'
        self.evolution_log = self.games_dir / 'evolution_log_v2.jsonl'
        self.primitives_path = self.pod_root / 'game_primitives.json'

        self.ember = Ember()
        self.game_library: Dict[str, GameGenome] = {}
        self.generation_count = 0
        self.primitives_library = {}

        self.asset_pipeline = AssetPipeline(self.games_dir / 'assets')

        self._load_primitives()
        self._load_library()

    def _load_primitives(self):
        """Load game primitives library"""
        if self.primitives_path.exists():
            self.primitives_library = json.loads(self.primitives_path.read_text())
            print(f"  ✓ Loaded primitives library with {len(self.primitives_library)} categories")

    def _load_library(self):
        """Load existing game library (supports both old and new formats)"""
        if self.library_path.exists():
            try:
                data = json.loads(self.library_path.read_text())

                # New format: {'games': [...], 'metadata': {...}}
                if 'games' in data and 'metadata' in data:
                    self.generation_count = data['metadata'].get('generation_count', 0)
                    for game_data in data['games']:
                        name = game_data.get('name')
                        if name:
                            self.game_library[name] = GameGenome.from_dict(game_data)
                # Old format: {game_name: genome_dict, '_generation_count': N}
                else:
                    self.generation_count = data.get('_generation_count', 0)
                    for name, genome_dict in data.items():
                        if name != '_generation_count':
                            self.game_library[name] = GameGenome.from_dict(genome_dict)

                print(f"  ✓ Loaded {len(self.game_library)} games, generation {self.generation_count}")
            except Exception as e:
                print(f"  ⚠️  Failed to load library: {e}")

    def _save_library(self):
        """Save game library in format expected by visualizer"""
        games_list = []
        for name, genome in self.game_library.items():
            game_data = genome.to_dict()
            game_data['name'] = name
            games_list.append(game_data)

        library_data = {
            'games': games_list,
            'metadata': {
                'total_games': len(games_list),
                'generation_count': self.generation_count,
                'last_updated': datetime.now().isoformat()
            }
        }
        self.write_file_directly(self.library_path, json.dumps(library_data, indent=2))

    def _log_evolution(self, event: Dict):
        """Log evolution event"""
        event['timestamp'] = datetime.now().isoformat()
        with open(self.evolution_log, 'a') as f:
            f.write(json.dumps(event) + '\n')

    async def create_complex_seed_games(self):
        """Create sophisticated seed games with primitive definitions"""
        print("\n🌱 Creating complex seed games...")

        seed_concepts = [
            {
                'name': 'physics_platformer_genesis',
                'primitives': {
                    'movement': ['continuous_2d', 'physics_momentum'],
                    'action': ['timing_windows'],
                    'space': ['continuous_2d'],
                    'feedback': ['scoring', 'health_lives', 'visual_juice'],
                    'systems': ['collision_detection', 'camera_system']
                },
                'concept': '''Physics-based platformer with momentum and satisfying movement feel.

Features:
- Variable jump height (hold longer = higher)
- Wall-jumping with momentum conservation
- Moving platforms with physics
- Collectible coins
- Screen shake on landing
- Particle effects
- Smooth camera follow
- Lives system with respawn

The goal: Create a tight, responsive platformer that feels amazing to play.'''
            },
            {
                'name': 'roguelike_dungeon_genesis',
                'primitives': {
                    'movement': ['grid_based'],
                    'action': ['discrete_turns'],
                    'space': ['tile_grid', 'procedural_generation'],
                    'feedback': ['health_lives', 'resources'],
                    'systems': ['collision_detection', 'inventory', 'ai_opponents', 'procedural_content']
                },
                'concept': '''Classic roguelike with procedural dungeons and tactical combat.

Features:
- BSP tree dungeon generation
- Turn-based movement (roguelike controls: HJKL or arrows)
- Fog of war
- Enemies with simple AI (chase player when visible)
- Items: potions, weapons
- Grid-based combat
- Permadeath
- ASCII-inspired modern graphics

The goal: Strategic, replayable dungeon crawler.'''
            },
            {
                'name': 'tower_defense_genesis',
                'primitives': {
                    'movement': ['pathfinding'],
                    'action': ['drag_drop', 'resource_management'],
                    'space': ['graph_network'],
                    'feedback': ['resources', 'visual_juice'],
                    'systems': ['ai_opponents', 'upgrade_trees']
                },
                'concept': '''Tower defense with A* pathfinding and strategic placement.

Features:
- Enemy waves with A* pathfinding to goal
- Drag-and-drop tower placement
- Currency earned from kills
- Tower upgrade system (damage, range, rate)
- Multiple tower types
- Visual projectiles
- Wave system with increasing difficulty

The goal: Strategic tower placement with economic decisions.'''
            },
            {
                'name': 'rhythm_game_genesis',
                'primitives': {
                    'movement': ['grid_based'],
                    'action': ['timing_windows'],
                    'feedback': ['combo_multipliers', 'visual_juice'],
                    'systems': ['sound_system']
                },
                'concept': '''Rhythm game with perfect/good/miss timing windows.

Features:
- Notes falling from top
- Hit zones at bottom (4 lanes)
- Timing windows: perfect (±50ms), good (±100ms), miss
- Combo multiplier (resets on miss)
- Visual feedback (explosions on perfect)
- Generated rhythm pattern
- Score system

The goal: Satisfying rhythm mechanics with flow state gameplay.'''
            },
            {
                'name': 'puzzle_mechanics_genesis',
                'primitives': {
                    'movement': ['grid_based'],
                    'action': ['discrete_turns'],
                    'space': ['tile_grid'],
                    'feedback': ['progress'],
                    'systems': ['state_machine']
                },
                'concept': '''Sokoban-style puzzle with undo and elegant mechanics.

Features:
- Push boxes to goals
- Undo system (full history)
- Level progression
- Move counter
- Grid-based movement
- Win detection
- Clean, minimal visual style
- Multiple levels with increasing complexity

The goal: Pure puzzle mechanics with "aha!" moments.'''
            }
        ]

        for seed in seed_concepts:
            if seed['name'] in self.game_library:
                print(f"  ⏭  {seed['name']} already exists")
                continue

            print(f"  🎮 Creating {seed['name']}...")
            print(f"    Primitives: {', '.join([p for cat in seed['primitives'].values() for p in cat])}")

            # Extract only relevant primitive details
            relevant_primitives = {}
            for category, prims in seed['primitives'].items():
                relevant_primitives[category] = {}
                for prim in prims:
                    if prim in self.primitives_library.get(category, {}):
                        relevant_primitives[category][prim] = self.primitives_library[category][prim]

            # Generate game code and write via Python (more reliable than tool-based writing)
            game_path = self.games_dir / f"{seed['name']}.html"

            prompt = f"""Create a complete, polished HTML5 game.

GAME NAME: {seed['name']}

CONCEPT:
{seed['concept']}

PRIMITIVES TO IMPLEMENT:
{json.dumps(relevant_primitives, indent=2)}

Requirements:
- Single standalone HTML file with <!DOCTYPE html>
- HTML5 Canvas rendering
- Smooth 60fps gameplay
- Responsive controls
- Modern visual style with polish
- Clear UI/HUD
- Game states (menu, playing, game over)
- Restart functionality (R key)

Make it POLISHED and FUN. This is a complex seed game.

IMPORTANT: Return ONLY the complete HTML code, starting with <!DOCTYPE html>
Do NOT attempt to write the file yourself - just return the HTML code."""

            try:
                # Get HTML code from Ember
                game_code = await self.ember.chat(prompt)

                # Write file via Python
                self.write_file_directly(game_path, game_code)

                # Verify file was created
                if not game_path.exists():
                    print(f"    ✗ Failed to create {seed['name']}")
                    continue

                print(f"    ✓ Created {game_path.name}")

                # Create genome
                genome = GameGenome()
                genome.primitives = seed['primitives']
                genome.tech_stack = ['canvas', 'html5']
                genome.generation = 0
                genome.parent_games = []
                genome.fitness_score = 0.6  # Higher baseline for complex seeds

                self.game_library[seed['name']] = genome

                self._log_evolution({
                    'event': 'complex_seed_created',
                    'game': seed['name'],
                    'primitives': seed['primitives'],
                    'generation': 0
                })

                print(f"    ✓ Created {seed['name']}")

            except Exception as e:
                print(f"    ✗ Failed to create {seed['name']}: {e}")

        self._save_library()
        print(f"  ✓ Seed population: {len(self.game_library)} games")

    async def evolve_primitive_game(self):
        """Evolve a new game using primitive-based crossover"""
        print(f"\n🧬 Evolving Generation {self.generation_count + 1}...")

        if len(self.game_library) < 2:
            print("  ⚠️  Need at least 2 games to evolve")
            return None

        # Select parents (favor high fitness)
        sorted_games = sorted(
            self.game_library.items(),
            key=lambda x: x[1].fitness_score + x[1].innovation_score,
            reverse=True
        )

        parent_pool = sorted_games[:max(2, len(sorted_games) // 2)]
        parent1_name, parent1 = random.choice(parent_pool)
        parent2_name, parent2 = random.choice(parent_pool)

        print(f"  🧬 Parents: {parent1_name} (gen {parent1.generation}, fitness {parent1.fitness_score:.2f})")
        print(f"            + {parent2_name} (gen {parent2.generation}, fitness {parent2.fitness_score:.2f})")

        # Show primitive inheritance
        print(f"    Parent 1 primitives: {sum(len(v) for v in parent1.primitives.values())} total")
        print(f"    Parent 2 primitives: {sum(len(v) for v in parent2.primitives.values())} total")

        prompt = f"""You are evolving games using PRIMITIVES! Create a NEW game combining these parents:

PARENT 1: {parent1_name}
Primitives:
{json.dumps(parent1.primitives, indent=2)}
Generation: {parent1.generation}
Fitness: {parent1.fitness_score:.2f}

PARENT 2: {parent2_name}
Primitives:
{json.dumps(parent2.primitives, indent=2)}
Generation: {parent2.generation}
Fitness: {parent2.fitness_score:.2f}

AVAILABLE PRIMITIVES LIBRARY:
{json.dumps(self.primitives_library, indent=2)}

Your mission:
1. **Analyze** what makes each parent successful
2. **Select** the best primitives from each parent
3. **Add** ONE new primitive from the library (choose wisely!)
4. **Combine** primitives in a novel way that creates emergent gameplay
5. **Ensure** the combination makes sense (e.g., grid_based + physics_momentum = interesting challenge)

Guidelines:
- The child should feel like a natural evolution
- Add complexity but maintain coherence
- Aim for genre-blending innovation
- Implement primitives faithfully according to their definitions
- Polish and juice are important (particles, shake, feedback)

Technical Requirements:
- Single HTML file with embedded CSS/JS
- HTML5 Canvas rendering
- 60fps gameplay
- Modern visual design
- Clear UI/HUD
- Game states (menu, playing, game over)
- Restart functionality

Create something INNOVATIVE that inherits the best DNA from both parents!

Return ONLY the complete HTML code, starting with <!DOCTYPE html>"""

        try:
            game_code = await self.ember.chat(prompt)

            # Generate name
            self.generation_count += 1
            game_name = f"evolved_gen{self.generation_count:03d}_{random.randint(1000, 9999)}"
            game_path = self.games_dir / f"{game_name}.html"

            # Save game
            self.write_file_directly(game_path, game_code)

            # Create genome (combine parent primitives)
            genome = GameGenome()
            for category in genome.primitives.keys():
                p1_prims = set(parent1.primitives.get(category, []))
                p2_prims = set(parent2.primitives.get(category, []))
                genome.primitives[category] = list(p1_prims | p2_prims)

            genome.tech_stack = list(set(parent1.tech_stack + parent2.tech_stack))
            genome.generation = max(parent1.generation, parent2.generation) + 1
            genome.parent_games = [parent1_name, parent2_name]
            genome.fitness_score = 0.5  # Will be evaluated
            genome.innovation_score = 0.0

            self.game_library[game_name] = genome

            self._log_evolution({
                'event': 'primitive_evolution',
                'game': game_name,
                'parents': [parent1_name, parent2_name],
                'generation': genome.generation,
                'primitives': genome.primitives
            })

            self._save_library()

            total_primitives = sum(len(v) for v in genome.primitives.values())
            print(f"  ✓ Evolved: {game_name}")
            print(f"    Generation: {genome.generation}")
            print(f"    Primitives: {total_primitives}")

            return game_name

        except Exception as e:
            print(f"  ✗ Evolution failed: {e}")
            return None

    async def evaluate_game(self, game_name: str):
        """Evaluate game quality with primitive awareness"""
        print(f"\n📊 Evaluating {game_name}...")

        if game_name not in self.game_library:
            print("  ⚠️  Game not in library")
            return

        game_path = self.games_dir / f"{game_name}.html"
        if not game_path.exists():
            print("  ⚠️  Game file not found")
            return

        genome = self.game_library[game_name]

        prompt = f"""Evaluate this evolved game's quality:

Game: {game_name}
Generation: {genome.generation}
Primitives Implemented:
{json.dumps(genome.primitives, indent=2)}

Rate the game (0.0 to 1.0):
1. **Primitive Implementation** - Are primitives correctly/fully implemented?
2. **Gameplay Fun** - Engaging mechanics and satisfying feel?
3. **Polish** - Visual appeal, particles, juice, smooth animations?
4. **Innovation** - Novel combinations or unique mechanics?
5. **Completeness** - Finished, playable game with all states?
6. **Coherence** - Do primitives work well together?

Return ONLY a JSON object:
{{
  "primitive_implementation": 0.0-1.0,
  "gameplay_fun": 0.0-1.0,
  "polish": 0.0-1.0,
  "innovation": 0.0-1.0,
  "completeness": 0.0-1.0,
  "coherence": 0.0-1.0,
  "notes": "brief evaluation summary"
}}"""

        try:
            response = await self.ember.chat(prompt)

            # Parse evaluation
            import re
            json_match = re.search(r'\{[^}]+\}', response, re.DOTALL)
            if json_match:
                eval_data = json.loads(json_match.group())

                # Calculate fitness (weighted for new criteria)
                fitness = (
                    eval_data['primitive_implementation'] * 0.25 +
                    eval_data['gameplay_fun'] * 0.25 +
                    eval_data['polish'] * 0.15 +
                    eval_data['innovation'] * 0.20 +
                    eval_data['completeness'] * 0.10 +
                    eval_data['coherence'] * 0.05
                )

                genome.fitness_score = fitness
                genome.innovation_score = eval_data['innovation']

                self._save_library()

                print(f"  ✓ Fitness: {fitness:.2f}")
                print(f"    Innovation: {eval_data['innovation']:.2f}")
                print(f"    Primitive Implementation: {eval_data['primitive_implementation']:.2f}")
                print(f"    Notes: {eval_data['notes']}")

                self._log_evolution({
                    'event': 'evaluation',
                    'game': game_name,
                    'fitness': fitness,
                    'details': eval_data
                })
            else:
                print(f"  ⚠️  Could not parse evaluation")

        except Exception as e:
            print(f"  ✗ Evaluation failed: {e}")

    async def run_evolution_cycle(self):
        """Run one complete primitive-based evolution cycle"""
        print("\n" + "="*70)
        print("🎮 EMBER GAME EVOLVER V2 - Primitive-Based Evolution")
        print("="*70)

        # Create complex seeds if library is empty
        if len(self.game_library) == 0:
            await self.run_task(
                self.create_complex_seed_games,
                "create_complex_seeds"
            )

        # Evolve new game using primitives
        new_game = await self.run_task(
            self.evolve_primitive_game,
            "evolve_primitive_game"
        )

        if new_game:
            # Evaluate the new game
            await self.run_task(
                self.evaluate_game(new_game),
                "evaluate_game"
            )

        # Print stats
        print("\n" + "="*70)
        print(f"📈 EVOLUTION STATS")
        print("="*70)
        print(f"  Total Games: {len(self.game_library)}")
        print(f"  Current Generation: {self.generation_count}")

        if self.game_library:
            avg_fitness = sum(g.fitness_score for g in self.game_library.values()) / len(self.game_library)
            max_fitness = max(g.fitness_score for g in self.game_library.values())
            print(f"  Average Fitness: {avg_fitness:.2f}")
            print(f"  Max Fitness: {max_fitness:.2f}")

            # Primitive diversity
            all_primitives = set()
            for genome in self.game_library.values():
                for prims in genome.primitives.values():
                    all_primitives.update(prims)
            print(f"  Primitive Diversity: {len(all_primitives)} unique primitives in use")

            # Show top 3 games
            top_games = sorted(
                self.game_library.items(),
                key=lambda x: x[1].fitness_score,
                reverse=True
            )[:3]
            print(f"\n  🏆 Top Games:")
            for name, genome in top_games:
                prim_count = sum(len(v) for v in genome.primitives.values())
                print(f"    {name}: {genome.fitness_score:.2f} (gen {genome.generation}, {prim_count} primitives)")

        self.print_stats()
        print("="*70)

        # Generate visualizations
        print("\n📊 Generating evolution visualizations...")
        try:
            import subprocess
            subprocess.run([
                'python3',
                str(self.pod_root / 'evolution_visualizer.py')
            ], check=True, capture_output=True)
            print("   ✓ Visualizations updated!")
        except Exception as e:
            print(f"   ⚠️  Visualization generation failed: {e}")


async def main():
    """Main entry point"""
    evolver = EmberGameEvolverV2()
    await evolver.run_evolution_cycle()


if __name__ == '__main__':
    asyncio.run(main())
