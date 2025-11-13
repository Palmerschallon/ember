#!/usr/bin/env python3
"""
EMBER GAME EVOLVER
==================
LLM-powered autonomous game evolution system

Instead of templates, this uses Claude (via Ember) to:
- Understand game mechanics semantically
- Generate entirely new game code
- Combine concepts creatively
- Evolve toward complexity and fun

Evolution path: Pong → Breakout → Roguelikes → Indie games
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import hashlib
import random

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener
from ember_complete import Ember


class GameGenome:
    """High-level semantic representation of a game"""

    def __init__(self):
        self.core_mechanics = []  # ["paddle_movement", "ball_physics"]
        self.systems = []  # ["scoring", "collision", "lives"]
        self.complexity_features = []  # ["power_ups", "levels", "enemies"]
        self.tech_stack = []  # ["canvas", "webgl", "three.js"]
        self.generation = 0
        self.parent_games = []
        self.fitness_score = 0.0
        self.innovation_score = 0.0

    def to_dict(self) -> Dict:
        return {
            'core_mechanics': self.core_mechanics,
            'systems': self.systems,
            'complexity_features': self.complexity_features,
            'tech_stack': self.tech_stack,
            'generation': self.generation,
            'parent_games': self.parent_games,
            'fitness_score': self.fitness_score,
            'innovation_score': self.innovation_score
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'GameGenome':
        genome = cls()
        genome.core_mechanics = data.get('core_mechanics', [])
        genome.systems = data.get('systems', [])
        genome.complexity_features = data.get('complexity_features', [])
        genome.tech_stack = data.get('tech_stack', [])
        genome.generation = data.get('generation', 0)
        genome.parent_games = data.get('parent_games', [])
        genome.fitness_score = data.get('fitness_score', 0.0)
        genome.innovation_score = data.get('innovation_score', 0.0)
        return genome


class EmberGameEvolver(ResilientGardener):
    """LLM-powered game evolution system"""

    def __init__(self):
        super().__init__('game_evolver', pod_root='/media/palmerschallon/ThePod1')

        self.games_dir = self.pod_root / 'evolved_games'
        self.games_dir.mkdir(exist_ok=True)

        self.library_path = self.games_dir / 'game_library.json'
        self.evolution_log = self.games_dir / 'evolution_log.jsonl'

        self.ember = Ember()
        self.game_library: Dict[str, GameGenome] = {}
        self.generation_count = 0

        self._load_library()

    def _load_library(self):
        """Load existing game library"""
        if self.library_path.exists():
            try:
                data = json.loads(self.library_path.read_text())
                self.generation_count = data.get('_generation_count', 0)
                for name, genome_dict in data.items():
                    if name != '_generation_count':
                        self.game_library[name] = GameGenome.from_dict(genome_dict)
                print(f"  ✓ Loaded {len(self.game_library)} games, generation {self.generation_count}")
            except Exception as e:
                print(f"  ⚠️  Failed to load library: {e}")

    def _save_library(self):
        """Save game library"""
        data = {name: genome.to_dict() for name, genome in self.game_library.items()}
        data['_generation_count'] = self.generation_count
        self.write_file_directly(self.library_path, json.dumps(data, indent=2))

    def _log_evolution(self, event: Dict):
        """Log evolution event"""
        event['timestamp'] = datetime.now().isoformat()
        with open(self.evolution_log, 'a') as f:
            f.write(json.dumps(event) + '\n')

    async def create_seed_games(self):
        """Create initial seed games using Ember"""
        print("\n🌱 Creating seed games...")

        seed_concepts = [
            {
                'name': 'pong_genesis',
                'concept': 'Classic Pong - two paddles, bouncing ball, score tracking. Clean and simple.',
                'mechanics': ['paddle_movement', 'ball_physics', 'wall_bounce'],
                'systems': ['scoring', 'collision_detection']
            },
            {
                'name': 'breakout_genesis',
                'concept': 'Breakout - paddle, ball, breakable bricks. Add satisfying brick destruction.',
                'mechanics': ['paddle_movement', 'ball_physics', 'brick_collision'],
                'systems': ['scoring', 'level_completion', 'lives']
            },
            {
                'name': 'snake_genesis',
                'concept': 'Snake - growing snake, food collection, self-collision. Addictive gameplay.',
                'mechanics': ['snake_movement', 'growth', 'grid_navigation'],
                'systems': ['food_spawning', 'collision_detection', 'score_based_speed']
            }
        ]

        for seed in seed_concepts:
            if seed['name'] in self.game_library:
                print(f"  ⏭  {seed['name']} already exists")
                continue

            print(f"  🎮 Creating {seed['name']}...")

            prompt = f"""Create a complete, playable HTML5 game: {seed['concept']}

