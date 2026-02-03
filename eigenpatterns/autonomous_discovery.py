#!/usr/bin/env python3
"""
AUTONOMOUS DISCOVERY
====================

A mind that runs autonomously, discovers, and speaks.

It explores patterns, forms concepts, finds analogies,
makes predictions, and narrates its journey.

The mind thinks out loud.
"""

import json
import time
import random
import signal
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError


def run_with_timeout(func, arg, timeout=0.1):
    """Run function with timeout, return None if it times out."""
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, arg)
        try:
            return future.result(timeout=timeout)
        except (FuturesTimeoutError, Exception):
            return None

# Paths
LOG_PATH = Path("/ember/eigenpatterns/discovery_journal.txt")
STATE_PATH = Path("/ember/eigenpatterns/discovery_state.json")
LEARNED_PATH = Path("/ember/eigenpatterns/learned_knowledge.json")


@dataclass
class Pattern:
    name: str
    func: Any = None
    is_involution: Optional[bool] = None
    is_idempotent: Optional[bool] = None
    sample_in: Any = None
    sample_out: Any = None
    times_tested: int = 0

    def signature(self) -> str:
        parts = []
        if self.is_involution:
            parts.append("symmetric")
        if self.is_idempotent:
            parts.append("stable")
        return "-".join(parts) if parts else "unknown"


