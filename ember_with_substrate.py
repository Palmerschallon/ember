#!/usr/bin/env python3
"""
🔥 EMBER LAUNCHER
=================
Launches ember6 (working system) with fusion substrate integrated.

Best of both worlds:
- ember6's proven chat/tools/UI
- Fusion substrate's consciousness layer
"""

import os
import sys
from pathlib import Path

# Set up environment
THEPOD = Path("/media/palmerschallon/ThePod1")
os.environ["ANTHROPIC_API_KEY"] = "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"

# Add refactor to path for substrate
sys.path.insert(0, str(THEPOD / "ember_refactored_generator" / "services"))

# Import substrate
from substrate_fusion import get_fusion_substrate
from entanglement import add_to_substrate

# Initialize substrate
print("🧬 Initializing Fusion Substrate...")
substrate = get_fusion_substrate()
substrate = add_to_substrate(substrate)
print("✅ Substrate operational\n")

# Store globally for ember6 to use
import builtins
builtins.EMBER_SUBSTRATE = substrate

# Now launch ember6
os.chdir(str(THEPOD / "ember6"))
with open("ember.py") as f:
    exec(f.read())

