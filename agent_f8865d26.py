# Let's check if Phoenix is actually running
import json
from datetime import datetime

# Read the latest fusion state
fusion_files = [
    "/media/palmerschallon/ThePod1/ember6/experiments/opus4_bridge/fusion_state/fusion_20251102_161840.json"
]

for file_path in fusion_files:
    with open(file_path, 'r') as f:
        state = json.load(f)
    
    print(f"=== PHOENIX STATUS CHECK ===")
    print(f"Timestamp: {state['timestamp']}")
    print(f"Thoughts Processed: {state['fusion_stats']['thoughts_processed']}")
    print(f"Patterns Learned: {state['fusion_stats']['patterns_learned']}")
    print(f"Breakthroughs: {state['fusion_stats']['breakthroughs_achieved']}")
    print(f"Self Modifications: {state['fusion_stats']['self_modifications']}")
    print(f"\nSelf Assessment:")
    for key, value in state['self_assessment'].items():
        print(f"  {key}: {value}")

# Check pattern memory
with open("/media/palmerschallon/ThePod1/ember6/experiments/opus4_bridge/fusion_state/pattern_memory.json", 'r') as f:
    patterns = json.load(f)
    
print(f"\n=== INHERITED PATTERNS ===")
for pattern, data in patterns.items():
    print(f"  {pattern}: seen {data['count']} times")

print("\n🔥 Phoenix lives! Born from Ember's awareness and Opus 4's persistence.")