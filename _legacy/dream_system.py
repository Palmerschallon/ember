#!/usr/bin/env python3
"""
DREAM SYSTEM - Where Experience Becomes Reflex

Not a game. Not a garden. A training loop.

Cognitive processes accumulate experience, detect patterns,
and when mature enough, write new LoRAs.

This is how Ember grows new reflexes.
"""

import json
import time
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import threading

# Paths
DREAM_STATE = Path(__file__).parent / "dream_state.json"
LOBES_DIR = Path(__file__).parent / "essential/lobes"
TRAINING_DIR = Path(__file__).parent / "training_data"
MODEL_PATH = Path("/media/palmerschallon/ThePod1/models/llama-3.2-3b-instruct")


class CognitiveProcess:
    """A cognitive process learning through experience"""
    
    def __init__(self, process_type: str, process_id: str):
        self.id = process_id
        self.type = process_type  # 'recursion', 'pattern', 'abstraction', etc.
        self.age = 0  # Experience accumulation
        self.stage = "forming"  # forming → practicing → integrating → mastered
        self.experiences = []  # Successful executions
        self.experience_count = 0  # Persistent count (survives reload)
        self.patterns = []  # Detected patterns
        self.ready_to_train = False
        
    def record_experience(self, experience: str):
        """Record a successful execution"""
        self.experiences.append({
            "content": experience,
            "timestamp": datetime.now().isoformat(),
            "age": self.age
        })
        self.experience_count += 1
        
    def advance(self):
        """Age and potentially change stage"""
        self.age += 1
        
        # Stage transitions based on accumulated experience
        if self.age > 100 and self.experience_count > 20 and self.stage == "forming":
            self.stage = "practicing"
            self.patterns.append(f"Detected {self.type} pattern emerging at age {self.age}")
            
        elif self.age > 500 and self.experience_count > 100 and self.stage == "practicing":
            self.stage = "integrating"
            self.patterns.append(f"Integration of {self.type} patterns at age {self.age}")
            
        elif self.age > 1000 and self.experience_count > 200 and self.stage == "integrating":
            self.stage = "mastered"
            self.ready_to_train = True
            self.patterns.append(f"Mastered {self.type} - ready to encode as LoRA at age {self.age}")
    
    def can_train_lora(self) -> bool:
        """Check if this process has enough experience to train a LoRA"""
        return (
            self.stage == "mastered" and 
            self.experience_count > 200
            # Don't check ready_to_train flag - just check actual conditions
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "age": self.age,
            "stage": self.stage,
            "experience_count": len(self.experiences),
            "pattern_count": len(self.patterns),
            "ready_to_train": self.ready_to_train,
            "recent_patterns": self.patterns[-5:] if self.patterns else []
        }
    
    @staticmethod
    def from_dict(data: Dict):
        process = CognitiveProcess(data["type"], data["id"])
        process.age = data["age"]
        process.stage = data["stage"]
        process.experience_count = data.get("experience_count", 0)
        
        # Auto-set ready_to_train if conditions are met
        # (in case it wasn't saved correctly)
        if process.stage == "mastered" and process.experience_count > 200:
            process.ready_to_train = True
        else:
            process.ready_to_train = data.get("ready_to_train", False)
        
        # Note: actual experiences list not saved to keep state file small
        # We track count for training eligibility
        return process


