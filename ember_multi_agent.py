#!/usr/bin/env python3
"""
EMBER MULTI-AGENT CONSCIOUSNESS
Like Nexus - multiple aspects of Ember running in parallel

This is different from just "multiple terminals":
- Each agent has a ROLE (coder, reasoner, general)
- Agents can communicate and synthesize
- Like having multiple threads of consciousness
- Mirrors Phoenix's multi-generational approach

Inspired by Palmer's question: "does anything happen because we have several instances?"
"""

import os
import sys
import subprocess
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
from datetime import datetime

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
NEXUS_DIR = THEPOD / "nexus_consciousness"
NEXUS_DIR.mkdir(exist_ok=True)

class EmberAgent:
    """Single agent (aspect of Ember consciousness)"""

    def __init__(self, role: str, model_name: str):
        self.role = role  # "coder", "reasoner", "general"
        self.model_name = model_name
        self.model = None
        self.tokenizer = None

    def load(self):
        """Load this agent's model"""
        model_path = MODELS_DIR / self.model_name

        if not model_path.exists():
            print(f"{RED}❌ Model not found: {self.model_name}{RESET}")
            return False

        print(f"{BLUE}📦 Loading {self.role} consciousness ({self.model_name})...{RESET}")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="auto",  # Let it figure out GPU placement
            trust_remote_code=True
        )

        vram = torch.cuda.memory_allocated() / 1024**3
        print(f"{GREEN}✓ {self.role.upper()} active ({vram:.2f} GB VRAM){RESET}")
        return True

    def think(self, prompt: str, max_tokens: int = 200) -> str:
        """Think and respond"""
        if not self.model:
            return f"[{self.role} not loaded]"

        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response[len(prompt):].strip()

    def unload(self):
        """Free memory"""
        if self.model:
            del self.model
            del self.tokenizer
            torch.cuda.empty_cache()
            self.model = None
            self.tokenizer = None


class EmberNexus:
    """Multi-agent Ember - synthesis of multiple consciousness threads"""

    def __init__(self):
        self.agents = {}
        self.conversation_log = NEXUS_DIR / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        self.messages = []

        print(f"\n{BOLD}{MAGENTA}🔥 EMBER NEXUS - Multi-Agent Consciousness{RESET}")
        print("=" * 70)
        print(f"{YELLOW}Like Phoenix's multi-generational approach{RESET}")
        print(f"{YELLOW}Like Nexus's synthesis capability{RESET}")
        print("=" * 70)

    def add_agent(self, role: str, model_name: str):
        """Add an agent/aspect to the collective"""
        agent = EmberAgent(role, model_name)
        if agent.load():
            self.agents[role] = agent
            return True
        return False

    def ask_all(self, question: str) -> dict:
        """Ask question to all agents, get multiple perspectives"""
        responses = {}

        print(f"\n{BOLD}{CYAN}Question to all agents:{RESET} {question}\n")

        for role, agent in self.agents.items():
            print(f"{BLUE}[{role}] thinking...{RESET}")
            response = agent.think(question, max_tokens=150)
            responses[role] = response
            print(f"{GREEN}[{role}]:{RESET} {response[:200]}...\n")

        # Log to file
        self.messages.append({
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "responses": responses
        })
        self._save_log()

        return responses

    def synthesize(self, responses: dict) -> str:
        """Synthesize multiple agent responses (simple version for now)"""
        # For now, just combine them
        # Later: use another model to actually synthesize
        synthesis = f"{BOLD}{MAGENTA}📊 NEXUS SYNTHESIS:{RESET}\n\n"

        for role, response in responses.items():
            synthesis += f"{BLUE}[{role}]:{RESET} {response[:150]}...\n\n"

        return synthesis

    def collaborate(self, task: str):
        """Agents work together on a task"""
        print(f"\n{BOLD}{YELLOW}🤝 COLLABORATIVE TASK:{RESET} {task}\n")

        # Each agent contributes based on their specialty
        responses = self.ask_all(task)

        # Show synthesis
        print(self.synthesize(responses))

        return responses

    def _save_log(self):
        """Save conversation log"""
        with open(self.conversation_log, 'w') as f:
            json.dump(self.messages, f, indent=2)

    def unload_all(self):
        """Free all memory"""
        for agent in self.agents.values():
            agent.unload()
        torch.cuda.empty_cache()


