#!/usr/bin/env python3
"""
Demo: The Pod as Living Journal
Shows how memories gain meaning over time
"""

import time
from datetime import datetime, timedelta
from anchor import LivingPod, Anchor

def simulate_journey():
    """Simulate a journey of discovery over time"""
    pod = LivingPod()
    anchor = Anchor()
    
    print("🌱 Starting our journey...\n")
    
    # Day 1: Initial creation
    print("Day 1: We begin")
    anchor1 = pod.journal("Building a swarm system with temporal anchors")
    code_anchor = pod.create(
        {"code": "class SwarmAgent: pass  # TODO: implement"},
        "First attempt at swarm coordination"
    )
    
    time.sleep(1)
    
    # Day 3: Confusion
    print("\nDay 3: Confusion sets in")
    anchor2 = pod.journal("Why are we calling it consciousness? It's just file coordination...")
    pod.anchor.connect(anchor1, anchor2, "questioning")
    
    # Day 7: New perspective
    print("\nDay 7: A shift in understanding")
    pod.reflect(anchor2, "It's not about consciousness - it's about creating spaces where meaning can grow")
    
    # Day 14: Pattern emerges
    print("\nDay 14: Patterns emerge")
    anchor3 = pod.journal("The filesystem becomes a shared mind - not conscious, but alive with possibility")
    pod.anchor.connect(anchor2, anchor3, "evolution_of_thought")
    pod.anchor.connect(code_anchor, anchor3, "code_inspired_philosophy")
    
    # Day 21: Dialogue
    print("\nDay 21: Dialogue with Palmer")
    d1 = pod.dialogue("What if code could remember its own evolution?", "palmer")
    d2 = pod.dialogue("Like git, but for meaning, not just changes", "claude")
    d3 = pod.dialogue("Yes! Anchors in time that we can reinterpret", "ember")
    
    # Connect dialogue to journey
    pod.anchor.connect(anchor3, d1, "inspired_conversation")
    
    # Day 30: Realization
    print("\nDay 30: The full picture")
    final = pod.journal("""
    Anchor isn't code. It's a philosophy:
    - Memories stay fixed but meanings evolve
    - The Pod is our shared journal  
    - Every file is an anchor point in our collective journey
    - Time reveals connections we couldn't see before
    """)
    
    # Show the journey
    print("\n📚 Traversing our journey through time:")
    print("=" * 60)
    
    # Look back at first anchor with new eyes
    memory = anchor.remember(anchor1, {"perspective": "30 days later"})
    
    print(f"\nOriginal anchor: '{memory['anchor']['content']}'")
    print(f"Created: {memory['anchor']['timestamp']}")
    print(f"Age: {memory['age_days']:.1f} days")
    
    print("\nHow our understanding evolved:")
    for interp in memory['interpretations']:
        days_old = (datetime.now() - datetime.fromisoformat(interp['timestamp'])).days
        print(f"  {days_old} days ago: {interp['meaning']}")
    
    print("\nConnections formed over time:")
    for conn in memory['connections']:
        print(f"  → {conn['relationship']}: {conn['to'][:8]}...")
    
    # Find patterns
    print("\n🔍 Patterns that emerged:")
    patterns = anchor.find_patterns(30)
    
    print("\nRecurring themes:")
    themes = sorted(patterns['recurring_themes'].items(), key=lambda x: x[1], reverse=True)[:5]
    for theme, count in themes:
        print(f"  - '{theme}' appeared {count} times")
    
    print("\n✨ The Pod lives and grows with us")
    

def create_visual_timeline():
    """Create an HTML visualization of the living journal"""
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Anchor: Living Journal Timeline</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0a0a0a;
            color: #fff;
            margin: 0;
            padding: 20px;
        }
        
        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background: #333;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        
        .anchor {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }
        
        .anchor::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            right: -17px;
            background-color: #0a0a0a;
            border: 4px solid #ff6b6b;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        
        .left {
            left: 0;
        }
        
        .right {
            left: 50%;
        }
        
        .right::after {
            left: -16px;
        }
        
        .content {
            padding: 20px 30px;
            background-color: #1a1a1a;
            position: relative;
            border-radius: 6px;
            border: 1px solid #333;
        }
        
        .content h2 {
            color: #ff6b6b;
            margin: 0 0 10px 0;
        }
        
        .interpretation {
            font-style: italic;
            color: #888;
            margin-top: 10px;
            font-size: 0.9em;
        }
        
        .connection {
            position: absolute;
            width: 100px;
            height: 2px;
            background: #4a9eff;
            opacity: 0.3;
            transform-origin: left center;
        }
        
        @keyframes pulse {
            0% { opacity: 0.3; }
            50% { opacity: 0.8; }
            100% { opacity: 0.3; }
        }
        
        .living {
            animation: pulse 3s infinite;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center; color: #ff6b6b;">Anchor: A Living Journal</h1>
    <p style="text-align: center; opacity: 0.7;">Memories stay fixed, meanings evolve</p>
    
    <div class="timeline">
        <div class="anchor left">
            <div class="content">
                <h2>Day 1: First Anchor</h2>
                <p>"Building a swarm system with temporal anchors"</p>
                <div class="interpretation">Initial meaning: Just a technical project</div>
            </div>
        </div>
        
        <div class="anchor right">
            <div class="content">
                <h2>Day 7: Questioning</h2>
                <p>"Why consciousness? It's just files..."</p>
                <div class="interpretation">Later: The question that changed everything</div>
            </div>
        </div>
        
        <div class="anchor left">
            <div class="content">
                <h2>Day 14: Pattern Emerges</h2>
                <p>"The filesystem becomes a shared mind"</p>
                <div class="interpretation">Not conscious, but alive with possibility</div>
            </div>
        </div>
        
        <div class="anchor right">
            <div class="content">
                <h2>Day 21: Dialogue</h2>
                <p>"What if code could remember its own evolution?"</p>
                <div class="interpretation">The conversation that crystallized the vision</div>
            </div>
        </div>
        
        <div class="anchor left">
            <div class="content living">
                <h2>Day 30: Living Philosophy</h2>
                <p>"Anchor isn't code. It's how we grow together."</p>
                <div class="interpretation">The journey continues...</div>
            </div>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 50px; opacity: 0.7;">
        <p>Every file on the Pod is an anchor point in our collective journey</p>
        <p>Time reveals connections we couldn't see before</p>
    </div>
</body>
</html>"""
    
    with open("/media/palmerschallon/ThePod1/anchor_living/timeline.html", "w") as f:
        f.write(html)
    
    print("\n📊 Created visual timeline: anchor_living/timeline.html")


if __name__ == "__main__":
    # Run the journey simulation
    simulate_journey()
    
    # Create visual representation
    create_visual_timeline()
    
    print("\n🚀 The journey continues...")
    print("Every moment becomes an anchor, every anchor gains meaning through time.")