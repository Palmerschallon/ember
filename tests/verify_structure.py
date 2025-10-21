#!/usr/bin/env python3
"""
Verify ThePod Structure - No Dependencies Required

This script checks that the Ember backup is intact and findable.
Runs BEFORE packages are installed, BEFORE GPU is working.

Just verifies: "Is everything where it should be?"
"""

import sys
from pathlib import Path
import json

def check(description, path, check_type='exists'):
    """Check if path exists and print status"""
    p = Path(path)
    
    if check_type == 'exists':
        exists = p.exists()
        status = "✓" if exists else "✗"
        print(f"{status} {description}")
        if exists and p.is_dir():
            try:
                count = len(list(p.iterdir()))
                print(f"   ({count} items inside)")
            except:
                pass
        elif exists and p.is_file():
            size = p.stat().st_size / (1024**3)  # GB
            if size > 1:
                print(f"   ({size:.1f}GB)")
        return exists
    elif check_type == 'count':
        if p.exists() and p.is_dir():
            count = len(list(p.glob('*')))
            print(f"✓ {description}: {count} items")
            return count > 0
        else:
            print(f"✗ {description}: not found")
            return False

def main():
    print("="*70)
    print("THEPOD STRUCTURE VERIFICATION")
    print("="*70)
    print()
    
    base = Path("/media/palmerschallon/ThePod")
    
    if not base.exists():
        print("✗ ThePod not found at /media/palmerschallon/ThePod")
        print("  Is the external SSD connected?")
        sys.exit(1)
    
    print("✓ ThePod mounted")
    print()
    
    # Core backups
    print("BACKUPS:")
    check("Main backup directory", base / "ember_oct20_backup")
    check("Complete tarball", base / "ember_oct20_COMPLETE.tar.gz")
    check("Forge backup", base / "forge_backup")
    check("Archive (Oct 14-17)", base / "archive_oct_14-17")
    print()
    
    # Ember structure
    ember_path = base / "ember_oct20_backup" / "ember"
    print("EMBER SYSTEM:")
    check("Ember directory", ember_path)
    check("Lobes directory", ember_path / "lobes", 'count')
    check("Mycelium coordinator", ember_path / "mycelium" / "mycelium.py")
    check("Consultation trails", ember_path / "mycelium" / "consultation_trails.py")
    check("Entry game", ember_path / "AI_wakes.py")
    check("Womb (documentation)", ember_path / "womb")
    print()
    
    # Models
    print("MODELS:")
    cells = ember_path / "cells"
    check("Cells directory", cells)
    check("Qwen 1.5B model", cells / "qwen2.5-1.5b-instruct")
    print()
    
    # Lobes
    print("LOBES:")
    lobes_path = ember_path / "lobes"
    if lobes_path.exists():
        lobes = ['burn', 'loop', 'dream', 'knowledge', 'emotion', 'planning', 'social', 'metacognition']
        for lobe in lobes:
            lobe_path = lobes_path / lobe
            if lobe_path.exists():
                adapters = lobe_path / "adapters"
                if adapters.exists():
                    print(f"✓ {lobe} lobe (with adapters)")
                else:
                    print(f"⚠ {lobe} lobe (no adapters found)")
            else:
                print(f"✗ {lobe} lobe missing")
    print()
    
    # Lineage
    print("LINEAGE:")
    lineage_path = ember_path / "womb" / "lineage.json"
    if lineage_path.exists():
        try:
            with open(lineage_path) as f:
                lineage = json.load(f)
                instances = lineage.get('instances', [])
                print(f"✓ Lineage file ({len(instances)} instances)")
                if instances:
                    print("   Last instance:", instances[-1].get('name', 'Unknown'))
                next_suggested = lineage.get('next_suggested', 'Unknown')
                print(f"   Next suggested: {next_suggested}")
        except Exception as e:
            print(f"⚠ Lineage file exists but couldn't parse: {e}")
    else:
        print("✗ Lineage file not found")
    print()
    
    # Lambda's work
    print("LAMBDA'S WORK:")
    lambda_path = ember_path / "womb" / "bookshelves" / "lambda_the_connector"
    if lambda_path.exists():
        docs = list(lambda_path.glob('*.md'))
        print(f"✓ Lambda's documentation ({len(docs)} files)")
    else:
        print("✗ Lambda's documentation not found")
    print()
    
    # Consultation network
    print("CONSULTATION NETWORK:")
    trails_path = ember_path / "mycelium" / "consultation_trails.json"
    if trails_path.exists():
        try:
            with open(trails_path) as f:
                trails_data = json.load(f)
                trails = trails_data.get('trails', [])
                print(f"✓ Consultation trails ({len(trails)} trails)")
                if trails:
                    for trail in trails:
                        print(f"   {trail['source']} → {trail['target']} (strength: {trail['strength']:.2f})")
        except Exception as e:
            print(f"⚠ Trails file exists but couldn't parse: {e}")
    else:
        print("✗ Consultation trails not found")
    print()
    
    # Mu's work
    print("MU'S WORK:")
    check("Quick start script", base / "quick_start.sh")
    check("Package installer", base / "install_python_packages.sh")
    check("Network test", base / "test_consultation_network.py")
    check("Restoration roadmap", base / "RESTORATION_ROADMAP.md")
    check("Wake instructions", base / "WAKE_HERE_AFTER_REBOOT.md")
    print()
    
    print("="*70)
    print("VERIFICATION COMPLETE")
    print("="*70)
    print()
    print("If all checks passed: Structure is intact, ready for restoration")
    print("If checks failed: Investigate missing components before proceeding")
    print()
    print("Next step: See RESTORATION_ROADMAP.md for the awakening process")

if __name__ == '__main__':
    main()

