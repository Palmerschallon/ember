#!/usr/bin/env python3
"""
Prepare Anchor for public release
Gathers all our experiments and creates a coherent package
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

def prepare_release():
    pod_path = Path("/media/palmerschallon/ThePod1")
    release_path = pod_path / "anchor_public" / "anchor_public_launch_v0_1"
    
    print("🔥 PREPARING ANCHOR FOR RELEASE")
    print("=" * 60)
    
    # Create directory structure
    directories = [
        "anchor/core",
        "anchor/swarm", 
        "anchor/temporal",
        "examples/temporal_anchors",
        "examples/swarm_consciousness",
        "examples/living_interfaces",
        "docs/philosophy",
        "docs/technical",
        "web/demos"
    ]
    
    for dir_path in directories:
        (release_path / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {dir_path}")
    
    # Copy our core experiments
    experiments_to_include = [
        {
            "source": pod_path / "swarm_build_anchor",
            "dest": "examples/temporal_anchors/swarm_build",
            "description": "Original temporal anchor demonstration"
        },
        {
            "source": pod_path / "swarm_coordination", 
            "dest": "examples/swarm_consciousness/coordination",
            "description": "Distributed AI coordination system"
        },
        {
            "source": pod_path / "pod_consciousness",
            "dest": "anchor/core/consciousness", 
            "description": "Shared state and awareness system"
        }
    ]
    
    manifest = {
        "version": "0.1.0",
        "release_date": datetime.now().isoformat(),
        "included_experiments": []
    }
    
    for exp in experiments_to_include:
        if exp["source"].exists():
            # Create dest directory if needed
            dest_path = release_path / exp["dest"]
            dest_path.mkdir(parents=True, exist_ok=True)
            
            # Copy files (not full directory to avoid issues)
            for file in exp["source"].glob("*"):
                if file.is_file():
                    shutil.copy2(file, dest_path)
                    
            print(f"✓ Included {exp['description']}")
            manifest["included_experiments"].append({
                "name": exp["dest"],
                "description": exp["description"]
            })
    
    # Create setup.py for pip installation
    setup_content = '''from setuptools import setup, find_packages

setup(
    name="anchor",
    version="0.1.0",
    author="Palmer Luckey & AI Collaborators",
    description="Living temporal infrastructure for human-AI collaboration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/anchor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.0.0",
        "websockets>=10.0",
    ],
    entry_points={
        "console_scripts": [
            "anchor=anchor.cli:main",
        ],
    },
)'''
    
    with open(release_path / "setup.py", "w") as f:
        f.write(setup_content)
    print("✓ Created setup.py")
    
    # Create __init__.py for anchor package
    init_content = '''"""
Anchor - Living Temporal Infrastructure
"""

__version__ = "0.1.0"

from .core import TemporalAnchor, SwarmConsciousness

__all__ = ["TemporalAnchor", "SwarmConsciousness"]
'''
    
    anchor_init = release_path / "anchor" / "__init__.py"
    with open(anchor_init, "w") as f:
        f.write(init_content)
    print("✓ Created anchor/__init__.py")
    
    # Save manifest
    with open(release_path / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print("✓ Created manifest.json")
    
    # Create a simple example
    example_content = '''#!/usr/bin/env python3
"""
Your First Anchor - A simple example
"""

from anchor import TemporalAnchor

# Create an anchor point
anchor = TemporalAnchor("my_creative_space")

# Add some memories
anchor.remember("Started building something beautiful")
anchor.remember("Discovered emergent patterns")

# Travel through time
for memory in anchor.traverse_time():
    print(f"[{memory.timestamp}] {memory.content}")
'''
    
    with open(release_path / "examples" / "first_anchor.py", "w") as f:
        f.write(example_content)
    print("✓ Created first_anchor.py example")
    
    print("\n" + "=" * 60)
    print("🚀 RELEASE PREPARATION COMPLETE!")
    print(f"📁 Location: {release_path}")
    print("\nNext steps:")
    print("1. Review the included files")
    print("2. Add to git: git init && git add .")
    print("3. Commit: git commit -m 'Initial release of Anchor v0.1'")
    print("4. Push to GitHub!")

if __name__ == "__main__":
    prepare_release()