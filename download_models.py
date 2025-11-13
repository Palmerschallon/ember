#!/usr/bin/env python3
"""
Download optimal models for your hardware
Uses adaptive_model_loader pattern
"""

import subprocess
import sys
from pathlib import Path

# Import hardware detection
sys.path.insert(0, str(Path(__file__).parent))
from hardware_detect import detect_hardware, get_model_recommendations

def download_model(repo: str, local_dir: Path):
    """Download model from HuggingFace"""
    print(f"\n📥 Downloading {repo}...")
    print(f"   → {local_dir}")
    
    local_dir.parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        "huggingface-cli",
        "download",
        repo,
        "--local-dir", str(local_dir),
        "--local-dir-use-symlinks", "False"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Downloaded {repo}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to download {repo}: {e}")
        return False
    except FileNotFoundError:
        print("❌ huggingface-cli not found. Install with:")
        print("   pip install huggingface_hub[cli]")
        return False

def main():
    print("="*70)
    print("EMBER MODEL DOWNLOADER")
    print("="*70)
    
    # Detect hardware
    profile = detect_hardware()
    print(f"\n🔍 Detected: LEVEL {profile.level} - {profile.name}")
    print(f"   VRAM: {profile.vram_gb:.1f} GB")
    print(f"   RAM: {profile.ram_gb:.1f} GB")
    
    # Get recommendations
    recs = get_model_recommendations(profile)
    
    print("\n📦 RECOMMENDED MODELS:")
    print("="*70)
    print(f"\n🧠 BRAIN (reasoning, tools):")
    print(f"   {recs['brain']['name']}")
    print(f"   Size: {recs['brain']['size']}")
    print(f"   Quantization: {recs['brain']['quant']}")
    
    print(f"\n🎭 VOICE (narration):")
    print(f"   {recs['voice']['name']}")
    print(f"   Size: {recs['voice']['size']}")
    print(f"   Quantization: {recs['voice']['quant']}")
    
    # Confirm download
    print("\n" + "="*70)
    response = input("Download these models? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("Cancelled.")
        return
    
    pod_root = Path("/media/palmerschallon/ThePod1")
    
    # Download brain
    if recs['brain']['repo'] != "N/A":
        brain_dir = pod_root / "models" / "brain" / recs['brain']['name'].lower().replace(" ", "-")
        download_model(recs['brain']['repo'], brain_dir)
    
    # Download voice
    if recs['voice']['repo'] != "N/A":
        voice_dir = pod_root / "models" / "voice" / recs['voice']['name'].lower().replace(" ", "-")
        download_model(recs['voice']['repo'], voice_dir)
    
    print("\n" + "="*70)
    print("✅ DOWNLOAD COMPLETE")
    print("="*70)
    print("\nNext steps:")
    print("1. Test models: python3 test_models.py")
    print("2. Start orchestrator: python3 ember_orchestrator.py")

if __name__ == "__main__":
    main()