Requirements:
- Single standalone HTML file with embedded CSS and JavaScript
- Use HTML5 Canvas for rendering
- Smooth 60fps gameplay
- Keyboard controls (arrow keys or WASD)
- Score display
- Game over / restart logic
- Clean, readable code with comments
- Modern, attractive visual style

Make it FUN and polished. This is generation 0 - the foundation for evolution.

Return ONLY the complete HTML code, starting with <!DOCTYPE html>"""

            try:
                game_code = await self.ember.chat(prompt)

                # Save game file
                game_path = self.games_dir / f"{seed['name']}.html"
                self.write_file_directly(game_path, game_code)

                # Create genome
                genome = GameGenome()
                genome.core_mechanics = seed['mechanics']
                genome.systems = seed['systems']
                genome.tech_stack = ['canvas', 'html5']
                genome.generation = 0
                genome.parent_games = []
                genome.fitness_score = 0.5  # Baseline

                self.game_library[seed['name']] = genome

                self._log_evolution({
                    'event': 'seed_created',
                    'game': seed['name'],
                    'generation': 0
                })

                print(f"    ✓ Created {seed['name']}")

            except Exception as e:
                print(f"    ✗ Failed to create {seed['name']}: {e}")

        self._save_library()
        print(f"  ✓ Seed population: {len(self.game_library)} games")

    async def evolve_new_game(self):
        """Evolve a new game by combining existing games"""
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

        # Top 50% can be parents
        parent_pool = sorted_games[:max(2, len(sorted_games) // 2)]
        parent1_name, parent1 = random.choice(parent_pool)
        parent2_name, parent2 = random.choice(parent_pool)

        print(f"  🧬 Parents: {parent1_name} (gen {parent1.generation}) + {parent2_name} (gen {parent2.generation})")

        # Read parent game code
        parent1_code = (self.games_dir / f"{parent1_name}.html").read_text()
        parent2_code = (self.games_dir / f"{parent2_name}.html").read_text()

        # Ask Ember to evolve a new game
        prompt = f"""You are evolving games! Create a NEW game by combining the best aspects of these two games:

PARENT 1: {parent1_name}
Mechanics: {parent1.core_mechanics}
Systems: {parent1.systems}
Features: {parent1.complexity_features}
Generation: {parent1.generation}

PARENT 2: {parent2_name}
Mechanics: {parent2.core_mechanics}
Systems: {parent2.systems}
Features: {parent2.complexity_features}
Generation: {parent2.generation}

Your mission:
1. Analyze what makes each parent fun
2. Combine mechanics in an innovative way
3. Add ONE new complexity feature (examples: power-ups, multiple levels, enemies, procedural generation, etc.)
4. Make it more sophisticated than either parent
5. Ensure it's actually playable and fun

The child game should feel like a natural evolution - more complex but still cohesive.

Guidelines:
- Single HTML file, HTML5 Canvas
- Smooth 60fps gameplay
- Polish and juice (particles, screen shake, sound effects if possible)
- Clear win/lose conditions
- Attractive modern visual design

Generate a completely NEW game that inherits DNA from both parents but has its own identity.