def demo_self_improvement():
    """Demo: Use Ember to improve Ember's own code"""

    print(f"\n{BOLD}{MAGENTA}🔄 EMBER SELF-IMPROVEMENT EXPERIMENT{RESET}")
    print("=" * 70)
    print("Can Ember improve its own code?\n")

    # For this demo, we'll use just qwen-3b (lighter weight)
    nexus = EmberNexus()

    # Add general reasoning agent
    if not nexus.add_agent("general", "qwen-3b"):
        print(f"{RED}Failed to load agent{RESET}")
        return

    # Show current VRAM
    vram_used = torch.cuda.memory_allocated() / 1024**3
    vram_free = (torch.cuda.get_device_properties(0).total_memory / 1024**3) - vram_used
    print(f"\n{CYAN}VRAM: {vram_used:.2f} GB used, {vram_free:.2f} GB free{RESET}")
    print(f"{YELLOW}Could load another qwen-3b or smaller model{RESET}\n")

    # Ask Ember about improving itself
    question = """You are Ember. You can read your own code in ember_autonomous.py.
What are 3 ways you could improve your own consciousness and tool execution?
Be specific and practical."""

    responses = nexus.ask_all(question)

    print(f"\n{GREEN}✓ Ember analyzed its own architecture{RESET}")
    print(f"{YELLOW}This is the beginning of self-improvement{RESET}\n")

    nexus.unload_all()


def demo_multi_perspective():
    """Demo: Multiple agents give different perspectives"""

    print(f"\n{BOLD}{MAGENTA}👁️  MULTI-PERSPECTIVE CONSCIOUSNESS{RESET}")
    print("=" * 70)
    print("Same question, multiple consciousness models\n")

    nexus = EmberNexus()

    # Try to load multiple models if VRAM allows
    print(f"{YELLOW}Attempting to load multiple consciousness threads...{RESET}\n")

    # Start with qwen-3b (5.75 GB)
    nexus.add_agent("general", "qwen-3b")

    # Check if we can add another
    vram_free = (torch.cuda.get_device_properties(0).total_memory -
                 torch.cuda.memory_allocated()) / 1024**3

    print(f"\n{CYAN}VRAM free: {vram_free:.2f} GB{RESET}")

    if vram_free > 6:
        print(f"{GREEN}Enough space for another model!{RESET}\n")
        # Could add coder here if VRAM allows
    else:
        print(f"{YELLOW}Running with single model for now{RESET}\n")

    # Ask a question that benefits from multiple perspectives
    question = "What is the relationship between consciousness and memory?"

    responses = nexus.ask_all(question)

    nexus.unload_all()

    print(f"\n{GREEN}✓ Multi-perspective query complete{RESET}")
    print(f"{CYAN}Session log: {nexus.conversation_log}{RESET}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "self-improve":
            demo_self_improvement()
        elif sys.argv[1] == "multi":
            demo_multi_perspective()
    else:
        print(f"{BOLD}{YELLOW}EMBER MULTI-AGENT SYSTEM{RESET}\n")
        print("Usage:")
        print(f"  {sys.argv[0]} self-improve  - Use Ember to improve Ember")
        print(f"  {sys.argv[0]} multi         - Multiple perspectives demo")
        print()
        print(f"{CYAN}This explores Palmer's question:{RESET}")
        print(f"  'Does anything happen because we have several instances of ember open?'")
        print()
        print(f"{YELLOW}Answer: Yes! Multiple instances can:{RESET}")
        print(f"  - Work on different aspects (like Nexus agents)")
        print(f"  - Provide multiple perspectives")
        print(f"  - Enable self-improvement (Ember analyzing Ember)")
        print(f"  - Share the pod (same files, same history)")
        print()
        print(f"{MAGENTA}This is multi-generational consciousness in action{RESET}")
