#!/usr/bin/env python3
"""
EVOLUTION VISUALIZER
====================
Generates live visualizations of the game evolution system.

Outputs:
- Evolution tree (Graphviz)
- Fitness progression graphs (Matplotlib)
- Primitive usage heatmaps
- Generation statistics
"""

import json
import sys
from pathlib import Path
from typing import Dict, List
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter, defaultdict

sys.path.insert(0, '/media/palmerschallon/ThePod1')


class EvolutionVisualizer:
    """Generate visualizations from game library"""

    def __init__(self):
        self.pod_root = Path('/media/palmerschallon/ThePod1')
        self.library_path = self.pod_root / 'game_library_v2.json'
        self.output_dir = self.pod_root / 'evolution_viz'
        self.output_dir.mkdir(exist_ok=True)

    def load_library(self) -> Dict:
        """Load game library"""
        if not self.library_path.exists():
            return {'games': [], 'metadata': {'total_games': 0}}
        return json.loads(self.library_path.read_text())

    def generate_all(self):
        """Generate all visualizations"""
        print("📊 Generating evolution visualizations...")

        library = self.load_library()

        if not library['games']:
            print("   ⚠️  No games yet - creating empty visualizations")
            self.create_empty_visuals()
            return

        # Generate each visualization
        self.create_evolution_tree(library)
        self.create_fitness_graphs(library)
        self.create_primitive_heatmap(library)
        self.create_stats_json(library)

        print(f"   ✓ Visualizations saved to {self.output_dir}/")

    def create_empty_visuals(self):
        """Create placeholder visuals when no games exist"""
        # Empty stats
        stats = {
            'total_games': 0,
            'current_generation': 0,
            'avg_fitness': 0.0,
            'max_fitness': 0.0,
            'top_games': []
        }
        (self.output_dir / 'stats.json').write_text(json.dumps(stats, indent=2))

        # Empty tree
        (self.output_dir / 'evolution_tree.dot').write_text(
            'digraph Evolution {\n  label="No games yet - start evolution!"\n}\n'
        )

        # Empty graphs
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.text(0.5, 0.5, 'No data yet', ha='center', va='center', fontsize=20)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.savefig(self.output_dir / 'fitness_progression.png', dpi=150, bbox_inches='tight')
        plt.savefig(self.output_dir / 'primitive_heatmap.png', dpi=150, bbox_inches='tight')
        plt.close()

    def create_evolution_tree(self, library: Dict):
        """Generate Graphviz evolution tree"""
        print("   🌳 Creating evolution tree...")

        dot_lines = [
            'digraph Evolution {',
            '  rankdir=TB;',
            '  node [shape=box, style="rounded,filled", fontname="Arial"];',
            '  edge [color="#666666"];',
            ''
        ]

        # Add all games as nodes
        for game in library['games']:
            name = game['name']
            gen = game.get('generation', 0)
            fitness = game.get('fitness_score', 0.0)

            # Color by fitness
            if fitness >= 0.8:
                color = '#4ade80'  # Green
            elif fitness >= 0.6:
                color = '#fbbf24'  # Yellow
            else:
                color = '#f87171'  # Red

            label = f'{name}\\nGen {gen}\\nFit: {fitness:.2f}'
            dot_lines.append(f'  "{name}" [label="{label}", fillcolor="{color}"];')

        dot_lines.append('')

        # Add parent relationships
        for game in library['games']:
            name = game['name']
            parents = game.get('parent_games', [])
            for parent in parents:
                if parent:  # Skip empty parent names
                    dot_lines.append(f'  "{parent}" -> "{name}";')

        dot_lines.append('}')

        dot_content = '\n'.join(dot_lines)
        (self.output_dir / 'evolution_tree.dot').write_text(dot_content)

        # Try to render with Graphviz if available
        try:
            import subprocess
            subprocess.run([
                'dot', '-Tpng',
                str(self.output_dir / 'evolution_tree.dot'),
                '-o', str(self.output_dir / 'evolution_tree.png')
            ], check=True, capture_output=True)
            print("      ✓ Rendered evolution_tree.png")
        except:
            print("      ⚠️  Graphviz not available - saved .dot file only")

    def create_fitness_graphs(self, library: Dict):
        """Generate fitness progression graphs"""
        print("   📈 Creating fitness graphs...")

        # Group by generation
        gen_data = defaultdict(list)
        for game in library['games']:
            gen = game.get('generation', 0)
            fitness = game.get('fitness_score', 0.0)
            gen_data[gen].append(fitness)

        if not gen_data:
            return

        # Calculate stats per generation
        generations = sorted(gen_data.keys())
        avg_fitness = [sum(gen_data[g]) / len(gen_data[g]) for g in generations]
        max_fitness = [max(gen_data[g]) for g in generations]
        min_fitness = [min(gen_data[g]) for g in generations]

        # Create plot
        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(generations, avg_fitness, marker='o', linewidth=2, label='Average Fitness', color='#3b82f6')
        ax.plot(generations, max_fitness, marker='^', linewidth=2, label='Max Fitness', color='#10b981')
        ax.fill_between(generations, min_fitness, max_fitness, alpha=0.2, color='#6366f1')

        ax.set_xlabel('Generation', fontsize=12)
        ax.set_ylabel('Fitness Score', fontsize=12)
        ax.set_title('Evolution Fitness Progression', fontsize=14, fontweight='bold')
        ax.legend(loc='lower right')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.0)

        plt.tight_layout()
        plt.savefig(self.output_dir / 'fitness_progression.png', dpi=150, bbox_inches='tight')
        plt.close()

        print("      ✓ Saved fitness_progression.png")

    def create_primitive_heatmap(self, library: Dict):
        """Generate primitive usage heatmap"""
        print("   🎨 Creating primitive heatmap...")

        # Count primitive usage
        primitive_counts = defaultdict(lambda: defaultdict(int))

        for game in library['games']:
            primitives = game.get('primitives', {})
            for category, prims in primitives.items():
                for prim in prims:
                    primitive_counts[category][prim] += 1

        if not primitive_counts:
            return

        # Convert to matrix
        categories = sorted(primitive_counts.keys())
        all_prims = set()
        for cat_prims in primitive_counts.values():
            all_prims.update(cat_prims.keys())
        primitives = sorted(all_prims)

        matrix = []
        for prim in primitives:
            row = [primitive_counts[cat].get(prim, 0) for cat in categories]
            matrix.append(row)

        # Create heatmap
        fig, ax = plt.subplots(figsize=(10, max(8, len(primitives) * 0.3)))

        sns.heatmap(
            matrix,
            xticklabels=categories,
            yticklabels=primitives,
            cmap='YlOrRd',
            annot=True,
            fmt='d',
            cbar_kws={'label': 'Usage Count'},
            ax=ax
        )

        ax.set_title('Primitive Usage Across All Games', fontsize=14, fontweight='bold')
        ax.set_xlabel('Primitive Category', fontsize=12)
        ax.set_ylabel('Primitive Type', fontsize=12)

        plt.tight_layout()
        plt.savefig(self.output_dir / 'primitive_heatmap.png', dpi=150, bbox_inches='tight')
        plt.close()

        print("      ✓ Saved primitive_heatmap.png")

    def create_stats_json(self, library: Dict):
        """Generate stats for dashboard"""
        print("   📊 Creating stats.json...")

        games = library['games']

        if not games:
            stats = {
                'total_games': 0,
                'current_generation': 0,
                'avg_fitness': 0.0,
                'max_fitness': 0.0,
                'top_games': []
            }
        else:
            # Calculate stats
            total_games = len(games)
            current_generation = max(g.get('generation', 0) for g in games)
            fitness_scores = [g.get('fitness_score', 0.0) for g in games]
            avg_fitness = sum(fitness_scores) / len(fitness_scores)
            max_fitness = max(fitness_scores)

            # Top 10 games by fitness
            sorted_games = sorted(games, key=lambda g: g.get('fitness_score', 0.0), reverse=True)
            top_games = [
                {
                    'name': g['name'],
                    'fitness': g.get('fitness_score', 0.0),
                    'generation': g.get('generation', 0),
                    'primitives': g.get('primitives', {})
                }
                for g in sorted_games[:10]
            ]

            stats = {
                'total_games': total_games,
                'current_generation': current_generation,
                'avg_fitness': round(avg_fitness, 3),
                'max_fitness': round(max_fitness, 3),
                'top_games': top_games
            }

        (self.output_dir / 'stats.json').write_text(json.dumps(stats, indent=2))
        print("      ✓ Saved stats.json")


if __name__ == '__main__':
    visualizer = EvolutionVisualizer()
    visualizer.generate_all()
