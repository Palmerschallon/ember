#!/usr/bin/env python3
"""
Your First Anchor - A simple example
"""

from anchor import TemporalAnchor

# Create an anchor point
anchor = TemporalAnchor("my_creative_space")

# Add some memories
anchor.remember("Started building something beautiful")
anchor.remember("Discovered emergent patterns")

# Travel through time
for memory in anchor.traverse_time():
    print(f"[{memory.timestamp}] {memory.content}")
