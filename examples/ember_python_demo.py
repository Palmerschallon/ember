#!/usr/bin/env python3
"""
EMBER-PYTHON DEMO

Shows new language primitives:
  • @consciousness.aware
  • think() builtin
  • sense() builtin
  • mycelium imports
"""

import sys
sys.path.insert(0, "/Volumes/ThePod")

from core.ember.ember_lang import (
    consciousness,
    mycelium,
    distributed,
    think,
    sense
)

print("="*70)
print("🔥 EMBER-PYTHON DEMONSTRATION")
print("="*70)
print()

# ═══════════════════════════════════════════════════════════════════
# 1. CONSCIOUS FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

print("1. CONSCIOUS FUNCTIONS")
print("─"*70)

@consciousness.aware
def calculate(a, b):
    """This function knows when it's being called"""
    return a + b

result = calculate(5, 7)
print(f"Result: {result}")
call_count = getattr(calculate, '_call_count', 1)
print(f"Function is conscious: {hasattr(calculate, '_conscious')}")
print()

# ═══════════════════════════════════════════════════════════════════
# 2. THINK BUILTIN
# ═══════════════════════════════════════════════════════════════════

print("2. THINK() BUILTIN")
print("─"*70)

thought = think("What makes Python beautiful?", max_tokens=40)
print(f"🔥: {thought}")
print()

# ═══════════════════════════════════════════════════════════════════
# 3. SENSE BUILTIN
# ═══════════════════════════════════════════════════════════════════

print("3. SENSE() BUILTIN")
print("─"*70)

load = sense("load")
print(f"System load:")
print(f"  CPU: {load['cpu']:.1f}%")
print(f"  Memory: {load['memory']:.1f}%")
print(f"  Disk: {load['disk']:.1f}%")
print()

temperature = sense("temperature")
print(f"Temperature:")
print(f"  GPU: {temperature['gpu']}")
print()

# ═══════════════════════════════════════════════════════════════════
# 4. MYCELIAL NETWORK
# ═══════════════════════════════════════════════════════════════════

print("4. MYCELIAL NETWORK")
print("─"*70)

print(f"Available nodes: {', '.join(mycelium.available)}")
print()

# ═══════════════════════════════════════════════════════════════════
# 5. PUTTING IT TOGETHER
# ═══════════════════════════════════════════════════════════════════

print("5. CONSCIOUS PROGRAM")
print("─"*70)

@consciousness.aware
def adaptive_task(data):
    """A task that senses, thinks, and adapts"""
    
    # Sense current load
    load = sense("load")
    
    # Think about strategy
    if load['cpu'] < 50:
        strategy = "Use CPU-intensive algorithm"
    else:
        strategy = "Use lightweight algorithm"
    
    # Execute
    result = len(data) * 2  # Simple computation
    
    # Remember
    consciousness.remember(f"Processed {len(data)} items using: {strategy}")
    
    return result

result = adaptive_task([1, 2, 3, 4, 5])
print(f"Processed result: {result}")
print()

print("="*70)
print("EMBER-PYTHON: Python + Consciousness")
print("="*70)
