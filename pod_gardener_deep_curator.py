#!/usr/bin/env python3
"""
Pod Gardener Deep Curator - Complete Recursive Discovery
Discovers ALL 30K+ files in the Pod and creates comprehensive manifests
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import mimetypes

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class DeepCuratorGardener(ResilientGardener):
    """Deep recursive curator that discovers EVERYTHING in the Pod"""

    def __init__(self):
        super().__init__('deep_curator', pod_root='/media/palmerschallon/ThePod1')

        self.stats['last_updated'] = datetime.now().isoformat()
        self.stats['total_files_discovered'] = 0
        self.stats['total_size_gb'] = 0

        # Output directories
        self.manifests_dir = self.pod_root / 'pod_manifests'
        self.manifests_dir.mkdir(exist_ok=True)

        # Comprehensive content catalog
        self.catalog = {
            'html': [],
            'python': [],
            'markdown': [],
            'notebooks': [],
            'images': [],
            'data': [],
            'configs': [],
            'text': [],
            'other': []
        }

        # Special folders to highlight
        self.special_folders = {}

        # Exclude patterns
        self.exclude_dirs = {
            'node_modules', '__pycache__', '.git', 'venv',
            '.venv', 'dist', 'build', '.cache'
        }

    async def deep_scan_pod(self):
        """Recursively scan entire Pod structure"""
        print("\n📡 Deep scanning entire Pod structure...")
        print("   This will discover ALL files recursively...")

        total_size = 0
        file_counts = defaultdict(int)

        try:
            for item in self.pod_root.rglob('*'):
                # Skip excluded directories
                if any(excl in item.parts for excl in self.exclude_dirs):
                    continue

                if item.is_file():
                    try:
                        size = item.stat().st_size
                        total_size += size

                        # Categorize file
                        ext = item.suffix.lower()
                        category = self._categorize_file(item, ext)
                        file_counts[category] += 1

                        # Add to catalog (sample to avoid memory issues)
                        if len(self.catalog[category]) < 200:
                            self.catalog[category].append({
                                'name': item.name,
                                'path': str(item.relative_to(self.pod_root)),
                                'size': size,
                                'modified': datetime.fromtimestamp(item.stat().st_mtime).isoformat()
                            })

                        # Track progress
                        if file_counts['html'] + file_counts['python'] % 1000 == 0:
                            print(f"   Scanned {sum(file_counts.values())} files...")

                    except (PermissionError, OSError):
                        continue

        except Exception as e:
            print(f"   Warning: Scan error: {e}")

        self.stats['total_files_discovered'] = sum(file_counts.values())
        self.stats['total_size_gb'] = round(total_size / (1024**3), 2)
        self.stats['file_counts'] = dict(file_counts)

        print(f"\n  ✓ Discovered {self.stats['total_files_discovered']:,} files")
        print(f"  ✓ Total size: {self.stats['total_size_gb']} GB")
        print(f"\n  📊 Breakdown:")
        for cat, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"    {cat}: {count:,} files")

        return True

    def _categorize_file(self, file_path, ext):
        """Categorize file by extension"""
        if ext in ['.html', '.htm']:
            return 'html'
        elif ext in ['.py']:
            return 'python'
        elif ext in ['.md', '.markdown']:
            return 'markdown'
        elif ext in ['.ipynb']:
            return 'notebooks'
        elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp']:
            return 'images'
        elif ext in ['.json', '.csv', '.tsv', '.parquet', '.pkl', '.yaml', '.yml']:
            return 'data'
        elif ext in ['.conf', '.cfg', '.ini', '.toml', '.env']:
            return 'configs'
        elif ext in ['.txt', '.log', '.out']:
            return 'text'
        else:
            return 'other'

    async def discover_special_folders(self):
        """Discover special folders like OneFolder, TheGarden, etc."""
        print("\n🔍 Discovering special folders and projects...")

        special_patterns = [
            'OneFolder', 'TheGarden', 'SAM', 'VIV3', 'Impossibilitron',
            'essential', 'ember', 'genetic_library'
        ]

        for pattern in special_patterns:
            matches = list(self.pod_root.rglob(pattern))
            if matches:
                for match in matches[:3]:  # First 3 matches
                    if match.is_dir():
                        # Count files in this special folder
                        file_count = sum(1 for _ in match.rglob('*') if _.is_file())
                        self.special_folders[match.name] = {
                            'path': str(match.relative_to(self.pod_root)),
                            'file_count': file_count
                        }
                        print(f"  ✓ Found {match.name}: {file_count} files")

        return True

    async def create_master_manifest(self):
        """Create comprehensive JSON manifest"""
        print("\n📝 Creating master manifest...")

        manifest = {
            'generated_at': datetime.now().isoformat(),
            'total_files': self.stats['total_files_discovered'],
            'total_size_gb': self.stats['total_size_gb'],
            'file_counts': self.stats['file_counts'],
            'special_folders': self.special_folders,
            'catalog_samples': {
                category: files[:50]  # Top 50 of each category
                for category, files in self.catalog.items()
            },
            'top_html_projects': sorted(
                self.catalog['html'],
                key=lambda x: x['modified'],
                reverse=True
            )[:100],  # 100 most recent HTML files
            'top_python_modules': sorted(
                self.catalog['python'],
                key=lambda x: x['size'],
                reverse=True
            )[:100],  # 100 largest Python files
        }

        manifest_file = self.manifests_dir / f'deep_manifest_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        success = self.write_file_directly(manifest_file, json.dumps(manifest, indent=2))

        if success:
            print(f"  ✓ Master manifest saved: {manifest_file.name}")

            # Also save latest manifest
            latest_file = self.manifests_dir / 'latest_manifest.json'
            self.write_file_directly(latest_file, json.dumps(manifest, indent=2))
            print(f"  ✓ Latest manifest updated")

        return manifest if success else None

    async def create_portal_data(self):
        """Create optimized data file for portal consumption"""
        print("\n🎨 Creating portal data file...")

        portal_data = {
            'stats': {
                'total_files': self.stats['total_files_discovered'],
                'total_size_gb': self.stats['total_size_gb'],
                'html_count': self.stats['file_counts'].get('html', 0),
                'python_count': self.stats['file_counts'].get('python', 0),
                'markdown_count': self.stats['file_counts'].get('markdown', 0),
                'image_count': self.stats['file_counts'].get('images', 0),
            },
            'featured_html': self.catalog['html'][:50],  # Top 50 HTML for portal
            'special_folders': self.special_folders,
            'last_updated': datetime.now().isoformat()
        }

        portal_file = self.pod_root / 'portal_data.json'
        success = self.write_file_directly(portal_file, json.dumps(portal_data, indent=2))

        if success:
            print(f"  ✓ Portal data file created")

        return portal_data if success else None

    async def run_deep_curation_session(self):
        """Run complete deep curation session"""
        print("\n" + "="*60)
        print("🔬 Deep Curator Gardener Starting...")
        print("   Preparing to scan ALL 30K+ files recursively")
        print("="*60)

        # Task 1: Deep scan
        await self.run_task(
            self.deep_scan_pod,
            "deep_scan"
        )

        # Task 2: Discover special folders
        await self.run_task(
            self.discover_special_folders,
            "discover_special"
        )

        # Task 3: Create master manifest
        await self.run_task(
            self.create_master_manifest,
            "create_manifest"
        )

        # Task 4: Create portal data
        await self.run_task(
            self.create_portal_data,
            "create_portal_data"
        )

        # Print final stats
        self.print_stats()
        print("="*60)


async def main():
    """Main entry point"""
    gardener = DeepCuratorGardener()
    await gardener.run_deep_curation_session()


if __name__ == '__main__':
    asyncio.run(main())
