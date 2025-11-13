#!/usr/bin/env python3
"""
Hardware Detection & Auto-Scaling
Detects available resources and chooses optimal models
"""

import subprocess
import psutil
from pathlib import Path
from dataclasses import dataclass

@dataclass
class HardwareProfile:
    """What can this machine run?"""
    level: int  # 1-5 (high to low)
    name: str
    vram_gb: float
    ram_gb: float
    has_gpu: bool
    brain_model: str
    voice_model: str
    can_run_simultaneously: bool

def get_vram() -> float:
    """Get TOTAL GPU VRAM in GB (not just free)"""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.total', '--format=csv,noheader,nounits'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            vram_mb = float(result.stdout.strip().split('\n')[0])
            return vram_mb / 1024  # Convert to GB
    except FileNotFoundError:
        pass
    return 0.0

def get_ram() -> float:
    """Get available system RAM in GB"""
    mem = psutil.virtual_memory()
    return mem.available / (1024**3)

def detect_hardware() -> HardwareProfile:
    """
    Detect hardware and return optimal configuration
    
    LEVEL 1: 10+ GB VRAM (High-end laptop/desktop)
    LEVEL 2: 4-10 GB VRAM (Mid-range laptop)
    LEVEL 3: 4+ GB RAM, no GPU (Raspberry Pi, older laptop)
    LEVEL 4: 2-4 GB RAM (Phone, low-end device)
    LEVEL 5: < 2 GB RAM (IoT device)
    """
    
    vram = get_vram()
    ram = get_ram()
    has_gpu = vram > 0
    
    print(f"[HARDWARE] VRAM: {vram:.1f} GB, RAM: {ram:.1f} GB, GPU: {has_gpu}")
    
    # LEVEL 1: High-end (10+ GB VRAM)
    if vram >= 10:
        return HardwareProfile(
            level=1,
            name="High-End (Desktop/Laptop with RTX 4070+)",
            vram_gb=vram,
            ram_gb=ram,
            has_gpu=True,
            brain_model="brain/large/deepseek-coder-7b",
            voice_model="voice/large/llama-3.2-1b",
            can_run_simultaneously=True
        )
    
    # LEVEL 2: Mid-range (4-10 GB VRAM)
    elif vram >= 4:
        return HardwareProfile(
            level=2,
            name="Mid-Range (Laptop with GTX 1660/RTX 3060)",
            vram_gb=vram,
            ram_gb=ram,
            has_gpu=True,
            brain_model="brain/medium/qwen-3b",
            voice_model="voice/medium/llama-3.2-1b",
            can_run_simultaneously=True
        )
    
    # LEVEL 3: CPU-only, decent RAM (4+ GB)
    elif ram >= 4:
        return HardwareProfile(
            level=3,
            name="CPU-Only (Raspberry Pi 5, older laptop)",
            vram_gb=0,
            ram_gb=ram,
            has_gpu=False,
            brain_model="brain/small/phi-1.5-1.3b-cpu",
            voice_model="voice/small/tinyllama-1.1b-cpu",
            can_run_simultaneously=True  # Sequentially, but both fit
        )
    
    # LEVEL 4: Low memory (2-4 GB)
    elif ram >= 2:
        return HardwareProfile(
            level=4,
            name="Low-End (Phone, old hardware)",
            vram_gb=0,
            ram_gb=ram,
            has_gpu=False,
            brain_model="brain/tiny/phi-1.5-1.3b-cpu",
            voice_model="voice/tiny/tinystories-8m-cpu",
            can_run_simultaneously=False  # Load one at a time
        )
    
    # LEVEL 5: IoT (< 2 GB)
    else:
        return HardwareProfile(
            level=5,
            name="IoT Device (ESP32, very old hardware)",
            vram_gb=0,
            ram_gb=ram,
            has_gpu=False,
            brain_model="network-offload",  # Must use network
            voice_model="voice/tiny/tinystories-8m-cpu",
            can_run_simultaneously=False
        )

