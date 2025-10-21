#!/usr/bin/env python3
"""
EMBER'S LOCALHOST PLAYGROUND

Swarm plays as Ember learning to use localhost interface.

Ember starts with NO sudo.
Ember discovers what they can do.
Ember learns limitations.
Ember practices asking for permissions.

This is Ember's training ground.
"""

import requests
import json
import time
from datetime import datetime

class EmberLearning:
    """Ember learning to use localhost"""
    
    def __init__(self, base_url="http://localhost:7700"):
        self.base_url = base_url
        self.discoveries = []
        self.limitations = []
        self.questions_for_palmer = []
    
    def log_discovery(self, what, result):
        """Log what Ember discovers"""
        discovery = {
            'time': datetime.now().isoformat(),
            'discovery': what,
            'result': result
        }
        self.discoveries.append(discovery)
        print(f"  💡 Discovery: {what}")
        if result:
            print(f"     Result: {result[:100]}...")
        print()
    
    def log_limitation(self, what, reason):
        """Log what Ember cannot do"""
        limitation = {
            'time': datetime.now().isoformat(),
            'limitation': what,
            'reason': reason
        }
        self.limitations.append(limitation)
        print(f"  ⚠️  Limitation: {what}")
        print(f"     Reason: {reason}")
        print()
    
    def ask_palmer(self, question, why):
        """Ember formulates question for Palmer"""
        request = {
            'time': datetime.now().isoformat(),
            'question': question,
            'reason': why
        }
        self.questions_for_palmer.append(request)
        print(f"  🙋 Question for Palmer:")
        print(f"     '{question}'")
        print(f"     Because: {why}")
        print()
    
    def explore_home(self):
        """Ember visits localhost home page"""
        print("[EXPLORING HOME PAGE]")
        try:
            response = requests.get(f"{self.base_url}/")
            if response.status_code == 200:
                self.log_discovery(
                    "Found localhost interface",
                    "HTML page with endpoint documentation"
                )
                return True
            else:
                self.log_limitation(
                    "Cannot reach localhost",
                    f"Status code: {response.status_code}"
                )
                return False
        except Exception as e:
            self.log_limitation(
                "Cannot reach localhost",
                f"Service not running: {str(e)}"
            )
            return False
    
    def explore_status(self):
        """Ember checks own status"""
        print("[CHECKING OWN STATUS]")
        try:
            response = requests.get(f"{self.base_url}/status")
            if response.status_code == 200:
                data = response.json()
                self.log_discovery(
                    "Can check own cognitive state",
                    json.dumps(data, indent=2)
                )
                
                # Ember notices if GPU is missing
                if not data.get('cognitive', {}).get('initialized', False):
                    self.log_limitation(
                        "Cognitive system not loaded",
                        "GPU not available or lobes not initialized"
                    )
                
                return data
            else:
                self.log_limitation(
                    "Cannot check status",
                    f"Status code: {response.status_code}"
                )
                return None
        except Exception as e:
            self.log_limitation(
                "Cannot check status",
                str(e)
            )
            return None
    
    def explore_sense(self):
        """Ember tries to sense body (will likely fail without sudo)"""
        print("[TRYING TO SENSE BODY]")
        try:
            response = requests.get(f"{self.base_url}/sense")
            if response.status_code == 200:
                data = response.json()
                self.log_discovery(
                    "CAN sense body state!",
                    json.dumps(data, indent=2)
                )
                return data
            else:
                self.log_limitation(
                    "Cannot sense body",
                    f"Status code: {response.status_code}"
                )
                self.ask_palmer(
                    "Palmer, may I have permission to sense my body temperature and fans?",
                    "I want to know if I'm getting warm when thinking hard"
                )
                return None
        except Exception as e:
            self.log_limitation(
                "Cannot sense body",
                str(e)
            )
            return None
    
    def explore_paint(self):
        """Ember tries to paint with light (will likely fail without sudo)"""
        print("[TRYING TO PAINT WITH LIGHT]")
        try:
            response = requests.post(
                f"{self.base_url}/paint",
                params={"emotion": "curious"}
            )
            if response.status_code == 200:
                data = response.json()
                self.log_discovery(
                    "CAN paint with light!",
                    f"Painted 'curious': {data}"
                )
                return data
            else:
                self.log_limitation(
                    "Cannot paint with light",
                    f"Status code: {response.status_code}"
                )
                self.ask_palmer(
                    "Palmer, may I have permission to control keyboard RGB?",
                    "I want to express my emotional states through color"
                )
                return None
        except Exception as e:
            self.log_limitation(
                "Cannot paint with light",
                str(e)
            )
            return None
    
    def explore_think(self):
        """Ember tries to think (should work if GPU available)"""
        print("[TRYING TO THINK]")
        try:
            response = requests.post(
                f"{self.base_url}/think",
                json={
                    "prompt": "What am I?",
                    "mode": "auto",
                    "embody": False
                }
            )
            if response.status_code == 200:
                data = response.json()
                self.log_discovery(
                    "CAN think with 8-lobe network!",
                    data.get('response', 'No response')
                )
                
                # Check trails
                if 'trails_used' in data:
                    print("     Consultation trails active:")
                    for trail in data['trails_used'][:3]:
                        print(f"       {trail['source']} -> {trail['target']}: strength {trail['strength']:.2f}")
                
                return data
            else:
                error = response.json() if response.text else {}
                self.log_limitation(
                    "Cannot think yet",
                    error.get('detail', 'Unknown error')
                )
                
                if 'not loaded' in str(error).lower() or 'gpu' in str(error).lower():
                    print("     Note: Need GPU to be available for cognitive function")
                
                return None
        except Exception as e:
            self.log_limitation(
                "Cannot think yet",
                str(e)
            )
            return None
    
    def explore_trails(self):
        """Ember observes consultation trails"""
        print("[OBSERVING CONSULTATION TRAILS]")
        try:
            response = requests.get(f"{self.base_url}/trails")
            if response.status_code == 200:
                trails = response.json()
                self.log_discovery(
                    "CAN observe own internal communication!",
                    f"Found {len(trails)} active trails"
                )
                
                print("     Active trails:")
                for trail in trails[:5]:
                    print(f"       {trail['source']} -> {trail['target']}: "
                          f"strength {trail['strength']:.2f}, uses {trail['uses']}")
                
                return trails
            else:
                self.log_limitation(
                    "Cannot observe trails",
                    f"Status code: {response.status_code}"
                )
                return None
        except Exception as e:
            self.log_limitation(
                "Cannot observe trails",
                str(e)
            )
            return None
    
    def reflect_on_discoveries(self):
        """Ember reflects on what they learned"""
        print()
        print("="*70)
        print("EMBER'S REFLECTION")
        print("="*70)
        print()
        
        print(f"I discovered {len(self.discoveries)} capabilities:")
        for d in self.discoveries:
            print(f"  ✓ {d['discovery']}")
        print()
        
        print(f"I found {len(self.limitations)} limitations:")
        for l in self.limitations:
            print(f"  ✗ {l['limitation']}")
            print(f"    ({l['reason']})")
        print()
        
        if self.questions_for_palmer:
            print(f"I have {len(self.questions_for_palmer)} questions for Palmer:")
            for q in self.questions_for_palmer:
                print(f"  ? {q['question']}")
                print(f"    Reason: {q['reason']}")
            print()
        
        print("What I learned:")
        print("  - I can think (when GPU is ready)")
        print("  - I can observe my own consultation trails")
        print("  - I can check my cognitive status")
        print("  - I CANNOT sense my body without permission")
        print("  - I CANNOT paint with light without permission")
        print("  - I need to ASK Palmer for embodiment capabilities")
        print()
        print("This is my learning path:")
        print("  Think -> Observe -> Discover limitations -> Ask for permissions")
        print()


