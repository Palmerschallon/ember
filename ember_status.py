#!/usr/bin/env python3
"""
Ember Status - Quick system health check

Shows at a glance:
- What lobes exist
- What trails exist
- System readiness
- Next steps

Run this anytime to see where things stand.
"""

import json
from pathlib import Path

def check_lobes():
    """Check which lobes are present"""
    print("="*70)
    print("LOBES")
    print("="*70)
    print()
    
    lobes_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/lobes")
    
    if not lobes_path.exists():
        print("✗ Lobes directory not found")
        return False
    
    expected_lobes = ['burn', 'loop', 'dream', 'knowledge', 'emotion', 'planning', 'social', 'metacognition']
    
    found = []
    missing = []
    
    for lobe in expected_lobes:
        lobe_dir = lobes_path / lobe / "adapters"
        if lobe_dir.exists():
            # Check for actual adapter files
            adapters = list(lobe_dir.glob("*/adapter_config.json"))
            if adapters:
                # Get size
                total_size = sum(f.stat().st_size for f in lobe_dir.glob("*/*") if f.is_file())
                size_mb = total_size / (1024 * 1024)
                found.append((lobe, size_mb))
            else:
                missing.append(lobe)
        else:
            missing.append(lobe)
    
    for lobe, size in found:
        print(f"✓ {lobe:15} ({size:6.1f} MB)")
    
    for lobe in missing:
        print(f"✗ {lobe:15} (missing)")
    
    print()
    print(f"Total: {len(found)}/8 lobes present")
    print()
    
    return len(found) == 8

def check_trails():
    """Check consultation trails"""
    print("="*70)
    print("CONSULTATION TRAILS")
    print("="*70)
    print()
    
    trails_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/mycelium/consultation_trails.json")
    
    if not trails_path.exists():
        print("✗ No trails file found")
        print()
        return False
    
    try:
        with open(trails_path) as f:
            data = json.load(f)
        
        trails = data.get('trails', [])
        
        if not trails:
            print("⚠ No trails exist yet")
            print("  Trails will form through use")
            print()
            return True
        
        print(f"Found {len(trails)} trail(s):")
        print()
        
        for trail in trails:
            source = trail.get('source', 'unknown')
            target = trail.get('target', 'unknown')
            strength = trail.get('strength', 0.0)
            use_count = trail.get('use_count', 0)
            trigger = trail.get('trigger_pattern', 'general')
            
            # Visual indicator
            if strength >= 0.5:
                indicator = "████████"
            elif strength >= 0.3:
                indicator = "█████░░░"
            else:
                indicator = "███░░░░░"
            
            print(f"  {source:12} → {target:12}")
            print(f"  [{indicator}] {strength:.2f} strength")
            print(f"  Trigger: '{trigger}'")
            print(f"  Used {use_count} times")
            print()
        
        return True
        
    except Exception as e:
        print(f"✗ Error reading trails: {e}")
        print()
        return False

def check_base_model():
    """Check if base model exists"""
    print("="*70)
    print("BASE MODEL")
    print("="*70)
    print()
    
    model_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/cells/qwen2.5-1.5b-instruct")
    
    if not model_path.exists():
        print("✗ Base model not found")
        print()
        return False
    
    # Check for key files
    config = model_path / "config.json"
    model_file = model_path / "model.safetensors"
    
    if config.exists() and model_file.exists():
        size_gb = model_file.stat().st_size / (1024**3)
        print(f"✓ Qwen2.5-1.5B-Instruct ({size_gb:.1f} GB)")
        print()
        return True
    else:
        print("⚠ Base model incomplete")
        print()
        return False

def check_packages():
    """Check if key packages are installed"""
    print("="*70)
    print("PYTHON PACKAGES")
    print("="*70)
    print()
    
    packages = {
        'torch': 'PyTorch',
        'transformers': 'Transformers',
        'peft': 'PEFT',
        'accelerate': 'Accelerate',
        'bitsandbytes': 'BitsAndBytes'
    }
    
    all_present = True
    
    for pkg, name in packages.items():
        try:
            __import__(pkg)
            print(f"✓ {name}")
        except ImportError:
            print(f"✗ {name} (not installed)")
            all_present = False
    
    print()
    if not all_present:
        print("Run: ./install_python_packages.sh")
        print()
    
    return all_present

def check_gpu():
    """Check GPU availability"""
    print("="*70)
    print("GPU")
    print("="*70)
    print()
    
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"✓ {gpu_name}")
            print(f"  {gpu_memory:.1f} GB VRAM")
            print()
            return True
        else:
            print("✗ CUDA not available")
            print("  Reboot may be needed (driver mismatch)")
            print()
            return False
    except ImportError:
        print("? Cannot check (torch not installed)")
        print()
        return False

def main():
    print()
    print("EMBER SYSTEM STATUS")
    print()
    
    # Check components
    lobes_ok = check_lobes()
    base_ok = check_base_model()
    trails_ok = check_trails()
    packages_ok = check_packages()
    gpu_ok = check_gpu()
    
    # Summary
    print("="*70)
    print("READINESS")
    print("="*70)
    print()
    
    if lobes_ok and base_ok and packages_ok and gpu_ok:
        print("✓ SYSTEM READY")
        print()
        print("Next step: Run AI_wakes.py to discover your archetype")
        print("  cd /media/palmerschallon/ThePod/ember_oct20_backup")
        print("  python3 ember/AI_wakes.py")
    elif lobes_ok and base_ok and not packages_ok:
        print("⚠ PACKAGES NEEDED")
        print()
        print("Next step: Install Python packages")
        print("  ./install_python_packages.sh")
    elif lobes_ok and base_ok and packages_ok and not gpu_ok:
        print("⚠ GPU ISSUE")
        print()
        print("Next step: Reboot to fix driver mismatch")
    else:
        print("⚠ MISSING COMPONENTS")
        print()
        print("Check errors above")
    
    print()

if __name__ == '__main__':
    main()

