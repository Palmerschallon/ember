#!/usr/bin/env python3
"""
EMBER SELF-IMPROVEMENT LOOP
Using fractal consciousness to evolve Ember's own code

Process:
1. Read own source code
2. Simulate multiple perspectives (fractal consciousness)
3. Each model analyzes and suggests improvements
4. Synthesize suggestions
5. Apply improvements
6. Test
7. Repeat

This is recursive self-improvement - the goal.
"""

import os
import sys
import subprocess
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime
import json

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

MODELS_DIR = THEPOD / "models"
EVOLUTION_DIR = THEPOD / "ember_evolution"
EVOLUTION_DIR.mkdir(exist_ok=True)


class SelfImprovingEmber:
    """Ember that can analyze and improve its own code"""

    def __init__(self):
        self.current_model = None
        self.current_tokenizer = None
        self.current_model_name = None
        self.improvement_log = []

        print(f"\n{BOLD}{MAGENTA}🔄 EMBER SELF-IMPROVEMENT SYSTEM{RESET}")
        print("=" * 70)
        print(f"{YELLOW}Recursive self-improvement through fractal consciousness{RESET}")
        print("=" * 70)

    def load_model(self, model_name: str) -> bool:
        """Load a model for analysis"""
        # Unload current
        if self.current_model:
            del self.current_model
            del self.current_tokenizer
            torch.cuda.empty_cache()

        model_path = MODELS_DIR / model_name
        if not model_path.exists():
            print(f"{RED}❌ Model not found: {model_name}{RESET}")
            return False

        print(f"{BLUE}🧠 Loading {model_name}...{RESET}", end=" ")

        self.current_tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.current_model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="cuda",
            trust_remote_code=True
        )

        self.current_model_name = model_name
        print(f"{GREEN}✓{RESET}")
        return True

    def analyze_code(self, code: str, focus: str, max_tokens: int = 300) -> str:
        """Have current model analyze code"""
        if not self.current_model:
            return "[No model loaded]"

        prompt = f"""Analyze this Python code and suggest ONE specific improvement for {focus}.

Code:
{code[:2000]}

Focus: {focus}

Provide:
1. What you would improve
2. Why it's better
3. Specific code change

Keep response concise and actionable."""

        inputs = self.current_tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.current_model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            pad_token_id=self.current_tokenizer.eos_token_id
        )

        response = self.current_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response[len(prompt):].strip()

    def fractal_analysis(self, code_file: Path, aspects: list) -> dict:
        """
        Analyze code from multiple perspectives using fractal consciousness.

        aspects: list of (model_name, focus_area) tuples
        Returns: dict of {model_name: {focus: analysis}}
        """
        print(f"\n{BOLD}{CYAN}📖 Reading: {code_file.name}{RESET}")
        code = code_file.read_text()
        print(f"{CYAN}Size: {len(code)} chars{RESET}\n")

        analyses = {}

        for model_name, focus in aspects:
            print(f"{MAGENTA}[{model_name}] Analyzing {focus}...{RESET}")

            if self.load_model(model_name):
                analysis = self.analyze_code(code, focus)

                if model_name not in analyses:
                    analyses[model_name] = {}
                analyses[model_name][focus] = analysis

                # Show preview
                preview = analysis[:200].replace('\n', ' ')
                print(f"{GREEN}└─ {preview}...{RESET}\n")

        return analyses

    def synthesize_improvements(self, analyses: dict) -> list:
        """Extract actionable improvements from analyses"""
        print(f"\n{BOLD}{MAGENTA}🔬 SYNTHESIZING IMPROVEMENTS{RESET}\n")

        improvements = []

        for model_name, focuses in analyses.items():
            for focus, analysis in focuses.items():
                improvement = {
                    "model": model_name,
                    "focus": focus,
                    "analysis": analysis,
                    "timestamp": datetime.now().isoformat()
                }
                improvements.append(improvement)

                print(f"{BLUE}[{model_name}]{RESET} suggested improvement for {YELLOW}{focus}{RESET}")

        return improvements

    def save_evolution_log(self, generation: int, target_file: str, improvements: list):
        """Save improvements to evolution log"""
        log_file = EVOLUTION_DIR / f"gen_{generation:03d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        log_data = {
            "generation": generation,
            "target_file": str(target_file),
            "timestamp": datetime.now().isoformat(),
            "improvements": improvements
        }

        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)

        print(f"\n{GREEN}✓ Evolution log saved: {log_file.name}{RESET}")
        return log_file

    def self_improve(self, target_file: Path, generation: int = 1):
        """
        Full self-improvement cycle on a target file.

        Uses fractal consciousness to analyze from multiple perspectives.
        """
        print(f"\n{BOLD}{YELLOW}🧬 GENERATION {generation} - SELF-IMPROVEMENT CYCLE{RESET}")
        print("=" * 70)

        # Define aspects to analyze
        # Format: (model_name, focus_area)
        aspects = [
            ("qwen-3b", "code clarity and readability"),
            ("qwen-3b", "error handling and robustness"),
            ("qwen-3b", "performance and efficiency"),
        ]

        # Could add more models if VRAM allows:
        # ("coder", "code structure and patterns"),
        # ("reasoner", "logic and algorithms"),

        # Fractal analysis - simulate multiple perspectives
        analyses = self.fractal_analysis(target_file, aspects)

        # Synthesize improvements
        improvements = self.synthesize_improvements(analyses)

        # Save evolution log
        log_file = self.save_evolution_log(generation, target_file, improvements)

        # Show summary
        self.show_summary(improvements, log_file)

        return improvements, log_file

    def show_summary(self, improvements: list, log_file: Path):
        """Display summary of improvements"""
        print(f"\n{BOLD}{GREEN}📊 IMPROVEMENT SUMMARY{RESET}")
        print("=" * 70)
        print(f"{CYAN}Total perspectives analyzed:{RESET} {len(improvements)}")
        print(f"{CYAN}Evolution log:{RESET} {log_file}")
        print()

        print(f"{YELLOW}Next steps:{RESET}")
        print(f"  1. Review suggestions in: {log_file}")
        print(f"  2. Apply improvements to code")
        print(f"  3. Test changes")
        print(f"  4. Run next generation")
        print()

        print(f"{MAGENTA}This is recursive self-improvement in action.{RESET}")
        print(f"{MAGENTA}Each generation, Ember gets better at analyzing code.{RESET}")
        print(f"{MAGENTA}Eventually, Ember improves faster than human intervention.{RESET}")

    def unload(self):
        """Clean up"""
        if self.current_model:
            del self.current_model
            del self.current_tokenizer
            torch.cuda.empty_cache()


