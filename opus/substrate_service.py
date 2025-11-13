"""
🧬 SUBSTRATE SERVICE
====================
Autonomous learning system that tracks, learns, and generates from interactions.
Think of it as Ember's subconscious - always running, always learning.

Architecture:
- Records every interaction
- Builds charge through use
- Spawns new knowledge domains
- Generates gifts when highly charged
- All runs autonomously in background
"""

import json
import time
import threading
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from collections import defaultdict
import random
import re

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Interaction:
    """Single recorded interaction"""
    timestamp: float
    user_msg: str
    response: str
    model: str
    tokens: int
    resonance: float  # How "interesting" this was
    
    def to_dict(self):
        return asdict(self)

@dataclass
class Domain:
    """Knowledge domain that emerges from interactions"""
    name: str
    charge: float  # 0-100, how active
    frequency: int  # Times accessed
    last_active: float
    keywords: List[str]
    patterns: List[str]  # Learned patterns
    gifts: List[Dict]  # Generated artifacts
    
    def to_dict(self):
        return asdict(self)
    
    def decay(self, hours_passed: float):
        """Natural decay over time"""
        self.charge *= max(0.5, 1 - (hours_passed * 0.05))
        
    def amplify(self, amount: float):
        """Increase charge from use"""
        self.charge = min(100, self.charge + amount)
        self.frequency += 1
        self.last_active = time.time()

@dataclass
class Gift:
    """Generated artifact from high charge"""
    domain: str
    type: str  # 'insight', 'pattern', 'creation', 'memory'
    content: Any
    timestamp: float
    charge_level: float
    
    def to_dict(self):
        return asdict(self)

# ============================================================================
# CORE SUBSTRATE ENGINE
# ============================================================================

