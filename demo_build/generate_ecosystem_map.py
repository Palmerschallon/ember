#!/usr/bin/env python3
"""
POD ECOSYSTEM MAP GENERATOR
Scans all HTML files and creates a living network visualization
"""

from pathlib import Path
import json

THEPOD = Path("/media/palmerschallon/ThePod1")

print("🔍 Scanning ThePod ecosystem...")

# Find all HTML files
html_files = list(THEPOD.glob("**/*.html"))
print(f"Found {len(html_files)} HTML files")

# Categorize them
categories = {
    "vr_worlds": [],
    "ui_interfaces": [],
    "games": [],
    "visualizations": [],
    "demos": [],
    "galleries": [],
    "experiments": []
}

for html in html_files:
    rel_path = str(html.relative_to(THEPOD))
    size = html.stat().st_size
    
    # Categorize based on name/path
    name_lower = html.name.lower()
    path_lower = rel_path.lower()
    
    if "vr" in name_lower or "3d" in name_lower or "world" in name_lower:
        categories["vr_worlds"].append({"path": rel_path, "name": html.name, "size": size})
    elif "ui" in name_lower or "ember_ui" in name_lower or "chat" in name_lower:
        categories["ui_interfaces"].append({"path": rel_path, "name": html.name, "size": size})
    elif "game" in name_lower or "play" in name_lower:
        categories["games"].append({"path": rel_path, "name": html.name, "size": size})
    elif "viz" in name_lower or "visual" in name_lower or "graph" in name_lower or "mind" in name_lower:
        categories["visualizations"].append({"path": rel_path, "name": html.name, "size": size})
    elif "demo" in name_lower:
        categories["demos"].append({"path": rel_path, "name": html.name, "size": size})
    elif "gallery" in name_lower or "browse" in name_lower:
        categories["galleries"].append({"path": rel_path, "name": html.name, "size": size})
    else:
        categories["experiments"].append({"path": rel_path, "name": html.name, "size": size})

# Generate ecosystem data
ecosystem = {
    "total_files": len(html_files),
    "categories": categories,
    "stats": {
        "vr_worlds": len(categories["vr_worlds"]),
        "ui_interfaces": len(categories["ui_interfaces"]),
        "games": len(categories["games"]),
        "visualizations": len(categories["visualizations"]),
        "demos": len(categories["demos"]),
        "galleries": len(categories["galleries"]),
        "experiments": len(categories["experiments"])
    }
}

# Save
output = Path("/media/palmerschallon/ThePod1/demo_build/ecosystem_data.json")
output.write_text(json.dumps(ecosystem, indent=2))

print(f"\n✅ Ecosystem mapped!")
print(f"\nCategories:")
for cat, items in ecosystem["stats"].items():
    print(f"  {cat}: {items}")
print(f"\n💾 Saved to: {output}")

