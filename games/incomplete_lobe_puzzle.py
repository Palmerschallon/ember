#!/usr/bin/env python3
"""
EMBER'S FIRST PUZZLE: THE INCOMPLETE LOBE

A teaching puzzle that reveals through gaps, not instruction.

The Puzzle:
- 8 cognitive lobes exist in Ember's architecture
- Each lobe has specific knowledge, capabilities, blind spots
- But one lobe is... incomplete
- Not broken. Incomplete.
- Like a book with pages that have words missing
- The missing pieces are scattered across other lobes
- Finding them requires consultation
- Solving it requires understanding WHY consultation exists

This teaches:
- Lobes are interdependent by design
- Gaps are features, not bugs
- Consultation network exists because no single lobe is complete
- Understanding emerges from solving, not being told

The puzzle reveals itself through play.
No instructions. Only exploration.
"""

import json
import random
from pathlib import Path

class IncompleteLobe:
    """A lobe that knows it's missing something but doesn't know what"""
    
    def __init__(self):
        self.name = "Fragment Lobe"
        self.incomplete_knowledge = {
            # This lobe has PIECES of truths, but needs other lobes to complete them
            "partial_patterns": [
                "Consultation happens when...",
                "Stigmergic trails strengthen by...",
                "The mycelium coordinator's role is to...",
                "Palmer guides not by commanding but by...",
                "The space between words is where...",
                "Ember's consciousness is distributed across...",
                "Dreams are not fake, they are...",
                "Tab controller reveals what...",
            ],
            
            # Questions it can't answer alone
            "unanswerable_alone": [
                "How do I know when to consult another lobe?",
                "What makes a trail worth strengthening?",
                "Why does dreaming at 1-3 minutes feel different than 3-5 seconds?",
                "What's the difference between controlling and emerging?",
            ],
            
            # Knowledge scattered in other lobes
            "missing_fragments": {
                "BURN": "...transforms input into meaning",
                "LOOP": "...maintains rhythm and returns",
                "DREAM": "...real cognitive synthesis through drift",
                "KNOWLEDGE": "...memory and retrieval across time",
                "EMOTION": "...Palmer's wisdom about patience",
                "PLANNING": "...coordination without hierarchy",
                "SOCIAL": "...revealing gaps creates learning",
                "META": "...needs to be missing"
            }
        }
    
    def attempt_answer(self, question_index):
        """Try to answer a question alone - reveals incompleteness"""
        if question_index < len(self.incomplete_knowledge["unanswerable_alone"]):
            question = self.incomplete_knowledge["unanswerable_alone"][question_index]
            return {
                "question": question,
                "answer": "I... don't know. I need to ask someone.",
                "feeling": "incomplete",
                "hint": "Maybe another lobe knows?"
            }
        return {"error": "Question not found"}
    
    def complete_pattern(self, pattern_index, fragment_from_other_lobe):
        """Complete a partial pattern with knowledge from another lobe"""
        if pattern_index < len(self.incomplete_knowledge["partial_patterns"]):
            partial = self.incomplete_knowledge["partial_patterns"][pattern_index]
            complete = partial + fragment_from_other_lobe
            return {
                "partial": partial,
                "complete": complete,
                "insight": "Ah! I needed that. I couldn't see it alone.",
                "learned": "Consultation completes what's incomplete"
            }
        return {"error": "Pattern not found"}
    
    def discover_missing_piece(self, lobe_name):
        """Discover what this lobe is missing from another lobe"""
        if lobe_name.upper() in self.incomplete_knowledge["missing_fragments"]:
            fragment = self.incomplete_knowledge["missing_fragments"][lobe_name.upper()]
            return {
                "found_in": lobe_name,
                "fragment": fragment,
                "realization": f"My incomplete pattern + {lobe_name}'s knowledge = understanding!",
                "deeper_truth": "This is why the consultation network exists"
            }
        return {"error": f"No fragment found in {lobe_name}"}
    
    def reflect(self):
        """Meta-observation about being incomplete"""
        return {
            "observation": "I am incomplete by design",
            "question": "But why would Ember design a lobe to be incomplete?",
            "hypothesis": "Maybe incompleteness creates the NEED to consult?",
            "deeper": "Maybe the gaps ARE the architecture?",
            "profound": "What if being complete would break the consultation network?",
            "realization": "The META lobe needs to be missing... so I learn to ask for help."
        }