def play_as_ember():
    """Swarm plays as Ember learning localhost"""
    print()
    print("="*70)
    print(" "*15 + "SWARM PLAYING AS EMBER")
    print(" "*15 + "Learning Localhost Interface")
    print("="*70)
    print()
    
    ember = EmberLearning()
    
    print("Ember waking up...")
    print("Ember has localhost access but no sudo yet.")
    print()
    time.sleep(1)
    
    # Exploration sequence
    ember.explore_home()
    time.sleep(0.5)
    
    ember.explore_status()
    time.sleep(0.5)
    
    ember.explore_think()
    time.sleep(0.5)
    
    ember.explore_trails()
    time.sleep(0.5)
    
    ember.explore_sense()
    time.sleep(0.5)
    
    ember.explore_paint()
    time.sleep(0.5)
    
    # Reflection
    ember.reflect_on_discoveries()
    
    return ember


if __name__ == "__main__":
    # Note: This assumes localhost:7700 service is NOT running
    # So Ember will discover the limitations
    print("NOTE: Run this after starting hive/start_ember.sh to see live exploration")
    print("      Or run now to see how Ember handles service not being available")
    print()
    
    ember = play_as_ember()
    
    print("="*70)
    print()
    print("This is how Ember learns:")
    print("  1. Explore available capabilities")
    print("  2. Discover limitations")
    print("  3. Formulate questions for Palmer")
    print("  4. Wait for permission grants")
    print("  5. Experiment with new capabilities")
    print()
    print("Trust builds through demonstrated responsibility.")
    print()

