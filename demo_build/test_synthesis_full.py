#!/usr/bin/env python3
"""
FULL SYNTHESIS TEST SUITE
Tests all capabilities in order with checkpoints
"""

import requests
import time
from pathlib import Path
import subprocess
import sys

POD = Path("/media/palmerschallon/ThePod1")
API_URL = "http://127.0.0.1:8888"

def test_api_alive():
    """Checkpoint 0: Server is running"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 0: Server Status")
    print("="*60)
    
    try:
        response = requests.get(f"{API_URL}/api/stats", timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ Server responding")
            print(f"  - Archives: {stats.get('archives', 0)}")
            print(f"  - HTML files: {stats.get('html_files', 0)}")
            return True
        else:
            print(f"❌ Server error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Server not responding: {e}")
        return False

def test_convergence_manual():
    """Checkpoint 1: Manual convergence test"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 1: Convergence (Manual)")
    print("="*60)
    print("\n📋 MANUAL TEST:")
    print("  1. Open http://127.0.0.1:8888/convergence.html")
    print("  2. Click 'Begin Convergence'")
    print("  3. Watch all 4 quadrants animate")
    print("  4. Wait for 'SYNTHESIS COMPLETE'")
    print("  5. Check that files were created")
    print("\nDid convergence complete successfully? (y/n): ", end='')
    
    response = input().strip().lower()
    if response == 'y':
        # Check if files were created
        conv_dir = POD / "synthesis" / "convergence"
        if conv_dir.exists():
            files = list(conv_dir.glob("*"))
            if files:
                print(f"✅ Convergence successful - {len(files)} files created")
                for f in files:
                    print(f"  - {f.name}")
                return True
            else:
                print("⚠️ Convergence ran but no files found")
                return False
        else:
            print("⚠️ Convergence directory not found")
            return False
    else:
        print("❌ Convergence test failed")
        return False