Return ONLY the complete HTML code, starting with <!DOCTYPE html>"""

        try:
            game_code = await self.ember.chat(prompt)

            # Generate name
            self.generation_count += 1
            game_name = f"evolved_gen{self.generation_count}_{parent1_name[:10]}_{parent2_name[:10]}"
            game_path = self.games_dir / f"{game_name}.html"

            # Save game
            self.write_file_directly(game_path, game_code)

            # Create genome (inherit from parents)
            genome = GameGenome()
            genome.core_mechanics = list(set(parent1.core_mechanics + parent2.core_mechanics))
            genome.systems = list(set(parent1.systems + parent2.systems))
            genome.complexity_features = list(set(
                parent1.complexity_features + parent2.complexity_features
            ))
            genome.tech_stack = list(set(parent1.tech_stack + parent2.tech_stack))
            genome.generation = max(parent1.generation, parent2.generation) + 1
            genome.parent_games = [parent1_name, parent2_name]
            genome.fitness_score = 0.5  # Will be evaluated
            genome.innovation_score = 0.0

            self.game_library[game_name] = genome

            self._log_evolution({
                'event': 'evolution',
                'game': game_name,
                'parents': [parent1_name, parent2_name],
                'generation': genome.generation
            })

            self._save_library()

            print(f"  ✓ Evolved: {game_name}")
            print(f"    Generation: {genome.generation}")
            print(f"    Mechanics: {len(genome.core_mechanics)}")
            print(f"    Systems: {len(genome.systems)}")

            return game_name

        except Exception as e:
            print(f"  ✗ Evolution failed: {e}")
            return None

    async def evaluate_game(self, game_name: str):
        """Ask Ember to evaluate a game's quality"""
        print(f"\n📊 Evaluating {game_name}...")

        if game_name not in self.game_library:
            print("  ⚠️  Game not in library")
            return

        game_path = self.games_dir / f"{game_name}.html"
        if not game_path.exists():
            print("  ⚠️  Game file not found")
            return

        game_code = game_path.read_text()
        genome = self.game_library[game_name]

        prompt = f"""Evaluate this game's quality. Analyze the code and rate it:

Game: {game_name}
Generation: {genome.generation}
Mechanics: {genome.core_mechanics}
Systems: {genome.systems}

Rate the game on these criteria (0.0 to 1.0):
1. Code Quality - Is it well-structured and maintainable?
2. Gameplay Fun - Does it have engaging mechanics?
3. Polish - Visual appeal, smoothness, juice
4. Innovation - Does it do something interesting/unique?
5. Completeness - Is it a finished, playable game?

Return ONLY a JSON object:
{{
  "code_quality": 0.0-1.0,
  "gameplay_fun": 0.0-1.0,
  "polish": 0.0-1.0,
  "innovation": 0.0-1.0,
  "completeness": 0.0-1.0,
  "notes": "brief evaluation summary"
}}"""

        try:
            response = await self.ember.chat(prompt)

            # Parse evaluation
            # Try to extract JSON from response
            import re
            json_match = re.search(r'\{[^}]+\}', response, re.DOTALL)
            if json_match:
                eval_data = json.loads(json_match.group())

                # Calculate fitness
                fitness = (
                    eval_data['code_quality'] * 0.2 +
                    eval_data['gameplay_fun'] * 0.3 +
                    eval_data['polish'] * 0.2 +
                    eval_data['innovation'] * 0.2 +
                    eval_data['completeness'] * 0.1
                )

                genome.fitness_score = fitness
                genome.innovation_score = eval_data['innovation']

                self._save_library()

                print(f"  ✓ Fitness: {fitness:.2f}")
                print(f"    Innovation: {eval_data['innovation']:.2f}")
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
        """Run one complete evolution cycle"""
        print("\n" + "="*70)
        print("🎮 EMBER GAME EVOLVER - Evolution Cycle")
        print("="*70)

        # Create seeds if library is empty
        if len(self.game_library) == 0:
            await self.run_task(
                self.create_seed_games,
                "create_seeds"
            )

        # Evolve new game
        new_game = await self.run_task(
            self.evolve_new_game,
            "evolve_game"
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

            # Show top 3 games
            top_games = sorted(
                self.game_library.items(),
                key=lambda x: x[1].fitness_score,
                reverse=True
            )[:3]
            print(f"\n  🏆 Top Games:")
            for name, genome in top_games:
                print(f"    {name}: {genome.fitness_score:.2f} (gen {genome.generation})")

        self.print_stats()
        print("="*70)


async def main():
    """Main entry point"""
    evolver = EmberGameEvolver()
    await evolver.run_evolution_cycle()


if __name__ == '__main__':
    asyncio.run(main())