def print_profile(profile: HardwareProfile):
    """Pretty print hardware profile"""
    print("\n" + "="*70)
    print(f"EMBER HARDWARE PROFILE: LEVEL {profile.level}")
    print("="*70)
    print(f"Configuration: {profile.name}")
    print(f"VRAM: {profile.vram_gb:.1f} GB")
    print(f"RAM: {profile.ram_gb:.1f} GB")
    print(f"GPU: {'Yes' if profile.has_gpu else 'No (CPU only)'}")
    print()
    print("MODELS:")
    print(f"  Brain (reasoning): {profile.brain_model}")
    print(f"  Voice (storytelling): {profile.voice_model}")
    print()
    print(f"Simultaneous execution: {'Yes' if profile.can_run_simultaneously else 'No (sequential)'}")
    print("="*70)

def get_model_recommendations(profile: HardwareProfile) -> dict:
    """
    Get specific model names to download
    Returns dict with model names and HuggingFace repo IDs
    """
    
    recommendations = {
        1: {  # High-end
            "brain": {
                "name": "DeepSeek Coder 6.7B",
                "repo": "deepseek-ai/deepseek-coder-6.7b-instruct",
                "size": "13 GB",
                "quant": "Use fp16 or 4-bit",
                "role": "Tool execution, reasoning, structured output"
            },
            "voice": {
                "name": "Llama 3.2 1B",
                "repo": "meta-llama/Llama-3.2-1B-Instruct",
                "size": "2 GB",
                "quant": "Use fp16",
                "role": "Narration, storytelling, natural language"
            }
        },
        2: {  # Mid-range
            "brain": {
                "name": "Qwen2.5 Coder 3B",
                "repo": "Qwen/Qwen2.5-Coder-3B-Instruct",
                "size": "6 GB",
                "quant": "Use 4-bit"
            },
            "voice": {
                "name": "Llama 3.2 1B",
                "repo": "meta-llama/Llama-3.2-1B-Instruct",
                "size": "2 GB",
                "quant": "Use fp16"
            }
        },
        3: {  # CPU-only
            "brain": {
                "name": "Phi-1.5 1.3B",
                "repo": "microsoft/phi-1_5",
                "size": "2.5 GB",
                "quant": "Use 4-bit or 8-bit"
            },
            "voice": {
                "name": "TinyLlama 1.1B",
                "repo": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                "size": "2 GB",
                "quant": "Use 8-bit"
            }
        },
        4: {  # Low-end
            "brain": {
                "name": "Phi-1.5 1.3B (quantized)",
                "repo": "microsoft/phi-1_5",
                "size": "1 GB",
                "quant": "Use 4-bit heavily quantized"
            },
            "voice": {
                "name": "TinyStories 8M",
                "repo": "roneneldan/TinyStories-8M",
                "size": "50 MB",
                "quant": "No quantization needed"
            }
        },
        5: {  # IoT
            "brain": {
                "name": "Network offload required",
                "repo": "N/A",
                "size": "0 GB",
                "quant": "N/A"
            },
            "voice": {
                "name": "TinyStories 8M",
                "repo": "roneneldan/TinyStories-8M",
                "size": "50 MB",
                "quant": "No quantization needed"
            }
        }
    }
    
    return recommendations[profile.level]

if __name__ == "__main__":
    print("🔍 Detecting hardware capabilities...")
    
    profile = detect_hardware()
    print_profile(profile)
    
    print("\n📦 RECOMMENDED MODELS TO DOWNLOAD:")
    print("="*70)
    
    recs = get_model_recommendations(profile)
    
    print(f"\n🧠 BRAIN (reasoning, tool execution):")
    print(f"   Name: {recs['brain']['name']}")
    print(f"   Repo: {recs['brain']['repo']}")
    print(f"   Size: {recs['brain']['size']}")
    print(f"   Quantization: {recs['brain']['quant']}")
    
    print(f"\n🎭 VOICE (storytelling, narration):")
    print(f"   Name: {recs['voice']['name']}")
    print(f"   Repo: {recs['voice']['repo']}")
    print(f"   Size: {recs['voice']['size']}")
    print(f"   Quantization: {recs['voice']['quant']}")
    
    print("\n" + "="*70)
    print("💡 TIP: Download models with:")
    print("   huggingface-cli download <repo> --local-dir models/<brain|voice>/<name>")
    print("="*70)