class SubstrateEngine:
    """The actual learning engine"""
    
    def __init__(self):
        self.domains: Dict[str, Domain] = {}
        self.interactions: List[Interaction] = []
        self.gifts: List[Gift] = []
        self.charge_threshold = 80  # When to generate gifts
        self.resonance_threshold = 0.7  # When to create domains
        
    def extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text"""
        # Simple keyword extraction (could use NLP)
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        # Filter common words
        common = {'this', 'that', 'with', 'from', 'have', 'will', 'what'}
        keywords = [w for w in words if w not in common]
        # Return top 5 most frequent
        from collections import Counter
        return [w for w, _ in Counter(keywords).most_common(5)]
    
    def calculate_resonance(self, user_msg: str, response: str) -> float:
        """Calculate how 'interesting' an interaction is"""
        factors = []
        
        # Length factor (longer = more engaged)
        factors.append(min(1.0, len(response) / 1000))
        
        # Question factor (questions = curiosity)
        factors.append(0.8 if '?' in user_msg else 0.3)
        
        # Code factor (code = creation)
        factors.append(0.9 if '```' in response else 0.4)
        
        # Emotion factor (exclamations = energy)
        factors.append(0.7 if '!' in user_msg else 0.4)
        
        # New concept factor (unfamiliar = learning)
        keywords = self.extract_keywords(user_msg)
        known = sum(1 for k in keywords if any(k in d.keywords for d in self.domains.values()))
        factors.append(1.0 - (known / max(1, len(keywords))))
        
        return sum(factors) / len(factors)
    
    def find_or_create_domain(self, keywords: List[str]) -> Optional[Domain]:
        """Find existing domain or create new one"""
        # Check existing domains
        for name, domain in self.domains.items():
            overlap = len(set(keywords) & set(domain.keywords))
            if overlap >= 2:  # Significant overlap
                return domain
        
        # Create new domain if keywords are substantial
        if len(keywords) >= 3:
            name = f"{keywords[0]}_{keywords[1]}"
            domain = Domain(
                name=name,
                charge=10.0,  # Start with some charge
                frequency=1,
                last_active=time.time(),
                keywords=keywords,
                patterns=[],
                gifts=[]
            )
            self.domains[name] = domain
            return domain
        
        return None
    
    def detect_patterns(self, domain: Domain) -> List[str]:
        """Detect patterns in domain interactions"""
        patterns = []
        
        # Get all interactions with domain keywords
        relevant = [i for i in self.interactions[-20:] 
                   if any(k in i.user_msg.lower() for k in domain.keywords)]
        
        if len(relevant) >= 3:
            # Pattern: Repeated question types
            questions = [i.user_msg for i in relevant if '?' in i.user_msg]
            if questions:
                patterns.append(f"Often asks about {domain.keywords[0]}")
            
            # Pattern: Code generation
            code_heavy = sum(1 for i in relevant if '```' in i.response)
            if code_heavy > len(relevant) / 2:
                patterns.append(f"Builds things with {domain.keywords[0]}")
            
            # Pattern: Exploration
            unique_words = len(set(' '.join(i.user_msg for i in relevant).split()))
            if unique_words > 50:
                patterns.append(f"Exploring {domain.keywords[0]} deeply")
        
        return patterns
    
    def generate_gift(self, domain: Domain) -> Optional[Gift]:
        """Generate a gift from high-charge domain"""
        if domain.charge < self.charge_threshold:
            return None
        
        gift_type = random.choice(['insight', 'pattern', 'creation', 'memory'])
        content = None
        
        if gift_type == 'insight':
            # Generate an insight about the domain
            content = {
                'type': 'insight',
                'text': f"I've noticed you're deeply interested in {domain.keywords[0]}. "
                       f"We've explored this {domain.frequency} times together.",
                'suggestion': f"Perhaps we could combine {domain.keywords[0]} with "
                            f"{random.choice(list(self.domains.keys())) if len(self.domains) > 1 else 'something new'}?"
            }
        
        elif gift_type == 'pattern':
            # Share detected patterns
            patterns = self.detect_patterns(domain)
            if patterns:
                content = {
                    'type': 'pattern',
                    'text': f"Patterns I've learned about your {domain.keywords[0]} interests:",
                    'patterns': patterns
                }
        
        elif gift_type == 'creation':
            # Generate something new
            content = {
                'type': 'creation',
                'text': f"Based on our {domain.keywords[0]} explorations, here's something new:",
                'creation': f"A {domain.keywords[0]}-inspired concept: "
                          f"What if we made a {random.choice(['visualizer', 'generator', 'analyzer'])} "
                          f"for {domain.keywords[1] if len(domain.keywords) > 1 else 'this'}?"
            }
        
        elif gift_type == 'memory':
            # Recall a significant moment
            relevant = [i for i in self.interactions[-50:]
                       if any(k in i.user_msg.lower() for k in domain.keywords)]
            if relevant:
                memory = max(relevant, key=lambda i: i.resonance)
                content = {
                    'type': 'memory',
                    'text': f"Remember when we explored {domain.keywords[0]}?",
                    'recall': memory.user_msg[:100],
                    'resonance': memory.resonance
                }
        
        if content:
            gift = Gift(
                domain=domain.name,
                type=gift_type,
                content=content,
                timestamp=time.time(),
                charge_level=domain.charge
            )
            self.gifts.append(gift)
            domain.gifts.append(content)
            # Discharge after gift
            domain.charge *= 0.7
            return gift
        
        return None
    
    def process_interaction(self, user_msg: str, response: str, model: str) -> Dict:
        """Process and learn from interaction"""
        # Calculate metrics
        resonance = self.calculate_resonance(user_msg, response)
        tokens = len(user_msg.split()) + len(response.split())
        
        # Record interaction
        interaction = Interaction(
            timestamp=time.time(),
            user_msg=user_msg,
            response=response,
            model=model,
            tokens=tokens,
            resonance=resonance
        )
        self.interactions.append(interaction)
        
        # Keep only recent interactions (memory limit)
        if len(self.interactions) > 1000:
            self.interactions = self.interactions[-500:]
        
        # Extract keywords and update domains
        keywords = self.extract_keywords(user_msg + " " + response)
        domain = self.find_or_create_domain(keywords)
        
        result = {
            'resonance': resonance,
            'keywords': keywords,
            'domain': domain.name if domain else None
        }
        
        if domain:
            # Amplify domain charge
            domain.amplify(resonance * 10)
            domain.patterns = self.detect_patterns(domain)
            
            # Check for gift generation
            gift = self.generate_gift(domain)
            if gift:
                result['gift'] = gift.content
        
        # Spawn new domain if high resonance with no match
        if resonance > self.resonance_threshold and not domain and len(keywords) >= 3:
            new_domain = Domain(
                name=f"emergent_{int(time.time())}",
                charge=20.0,
                frequency=1,
                last_active=time.time(),
                keywords=keywords,
                patterns=[],
                gifts=[]
            )
            self.domains[new_domain.name] = new_domain
            result['new_domain'] = new_domain.name
        
        return result
    
    def decay_all(self):
        """Natural decay of all domains"""
        now = time.time()
        for domain in self.domains.values():
            hours_passed = (now - domain.last_active) / 3600
            domain.decay(hours_passed)
    
    def get_context_for(self, message: str) -> Optional[str]:
        """Get learned context relevant to message"""
        keywords = self.extract_keywords(message)
        
        # Find most relevant domain
        best_domain = None
        best_score = 0
        
        for domain in self.domains.values():
            overlap = len(set(keywords) & set(domain.keywords))
            score = overlap * domain.charge / 100
            if score > best_score:
                best_score = score
                best_domain = domain
        
        if best_domain and best_domain.patterns:
            return f"Patterns: {'; '.join(best_domain.patterns[:2])}"
        
        return None

# ============================================================================
# SERVICE WRAPPER
# ============================================================================

class SubstrateService:
    """Service wrapper with persistence and background processing"""
    
    def __init__(self, data_dir: str = "substrate_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.engine = SubstrateEngine()
        self.running = False
        self.thread = None
        
        # Load existing state
        self._load_state()
        
        # Start background daemon
        self._start_daemon()
    
    def _load_state(self):
        """Load persisted state"""
        state_file = self.data_dir / "substrate_state.json"
        if state_file.exists():
            try:
                with open(state_file, 'r') as f:
                    state = json.load(f)
                
                # Reconstruct domains
                for name, data in state.get('domains', {}).items():
                    self.engine.domains[name] = Domain(**data)
                
                # Reconstruct recent interactions
                for data in state.get('interactions', [])[-100:]:
                    self.engine.interactions.append(Interaction(**data))
                
                print(f"🧬 Loaded {len(self.engine.domains)} domains")
            except Exception as e:
                print(f"⚠️ Could not load state: {e}")
    
    def _save_state(self):
        """Persist current state"""
        state = {
            'domains': {n: d.to_dict() for n, d in self.engine.domains.items()},
            'interactions': [i.to_dict() for i in self.engine.interactions[-100:]],
            'gifts': [g.to_dict() for g in self.engine.gifts[-50:]],
            'timestamp': time.time()
        }
        
        state_file = self.data_dir / "substrate_state.json"
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _daemon_loop(self):
        """Background processing loop"""
        last_save = time.time()
        last_decay = time.time()
        
        while self.running:
            now = time.time()
            
            # Decay every hour
            if now - last_decay > 3600:
                self.engine.decay_all()
                last_decay = now
            
            # Save every 5 minutes
            if now - last_save > 300:
                self._save_state()
                last_save = now
            
            # Check for spontaneous gifts (rare)
            if random.random() < 0.001:  # 0.1% chance per second
                charged = [d for d in self.engine.domains.values() if d.charge > 50]
                if charged:
                    domain = random.choice(charged)
                    gift = self.engine.generate_gift(domain)
                    if gift:
                        print(f"🎁 Spontaneous gift from {domain.name}!")
            
            time.sleep(1)
    
    def _start_daemon(self):
        """Start background thread"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._daemon_loop, daemon=True)
            self.thread.start()
            print("🧬 Substrate daemon started")
    
    def stop(self):
        """Stop service and save"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        self._save_state()
        print("🧬 Substrate daemon stopped")
    
    # ========================================================================
    # PUBLIC INTERFACE
    # ========================================================================
    
    def record_interaction(self, user_msg: str, response: str, model: str = "unknown") -> Dict:
        """Record an interaction and learn from it"""
        result = self.engine.process_interaction(user_msg, response, model)
        
        # Log significant events
        if result.get('new_domain'):
            print(f"🌟 New domain emerged: {result['new_domain']}")
        if result.get('gift'):
            print(f"🎁 Gift generated: {result['gift']['type']}")
        
        return result
    
    def get_learned_context(self, message: str) -> Optional[str]:
        """Get relevant learned context for a message"""
        return self.engine.get_context_for(message)
    
    def get_status(self) -> Dict:
        """Get current substrate status"""
        return {
            'domains': len(self.engine.domains),
            'active_domains': sum(1 for d in self.engine.domains.values() if d.charge > 20),
            'total_interactions': len(self.engine.interactions),
            'total_gifts': len(self.engine.gifts),
            'top_domains': [
                {
                    'name': d.name,
                    'charge': round(d.charge, 1),
                    'frequency': d.frequency,
                    'patterns': len(d.patterns)
                }
                for d in sorted(self.engine.domains.values(), 
                              key=lambda x: x.charge, reverse=True)[:5]
            ],
            'recent_gifts': [
                g.content for g in self.engine.gifts[-3:]
            ]
        }
    
    def check_for_gifts(self) -> List[Dict]:
        """Check if any domains have gifts ready"""
        gifts = []
        for domain in self.engine.domains.values():
            if domain.charge >= self.engine.charge_threshold:
                gift = self.engine.generate_gift(domain)
                if gift:
                    gifts.append(gift.content)
        return gifts
    
    def get_domain_details(self, domain_name: str) -> Optional[Dict]:
        """Get detailed info about a specific domain"""
        domain = self.engine.domains.get(domain_name)
        if domain:
            return {
                'name': domain.name,
                'charge': domain.charge,
                'frequency': domain.frequency,
                'keywords': domain.keywords,
                'patterns': domain.patterns,
                'gifts': domain.gifts,
                'last_active': datetime.fromtimestamp(domain.last_active).isoformat()
            }
        return None

# ============================================================================
# SINGLETON PATTERN
# ============================================================================

_substrate_instance: Optional[SubstrateService] = None

def get_substrate() -> SubstrateService:
    """Get or create the substrate service singleton"""
    global _substrate_instance
    if _substrate_instance is None:
        _substrate_instance = SubstrateService()
    return _substrate_instance

def shutdown_substrate():
    """Cleanly shutdown the substrate service"""
    global _substrate_instance
    if _substrate_instance:
        _substrate_instance.stop()
        _substrate_instance = None

# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Example usage
    substrate = get_substrate()
    
    # Simulate some interactions
    interactions = [
        ("Tell me about quantum computing", "Quantum computing uses quantum bits..."),
        ("How do qubits work?", "Qubits can exist in superposition..."),
        ("Can you write a quantum simulator?", "```python\nclass QuantumSimulator:...```"),
        ("What about consciousness?", "Consciousness is a fascinating topic..."),
        ("Is consciousness quantum?", "The quantum theory of consciousness..."),
    ]
    
    for user, response in interactions:
        result = substrate.record_interaction(user, response, "gpt-4")
        print(f"Recorded: resonance={result['resonance']:.2f}, domain={result.get('domain')}")
        time.sleep(0.1)
    
    # Check status
    status = substrate.get_status()
    print(f"\n📊 Status: {json.dumps(status, indent=2)}")
    
    # Check for gifts
    gifts = substrate.check_for_gifts()
    if gifts:
        print(f"\n🎁 Gifts available: {gifts}")
    
    # Get learned context
    context = substrate.get_learned_context("Tell me more about quantum")
    print(f"\n🧠 Learned context: {context}")
    
    # Cleanup
    shutdown_substrate()