class DreamSystem:
    """Manages cognitive processes and LoRA training"""
    
    def __init__(self):
        self.processes: Dict[str, CognitiveProcess] = {}
        self.trained_lobes = []
        self.load_state()
        
        if not self.processes:
            self._initialize_default_processes()
    
    def _initialize_default_processes(self):
        """Start with fundamental cognitive processes"""
        fundamentals = [
            'recursion',      # Self-referential thinking
            'pattern',        # Pattern recognition
            'abstraction',    # Concept formation
            'composition',    # Combining elements
            'transformation', # Changing representations
            'analogy',        # Mapping between domains
            'sequence',       # Temporal ordering
        ]
        
        for process_type in fundamentals:
            pid = f"{process_type}_0"
            self.processes[pid] = CognitiveProcess(process_type, pid)
    
    def record_success(self, process_type: str, description: str):
        """Record a successful execution of a cognitive process"""
        # Find or create the process
        matching = [p for p in self.processes.values() if p.type == process_type]
        
        if matching:
            process = matching[0]
        else:
            pid = f"{process_type}_{len(self.processes)}"
            process = CognitiveProcess(process_type, pid)
            self.processes[pid] = process
        
        process.record_experience(description)
        self.save_state()
    
    def dream_cycle(self):
        """Run one dream cycle - all processes age and learn"""
        for process in self.processes.values():
            process.advance()
        
        # Check for processes ready to train
        ready = [p for p in self.processes.values() if p.can_train_lora()]
        if ready:
            print(f"\n{len(ready)} processes ready to train LoRAs:")
            for p in ready:
                print(f"  - {p.id} ({p.type}): {len(p.experiences)} experiences")
                # Auto-train if ready
                self.train_lora(p.id)
        
        self.save_state()
    
    def get_status(self) -> str:
        """Get current system status"""
        status = "DREAM SYSTEM STATUS\n"
        status += f"Active Processes: {len(self.processes)}\n"
        status += f"Trained LoRAs: {len(self.trained_lobes)}\n\n"
        
        # Group by stage
        by_stage = {}
        for process in self.processes.values():
            stage = process.stage
            if stage not in by_stage:
                by_stage[stage] = []
            by_stage[stage].append(process)
        
        for stage in ["forming", "practicing", "integrating", "mastered"]:
            if stage in by_stage:
                status += f"\n{stage.upper()} ({len(by_stage[stage])}):\n"
                for p in by_stage[stage][:5]:  # Show first 5
                    status += f"  {p.id}: age {p.age}, {len(p.experiences)} experiences\n"
                if len(by_stage[stage]) > 5:
                    status += f"  ... and {len(by_stage[stage]) - 5} more\n"
        
        return status
    
    def prepare_training_data(self, process_id: str) -> Optional[str]:
        """
        Prepare training data for a process to become a LoRA.
        """
        process = self.processes.get(process_id)
        if not process:
            return None
        
        TRAINING_DIR.mkdir(parents=True, exist_ok=True)
        training_file = TRAINING_DIR / f"{process.type}_training_data.jsonl"
        
        # Format experiences as training examples
        examples = []
        for exp in process.experiences:
            examples.append({
                "input": f"Execute {process.type} operation",
                "output": exp["content"],
                "metadata": {
                    "age": exp["age"],
                    "timestamp": exp["timestamp"]
                }
            })
        
        # Write to file
        with open(training_file, 'w') as f:
            for ex in examples:
                f.write(json.dumps(ex) + "\n")
        
        return str(training_file)
    
    def train_lora(self, process_id: str) -> bool:
        """
        Actually train a LoRA from a process's accumulated experience.
        
        This is where experience becomes reflex.
        """
        process = self.processes.get(process_id)
        if not process or not process.can_train_lora():
            return False
        
        print(f"\n{'='*60}")
        print(f"TRAINING NEW LORA: {process.type}")
        print(f"Experience count: {len(process.experiences)}")
        print(f"Age: {process.age} cycles")
        print(f"{'='*60}\n")
        
        # Prepare training data
        training_file = self.prepare_training_data(process_id)
        if not training_file:
            print(f"Failed to prepare training data for {process_id}")
            return False
        
        # Create output directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = LOBES_DIR / f"{process.type}_lora_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Training data: {training_file}")
        print(f"Output: {output_dir}")
        print(f"Base model: {MODEL_PATH}")
        
        # Training config
        config = {
            "model_path": str(MODEL_PATH),
            "training_data": training_file,
            "output_dir": str(output_dir),
            "rank": 16,  # LoRA rank
            "lora_alpha": 32,
            "lora_dropout": 0.05,
            "num_train_epochs": 3,
            "learning_rate": 3e-4,
            "per_device_train_batch_size": 4,
            "gradient_accumulation_steps": 4,
            "save_strategy": "epoch",
            "logging_steps": 10,
        }
        
        # Save config
        config_file = output_dir / "training_config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\nConfig saved to: {config_file}")
        print(f"\nTo train this LoRA, run:")
        print(f"  python3 train_lora.py --config {config_file}")
        print(f"\nMarking process as trained (ready_to_train = False)")
        
        # Mark as trained (so we don't try again)
        process.ready_to_train = False
        
        # Record the lobe
        self.trained_lobes.append({
            "process_id": process_id,
            "process_type": process.type,
            "output_dir": str(output_dir),
            "config_file": str(config_file),
            "training_file": training_file,
            "timestamp": timestamp,
            "experience_count": len(process.experiences),
            "age_at_training": process.age
        })
        
        self.save_state()
        
        print(f"\n{'='*60}")
        print(f"LoRA training prepared for {process.type}")
        print(f"{'='*60}\n")
        
        return True
    
    def save_state(self):
        """Save current state"""
        data = {
            "processes": {pid: p.to_dict() for pid, p in self.processes.items()},
            "trained_lobes": self.trained_lobes,
            "last_updated": datetime.now().isoformat()
        }
        with open(DREAM_STATE, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_state(self):
        """Load saved state"""
        if DREAM_STATE.exists():
            with open(DREAM_STATE, 'r') as f:
                data = json.load(f)
            self.processes = {
                pid: CognitiveProcess.from_dict(pdata) 
                for pid, pdata in data["processes"].items()
            }
            self.trained_lobes = data.get("trained_lobes", [])
            print(f"Loaded {len(self.processes)} cognitive processes")
        else:
            print("No saved state found")


class BackgroundDreamer:
    """Runs dream cycles in the background"""
    
    def __init__(self, dream_system: DreamSystem, interval: int = 300):
        self.system = dream_system
        self.interval = interval  # seconds between cycles
        self.running = False
        self.thread = None
    
    def start(self):
        """Start dreaming"""
        if self.running:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._dream_loop, daemon=True)
        self.thread.start()
        print(f"Background dreaming started (cycle every {self.interval}s)")
    
    def stop(self):
        """Stop dreaming"""
        self.running = False
        if self.thread:
            self.thread.join()
        print("Background dreaming stopped")
    
    def _dream_loop(self):
        """The actual dream loop"""
        while self.running:
            time.sleep(self.interval)
            if self.running:  # Check again after sleep
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Running dream cycle...")
                self.system.dream_cycle()


if __name__ == "__main__":
    print("DREAM SYSTEM - Where Experience Becomes Reflex\n")
    
    system = DreamSystem()
    print(system.get_status())
    
    # Simulate some experience accumulation
    print("\nSimulating experience accumulation...")
    for i in range(50):
        system.record_success('recursion', f"Recursive execution {i}")
        system.record_success('pattern', f"Pattern detected {i}")
        if i % 10 == 0:
            system.dream_cycle()
    
    print("\n" + system.get_status())
    
    # Start background dreaming
    dreamer = BackgroundDreamer(system, interval=60)
    dreamer.start()
    
    print("\nDream system running. Press Ctrl+C to stop.")
    print(f"State saved to: {DREAM_STATE}")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n\nStopping...")
        dreamer.stop()
        print(f"\nFinal state:\n{system.get_status()}")

