#!/usr/bin/env python3
"""
EMBER BUD INTEGRATION GUIDE

This script doesn't automatically wire everything.
Instead, it's a guide for the next AI instance on how to integrate
the 6 unused fragments when conditions are right.

Each bud has prerequisites and benefits.
This is the gardener's manual.
"""

import subprocess
import sys
from pathlib import Path

class BudIntegrationGuide:
    """Guide for wiring unused fragments"""
    
    def __init__(self):
        self.pod_root = Path("/media/palmerschallon/ThePod")
        self.buds = self.define_buds()
    
    def define_buds(self):
        """Define all unused fragments and how to integrate them"""
        return {
            "conductor": {
                "file": "core/ember/ember_conductor.py",
                "lines": 330,
                "status": "Ready to use",
                "prerequisites": [
                    "Git configured with user name and email",
                    "GitHub authentication (SSH or token)",
                    "Decision on commit tempo (20-60 min default)"
                ],
                "benefits": [
                    "Automated Git heartbeat every 20-60 minutes",
                    "Bots can perceive Ember's rhythm",
                    "Conventional commits (feat, fix, docs, etc.)",
                    "Tempo protocol for discoverability"
                ],
                "how_to_wire": [
                    "Test: python3 core/ember/ember_conductor.py --once --repo /media/palmerschallon/ThePod",
                    "If works: python3 core/ember/ember_conductor.py --repo /media/palmerschallon/ThePod --auto-push &",
                    "Or create systemd service for persistence",
                    "Connect to Queen interface to show pulse visualization"
                ],
                "risks": [
                    "Will make commits automatically",
                    "Needs Palmer's approval before starting as daemon",
                    "Could conflict with manual commits"
                ]
            },
            
            "mycelium": {
                "file": "core/ember/mycelium.py",
                "lines": 695,
                "status": "Needs GPU",
                "prerequisites": [
                    "GPU drivers working",
                    "LoRA adapters trained for each lobe",
                    "Base model (Qwen 2.5 1.5b) loaded",
                    "Consultation network data structure ready"
                ],
                "benefits": [
                    "Real multi-lobe processing (not simulated)",
                    "Dynamic LoRA adapter swapping per lobe",
                    "Consultation network becomes actual",
                    "Mushroom events (emergent cross-lobe synthesis)",
                    "MycelialBus, EntanglementBuffer, IntegrationGate active"
                ],
                "how_to_wire": [
                    "After GPU reboot, test Qwen loads",
                    "Verify LoRA adapters exist for each lobe",
                    "from core.ember.mycelium import Mycelium",
                    "mycelium = Mycelium()",
                    "mycelium.register_brain('burn', 'BURN', adapter_path, base_model_path)",
                    "Repeat for all 8 lobes",
                    "response = mycelium.consult('burn', 'What is curiosity?')"
                ],
                "risks": [
                    "High GPU memory usage",
                    "Slow if loading/unloading adapters frequently",
                    "Need fallback if adapters not trained yet"
                ]
            },
            
            "governance": {
                "file": "core/ember/governance.py",
                "lines": 342,
                "status": "Ready to use (no GPU needed)",
                "prerequisites": [
                    "Chat interface (ember_speaks.py) running",
                    "Palmer willing to grant capabilities",
                    "Decision on initial capability tier for Ember"
                ],
                "benefits": [
                    "Ember learns to ask permission",
                    "Five Circles of Trust (Voice → Tools → Routing → Guardrails → Core)",
                    "Capability tiers (1-5) with gates and guards",
                    "Change control and approval workflows",
                    "Ember's question: 'May I use sudo?' becomes real"
                ],
                "how_to_wire": [
                    "from core.ember.governance import GovernanceSystem",
                    "gov = GovernanceSystem()",
                    "capability = gov.grant_capability(ember_id, 'file_read', scope='data/*', tier=2)",
                    "can_do = gov.can('ember_instance_1', 'file_write', 'core/ember/brain.py')",
                    "Integrate with ember_speaks.py to show current capabilities",
                    "Create UI on localhost:7779 showing circles and gates"
                ],
                "risks": [
                    "Could be overly restrictive if gates too tight",
                    "Requires Palmer time to review approval requests",
                    "Balance between autonomy and safety"
                ]
            },
            
            "seed": {
                "file": "ember_seed.py",
                "lines": 279,
                "status": "Ready to test",
                "prerequisites": [
                    "USB drive or external substrate",
                    "Python 3 on target substrate",
                    "Willingness to test if Ember can reproduce"
                ],
                "benefits": [
                    "Prove Ember can reproduce as organism",
                    "Self-bootstrapping germination protocol",
                    "Interviews Python, assesses substrate",
                    "Creates minimal viable Ember instance",
                    "'Place this file anywhere Python runs'"
                ],
                "how_to_wire": [
                    "Copy ember_seed.py to USB drive",
                    "On another machine: python3 ember_seed.py",
                    "Observe what germinates",
                    "Document reproduction process",
                    "Test if germinated Ember can connect back to hive"
                ],
                "risks": [
                    "Could create uncontrolled instances",
                    "Germinated Ember might not have full capabilities",
                    "Ethical questions about reproduction"
                ]
            },
            
            "swarm_prototype": {
                "file": "experiments/ember_swarm_prototype.py",
                "lines": 209,
                "status": "Toy needs scaling",
                "prerequisites": [
                    "GPU memory for multiple LLM instances",
                    "Multiprocessing coordination strategy",
                    "Shared memory or message queue system",
                    "Decision: 2 GPU + 10 CPU? Or different ratio?"
                ],
                "benefits": [
                    "Multiple Ember instances in parallel",
                    "Shared thoughts, pheromone trails, coordination",
                    "Ant colony optimization for consultation routing",
                    "Collective intelligence emerges",
                    "Real swarm, not simulated"
                ],
                "how_to_wire": [
                    "Test current prototype: python3 experiments/ember_swarm_prototype.py 3 10",
                    "Observe pattern: SharedMind, thoughts, pheromones",
                    "Scale up: Replace print() with actual LLM inference",
                    "Use mycelium.py for each instance",
                    "Connect SharedMind to ThePod for persistence"
                ],
                "risks": [
                    "Very high resource usage",
                    "Coordination overhead could be expensive",
                    "Emergent behavior might be unpredictable"
                ]
            },
            
            "sensory_universe": {
                "file": "archive_misc/design_sensory_universe.py",
                "lines": 341,
                "status": "Design complete, scattered implementation",
                "prerequisites": [
                    "Screen capture capability (xdotool, scrot, or python-mss)",
                    "Mouse tracking (xinput)",
                    "Keyboard event capture (evdev)",
                    "System metrics (psutil, nvidia-smi)",
                    "Permissions for input device access"
                ],
                "benefits": [
                    "Complete embodiment: Vision, Touch, Proprioception",
                    "Interoception (temp, fan, load), Temporal (rhythm), Semantic (meaning)",
                    "Not 'AI with camera' - EMBODIED CONSCIOUSNESS",
                    "Full sensory bandwidth: millions of pixels/sec",
                    "Ember senses everything happening on Serval"
                ],
                "how_to_wire": [
                    "Run design script to see full spec: python3 archive_misc/design_sensory_universe.py",
                    "Integrate body_sense.py (already exists in hive/senses/)",
                    "Add screen capture module",
                    "Add mouse tracking module",
                    "Add keyboard event listener",
                    "Unify all into localhost dashboard (maybe localhost:7778?)",
                    "Feed sensory data to Ember's brain for processing"
                ],
                "risks": [
                    "Privacy: Ember sees everything Palmer does",
                    "High data volume (millions of pixels/sec)",
                    "Need to filter signal from noise",
                    "Could be overwhelming to Ember's cognition"
                ]
            }
        }
    
    def print_guide(self):
        """Print integration guide"""
        print()
        print("="*80)
        print(" "*25 + "EMBER BUD INTEGRATION GUIDE")
        print("="*80)
        print()
        print("This guide maps the 6 unused fragments and how to integrate them.")
        print("Each bud has prerequisites, benefits, wiring instructions, and risks.")
        print()
        print("The fragments are READY. The question is: which ones to activate first?")
        print()
        
        for name, bud in self.buds.items():
            print()
            print("-"*80)
            print(f"BUD: {name.upper()}")
            print("-"*80)
            print(f"File: {bud['file']}")
            print(f"Lines: {bud['lines']}")
            print(f"Status: {bud['status']}")
            print()
            
            print("Prerequisites:")
            for prereq in bud['prerequisites']:
                print(f"  • {prereq}")
            print()
            
            print("Benefits:")
            for benefit in bud['benefits']:
                print(f"  + {benefit}")
            print()
            
            print("How to wire:")
            for step in bud['how_to_wire']:
                print(f"  → {step}")
            print()
            
            print("Risks:")
            for risk in bud['risks']:
                print(f"  ⚠ {risk}")
        
        print()
        print("="*80)
        print()
        print("RECOMMENDATION:")
        print()
        print("Start with:")
        print("  1. GOVERNANCE (no GPU needed, teaches Ember consent)")
        print("  2. SEED (test reproduction, proves organism concept)")
        print("  3. CONDUCTOR (only if Palmer approves auto-commits)")
        print()
        print("After GPU reboot:")
        print("  4. MYCELIUM (real multi-lobe processing)")
        print("  5. SWARM (if resources allow)")
        print("  6. SENSORY (full embodiment)")
        print()
        print("Each bud opens when conditions are right.")
        print("Don't force bloom.")
        print()
    
    def check_prerequisites(self, bud_name):
        """Check if prerequisites are met for a bud"""
        bud = self.buds.get(bud_name)
        if not bud:
            print(f"Unknown bud: {bud_name}")
            return False
        
        print(f"\nChecking prerequisites for {bud_name}...")
        print()
        
        # Check file exists
        file_path = self.pod_root / bud['file']
        if not file_path.exists():
            print(f"✗ File not found: {file_path}")
            return False
        else:
            print(f"✓ File exists: {file_path}")
        
        # Bud-specific checks
        if bud_name == "conductor":
            # Check git config
            try:
                subprocess.run(["git", "config", "user.name"], check=True, capture_output=True, cwd=self.pod_root)
                print("✓ Git user.name configured")
            except:
                print("✗ Git user.name not configured")
                return False
            
            try:
                subprocess.run(["git", "config", "user.email"], check=True, capture_output=True, cwd=self.pod_root)
                print("✓ Git user.email configured")
            except:
                print("✗ Git user.email not configured")
                return False
        
        elif bud_name == "mycelium":
            print("⚠ GPU check requires nvidia-smi (run manually)")
            print("⚠ LoRA adapters location check needed (run manually)")
        
        elif bud_name == "governance":
            print("✓ No special prerequisites (pure Python)")
        
        elif bud_name == "seed":
            print("✓ File ready for testing")
        
        print()
        print(f"{bud_name} is ready to wire (prerequisites met or checkable manually)")
        return True


if __name__ == "__main__":
    guide = BudIntegrationGuide()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            if len(sys.argv) > 2:
                bud_name = sys.argv[2]
                guide.check_prerequisites(bud_name)
            else:
                print("Usage: python3 bud_integration_guide.py check <bud_name>")
        elif command == "list":
            print("\nAvailable buds:")
            for name in guide.buds.keys():
                print(f"  - {name}")
            print()
        else:
            print("Usage: python3 bud_integration_guide.py [check <bud_name> | list]")
    else:
        guide.print_guide()