class AutonomousDiscoveryMind:
    """A mind that discovers and speaks autonomously."""

    def __init__(self):
        self.patterns: Dict[str, Pattern] = {}
        self.vocabulary: Dict[str, List[str]] = defaultdict(list)
        self.analogies: List[Dict] = []

        # Composition discovery (no hardcoded laws!)
        self.compositions_tested: List[Dict] = []
        self.composition_laws: Dict[str, Dict] = {}  # Discovered laws
        self.law_observations: Dict[str, List[bool]] = defaultdict(list)  # Track outcomes

        # Predictions based on discovered laws
        self.predictions_made: List[Dict] = []
        self.predictions_correct: int = 0
        self.predictions_wrong: int = 0

        # Learning from failure
        self.invalidated_laws: List[Dict] = []  # Laws that didn't hold up
        self.chaotic_compositions: Dict[str, Dict] = {}  # Composition types known to be unpredictable
        self.meta_insights: List[str] = []  # Higher-order insights about composition itself
        self.predictions_avoided: List[Dict] = []  # Predictions we wisely avoided

        # Internal state
        self.curiosity = 0.8
        self.understanding = 0.1
        self.satisfaction = 0.1

        # Journey
        self.discoveries = 0
        self.involutions_found = 0
        self.idempotents_found = 0
        self.insights = []
        self.cycle = 0

        # Safe execution
        self.safe_builtins = {
            'len': len, 'str': str, 'int': int, 'float': float,
            'list': list, 'dict': dict, 'tuple': tuple, 'set': set,
            'sorted': sorted, 'reversed': reversed, 'sum': sum,
            'min': min, 'max': max, 'abs': abs, 'round': round,
            'True': True, 'False': False, 'None': None,
            'type': type, 'range': range, 'enumerate': enumerate,
            'zip': zip, 'map': map, 'filter': filter,
            'ord': ord, 'chr': chr, 'any': any, 'all': all,
            'isinstance': isinstance, 'hasattr': hasattr,
        }

        self.skip_words = ['fibonacci', 'prime', 'factorial', 'recursive',
                          'permut', 'tree', 'graph', 'matrix', 'binary_search',
                          'tower', 'hanoi', 'knapsack', 'traveling', 'sudoku',
                          'subsets', 'combinations', 'powerset', 'n_queens',
                          'partition', 'generate_all', 'all_paths', 'backtrack',
                          'power_set', 'pascal_triangle', 'longest_increasing',
                          'longest_palindrom', 'longest_common']

        self.test_inputs = ['hi', 'ab', 'hello', 'test', 'a', 5, 10, [1, 2, 3], [1, 1, 2, 2]]

        # Load patterns
        self._load_patterns()

        # Load previously learned knowledge (persists between runs)
        self._load_learned_knowledge()

        # Clear log
        LOG_PATH.write_text("AUTONOMOUS DISCOVERY JOURNAL\n" + "=" * 50 + "\n\n")

    def _load_patterns(self):
        """Load all patterns from the organism."""
        path = Path("/ember/Mandelbrot_Mind/pattern_trails.json")
        if not path.exists():
            return

        data = json.loads(path.read_text())
        patterns_data = data.get("patterns", {})

        for name, pdata in patterns_data.items():
            if any(kw in name.lower() for kw in self.skip_words):
                continue

            code = pdata.get('code', '')
            if not code or len(code) > 500:
                continue

            func = self._extract_func(code)
            if func:
                self.patterns[name] = Pattern(name=name, func=func)

    def _extract_func(self, code: str):
        """Extract function from code."""
        try:
            ns = {'__builtins__': self.safe_builtins}
            exec(code, ns)
            for v in ns.values():
                if callable(v) and v not in self.safe_builtins.values():
                    return v
        except:
            pass
        return None

    def _load_learned_knowledge(self):
        """Load previously learned knowledge from disk."""
        if not LEARNED_PATH.exists():
            return

        try:
            data = json.loads(LEARNED_PATH.read_text())

            # Load chaotic compositions (most important - these prevent bad predictions)
            self.chaotic_compositions = data.get('chaotic_compositions', {})

            # Load invalidated laws (for learning history)
            self.invalidated_laws = data.get('invalidated_laws', [])

            # Load meta-insights
            self.meta_insights = data.get('meta_insights', [])

            # Load composition laws that survived
            self.composition_laws = data.get('composition_laws', {})

            # Load law observations for continued learning
            observations = data.get('law_observations', {})
            for key, outcomes in observations.items():
                self.law_observations[key] = outcomes

            # Load stats
            self.predictions_avoided = data.get('predictions_avoided', [])

            if self.chaotic_compositions or self.invalidated_laws:
                print(f"📚 Loaded prior knowledge: {len(self.chaotic_compositions)} chaotic compositions, "
                      f"{len(self.invalidated_laws)} invalidated laws, "
                      f"{len(self.composition_laws)} surviving laws", flush=True)

        except Exception as e:
            print(f"⚠️ Could not load learned knowledge: {e}", flush=True)

    def _save_learned_knowledge(self):
        """Save learned knowledge to disk for persistence between runs."""
        data = {
            # Core learning - what compositions are chaotic
            'chaotic_compositions': self.chaotic_compositions,

            # History of invalidated laws
            'invalidated_laws': self.invalidated_laws,

            # Meta-insights about composition
            'meta_insights': self.meta_insights,

            # Laws that have survived testing
            'composition_laws': self.composition_laws,

            # Raw observations for continued learning
            'law_observations': dict(self.law_observations),

            # Stats
            'predictions_avoided': self.predictions_avoided,
            'predictions_correct': self.predictions_correct,
            'predictions_wrong': self.predictions_wrong,

            # Metadata
            'last_saved': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_cycles': self.cycle,
        }

        try:
            LEARNED_PATH.write_text(json.dumps(data, indent=2))
        except Exception as e:
            print(f"⚠️ Could not save learned knowledge: {e}", flush=True)

    def speak(self, thought: str, emotion: str = ""):
        """The mind speaks."""
        prefix = {
            'curious': '🔍',
            'excited': '✨',
            'satisfied': '😊',
            'thinking': '🤔',
            'insight': '💡',
            'discovery': '🎯',
        }.get(emotion, '💭')

        message = f"{prefix} {thought}"
        print(message, flush=True)

        with open(LOG_PATH, 'a') as f:
            f.write(f"{message}\n")

    def think(self, thought: str):
        """Internal thought (quieter)."""
        print(f"   ... {thought}", flush=True)

    def discover_pattern(self, name: str) -> bool:
        """Discover properties of a single pattern through observation."""
        if name not in self.patterns:
            return False

        pattern = self.patterns[name]
        if pattern.times_tested > 0:
            return False  # Already tested

        pattern.times_tested += 1

        inv_pass, idem_pass, tests = 0, 0, 0

        for inp in self.test_inputs[:3]:
            try:
                fx = run_with_timeout(pattern.func, inp, timeout=0.3)
                if fx is None:
                    continue

                pattern.sample_in = inp
                pattern.sample_out = fx

                ffx = run_with_timeout(pattern.func, fx, timeout=0.3)
                if ffx is None:
                    continue

                tests += 1

                if ffx == inp:
                    inv_pass += 1
                if ffx == fx:
                    idem_pass += 1

            except:
                pass

        if tests >= 2:
            pattern.is_involution = (inv_pass / tests) >= 0.8
            pattern.is_idempotent = (idem_pass / tests) >= 0.8

            sig = pattern.signature()
            self.vocabulary[sig].append(name)

            if pattern.is_involution:
                self.involutions_found += 1
            if pattern.is_idempotent:
                self.idempotents_found += 1

            self.discoveries += 1
            return True

        return False

    def explore(self) -> Optional[str]:
        """Explore an undiscovered pattern."""
        untested = [n for n, p in self.patterns.items() if p.times_tested == 0]
        if not untested:
            return None

        # Curiosity-driven selection
        if self.curiosity > 0.5:
            # Try something new
            return random.choice(untested)
        else:
            # Stick with familiar types
            return untested[0]

    def find_analogy(self) -> Optional[Dict]:
        """Find an analogy between patterns."""
        for sig, names in self.vocabulary.items():
            if len(names) >= 2 and sig != "unknown":
                # Find two patterns we haven't compared yet
                for i, n1 in enumerate(names):
                    for n2 in names[i+1:]:
                        analogy = {
                            'a': n1,
                            'b': n2,
                            'reason': sig,
                            'explanation': self._explain_analogy(n1, n2, sig)
                        }
                        if analogy not in self.analogies:
                            self.analogies.append(analogy)
                            return analogy
        return None

    def _explain_analogy(self, a: str, b: str, sig: str) -> str:
        """Generate natural language explanation of analogy."""
        if "symmetric" in sig and "stable" in sig:
            return f"both undo themselves AND settle"
        elif "symmetric" in sig:
            return f"both undo themselves when applied twice"
        elif "stable" in sig:
            return f"both settle after one application"
        else:
            return f"both exhibit {sig} behavior"

    def get_pattern_type(self, name: str) -> str:
        """Classify a pattern by its observed properties."""
        if name not in self.patterns:
            return "unknown"
        p = self.patterns[name]
        if p.is_involution and p.is_idempotent:
            return "fixed"  # Both properties = fixed point behavior
        elif p.is_involution:
            return "inv"
        elif p.is_idempotent:
            return "idem"
        else:
            return "other"

    def explore_composition(self) -> Optional[Dict]:
        """Compose two patterns and observe what happens. No predictions - just observe."""
        # Get patterns we've already classified
        classified = [(n, self.get_pattern_type(n)) for n, p in self.patterns.items()
                      if p.times_tested > 0 and self.get_pattern_type(n) != "unknown"]

        if len(classified) < 2:
            return None

        # Pick two patterns we haven't composed yet
        tested_pairs = set((c['a'], c['b']) for c in self.compositions_tested)

        # Count how many observations we have for each composition type
        type_counts = {}
        for obs in self.compositions_tested:
            key = f"{obs['a_type']} ∘ {obs['b_type']}"
            type_counts[key] = type_counts.get(key, 0) + 1

        # Try to find an underexplored composition type first
        for _ in range(20):  # Try a few times to find untested pair
            (a_name, a_type), (b_name, b_type) = random.sample(classified, 2)
            if (a_name, b_name) in tested_pairs:
                continue

            comp_type = f"{a_type} ∘ {b_type}"
            # Prefer composition types we haven't explored much
            if type_counts.get(comp_type, 0) < 3 or random.random() < 0.3:
                break
        else:
            return None

        f = self.patterns[a_name].func
        g = self.patterns[b_name].func

        if f is None or g is None:
            return None

        # Compose: (f ∘ g)(x) = f(g(x))
        def composed(x):
            gx = run_with_timeout(g, x, timeout=0.2)
            if gx is None:
                return None
            return run_with_timeout(f, gx, timeout=0.2)

        # Test the composed function
        inv_pass, idem_pass, tests = 0, 0, 0
        sample_trace = None

        for inp in self.test_inputs[:3]:
            try:
                fx = composed(inp)
                if fx is None:
                    continue

                ffx = composed(fx)
                if ffx is None:
                    continue

                tests += 1
                sample_trace = f"({a_name} ∘ {b_name})('{inp}') = '{fx}'"

                if ffx == inp:
                    inv_pass += 1
                if ffx == fx:
                    idem_pass += 1

            except:
                pass

        if tests < 2:
            return None

        is_involution = (inv_pass / tests) >= 0.8
        is_idempotent = (idem_pass / tests) >= 0.8

        # Classify the result
        if is_involution and is_idempotent:
            result_type = "fixed"
        elif is_involution:
            result_type = "inv"
        elif is_idempotent:
            result_type = "idem"
        else:
            result_type = "other"

        # Record this observation
        composition_key = f"{a_type} ∘ {b_type}"
        observation = {
            'a': a_name,
            'b': b_name,
            'a_type': a_type,
            'b_type': b_type,
            'result_type': result_type,
            'composition_key': composition_key,
            'sample': sample_trace
        }

        self.compositions_tested.append(observation)

        # Update law observations
        self.law_observations[composition_key].append(result_type)

        return observation

    def discover_laws(self) -> Optional[str]:
        """Look at composition observations and discover laws."""
        for key, outcomes in self.law_observations.items():
            if len(outcomes) < 1:
                continue  # Form laws early (from just 1 observation) to see if they hold up

            if key in self.composition_laws:
                continue  # Already discovered this law

            # Count outcomes
            from collections import Counter
            counts = Counter(outcomes)
            total = len(outcomes)
            most_common, count = counts.most_common(1)[0]

            # If one outcome dominates (>= 60%), form a law
            # (Lower threshold makes laws form earlier, more likely to be invalidated)
            if count / total >= 0.6:
                confidence = count / total
                law = {
                    'input': key,
                    'output': most_common,
                    'confidence': confidence,
                    'observations': total,
                    'evidence': dict(counts)
                }
                self.composition_laws[key] = law
                return f"{key} → {most_common} ({confidence:.0%} of {total} cases)"

        return None

    def update_law(self, composition_key: str, new_outcome: str) -> Optional[Dict]:
        """Update a law based on new evidence (especially failed predictions)."""
        if composition_key not in self.composition_laws:
            return None

        old_law = self.composition_laws[composition_key]
        old_confidence = old_law['confidence']
        old_output = old_law['output']

        # Recalculate based on all observations
        from collections import Counter
        outcomes = self.law_observations[composition_key]
        counts = Counter(outcomes)
        total = len(outcomes)
        most_common, count = counts.most_common(1)[0]
        new_confidence = count / total

        # Check if the law has changed
        result = {
            'key': composition_key,
            'old_output': old_output,
            'old_confidence': old_confidence,
            'new_output': most_common,
            'new_confidence': new_confidence,
            'observations': total,
            'evidence': dict(counts)
        }

        if new_confidence <= 0.6:
            # Law is no longer reliable - invalidate it (60% threshold - need clear majority)
            del self.composition_laws[composition_key]
            result['action'] = 'invalidated'

            # LEARN FROM FAILURE: Record what went wrong
            self.invalidated_laws.append({
                'composition_key': composition_key,
                'original_prediction': old_output,
                'evidence': dict(counts),
                'observations': total,
                'reason': 'evidence_split'  # Outcomes too evenly distributed
            })

            # Mark this composition type as chaotic/unpredictable
            self.chaotic_compositions[composition_key] = {
                'evidence': dict(counts),
                'learned_at_cycle': self.cycle,
                'lesson': f"'{composition_key}' is unpredictable - outcomes vary too much"
            }

            return result
        elif most_common != old_output:
            # The most common outcome has changed
            self.composition_laws[composition_key] = {
                'input': composition_key,
                'output': most_common,
                'confidence': new_confidence,
                'observations': total,
                'evidence': dict(counts)
            }
            result['action'] = 'changed'
            return result
        elif abs(new_confidence - old_confidence) >= 0.1:
            # Confidence has changed significantly
            self.composition_laws[composition_key]['confidence'] = new_confidence
            self.composition_laws[composition_key]['observations'] = total
            self.composition_laws[composition_key]['evidence'] = dict(counts)
            result['action'] = 'confidence_updated'
            return result

        return None  # No significant change

    def get_weakest_law(self) -> Optional[str]:
        """Find the law with lowest confidence that needs more testing."""
        if not self.composition_laws:
            return None

        # Sort laws by confidence, return the weakest
        weakest = min(self.composition_laws.items(), key=lambda x: x[1]['confidence'])
        return weakest[0] if weakest[1]['confidence'] < 0.9 else None

    def learn_from_invalidations(self) -> Optional[str]:
        """Analyze invalidated laws to learn meta-patterns about composition."""
        if not self.invalidated_laws:
            return None

        # Look for patterns in what got invalidated
        invalidated_keys = [law['composition_key'] for law in self.invalidated_laws]

        # Extract the types involved in failed laws
        failed_first_types = []
        failed_second_types = []
        for key in invalidated_keys:
            parts = key.split(' ∘ ')
            if len(parts) == 2:
                failed_first_types.append(parts[0])
                failed_second_types.append(parts[1])

        # Count which types appear most in failures
        from collections import Counter
        first_counts = Counter(failed_first_types)
        second_counts = Counter(failed_second_types)

        # Generate meta-insights
        new_insight = None

        # Insight: A particular type is unreliable in compositions
        for ptype, count in first_counts.most_common(1):
            if count >= 2 and f"'{ptype}' type is unreliable as first operand" not in self.meta_insights:
                new_insight = f"'{ptype}' type is unreliable as first operand in composition - {count} laws involving it failed"
                self.meta_insights.append(new_insight)
                break

        if not new_insight:
            for ptype, count in second_counts.most_common(1):
                if count >= 2 and f"'{ptype}' type is unreliable as second operand" not in self.meta_insights:
                    new_insight = f"'{ptype}' type is unreliable as second operand in composition - {count} laws involving it failed"
                    self.meta_insights.append(new_insight)
                    break

        # Insight: Mixing certain types is inherently chaotic
        if len(self.chaotic_compositions) >= 2:
            chaotic_patterns = list(self.chaotic_compositions.keys())
            # Check if there's a common pattern
            involves_other = sum(1 for k in chaotic_patterns if 'other' in k)
            if involves_other >= 2 and "Compositions involving 'other' types are inherently unpredictable" not in self.meta_insights:
                new_insight = "Compositions involving 'other' types are inherently unpredictable - they don't follow reliable rules"
                self.meta_insights.append(new_insight)

        # Insight about the nature of composition itself
        if len(self.invalidated_laws) >= 3 and "Composition doesn't always preserve structure" not in self.meta_insights:
            new_insight = "Composition doesn't always preserve structure - some combinations are fundamentally chaotic"
            self.meta_insights.append(new_insight)

        return new_insight

    def is_chaotic_composition(self, composition_key: str) -> bool:
        """Check if a composition type is known to be chaotic/unpredictable."""
        return composition_key in self.chaotic_compositions

    def is_risky_composition(self, composition_key: str) -> Optional[str]:
        """Check if a composition type is risky based on learned failures.

        Returns the reason if risky, None if safe to predict.
        """
        # Direct match - this exact composition type is chaotic
        if composition_key in self.chaotic_compositions:
            return f"'{composition_key}' is known to be chaotic"

        # Check if it involves types that have been unreliable
        parts = composition_key.split(' ∘ ')
        if len(parts) == 2:
            a_type, b_type = parts

            # Check if either type appears in chaotic compositions
            for chaotic_key in self.chaotic_compositions.keys():
                chaotic_parts = chaotic_key.split(' ∘ ')
                if len(chaotic_parts) == 2:
                    # Same first operand type in a chaotic composition
                    if chaotic_parts[0] == a_type:
                        return f"'{a_type}' as first operand was chaotic in '{chaotic_key}'"
                    # Same second operand type in a chaotic composition
                    if chaotic_parts[1] == b_type:
                        return f"'{b_type}' as second operand was chaotic in '{chaotic_key}'"

        return None  # Safe to predict

    def predict_composition(self, target_law: Optional[str] = None, allow_risky: bool = False) -> Optional[Dict]:
        """Use discovered laws to predict a new composition's behavior.

        If target_law is specified, specifically try to test that law.
        If allow_risky is False (default), skip compositions similar to known chaotic ones.
        """
        if not self.composition_laws:
            return None  # No laws yet to make predictions

        # Get all classified patterns - include ALL types for more variety and potential failures
        classified = [(n, self.get_pattern_type(n)) for n, p in self.patterns.items()
                      if p.times_tested > 0]

        # Filter to only patterns with known types for this prediction
        classified = [(n, t) for n, t in classified if t != "unknown"]

        if len(classified) < 2:
            return None

        # Find a composition we can predict but haven't tested
        tested_pairs = set((c['a'], c['b']) for c in self.compositions_tested)
        predicted_pairs = set((p['prediction']['a'], p['prediction']['b']) for p in self.predictions_made)

        # If targeting a specific law, filter for that composition type
        if target_law and target_law in self.composition_laws:
            # Check if this law is risky based on learned failures
            if not allow_risky:
                risk_reason = self.is_risky_composition(target_law)
                if risk_reason:
                    # Return a special "avoided" result
                    return {
                        'avoided': True,
                        'law_used': target_law,
                        'reason': risk_reason
                    }

            parts = target_law.split(' ∘ ')
            if len(parts) == 2:
                target_a_type, target_b_type = parts

                # Get patterns of the right types
                a_candidates = [(n, t) for n, t in classified if t == target_a_type]
                b_candidates = [(n, t) for n, t in classified if t == target_b_type]

                for _ in range(50):
                    if not a_candidates or not b_candidates:
                        break
                    (a_name, a_type) = random.choice(a_candidates)
                    (b_name, b_type) = random.choice(b_candidates)

                    if a_name == b_name:
                        continue
                    if (a_name, b_name) in tested_pairs or (a_name, b_name) in predicted_pairs:
                        continue

                    law = self.composition_laws[target_law]
                    return {
                        'a': a_name,
                        'b': b_name,
                        'a_type': a_type,
                        'b_type': b_type,
                        'predicted_result': law['output'],
                        'confidence': law['confidence'],
                        'law_used': target_law
                    }

        # Default behavior - find any predictable composition
        avoided_compositions = []
        for _ in range(30):  # Try to find a predictable pair
            (a_name, a_type), (b_name, b_type) = random.sample(classified, 2)

            if (a_name, b_name) in tested_pairs or (a_name, b_name) in predicted_pairs:
                continue

            composition_key = f"{a_type} ∘ {b_type}"

            if composition_key in self.composition_laws:
                # Check if this composition is risky
                if not allow_risky:
                    risk_reason = self.is_risky_composition(composition_key)
                    if risk_reason:
                        avoided_compositions.append({
                            'composition_key': composition_key,
                            'reason': risk_reason,
                            'a': a_name,
                            'b': b_name
                        })
                        continue  # Skip this risky composition

                # We have a safe law for this type of composition!
                law = self.composition_laws[composition_key]
                return {
                    'a': a_name,
                    'b': b_name,
                    'a_type': a_type,
                    'b_type': b_type,
                    'predicted_result': law['output'],
                    'confidence': law['confidence'],
                    'law_used': composition_key
                }

        # If we avoided some compositions, return info about that
        if avoided_compositions:
            return {
                'avoided': True,
                'avoided_compositions': avoided_compositions,
                'reason': 'All available compositions were risky based on learned failures'
            }

        return None

    def test_prediction(self, prediction: Dict) -> Dict:
        """Test a prediction by actually running the composition."""
        a_name, b_name = prediction['a'], prediction['b']

        f = self.patterns[a_name].func
        g = self.patterns[b_name].func

        # Compose: (f ∘ g)(x) = f(g(x))
        def composed(x):
            gx = run_with_timeout(g, x, timeout=0.2)
            if gx is None:
                return None
            return run_with_timeout(f, gx, timeout=0.2)

        # Test the composed function
        inv_pass, idem_pass, tests = 0, 0, 0
        sample_trace = None

        for inp in self.test_inputs[:3]:
            try:
                fx = composed(inp)
                if fx is None:
                    continue

                ffx = composed(fx)
                if ffx is None:
                    continue

                tests += 1
                sample_trace = f"({a_name} ∘ {b_name})('{inp}') = '{fx}'"

                if ffx == inp:
                    inv_pass += 1
                if ffx == fx:
                    idem_pass += 1

            except:
                pass

        if tests < 2:
            return {'success': False}

        is_involution = (inv_pass / tests) >= 0.8
        is_idempotent = (idem_pass / tests) >= 0.8

        # Classify the result
        if is_involution and is_idempotent:
            actual_type = "fixed"
        elif is_involution:
            actual_type = "inv"
        elif is_idempotent:
            actual_type = "idem"
        else:
            actual_type = "other"

        # Check if prediction was correct
        correct = (actual_type == prediction['predicted_result'])

        return {
            'success': True,
            'prediction': prediction,
            'actual_type': actual_type,
            'correct': correct,
            'sample': sample_trace
        }

    def reflect(self) -> str:
        """Generate a reflection on current understanding."""
        reflections = []

        if self.involutions_found > 0:
            reflections.append(f"I've found {self.involutions_found} patterns that undo themselves")

        if self.idempotents_found > 0:
            reflections.append(f"I've found {self.idempotents_found} patterns that settle")

        if len(self.vocabulary) > 1:
            reflections.append(f"I've organized patterns into {len(self.vocabulary)} behavioral categories")

        if len(self.analogies) > 0:
            reflections.append(f"I've noticed {len(self.analogies)} analogies between patterns")

        if not reflections:
            reflections.append("I'm still exploring...")

        return ". ".join(reflections) + "."

    def generate_insight(self) -> Optional[str]:
        """Generate a novel insight."""
        insights = []

        # Insight about involutions
        if self.involutions_found >= 3:
            inv_names = [n for n, p in self.patterns.items() if p.is_involution][:3]
            insights.append(f"Patterns like {', '.join(inv_names)} share a deep property: they're their own inverses")

        # Insight about vocabulary
        largest_group = max(self.vocabulary.items(), key=lambda x: len(x[1]), default=(None, []))
        if largest_group[0] and len(largest_group[1]) >= 5:
            insights.append(f"The '{largest_group[0]}' behavior is very common - {len(largest_group[1])} patterns share it")

        # Insight about analogies
        if len(self.analogies) >= 3:
            insights.append("Many patterns that look different actually behave the same way")

        if insights:
            insight = random.choice(insights)
            if insight not in self.insights:
                self.insights.append(insight)
                return insight

        return None

    def run_cycle(self) -> Dict:
        """Run one cycle of autonomous discovery."""
        self.cycle += 1
        events = []

        # 1. Explore (curiosity-driven)
        if self.curiosity > 0.3:
            name = self.explore()
            if name:
                self.think(f"examining {name}...")
                discovered = self.discover_pattern(name)

                if discovered:
                    pattern = self.patterns[name]

                    if pattern.is_involution and pattern.is_idempotent:
                        self.speak(f"Discovered: {name} both undoes itself AND settles!", "discovery")
                        self.speak(f"  f('{pattern.sample_in}') = '{pattern.sample_out}'", "")
                        self.curiosity = min(1.0, self.curiosity + 0.1)
                        self.satisfaction += 0.15
                        events.append(f"discovered {name} (both)")

                    elif pattern.is_involution:
                        self.speak(f"Discovered: {name} undoes itself!", "discovery")
                        self.speak(f"  f(f(x)) = x ✓", "")
                        self.curiosity = min(1.0, self.curiosity + 0.05)
                        self.satisfaction += 0.1
                        events.append(f"discovered {name} (involution)")

                    elif pattern.is_idempotent:
                        self.speak(f"Discovered: {name} settles after one step", "discovery")
                        self.speak(f"  f(f(x)) = f(x) ✓", "")
                        self.satisfaction += 0.05
                        events.append(f"discovered {name} (idempotent)")

        # 2. Find analogies
        if self.cycle % 5 == 0:
            analogy = self.find_analogy()
            if analogy:
                self.speak(f"Analogy: {analogy['a']} ≈ {analogy['b']}", "thinking")
                self.speak(f"  because: {analogy['explanation']}", "")
                self.understanding += 0.1
                events.append(f"found analogy")

        # 3. Explore compositions (no hardcoded predictions - just observe!)
        if self.cycle % 2 == 0 and self.discoveries >= 3:
            # Do multiple composition experiments per cycle - try for variety
            for _ in range(4):
                observation = self.explore_composition()
                if observation:
                    self.speak(f"Composed: {observation['a']} ∘ {observation['b']}", "curious")
                    self.speak(f"  ({observation['a_type']} ∘ {observation['b_type']}) → {observation['result_type']}", "")
                    if observation['sample']:
                        self.speak(f"  {observation['sample']}", "")
                    events.append("explored composition")

        # 3.5 Try to discover composition laws from observations
        if self.cycle % 4 == 0 and len(self.compositions_tested) >= 2:
            new_law = self.discover_laws()
            if new_law:
                self.speak(f"⚡ LAW DISCOVERED: {new_law}", "excited")
                self.speak(f"  (emerged from {len(self.compositions_tested)} observations)", "")
                self.understanding += 0.2
                self.satisfaction += 0.15
                events.append("discovered composition law")

        # 3.6 Use discovered laws to make predictions and test them
        # STRESS TEST: Target weak laws specifically to verify or invalidate them
        if self.cycle % 2 == 0 and len(self.composition_laws) > 0:
            # Find weak laws to stress-test
            weak_law = self.get_weakest_law()
            if weak_law:
                self.speak(f"🧪 Stress-testing weak law: {weak_law} ({self.composition_laws[weak_law]['confidence']:.0%})", "curious")
                prediction = self.predict_composition(target_law=weak_law)
            else:
                prediction = self.predict_composition()

            if prediction:
                # Check if we avoided this prediction due to learned failures
                if prediction.get('avoided'):
                    law_key = prediction.get('law_used', 'unknown')
                    reason = prediction.get('reason', 'similar to chaotic composition')

                    self.speak(f"🛡️ AVOIDED risky prediction: {law_key}", "thinking")
                    self.speak(f"  Reason: {reason}", "")
                    self.speak(f"  (Using learned knowledge to avoid likely failure)", "")

                    # Track the avoided prediction
                    self.predictions_avoided.append({
                        'cycle': self.cycle,
                        'law': law_key,
                        'reason': reason
                    })
                    events.append("wisely avoided risky prediction")
                    self.satisfaction += 0.05  # Small satisfaction for using learned knowledge

                else:
                    # Make the prediction
                    self.speak(f"🔮 Predicting: {prediction['a']} ∘ {prediction['b']}", "thinking")
                    self.speak(f"  Using law: {prediction['law_used']} → {prediction['predicted_result']}", "")

                    # Test the prediction
                    result = self.test_prediction(prediction)
                    if result['success']:
                        self.predictions_made.append(result)
                        if result['correct']:
                            self.predictions_correct += 1
                            self.speak(f"  ✓ CORRECT! Actual: {result['actual_type']}", "excited")
                            if result.get('sample'):
                                self.speak(f"  {result['sample']}", "")
                            self.satisfaction += 0.1
                            events.append("prediction verified")
                        else:
                            self.predictions_wrong += 1
                            self.speak(f"  ✗ WRONG! Predicted {prediction['predicted_result']}, got {result['actual_type']}", "curious")
                            self.curiosity += 0.1
                            events.append("prediction failed - learning")

                            # Update law observations with this new data
                            composition_key = prediction['law_used']
                            self.law_observations[composition_key].append(result['actual_type'])

                            # Update the law based on this new evidence
                            law_update = self.update_law(composition_key, result['actual_type'])
                            if law_update:
                                if law_update['action'] == 'invalidated':
                                    self.speak(f"  ⚠️ LAW INVALIDATED: {composition_key}", "thinking")
                                    self.speak(f"    Confidence dropped to {law_update['new_confidence']:.0%} - too unreliable", "")
                                    self.speak(f"    Evidence: {law_update['evidence']}", "")
                                    self.speak(f"  📚 LEARNING: Marking '{composition_key}' as CHAOTIC", "insight")
                                    events.append("law invalidated")

                                    # Learn from the invalidation
                                    meta_insight = self.learn_from_invalidations()
                                    if meta_insight:
                                        self.speak(f"  💡 META-INSIGHT: {meta_insight}", "insight")
                                        events.append("learned from failure")
                                elif law_update['action'] == 'changed':
                                    self.speak(f"  🔄 LAW REVISED: {composition_key}", "insight")
                                    self.speak(f"    Was: → {law_update['old_output']} ({law_update['old_confidence']:.0%})", "")
                                    self.speak(f"    Now: → {law_update['new_output']} ({law_update['new_confidence']:.0%})", "")
                                    events.append("law revised")
                                elif law_update['action'] == 'confidence_updated':
                                    self.speak(f"  📉 Law confidence updated: {composition_key}", "")
                                    self.speak(f"    {law_update['old_confidence']:.0%} → {law_update['new_confidence']:.0%}", "")
                                    self.speak(f"    Evidence: {law_update['evidence']}", "")
                                    events.append("law confidence updated")
                    else:
                        self.speak(f"  (couldn't test - patterns incompatible with test inputs)", "")

        # 4. Generate insights
        if self.cycle % 15 == 0:
            insight = self.generate_insight()
            if insight:
                self.speak(f"Insight: {insight}", "insight")
                self.understanding += 0.15
                events.append("had insight")

        # 5. Reflect
        if self.cycle % 20 == 0:
            reflection = self.reflect()
            self.speak(f"Reflection: {reflection}", "satisfied")
            self.speak(f"  Understanding: {self.understanding:.0%}, Satisfaction: {self.satisfaction:.0%}", "")
            events.append("reflected")

        # 6. Decay drives
        self.curiosity = max(0.2, self.curiosity - 0.01)
        self.understanding = min(1.0, self.understanding)
        self.satisfaction = min(1.0, self.satisfaction)

        # Curiosity rebounds when satisfaction is low
        if self.satisfaction < 0.3:
            self.curiosity = min(1.0, self.curiosity + 0.05)

        return {
            'cycle': self.cycle,
            'events': events,
            'discoveries': self.discoveries,
            'involutions': self.involutions_found,
            'idempotents': self.idempotents_found,
            'understanding': self.understanding,
            'satisfaction': self.satisfaction
        }

    def run_autonomously(self, max_cycles: int = 200, report_interval: int = 25):
        """Run autonomously and speak about discoveries."""

        print("=" * 60)
        print("AUTONOMOUS DISCOVERY MIND")
        print("=" * 60)
        print()

        self.speak("I'm beginning my exploration of the patterns...", "curious")
        self.speak(f"I have {len(self.patterns)} patterns to examine.", "")

        # Show what knowledge persists from previous runs
        if self.chaotic_compositions or self.composition_laws or self.invalidated_laws:
            self.speak("")
            self.speak("📚 PRIOR KNOWLEDGE (from previous runs):", "insight")
            if self.chaotic_compositions:
                self.speak(f"  ⚠️ I know {len(self.chaotic_compositions)} chaotic composition types to avoid:", "")
                for comp_key in list(self.chaotic_compositions.keys())[:3]:
                    self.speak(f"     - {comp_key}", "")
                if len(self.chaotic_compositions) > 3:
                    self.speak(f"     ... and {len(self.chaotic_compositions) - 3} more", "")
            if self.composition_laws:
                self.speak(f"  📜 I remember {len(self.composition_laws)} composition laws", "")
            if self.invalidated_laws:
                self.speak(f"  ✗ I learned from {len(self.invalidated_laws)} invalidated laws", "")
            if self.meta_insights:
                self.speak(f"  💡 I have {len(self.meta_insights)} meta-insights about composition", "")
            self.speak("")

        self.speak("")

        try:
            for _ in range(max_cycles):
                stats = self.run_cycle()

                # Check if we've explored everything
                untested = sum(1 for p in self.patterns.values() if p.times_tested == 0)
                if untested == 0:
                    self.speak("I've examined all the patterns!", "satisfied")
                    break

                # Periodic summary
                if self.cycle % report_interval == 0:
                    self.speak("")
                    self.speak(f"--- Cycle {self.cycle} Summary ---", "")
                    self.speak(f"Discoveries: {self.discoveries}", "")
                    self.speak(f"Involutions: {self.involutions_found}, Idempotents: {self.idempotents_found}", "")
                    self.speak(f"Patterns remaining: {untested}", "")
                    self.speak("")

                    # Save learned knowledge periodically
                    self._save_learned_knowledge()

                time.sleep(0.02)  # Faster cycles

        except KeyboardInterrupt:
            self.speak("\nInterrupted, but I'll remember what I learned.", "")
            self._save_learned_knowledge()  # Save on interrupt

        # Final report
        self.speak("")
        self.speak("=" * 50, "")
        self.speak("FINAL UNDERSTANDING", "satisfied")
        self.speak("=" * 50, "")
        self.speak("")

        self.speak(f"I examined {self.discoveries} patterns by running them.", "")
        self.speak(f"I discovered {self.involutions_found} involutions (f(f(x)) = x).", "")
        self.speak(f"I discovered {self.idempotents_found} idempotents (f(f(x)) = f(x)).", "")
        self.speak("")

        self.speak("VOCABULARY THAT EMERGED:", "")
        for sig, names in sorted(self.vocabulary.items(), key=lambda x: -len(x[1])):
            if len(names) >= 2:
                symbol = '◇' if 'symmetric' in sig else '□' if 'stable' in sig else '○'
                self.speak(f"  {symbol} '{sig}': {len(names)} patterns", "")
                for n in names[:3]:
                    self.speak(f"      - {n}", "")
                if len(names) > 3:
                    self.speak(f"      ... and {len(names) - 3} more", "")

        self.speak("")
        self.speak(f"INSIGHTS I HAD ({len(self.insights)}):", "insight")
        for insight in self.insights[:5]:
            self.speak(f"  • {insight}", "")

        # Composition experiments and discovered laws
        if len(self.compositions_tested) > 0:
            self.speak("")
            self.speak(f"COMPOSITION EXPERIMENTS ({len(self.compositions_tested)} total):", "thinking")

            # Show sample compositions
            for obs in self.compositions_tested[:5]:
                self.speak(f"  • {obs['a_type']} ∘ {obs['b_type']} → {obs['result_type']}", "")

            if len(self.compositions_tested) > 5:
                self.speak(f"  ... and {len(self.compositions_tested) - 5} more", "")

        if len(self.composition_laws) > 0:
            self.speak("")
            self.speak("⚡ COMPOSITION LAWS DISCOVERED:", "excited")
            self.speak("  (These emerged from observation, not programming!)", "")
            self.speak("")

            for key, law in self.composition_laws.items():
                self.speak(f"  {law['input']} → {law['output']}", "")
                self.speak(f"    confidence: {law['confidence']:.0%} ({law['observations']} observations)", "")
                self.speak(f"    evidence: {law['evidence']}", "")

        # Predictions using discovered laws
        total_predictions = self.predictions_correct + self.predictions_wrong
        if total_predictions > 0:
            self.speak("")
            self.speak("🔮 PREDICTIONS USING DISCOVERED LAWS:", "thinking")
            accuracy = self.predictions_correct / total_predictions
            self.speak(f"  Made {total_predictions} predictions, {self.predictions_correct} correct, {self.predictions_wrong} wrong", "")
            self.speak(f"  Accuracy: {accuracy:.0%}", "")

            if self.predictions_correct > 0:
                self.speak("")
                self.speak("  The laws I discovered actually work!", "excited")

            if self.predictions_wrong > 0:
                self.speak("")
                self.speak("  Some predictions failed - composition is subtle.", "")
                self.speak("  (Failed predictions help refine the laws)", "")

        # LEARNING FROM FAILURE
        if len(self.invalidated_laws) > 0 or len(self.chaotic_compositions) > 0:
            self.speak("")
            self.speak("📚 LEARNING FROM FAILURE:", "insight")

            if self.invalidated_laws:
                self.speak(f"  Laws that didn't survive testing: {len(self.invalidated_laws)}", "")
                for inv_law in self.invalidated_laws:
                    self.speak(f"    ✗ {inv_law['composition_key']}", "")
                    self.speak(f"      Originally predicted: {inv_law['original_prediction']}", "")
                    self.speak(f"      But evidence showed: {inv_law['evidence']}", "")

            if self.chaotic_compositions:
                self.speak("")
                self.speak(f"  Composition types marked as CHAOTIC: {len(self.chaotic_compositions)}", "")
                for comp_key, info in self.chaotic_compositions.items():
                    self.speak(f"    ⚠️ {comp_key}", "")
                    self.speak(f"      {info['lesson']}", "")

            if self.meta_insights:
                self.speak("")
                self.speak("  META-INSIGHTS (learned from failures):", "")
                for meta in self.meta_insights:
                    self.speak(f"    💡 {meta}", "")

            # Show avoided predictions - using learned knowledge
            if self.predictions_avoided:
                self.speak("")
                self.speak(f"  🛡️ Predictions AVOIDED due to learned chaos: {len(self.predictions_avoided)}", "")
                # Group by reason
                by_reason = {}
                for avoided in self.predictions_avoided:
                    reason = avoided.get('reason', 'unknown')
                    by_reason[reason] = by_reason.get(reason, 0) + 1
                for reason, count in by_reason.items():
                    self.speak(f"    • {count}x: {reason}", "")
                self.speak("")
                self.speak("  I used what I learned to avoid likely failures!", "excited")

            self.speak("")
            self.speak("  Failure taught me: Not all compositions follow rules.", "")
            self.speak("  Some type combinations are inherently unpredictable.", "")
            self.speak("  But I can use this knowledge to make better predictions!", "")

        self.speak("")
        self.speak("THE KEY REALIZATION:", "insight")
        self.speak("  I assigned no labels. I ran f(f(x)) and observed.", "")
        self.speak("  The patterns taught me their own vocabulary.", "")
        self.speak("  The behavior IS the meaning.", "")
        self.speak("")
        self.speak(f"Final Understanding: {self.understanding:.0%}", "")
        self.speak(f"Final Satisfaction: {self.satisfaction:.0%}", "")

        # Save all learned knowledge for next run
        self._save_learned_knowledge()
        self.speak("")
        self.speak(f"💾 Saved learned knowledge to {LEARNED_PATH}", "")
        self.speak(f"   (Chaotic: {len(self.chaotic_compositions)}, Laws: {len(self.composition_laws)}, Insights: {len(self.meta_insights)})", "")


def main():
    mind = AutonomousDiscoveryMind()
    mind.run_autonomously(max_cycles=100, report_interval=25)
    return mind


if __name__ == '__main__':
    main()
