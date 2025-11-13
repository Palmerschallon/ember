#!/usr/bin/env python3
"""
DEEP SCAN - Find everything we're missing
Searches for VR worlds, games, visualizations, music, tools
"""

from pathlib import Path
import json

THEPOD = Path("/media/palmerschallon/ThePod1")

print("🔍 DEEP SCANNING ThePod for hidden gems...")
print("="*80)

findings = {
    "vr_worlds": [],
    "games": [],
    "music_audio": [],
    "visualizations": [],
    "tools_utilities": [],
    "demos": [],
    "experiments": []
}

# Scan for specific patterns
print("\n📂 Scanning for VR worlds...")
for f in THEPOD.rglob("*vr*.html"):
    if f.stat().st_size > 1000:  # Skip tiny files
        findings["vr_worlds"].append(str(f.relative_to(THEPOD)))

print("🎮 Scanning for games...")
for f in THEPOD.rglob("*game*.html"):
    if f.stat().st_size > 1000:
        findings["games"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*play*.html"):
    if f.stat().st_size > 1000:
        findings["games"].append(str(f.relative_to(THEPOD)))

print("🎵 Scanning for music/audio...")
for ext in ['*.wav', '*.mp3', '*.ogg']:
    for f in THEPOD.rglob(ext):
        findings["music_audio"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*sound*.html"):
    if f.stat().st_size > 1000:
        findings["music_audio"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*audio*.html"):
    if f.stat().st_size > 1000:
        findings["music_audio"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*music*.html"):
    if f.stat().st_size > 1000:
        findings["music_audio"].append(str(f.relative_to(THEPOD)))

print("📊 Scanning for visualizations...")
for f in THEPOD.rglob("*viz*.html"):
    if f.stat().st_size > 1000:
        findings["visualizations"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*graph*.html"):
    if f.stat().st_size > 1000:
        findings["visualizations"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*mind*.html"):
    if f.stat().st_size > 1000:
        findings["visualizations"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*brain*.html"):
    if f.stat().st_size > 1000:
        findings["visualizations"].append(str(f.relative_to(THEPOD)))

print("🛠️ Scanning for tools...")
for f in THEPOD.rglob("*tool*.html"):
    if f.stat().st_size > 1000:
        findings["tools_utilities"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*editor*.html"):
    if f.stat().st_size > 1000:
        findings["tools_utilities"].append(str(f.relative_to(THEPOD)))

print("🧪 Scanning for demos/experiments...")
for f in THEPOD.rglob("*demo*.html"):
    if f.stat().st_size > 1000:
        findings["demos"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*test*.html"):
    if f.stat().st_size > 5000:  # Bigger threshold for tests
        findings["experiments"].append(str(f.relative_to(THEPOD)))

for f in THEPOD.rglob("*experiment*.html"):
    if f.stat().st_size > 1000:
        findings["experiments"].append(str(f.relative_to(THEPOD)))

# Remove duplicates
for key in findings:
    findings[key] = sorted(list(set(findings[key])))

# Print summary
print("\n" + "="*80)
print("🔥 FINDINGS:")
print("="*80)
for category, items in findings.items():
    if items:
        print(f"\n{category.upper().replace('_', ' ')}: {len(items)} found")
        for item in items[:5]:
            print(f"  - {item}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")

# Save
output = Path("/media/palmerschallon/ThePod1/demo_build/deep_scan.json")
output.write_text(json.dumps(findings, indent=2))

print(f"\n✅ Deep scan complete: {output}")
print(f"\nTotal hidden gems found: {sum(len(v) for v in findings.values())}")

