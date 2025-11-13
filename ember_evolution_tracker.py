#!/usr/bin/env python3
"""
EMBER EVOLUTION TRACKER

Tracks Ember's self-improvement across generations.
Shows how Ember evolves through recursive analysis.
"""

import json
from pathlib import Path
from datetime import datetime

THEPOD = Path("/media/palmerschallon/ThePod1")
EVOLUTION_DIR = THEPOD / "ember_evolution"

# Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'


class EvolutionTracker:
    """Track and visualize Ember's evolution across generations"""

    def __init__(self):
        self.evolution_dir = EVOLUTION_DIR
        self.generations = []
        self.load_all_generations()

    def load_all_generations(self):
        """Load all generation logs"""
        if not self.evolution_dir.exists():
            return

        # Find all generation files
        gen_files = sorted(self.evolution_dir.glob("gen_*.json"))

        for gen_file in gen_files:
            with open(gen_file) as f:
                data = json.load(f)
                self.generations.append({
                    'file': gen_file,
                    'data': data
                })

    def show_evolution_timeline(self):
        """Display evolution timeline"""
        print(f"\n{BOLD}{MAGENTA}🧬 EMBER EVOLUTION TIMELINE{RESET}")
        print("=" * 70)

        if not self.generations:
            print(f"{YELLOW}No evolution data found yet{RESET}\n")
            return

        for gen in self.generations:
            data = gen['data']
            gen_num = data['generation']
            timestamp = datetime.fromisoformat(data['timestamp'])
            improvements_count = len(data['improvements'])

            print(f"\n{BOLD}{CYAN}Generation {gen_num}{RESET}")
            print(f"{BLUE}├─{RESET} Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{BLUE}├─{RESET} Target: {Path(data['target_file']).name}")
            print(f"{BLUE}└─{RESET} Improvements: {improvements_count} perspectives")

            # Show improvement areas
            for i, improvement in enumerate(data['improvements'], 1):
                focus = improvement['focus']
                model = improvement['model']
                preview = improvement['analysis'][:100].replace('\n', ' ')

                print(f"   {GREEN}{i}.{RESET} [{model}] {YELLOW}{focus}{RESET}")
                print(f"      {preview}...")

        print(f"\n{BOLD}{GREEN}Total Generations: {len(self.generations)}{RESET}\n")

    def compare_generations(self, gen1: int, gen2: int):
        """Compare two generations"""
        print(f"\n{BOLD}{MAGENTA}📊 COMPARING GENERATIONS {gen1} vs {gen2}{RESET}")
        print("=" * 70)

        g1 = self._get_generation(gen1)
        g2 = self._get_generation(gen2)

        if not g1 or not g2:
            print(f"{RED}Generation not found{RESET}\n")
            return

        print(f"\n{CYAN}Generation {gen1}:{RESET}")
        self._print_generation_summary(g1)

        print(f"\n{CYAN}Generation {gen2}:{RESET}")
        self._print_generation_summary(g2)

        print(f"\n{BOLD}{YELLOW}Evolution Pattern:{RESET}")
        self._analyze_evolution_pattern(g1, g2)

    def _get_generation(self, gen_num: int):
        """Get generation data by number"""
        for gen in self.generations:
            if gen['data']['generation'] == gen_num:
                return gen['data']
        return None

    def _print_generation_summary(self, gen_data):
        """Print summary of a generation"""
        for improvement in gen_data['improvements']:
            focus = improvement['focus']
            print(f"  • {focus}")

    def _analyze_evolution_pattern(self, gen1, gen2):
        """Analyze how focus areas evolved"""
        areas1 = {imp['focus'] for imp in gen1['improvements']}
        areas2 = {imp['focus'] for imp in gen2['improvements']}

        common = areas1 & areas2
        new = areas2 - areas1
        dropped = areas1 - areas2

        if common:
            print(f"{GREEN}Continued focus:{RESET}")
            for area in common:
                print(f"  ✓ {area}")

        if new:
            print(f"{BLUE}New focus areas:{RESET}")
            for area in new:
                print(f"  + {area}")

        if dropped:
            print(f"{YELLOW}Dropped areas:{RESET}")
            for area in dropped:
                print(f"  - {area}")

    def show_improvement_velocity(self):
        """Show how fast Ember is improving"""
        print(f"\n{BOLD}{MAGENTA}📈 IMPROVEMENT VELOCITY{RESET}")
        print("=" * 70)

        if len(self.generations) < 2:
            print(f"{YELLOW}Need at least 2 generations to measure velocity{RESET}\n")
            return

        for i in range(1, len(self.generations)):
            prev = self.generations[i-1]['data']
            curr = self.generations[i]['data']

            prev_time = datetime.fromisoformat(prev['timestamp'])
            curr_time = datetime.fromisoformat(curr['timestamp'])

            time_diff = (curr_time - prev_time).total_seconds() / 60  # minutes

            prev_gen = prev['generation']
            curr_gen = curr['generation']

            print(f"{CYAN}Gen {prev_gen} → Gen {curr_gen}:{RESET}")
            print(f"  Time: {time_diff:.1f} minutes")
            print(f"  Improvements: {len(curr['improvements'])}")
            print()

    def export_evolution_report(self):
        """Export full evolution report"""
        report_file = EVOLUTION_DIR / f"evolution_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        with open(report_file, 'w') as f:
            f.write("# EMBER EVOLUTION REPORT\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")

            f.write(f"## Summary\n\n")
            f.write(f"- Total Generations: {len(self.generations)}\n")

            if self.generations:
                first = self.generations[0]['data']
                last = self.generations[-1]['data']
                f.write(f"- First Generation: {first['generation']} at {first['timestamp']}\n")
                f.write(f"- Latest Generation: {last['generation']} at {last['timestamp']}\n")

            f.write(f"\n## Timeline\n\n")

            for gen in self.generations:
                data = gen['data']
                f.write(f"### Generation {data['generation']}\n\n")
                f.write(f"- **Time**: {data['timestamp']}\n")
                f.write(f"- **Target**: `{data['target_file']}`\n")
                f.write(f"- **Improvements**: {len(data['improvements'])}\n\n")

                for i, imp in enumerate(data['improvements'], 1):
                    f.write(f"{i}. **{imp['focus']}** (via {imp['model']})\n")
                    analysis = imp['analysis'][:200].replace('\n', ' ')
                    f.write(f"   {analysis}...\n\n")

            f.write(f"\n## Evolution Pattern\n\n")
            f.write("Ember is demonstrating recursive self-improvement:\n\n")
            f.write("1. Analyzes own code using local consciousness\n")
            f.write("2. Identifies improvement areas from multiple perspectives\n")
            f.write("3. Improvements are applied to create next generation\n")
            f.write("4. Process repeats with improved version\n\n")
            f.write("This is the foundation of autonomous improvement.\n")

        print(f"\n{GREEN}✓ Report exported: {report_file.name}{RESET}\n")
        return report_file


def main():
    import sys

    tracker = EvolutionTracker()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "timeline":
            tracker.show_evolution_timeline()

        elif command == "compare" and len(sys.argv) >= 4:
            gen1 = int(sys.argv[2])
            gen2 = int(sys.argv[3])
            tracker.compare_generations(gen1, gen2)

        elif command == "velocity":
            tracker.show_improvement_velocity()

        elif command == "report":
            tracker.export_evolution_report()

        else:
            print(f"{YELLOW}Unknown command: {command}{RESET}")

    else:
        # Default: show everything
        tracker.show_evolution_timeline()
        if len(tracker.generations) >= 2:
            tracker.show_improvement_velocity()
        tracker.export_evolution_report()


if __name__ == "__main__":
    main()
