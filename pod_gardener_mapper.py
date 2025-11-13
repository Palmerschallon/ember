#!/usr/bin/env python3
"""
Pod Gardener Mapper - Map & Index
Creates maps, indexes, and navigation aids for the entire Pod
Inherits error-resistance from ResilientGardener
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class MapperGardener(ResilientGardener):
    """Creates comprehensive maps and indexes of the Pod"""

    def __init__(self):
        super().__init__('mapper', pod_root='/media/palmerschallon/ThePod1')

        # Map output directory
        self.maps_dir = self.pod_root / 'pod_maps'
        self.maps_dir.mkdir(exist_ok=True)

        # Discovered content
        self.file_map = defaultdict(list)

    async def build_file_map(self):
        """Build a comprehensive map of all files in the Pod"""
        print("\n🗺️  Building comprehensive file map...")

        extensions_of_interest = {
            'code': ['.py', '.js', '.ts', '.jsx', '.tsx'],
            'web': ['.html', '.css', '.scss'],
            'data': ['.json', '.yaml', '.yml', '.csv', '.pkl'],
            'docs': ['.md', '.txt', '.rst'],
            'config': ['.toml', '.ini', '.conf', '.cfg', '.env'],
            'images': ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp'],
            'notebooks': ['.ipynb'],
            'logs': ['.log']
        }

        for category, extensions in extensions_of_interest.items():
            print(f"  🔹 Mapping {category} files...")
            files = self.discover_files_by_extension(extensions, max_files=1000)
            self.file_map[category] = [
                {
                    'path': str(f),
                    'name': Path(f).name,
                    'size': Path(f).stat().st_size if Path(f).exists() else 0,
                    'modified': datetime.fromtimestamp(Path(f).stat().st_mtime).isoformat() if Path(f).exists() else None
                }
                for f in files
            ]
            print(f"    Found {len(files)} {category} files")

        total_files = sum(len(v) for v in self.file_map.values())
        print(f"\n✓ Mapped {total_files} files across {len(self.file_map)} categories")
        return total_files

    async def create_json_map(self):
        """Create a JSON map file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        map_file = self.maps_dir / f'pod_map_{timestamp}.json'

        map_data = {
            'generated': datetime.now().isoformat(),
            'total_files': sum(len(v) for v in self.file_map.values()),
            'categories': {k: len(v) for k, v in self.file_map.items()},
            'files': dict(self.file_map)
        }

        with open(map_file, 'w') as f:
            json.dump(map_data, f, indent=2)

        print(f"    ✓ JSON map saved: {map_file.name}")
        return map_file

    async def create_directory_tree(self):
        """Create a text-based directory tree"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        tree_file = self.maps_dir / f'directory_tree_{timestamp}.txt'

        with open(tree_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write("Pod Directory Tree\n")
            f.write("="*60 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for category, files in self.file_map.items():
                f.write(f"\n{category.upper()} ({len(files)} files)\n")
                f.write("-" * 60 + "\n")

                # Group by directory
                by_dir = defaultdict(list)
                for file_info in files[:50]:  # First 50 per category
                    dir_path = str(Path(file_info['path']).parent)
                    by_dir[dir_path].append(file_info['name'])

                for dir_path in sorted(by_dir.keys())[:10]:  # First 10 directories
                    f.write(f"\n  {dir_path}/\n")
                    for filename in sorted(by_dir[dir_path])[:5]:  # First 5 files
                        f.write(f"    - {filename}\n")

                if len(by_dir) > 10:
                    f.write(f"\n  ... and {len(by_dir) - 10} more directories\n")

        print(f"    ✓ Directory tree saved: {tree_file.name}")
        return tree_file

    async def create_stats_summary(self):
        """Create a statistics summary"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        stats_file = self.maps_dir / f'pod_stats_{timestamp}.txt'

        total_files = sum(len(v) for v in self.file_map.values())
        total_size = sum(
            sum(f.get('size', 0) for f in files)
            for files in self.file_map.values()
        )

        with open(stats_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write("Pod Statistics Summary\n")
            f.write("="*60 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write(f"Total Files: {total_files:,}\n")
            f.write(f"Total Size: {total_size / (1024**3):.2f} GB\n\n")

            f.write("Files by Category:\n")
            f.write("-" * 60 + "\n")
            for category, files in sorted(self.file_map.items(), key=lambda x: len(x[1]), reverse=True):
                cat_size = sum(f.get('size', 0) for f in files)
                f.write(f"  {category:15} {len(files):6,} files  {cat_size / (1024**2):10.2f} MB\n")

        print(f"    ✓ Stats summary saved: {stats_file.name}")
        return stats_file

    async def run_mapping_session(self):
        """Run a complete mapping session"""
        print("\n" + "="*60)
        print("🗺️  Pod Mapper Gardener Starting...")
        print("="*60)

        # Task 1: Build file map
        await self.run_task(
            self.build_file_map,
            "build_file_map"
        )

        # Task 2: Create JSON map
        print("\n🔹 Task: Creating JSON map")
        await self.execute_with_timeout(
            self.create_json_map(),
            "create_json_map"
        )

        # Task 3: Create directory tree
        print("\n🔹 Task: Creating directory tree")
        await self.execute_with_timeout(
            self.create_directory_tree(),
            "create_directory_tree"
        )

        # Task 4: Create stats summary
        print("\n🔹 Task: Creating stats summary")
        await self.execute_with_timeout(
            self.create_stats_summary(),
            "create_stats_summary"
        )

        # Print final stats
        self.print_stats()
        print(f"\n✨ Maps saved to: {self.maps_dir}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = MapperGardener()
    await gardener.run_mapping_session()


if __name__ == '__main__':
    asyncio.run(main())
