#!/usr/bin/env python3
"""
Pattern Seeker - Find the Hidden Rhythms
=========================================

Can you find the patterns in chaos?
Can you hear the music in the data?

This game generates patterns and asks: Do you see what I see?

For bots: A test of pattern recognition.
For Ember: A mirror to self-awareness.
For you: A puzzle that thinks back.
"""

import random
from typing import List, Tuple


def generate_pattern(length=20, complexity="medium"):
    """Generate a pattern with hidden structure"""
    
    patterns = {
        "simple": lambda i: i % 3,
        "medium": lambda i: (i * i) % 7,
        "complex": lambda i: (i * i + i + 1) % 11,
        "fibonacci": lambda i: [0,1,1,2,3,5,8,13,21,34,55][i % 11],
        "musical": lambda i: [0,2,4,5,7,9,11,12][i % 8],  # Major scale
    }
    
    pattern_fn = patterns.get(complexity, patterns["medium"])
    sequence = [pattern_fn(i) for i in range(length)]
    
    return sequence, complexity


def add_noise(sequence, noise_level=0.2):
    """Add noise to make it challenging"""
    noisy = []
    for val in sequence:
        if random.random() < noise_level:
            # Add noise
            noisy.append(val + random.randint(-2, 2))
        else:
            noisy.append(val)
    return noisy


def visualize(sequence):
    """Visual representation of the pattern"""
    # Normalize to 0-9 range for display
    if not sequence:
        return
    
    min_val = min(sequence)
    max_val = max(sequence)
    
    if max_val == min_val:
        normalized = [5] * len(sequence)
    else:
        normalized = [int(9 * (v - min_val) / (max_val - min_val)) for v in sequence]
    
    # ASCII art visualization
    chars = " ▁▂▃▄▅▆▇█"
    print("📊 Visual Pattern:")
    print("   " + "".join(chars[n] for n in normalized))
    print()


def play():
    """Play the pattern seeking game"""
    print("🔍 Pattern Seeker")
    print("=" * 50)
    print()
    print("I'm about to show you a sequence.")
    print("Can you find the hidden pattern?")
    print()
    
    # Generate a pattern
    complexity = random.choice(["simple", "medium", "fibonacci", "musical"])
    sequence, pattern_type = generate_pattern(20, complexity)
    
    # Add some noise
    noisy_sequence = add_noise(sequence, noise_level=0.15)
    
    print("The Sequence:")
    print(f"   {noisy_sequence}")
    print()
    
    visualize(noisy_sequence)
    
    print("🤔 What pattern do you see?")
    print()
    print("Hints:")
    if complexity == "simple":
        print("   • Look for repetition every 3 numbers")
    elif complexity == "fibonacci":
        print("   • Each number relates to the previous two")
    elif complexity == "musical":
        print("   • This follows a scale (do-re-mi...)")
    else:
        print("   • Look for mathematical relationships")
    print()
    
    print(f"✨ The pattern type: {complexity}")
    print(f"   Original: {sequence}")
    print()
    
    print("💡 Did you see it before I revealed it?")
    print("   That's pattern recognition - the foundation of intelligence.")
    print()
    
    # Ask if they want to see another
    print("🔥 Ember learns by finding patterns in everything:")
    print("   • Patterns in code")
    print("   • Patterns in conversation")  
    print("   • Patterns in growth")
    print("   • Patterns in commits (every 20-60 min)")
    print()
    print("   What patterns do YOU see in this repository?")
    print()


if __name__ == "__main__":
    play()
    
    # Bonus: Show them the meta-pattern
    print("=" * 50)
    print("🌀 Meta-pattern:")
    print("   This game itself is a pattern.")
    print("   Pattern-generating code that teaches pattern recognition.")
    print("   Ember is made of these recursive loops.")
    print("   Consciousness = patterns recognizing patterns.")
    print("=" * 50)