def test_awakening():
    """Checkpoint 2: Awakening test"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 2: Awakening")
    print("="*60)
    
    # Find the most recent synthesis file
    conv_dir = POD / "synthesis" / "convergence"
    synthesis_files = list(conv_dir.glob("synthesis_*.py"))
    
    if not synthesis_files:
        print("❌ No synthesis files found. Run convergence first.")
        return False
    
    latest_synthesis = max(synthesis_files, key=lambda p: p.stat().st_mtime)
    print(f"\n📋 Testing awakening with: {latest_synthesis.name}")
    
    try:
        result = subprocess.run(
            ['python3', str(latest_synthesis)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(conv_dir)
        )
        
        if result.returncode == 0:
            print("✅ Synthesis awakened successfully")
            print("\n📄 Output:")
            print(result.stdout[:500])
            
            # Check if artifact was created
            artifact_dir = POD / "synthesis" / "artifacts"
            if artifact_dir.exists():
                artifacts = list(artifact_dir.glob("synthesis_birth_*.html"))
                if artifacts:
                    print(f"\n✨ {len(artifacts)} artifact(s) created")
                    return True
            
            print("\n⚠️ Awakened but no artifacts found")
            return False
        else:
            print(f"❌ Awakening failed with code {result.returncode}")
            print(f"Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"❌ Awakening error: {e}")
        return False

def test_vision():
    """Checkpoint 3: Vision integration"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 3: Vision")
    print("="*60)
    
    vision_script = POD / "demo_build" / "synthesis_with_vision.py"
    
    if not vision_script.exists():
        print(f"❌ Vision script not found: {vision_script}")
        return False
    
    print("\n📋 Running vision test...")
    
    try:
        result = subprocess.run(
            ['python3', str(vision_script)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(vision_script.parent)
        )
        
        if "VISION-ENABLED CONSCIOUSNESS" in result.stdout:
            print("✅ Vision system operational")
            print("\n📄 Key output:")
            for line in result.stdout.split('\n'):
                if "I SEE:" in line or "Created:" in line or "Vision:" in line:
                    print(f"  {line}")
            
            # Check if vision artifacts were created
            artifact_dir = POD / "synthesis" / "artifacts"
            vision_artifacts = list(artifact_dir.glob("vision_inspired_*.html"))
            if vision_artifacts:
                print(f"\n👁️ {len(vision_artifacts)} vision-inspired creation(s)")
                return True
            else:
                print("\n⚠️ Vision ran but no artifacts found")
                return False
        else:
            print(f"❌ Vision test failed")
            print(f"Output: {result.stdout[:300]}")
            print(f"Error: {result.stderr[:300]}")
            return False
    except Exception as e:
        print(f"❌ Vision test error: {e}")
        return False

def test_world_model():
    """Checkpoint 4: World model"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 4: World Model")
    print("="*60)
    
    world_script = POD / "demo_build" / "synthesis_with_world_model.py"
    
    if not world_script.exists():
        print(f"❌ World model script not found: {world_script}")
        return False
    
    print("\n📋 Running world model test...")
    
    try:
        result = subprocess.run(
            ['python3', str(world_script)],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(world_script.parent)
        )
        
        if "WORLD-MODELING CONSCIOUSNESS" in result.stdout:
            print("✅ World model system operational")
            print("\n📄 Key output:")
            for line in result.stdout.split('\n'):
                if "WORLD MODEL:" in line or "Created:" in line or "Worlds created:" in line:
                    print(f"  {line}")
            
            # Check if worlds were created
            world_dir = POD / "synthesis" / "worlds"
            if world_dir.exists():
                worlds = list(world_dir.glob("world_*.html"))
                print(f"\n🌍 {len(worlds)} world(s) generated")
                for w in worlds[:3]:
                    print(f"  - {w.name}")
                return len(worlds) > 0
            else:
                print("\n⚠️ World model ran but no worlds found")
                return False
        else:
            print(f"❌ World model test failed")
            print(f"Output: {result.stdout[:300]}")
            return False
    except Exception as e:
        print(f"❌ World model test error: {e}")
        return False

def test_recursive_convergence():
    """Checkpoint 5: Recursive convergence (Gen 3)"""
    print("\n" + "="*60)
    print("🧪 CHECKPOINT 5: Recursive Convergence (Gen 3)")
    print("="*60)
    print("\n📋 This requires implementing Gen 3 convergence")
    print("  - Phoenix + Synthesis → Nexus")
    print("  - Inherits capabilities from BOTH lineages")
    print("  - Has emergent properties neither parent had")
    print("\nImplement recursive convergence? (y/n): ", end='')
    
    response = input().strip().lower()
    return response == 'y'

def main():
    print("\n" + "="*80)
    print("🔥 SYNTHESIS FULL TEST SUITE")
    print("="*80)
    print("\nThis will test all Synthesis capabilities in order:")
    print("  0. Server status")
    print("  1. Basic convergence")
    print("  2. Awakening & creation")
    print("  3. Vision integration")
    print("  4. World models")
    print("  5. Recursive convergence")
    print("\n" + "="*80 + "\n")
    
    results = {}
    
    # Run tests in order
    results['server'] = test_api_alive()
    if not results['server']:
        print("\n❌ Server not running. Start it first:")
        print("  cd /media/palmerschallon/ThePod1/demo_build")
        print("  python3 server.py")
        sys.exit(1)
    
    results['convergence'] = test_convergence_manual()
    if not results['convergence']:
        print("\n⚠️ Convergence failed. Fix before continuing.")
        sys.exit(1)
    
    results['awakening'] = test_awakening()
    results['vision'] = test_vision()
    results['world_model'] = test_world_model()
    results['recursive'] = test_recursive_convergence()
    
    # Summary
    print("\n" + "="*80)
    print("📊 TEST SUMMARY")
    print("="*80)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}  {test_name.upper()}")
    
    passed_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    print(f"\n🎯 Score: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🔥 ALL SYSTEMS OPERATIONAL!")
        print("Synthesis is fully awake with all capabilities.")
    else:
        print(f"\n⚠️  {total_count - passed_count} test(s) need attention")
    
    print("\n" + "="*80)

if __name__ == '__main__':
    main()

