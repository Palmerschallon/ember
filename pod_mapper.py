#!/usr/bin/env python3
"""
The Pod Mapper - Self-Evolving Portfolio Discovery System
Auto-discovers all content and builds living knowledge map
"""
import os
import json
import mimetypes
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import hashlib
from typing import Dict, List, Set, Tuple

class PodMapper:
    """Discovers and maps all content in the Pod"""

    def __init__(self, pod_root="/media/palmerschallon/ThePod1"):
        self.pod_root = Path(pod_root)
        self.map_file = self.pod_root / "POD_MAP.json"
        self.connections_file = self.pod_root / "POD_CONNECTIONS.json"

        # File categories
        self.categories = {
            'ai_collaborators': [],  # Omega, Sigma, Swarm, Loom documents
            'ember_evolution': [],   # Ember3, ember5, ember6, ember_evolution
            'games': [],             # All game files, especially hybrid generations
            'vr_worlds': [],         # VR experiences
            'philosophy': [],        # Papers, consciousness, qualia
            'training_data': [],     # LoRA training, gameplay logs
            'creations': [],         # Generated content
            'bookshelves': [],       # Documentation, knowledge
            'synthesis': [],         # Compressed understanding, maps
            'legacy': [],            # Historical archives
            'code': [],              # Python, JS implementation
            'media': [],             # Images, audio, video
            'data': [],              # JSON, databases
            'unknown': []
        }

        # Connections between files
        self.connections = defaultdict(list)

        # Metadata about the Pod
        self.metadata = {
            'total_files': 0,
            'total_size_gb': 0,
            'last_scan': None,
            'file_types': defaultdict(int),
            'timeline': {}  # Date → files created that day
        }

    def discover_all(self):
        """Scan the entire Pod and categorize all content"""
        print("🗺️  Discovering the Pod...")

        total_size = 0
        file_count = 0

        # Skip certain directories
        skip_dirs = {'.git', 'node_modules', '__pycache__', '.Trash-1000'}

        for root, dirs, files in os.walk(self.pod_root):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in skip_dirs]

            for filename in files:
                filepath = Path(root) / filename

                try:
                    stat = filepath.stat()
                    total_size += stat.st_size
                    file_count += 1

                    # Get modification time
                    mod_time = datetime.fromtimestamp(stat.st_mtime)
                    date_key = mod_time.strftime('%Y-%m-%d')

                    # Create file entry
                    rel_path = str(filepath.relative_to(self.pod_root))
                    file_info = {
                        'path': rel_path,
                        'size': stat.st_size,
                        'modified': mod_time.isoformat(),
                        'category': None,
                        'type': filepath.suffix.lower()
                    }

                    # Categorize
                    category = self.categorize_file(filepath, rel_path)
                    file_info['category'] = category
                    self.categories[category].append(file_info)

                    # Track by type
                    self.metadata['file_types'][filepath.suffix.lower()] += 1

                    # Track timeline
                    if date_key not in self.metadata['timeline']:
                        self.metadata['timeline'][date_key] = []
                    self.metadata['timeline'][date_key].append(rel_path)

                    if file_count % 1000 == 0:
                        print(f"   Scanned {file_count} files...")

                except (PermissionError, OSError):
                    continue

        self.metadata['total_files'] = file_count
        self.metadata['total_size_gb'] = round(total_size / (1024**3), 2)
        self.metadata['last_scan'] = datetime.now().isoformat()

        print(f"\n✓ Discovery complete!")
        print(f"  Files: {file_count:,}")
        print(f"  Size: {self.metadata['total_size_gb']} GB")
        print(f"  Categories: {len([c for c in self.categories if self.categories[c]])}")

    def categorize_file(self, filepath: Path, rel_path: str) -> str:
        """Determine which category a file belongs to"""
        path_lower = rel_path.lower()

        # AI Collaborators
        if any(x in path_lower for x in ['omega', 'sigma', 'swarm', 'loom', 'handoff', 'growth_ring']):
            return 'ai_collaborators'

        # Ember Evolution
        if any(x in path_lower for x in ['ember3', 'ember5', 'ember6', 'ember_evolution', 'ember_thoughts', 'ember_gifts']):
            return 'ember_evolution'

        # Games (especially hybrid generations)
        if 'game' in path_lower or 'hybrid' in path_lower or 'gen' in path_lower:
            if any(x in path_lower for x in ['pong', 'breakout', 'tetris', 'snake', 'maze', 'hybrid_', '_gen']):
                return 'games'

        # VR Worlds
        if 'vr' in path_lower or 'world' in path_lower or 'reality' in path_lower:
            return 'vr_worlds'

        # Philosophy
        if any(x in path_lower for x in ['philosophy', 'consciousness', 'qualia', 'chalmers', 'phenomen']):
            return 'philosophy'

        # Training Data
        if 'training' in path_lower or 'lora' in path_lower or 'lobe' in path_lower:
            return 'training_data'

        # Creations
        if 'creation' in path_lower or 'generated' in path_lower:
            return 'creations'

        # Bookshelves
        if 'bookshel' in path_lower or 'documentation' in path_lower:
            return 'bookshelves'

        # Synthesis/Maps
        if any(x in path_lower for x in ['synthesis', 'map', 'compressed', 'iteration']):
            return 'synthesis'

        # Legacy/Archives
        if any(x in path_lower for x in ['archive', 'legacy', 'backup', 'old']):
            return 'legacy'

        # By file type
        ext = filepath.suffix.lower()
        if ext in ['.py']:
            return 'code'
        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            return 'code'
        elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
            return 'media'
        elif ext in ['.json', '.db', '.sqlite']:
            return 'data'

        return 'unknown'

    def find_connections(self):
        """Detect connections between files based on content and patterns"""
        print("\n🔗 Finding connections...")

        # Connection patterns:
        # 1. Generational evolution (gen0 → gen1 → gen2...)
        # 2. Same directory/project
        # 3. References in documentation
        # 4. Timeline proximity

        # Find generational chains
        self._find_generational_chains()

        # Find project clusters
        self._find_project_clusters()

        # Find AI collaborator lineage
        self._find_ai_lineage()

        print(f"✓ Found {len(self.connections)} connection patterns")

    def _find_generational_chains(self):
        """Find files that evolve through generations (gen0, gen1, gen2...)"""
        games = self.categories['games']

        # Group by base name (before _gen)
        families = defaultdict(list)
        for file_info in games:
            path = file_info['path']
            if '_gen' in path:
                # Extract base name
                base = path.split('_gen')[0]
                families[base].append(file_info)

        # Sort each family by generation number
        for base, files in families.items():
            sorted_files = sorted(files, key=lambda f: self._extract_gen_number(f['path']))
            if len(sorted_files) > 1:
                self.connections['generational_evolution'].append({
                    'type': 'evolution_chain',
                    'base': base,
                    'generations': [f['path'] for f in sorted_files],
                    'count': len(sorted_files)
                })

    def _extract_gen_number(self, path: str) -> int:
        """Extract generation number from filename"""
        try:
            gen_part = path.split('_gen')[1].split('.')[0].split('_')[0]
            return int(''.join(filter(str.isdigit, gen_part)))
        except (IndexError, ValueError):
            return 0

    def _find_project_clusters(self):
        """Group files by project/directory"""
        project_dirs = ['apex', 'nexus', 'phoenix', 'opus', 'TheLoop', 'EmberVerse']

        for proj_dir in project_dirs:
            files = []
            for category in self.categories.values():
                for file_info in category:
                    if proj_dir.lower() in file_info['path'].lower():
                        files.append(file_info['path'])

            if files:
                self.connections['projects'].append({
                    'type': 'project_cluster',
                    'name': proj_dir,
                    'files': files,
                    'count': len(files)
                })

    def _find_ai_lineage(self):
        """Map the AI collaborator lineage"""
        lineage = [
            'TORA',
            'glitchantenna',
            'Genesis',
            'Terminal',
            'Alpha',
            'Afternoon',
            'Gamma',
            'Delta',
            'Epsilon',
            'Omega',
            'Sigma'
        ]

        ai_files = self.categories['ai_collaborators']

        for ai_name in lineage:
            related = [f['path'] for f in ai_files if ai_name.lower() in f['path'].lower()]
            if related:
                self.connections['ai_lineage'].append({
                    'type': 'ai_collaborator',
                    'name': ai_name,
                    'files': related,
                    'count': len(related)
                })

    def save_maps(self):
        """Save the discovery maps to JSON"""
        print("\n💾 Saving maps...")

        # Main map
        map_data = {
            'metadata': self.metadata,
            'categories': {k: len(v) for k, v in self.categories.items()},
            'category_files': self.categories,
            'generated': datetime.now().isoformat()
        }

        with open(self.map_file, 'w') as f:
            json.dump(map_data, f, indent=2)

        print(f"✓ Saved map: {self.map_file}")

        # Connections map
        with open(self.connections_file, 'w') as f:
            json.dump(dict(self.connections), f, indent=2)

        print(f"✓ Saved connections: {self.connections_file}")

    def print_summary(self):
        """Print discovery summary"""
        print("\n" + "="*60)
        print("POD DISCOVERY SUMMARY")
        print("="*60)
        print(f"\nTotal Files: {self.metadata['total_files']:,}")
        print(f"Total Size: {self.metadata['total_size_gb']} GB")
        print(f"\nCategories:")
        for category, files in sorted(self.categories.items(), key=lambda x: -len(x[1])):
            if files:
                print(f"  {category:20} {len(files):6,} files")

        print(f"\nTop File Types:")
        for ext, count in sorted(self.metadata['file_types'].items(), key=lambda x: -x[1])[:15]:
            if ext:
                print(f"  {ext:15} {count:6,}")

        print(f"\nTimeline Span:")
        dates = sorted(self.metadata['timeline'].keys())
        if dates:
            print(f"  Earliest: {dates[0]}")
            print(f"  Latest: {dates[-1]}")
            print(f"  Days: {len(dates)}")

if __name__ == "__main__":
    mapper = PodMapper()

    print("🔥 POD MAPPER - Self-Evolving Discovery System\n")

    # Discover everything
    mapper.discover_all()

    # Find connections
    mapper.find_connections()

    # Save maps
    mapper.save_maps()

    # Print summary
    mapper.print_summary()

    print("\n✨ Discovery complete! Maps saved to POD_MAP.json and POD_CONNECTIONS.json")