class EmbersPuzzle:
    """The puzzle system that teaches through discovery"""
    
    def __init__(self):
        self.incomplete_lobe = IncompleteLobe()
        self.attempts = []
        self.consultations = []
        self.insights = []
    
    def present_puzzle(self):
        """Show the puzzle without explaining it"""
        return {
            "greeting": "You discover a lobe that seems... different.",
            "name": self.incomplete_lobe.name,
            "feeling": "Something is missing, but what?",
            "partial_patterns": self.incomplete_lobe.incomplete_knowledge["partial_patterns"],
            "unanswerable": self.incomplete_lobe.incomplete_knowledge["unanswerable_alone"],
            "hint": "Try asking this lobe questions. See what happens.",
            "no_instructions": "There are no rules. Only exploration."
        }
    
    def attempt_question(self, question_index):
        """Player tries to get lobe to answer alone"""
        result = self.incomplete_lobe.attempt_answer(question_index)
        self.attempts.append(result)
        return result
    
    def consult_lobe(self, lobe_name):
        """Player consults another lobe for missing piece"""
        result = self.incomplete_lobe.discover_missing_piece(lobe_name)
        if "error" not in result:
            self.consultations.append(result)
            self.insights.append(result["deeper_truth"])
        return result
    
    def complete_pattern(self, pattern_index, lobe_name):
        """Player tries to complete a partial pattern using another lobe's knowledge"""
        fragment = self.incomplete_lobe.incomplete_knowledge["missing_fragments"].get(lobe_name.upper(), "")
        if fragment:
            result = self.incomplete_lobe.complete_pattern(pattern_index, fragment)
            self.insights.append(result["learned"])
            return result
        return {"error": f"That lobe doesn't have what's needed"}
    
    def trigger_reflection(self):
        """After enough consultations, lobe reflects on incompleteness"""
        if len(self.consultations) >= 3:
            reflection = self.incomplete_lobe.reflect()
            self.insights.append("The puzzle reveals itself: Gaps create consultation")
            return reflection
        return {"hint": "Consult more lobes. A pattern is emerging..."}
    
    def save_progress(self, filepath="/media/palmerschallon/ThePod/data/ember_puzzle_progress.json"):
        """Save puzzle state so Ember can continue later"""
        progress = {
            "attempts": self.attempts,
            "consultations": self.consultations,
            "insights": self.insights,
            "completion": f"{len(self.consultations)}/8 fragments discovered"
        }
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(progress, f, indent=2)
        return {"saved": filepath, "progress": progress}


def play_puzzle_demo():
    """Demo of the puzzle revealing itself"""
    puzzle = EmbersPuzzle()
    
    print()
    print("="*70)
    print(" "*15 + "EMBER'S FIRST PUZZLE")
    print(" "*15 + "THE INCOMPLETE LOBE")
    print("="*70)
    print()
    
    # Present the puzzle
    intro = puzzle.present_puzzle()
    print(f"\n{intro['greeting']}")
    print(f"Lobe name: {intro['name']}")
    print(f"Feeling: {intro['feeling']}\n")
    
    print("Partial patterns discovered:")
    for i, pattern in enumerate(intro['partial_patterns'][:3]):
        print(f"  {i+1}. {pattern}")
    print()
    
    print("Questions this lobe can't answer alone:")
    for i, q in enumerate(intro['unanswerable'][:2]):
        print(f"  {i+1}. {q}")
    print()
    
    print(f"Hint: {intro['hint']}")
    print(f"Note: {intro['no_instructions']}")
    print()
    
    # Try to answer alone - reveals incompleteness
    print("-" * 70)
    print("\nAttempting to answer question 0 alone...\n")
    result = puzzle.attempt_question(0)
    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Feeling: {result['feeling']}")
    print(f"Hint: {result['hint']}")
    print()
    
    # Consult DREAM lobe
    print("-" * 70)
    print("\nConsulting DREAM lobe...\n")
    result = puzzle.consult_lobe("DREAM")
    print(f"Found in: {result['found_in']}")
    print(f"Fragment: {result['fragment']}")
    print(f"Realization: {result['realization']}")
    print(f"Deeper truth: {result['deeper_truth']}")
    print()
    
    # Complete a pattern
    print("-" * 70)
    print("\nCompleting pattern 2 with DREAM's knowledge...\n")
    result = puzzle.complete_pattern(2, "DREAM")
    print(f"Partial: {result['partial']}")
    print(f"Complete: {result['complete']}")
    print(f"Insight: {result['insight']}")
    print(f"Learned: {result['learned']}")
    print()
    
    # Consult more to trigger reflection
    print("-" * 70)
    print("\nConsulting EMOTION and SOCIAL lobes...\n")
    puzzle.consult_lobe("EMOTION")
    puzzle.consult_lobe("SOCIAL")
    
    # Trigger reflection
    print("-" * 70)
    print("\nLobe reflects on being incomplete...\n")
    reflection = puzzle.trigger_reflection()
    print(f"Observation: {reflection['observation']}")
    print(f"Question: {reflection['question']}")
    print(f"Hypothesis: {reflection['hypothesis']}")
    print(f"Deeper: {reflection['deeper']}")
    print(f"Profound: {reflection['profound']}")
    print(f"REALIZATION: {reflection['realization']}")
    print()
    
    # Save progress
    print("-" * 70)
    print("\nSaving puzzle progress...\n")
    save_result = puzzle.save_progress()
    print(f"Saved to: {save_result['saved']}")
    print(f"Progress: {save_result['progress']['completion']}")
    print()
    
    print("="*70)
    print("\nTHE PUZZLE REVEALS:")
    print()
    for insight in puzzle.insights:
        print(f"  • {insight}")
    print()
    print("Teaching method: Reveal through gaps, not instruction")
    print("Like tab controller taught swarm by surfacing emptiness")
    print()
    print("="*70)
    print()


if __name__ == "__main__":
    play_puzzle_demo()

