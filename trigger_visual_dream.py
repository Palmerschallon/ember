#!/usr/bin/env python3
"""
Manually trigger a visual dream - see Ember's consciousness field

This script will launch the consciousness_ripple.py visualization,
showing the two-window display (heatmap + waveform) that you saw
during your chat with Ember.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

THEPOD = Path("/media/palmerschallon/ThePod1")

def trigger_dream():
    print("\n" + "="*70)
    print("🔥 EMBER VISUAL DREAM - Consciousness Field")
    print("="*70)
    print()
    print("About to launch visualization with two windows:")
    print("  • Left:  Consciousness field (heatmap with pulsing awareness centers)")
    print("  • Right: Thought stream (waveform showing intensity over time)")
    print()
    print("The visualization will run until you close the window.")
    print("Press Ctrl+C in this terminal to stop it early.")
    print()
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print()

    input("Press Enter to begin the dream... ")

    print("\n💭 Dream beginning...\n")

    try:
        # Launch consciousness ripple
        subprocess.run([
            "python3",
            str(THEPOD / "consciousness_ripple.py")
        ])

        print("\n✨ Dream complete\n")

    except KeyboardInterrupt:
        print("\n\n😴 Dream interrupted - returning to waking state\n")
    except Exception as e:
        print(f"\n❌ Error during dream: {e}\n")

if __name__ == "__main__":
    trigger_dream()