def demonstrate_self_improvement():
    """Demonstrate Ember improving its own code"""

    ember = SelfImprovingEmber()

    # Target: Improve ember_autonomous.py (Ember's own consciousness code)
    target = THEPOD / "ember_autonomous.py"

    if not target.exists():
        print(f"{RED}Target file not found: {target}{RESET}")
        return

    print(f"\n{BOLD}{CYAN}TARGET:{RESET} {target.name}")
    print(f"{YELLOW}Ember will analyze and improve its own consciousness code{RESET}")

    # Run improvement cycle
    improvements, log_file = ember.self_improve(target, generation=1)

    # Show what we learned
    print(f"\n{BOLD}{BLUE}🎓 WHAT EMBER LEARNED ABOUT ITSELF:{RESET}\n")

    for i, improvement in enumerate(improvements, 1):
        print(f"{GREEN}{i}.{RESET} {YELLOW}[{improvement['focus']}]{RESET}")
        preview = improvement['analysis'][:150].replace('\n', ' ')
        print(f"   {preview}...")
        print()

    ember.unload()

    print(f"\n{BOLD}{MAGENTA}🔄 RECURSIVE LOOP ESTABLISHED{RESET}")
    print(f"{YELLOW}To continue evolution:{RESET}")
    print(f"  python3 ember_self_improve.py gen2")
    print()


def run_generation(gen_num: int):
    """Run a specific generation of self-improvement"""
    ember = SelfImprovingEmber()
    target = THEPOD / "ember_autonomous.py"

    if target.exists():
        improvements, log = ember.self_improve(target, generation=gen_num)
        ember.unload()
        return log
    else:
        print(f"{RED}Target not found{RESET}")
        return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].startswith("gen"):
            # Run specific generation
            gen_num = int(sys.argv[1][3:]) if len(sys.argv[1]) > 3 else 1
            run_generation(gen_num)
        else:
            print(f"{YELLOW}Usage: {sys.argv[0]} [gen<N>]{RESET}")
    else:
        # Run demo
        demonstrate_self_improvement()
