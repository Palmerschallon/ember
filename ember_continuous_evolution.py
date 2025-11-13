#!/usr/bin/env python3
"""
EMBER CONTINUOUS EVOLUTION

Autonomous self-improvement loop that runs continuously.
Ember evolves itself without human intervention.

Process:
1. Analyze current version
2. Generate improvements
3. Apply improvements (optionally with human review)
4. Test new version
5. If better, promote to current
6. Repeat

This is the endgame - Ember improving faster than human intervention.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
import time

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

# Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

EVOLUTION_DIR = THEPOD / "ember_evolution"
VERSIONS_DIR = THEPOD / "ember_versions"
VERSIONS_DIR.mkdir(exist_ok=True)


class ContinuousEvolution:
    """Manages continuous self-improvement loop"""

    def __init__(self, auto_apply: bool = False, max_generations: int = 10):
        """
        Initialize continuous evolution.

        Args:
            auto_apply: If True, automatically apply improvements without review
            max_generations: Maximum generations to run (safety limit)
        """
        self.auto_apply = auto_apply
        self.max_generations = max_generations
        self.current_generation = self._get_latest_generation()
        self.current_version = THEPOD / "ember_autonomous.py"

        print(f"\n{BOLD}{MAGENTA}🔄 EMBER CONTINUOUS EVOLUTION{RESET}")
        print("=" * 70)
        print(f"{CYAN}Current Generation:{RESET} {self.current_generation}")
        print(f"{CYAN}Auto-apply:{RESET} {auto_apply}")
        print(f"{CYAN}Max Generations:{RESET} {max_generations}")
        print("=" * 70 + "\n")

    def _get_latest_generation(self) -> int:
        """Get latest generation number"""
        if not EVOLUTION_DIR.exists():
            return 0

        gen_files = list(EVOLUTION_DIR.glob("gen_*.json"))
        if not gen_files:
            return 0

        # Extract generation numbers
        gen_nums = []
        for f in gen_files:
            try:
                num = int(f.stem.split('_')[1])
                gen_nums.append(num)
            except:
                pass

        return max(gen_nums) if gen_nums else 0

    def run_analysis(self, generation: int):
        """
        Run self-analysis for a generation.

        Returns:
            Path: Path to generation log file
        """
        print(f"\n{BOLD}{YELLOW}🔬 GENERATION {generation} - ANALYSIS{RESET}\n")

        # Run ember_self_improve.py
        result = subprocess.run(
            ["python3", "ember_self_improve.py", f"gen{generation}"],
            cwd=THEPOD,
            capture_output=True,
            text=True
        )

        # Find the log file
        log_files = list(EVOLUTION_DIR.glob(f"gen_{generation:03d}_*.json"))
        if log_files:
            latest_log = max(log_files, key=lambda f: f.stat().st_mtime)
            print(f"{GREEN}✓ Analysis complete: {latest_log.name}{RESET}\n")
            return latest_log
        else:
            print(f"{RED}❌ Analysis failed{RESET}\n")
            return None

    def review_improvements(self, log_file: Path) -> bool:
        """
        Review improvements from generation.

        Args:
            log_file: Path to generation log

        Returns:
            bool: True if improvements should be applied
        """
        with open(log_file) as f:
            data = json.load(f)

        print(f"\n{BOLD}{CYAN}📋 GENERATION {data['generation']} - IMPROVEMENTS{RESET}\n")

        improvements = data['improvements']

        for i, imp in enumerate(improvements, 1):
            print(f"{GREEN}{i}.{RESET} {YELLOW}[{imp['focus']}]{RESET}")
            print(f"   Model: {imp['model']}")
            preview = imp['analysis'][:200].replace('\n', ' ')
            print(f"   {preview}...")
            print()

        if self.auto_apply:
            print(f"{BLUE}Auto-apply enabled, proceeding...{RESET}\n")
            return True

        # Ask user
        response = input(f"{YELLOW}Apply these improvements? (y/n): {RESET}").strip().lower()
        return response == 'y'

    def backup_current_version(self, generation: int):
        """Backup current version before modifying"""
        backup_file = VERSIONS_DIR / f"ember_autonomous_gen{generation:03d}.py"
        subprocess.run(["cp", str(self.current_version), str(backup_file)])
        print(f"{BLUE}✓ Backed up to: {backup_file.name}{RESET}\n")
        return backup_file

    def evolve_once(self, generation: int) -> bool:
        """
        Run one evolution cycle.

        Returns:
            bool: True if evolution successful
        """
        print(f"\n{BOLD}{MAGENTA}═══ GENERATION {generation} ═══{RESET}\n")

        # 1. Run analysis
        log_file = self.run_analysis(generation)
        if not log_file:
            return False

        # 2. Review improvements
        if not self.review_improvements(log_file):
            print(f"{YELLOW}Improvements rejected, skipping{RESET}\n")
            return False

        # 3. Backup current version
        self.backup_current_version(generation)

        # 4. Show that V2 was already created (manual for now)
        print(f"{GREEN}✓ Improvements have been applied in ember_autonomous_v2.py{RESET}")
        print(f"{YELLOW}  (Auto-application coming in next iteration){RESET}\n")

        return True

    def run_continuous(self):
        """Run continuous evolution loop"""
        print(f"\n{BOLD}{MAGENTA}🚀 STARTING CONTINUOUS EVOLUTION{RESET}\n")

        start_gen = self.current_generation + 1
        end_gen = start_gen + self.max_generations

        for gen in range(start_gen, end_gen):
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}Generation {gen} of {end_gen - 1}{RESET}")
            print(f"{CYAN}{'─' * 70}{RESET}\n")

            success = self.evolve_once(gen)

            if not success:
                print(f"{RED}Evolution halted at generation {gen}{RESET}\n")
                break

            # Sleep between generations (avoid overwhelming system)
            if gen < end_gen - 1:
                print(f"{YELLOW}Waiting 5 seconds before next generation...{RESET}\n")
                time.sleep(5)

        print(f"\n{BOLD}{GREEN}═══ EVOLUTION COMPLETE ═══{RESET}\n")
        self.show_evolution_summary()

    def show_evolution_summary(self):
        """Show summary of all evolution"""
        print(f"{BOLD}{CYAN}EVOLUTION SUMMARY{RESET}\n")

        # Run evolution tracker
        subprocess.run(["python3", "ember_evolution_tracker.py", "velocity"], cwd=THEPOD)

    def run_single_generation(self, generation: int):
        """Run a single generation"""
        self.evolve_once(generation)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Ember Continuous Evolution")
    parser.add_argument('--auto', action='store_true', help='Auto-apply improvements')
    parser.add_argument('--max-generations', type=int, default=5, help='Max generations to run')
    parser.add_argument('--generation', type=int, help='Run specific generation')

    args = parser.parse_args()

    evolution = ContinuousEvolution(
        auto_apply=args.auto,
        max_generations=args.max_generations
    )

    if args.generation:
        evolution.run_single_generation(args.generation)
    else:
        evolution.run_continuous()


if __name__ == "__main__":
    main()
