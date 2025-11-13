#!/usr/bin/env python3
"""
Pod Master Indexer - THE SINGLE SOURCE OF TRUTH
Scans ALL 30K+ files recursively and builds comprehensive catalog
Every gardener should read/write to this index
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import mimetypes
import hashlib

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class IndexerGardener(ResilientGardener):
    """Builds and maintains the master index of ALL Pod content"""

    def __init__(self):
        super().__init__('indexer', pod_root='/media/palmerschallon/ThePod1')

        self.stats['files_indexed'] = 0
        self.stats['html_files'] = 0
        self.stats['code_files'] = 0
        self.stats['data_files'] = 0
        self.stats['image_files'] = 0

        # Master index file - SINGLE SOURCE OF TRUTH
        self.index_file = self.pod_root / 'pod_master_index.json'

        # Directories to skip
        self.skip_dirs = {
            '__pycache__', '.git', 'node_modules', '.venv',
            'venv', '.cache', 'logs', '.env'
        }

    def get_file_category(self, file_path):
        """Categorize file by extension and content"""
        ext = file_path.suffix.lower()

        # HTML/Web
        if ext in {'.html', '.htm'}:
            return 'html'

        # Code
        if ext in {'.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp', '.c', '.go', '.rs', '.rb', '.php'}:
            return 'code'

        # Data
        if ext in {'.json', '.xml', '.yaml', '.yml', '.toml', '.csv', '.sql'}:
            return 'data'

        # Images
        if ext in {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.bmp'}:
            return 'image'

        # Documents
        if ext in {'.md', '.txt', '.pdf', '.doc', '.docx'}:
            return 'document'

        # Config
        if ext in {'.conf', '.cfg', '.ini', '.env'}:
            return 'config'

        # Compressed
        if ext in {'.zip', '.tar', '.gz', '.bz2', '.7z'}:
            return 'archive'

        # Media
        if ext in {'.mp4', '.mp3', '.wav', '.avi', '.mov', '.webm'}:
            return 'media'

        return 'other'

    def extract_metadata(self, file_path):
        """Extract useful metadata from file"""
        try:
            stat = file_path.stat()

            metadata = {
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'category': self.get_file_category(file_path),
            }

            # For HTML files, try to extract title and detect special types
            if file_path.suffix.lower() in {'.html', '.htm'}:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(5000)  # First 5KB

                        # Extract title
                        if '<title>' in content:
                            title_start = content.find('<title>') + 7
                            title_end = content.find('</title>', title_start)
                            if title_end > title_start:
                                metadata['title'] = content[title_start:title_end].strip()

                        # Detect special types
                        tags = []
                        if 'vr' in content.lower() or 'a-frame' in content.lower():
                            tags.append('vr')
                        if 'three.js' in content.lower() or 'webgl' in content.lower():
                            tags.append('3d')
                        if 'canvas' in content.lower():
                            tags.append('interactive')
                        if 'd3' in content.lower() or 'chart' in content.lower():
                            tags.append('visualization')
                        if 'ember' in content.lower() and 'chat' in content.lower():
                            tags.append('ai')

                        if tags:
                            metadata['tags'] = tags

                except Exception:
                    pass

            return metadata

        except Exception as e:
            return {'error': str(e)}

    async def build_master_index(self):
        """Scan ALL files and build comprehensive index"""
        print("\n🗂️  Building Master Index of ENTIRE Pod...")
        print(f"   Starting recursive scan from: {self.pod_root}")

        # Load existing index if present to continue where we left off
        index = None
        already_indexed = set()

        if self.index_file.exists():
            try:
                with open(self.index_file, 'r') as f:
                    index = json.load(f)
                print(f"   📖 Found existing index: {index['total_files']:,} files already cataloged")

                # Build set of already-indexed file paths for quick lookup
                already_indexed = {entry['path'] for entry in index.get('files', [])}
                print(f"   ⏭️  Will skip {len(already_indexed):,} already-indexed files")

            except Exception as e:
                print(f"   ⚠ Could not load existing index: {e}")
                index = None

        # Initialize new index if none exists
        if index is None:
            index = {
                'timestamp': datetime.now().isoformat(),
                'total_files': 0,
                'total_size': 0,
                'categories': {},
                'files': [],
                'html_projects': [],
                'scan_complete': False,
                'progress_percentage': 0
            }
            print("   🆕 Starting fresh index from scratch")
        else:
            # Update timestamp for this run
            index['timestamp'] = datetime.now().isoformat()

        files_scanned = 0
        files_added_this_run = 0
        target_files = 5000  # Process 5000 NEW files per run

        # Walk entire directory tree
        import os
        for root, dirs, files in os.walk(self.pod_root):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in self.skip_dirs]

            for file in files:
                file_path = Path(root) / file

                # Skip if not a file
                if not file_path.is_file():
                    continue

                try:
                    # Get relative path
                    rel_path = str(file_path.relative_to(self.pod_root))

                    # Skip if already indexed
                    if rel_path in already_indexed:
                        files_scanned += 1
                        continue

                    # Stop after processing target NEW files in this run
                    if files_added_this_run >= target_files:
                        print(f"\n   ⏸️  Checkpoint: Added {files_added_this_run} NEW files this run")
                        print(f"   ⏭️  Skipped {files_scanned - files_added_this_run:,} already-indexed files")
                        break

                    # Extract metadata
                    metadata = self.extract_metadata(file_path)
                    category = metadata.get('category', 'other')

                    # Build file entry
                    file_entry = {
                        'path': rel_path,
                        'name': file_path.name,
                        'category': category,
                        'size': metadata.get('size', 0),
                        'modified': metadata.get('modified'),
                    }

                    # Add tags if present
                    if 'tags' in metadata:
                        file_entry['tags'] = metadata['tags']

                    # Add title for HTML
                    if 'title' in metadata:
                        file_entry['title'] = metadata['title']

                    # Add to index
                    index['files'].append(file_entry)

                    # Update category counts
                    if category not in index['categories']:
                        index['categories'][category] = 0
                    index['categories'][category] += 1

                    # Update totals
                    index['total_files'] += 1
                    index['total_size'] += metadata.get('size', 0)

                    # Track HTML projects separately
                    if category == 'html':
                        index['html_projects'].append(file_entry)
                        self.stats['html_files'] += 1

                    # Track by category for stats
                    if category == 'code':
                        self.stats['code_files'] += 1
                    elif category == 'data':
                        self.stats['data_files'] += 1
                    elif category == 'image':
                        self.stats['image_files'] += 1

                    files_scanned += 1
                    files_added_this_run += 1
                    self.stats['files_indexed'] += 1

                    # Progress update
                    if files_added_this_run % 500 == 0:
                        print(f"   📊 Added {files_added_this_run} new files (total: {index['total_files']:,})...")

                except Exception as e:
                    print(f"   ✗ Error indexing {file_path.name}: {e}")
                    continue

            if files_added_this_run >= target_files:
                break

        # Calculate progress
        estimated_total = 30807  # From actual count
        index['progress_percentage'] = round((index['total_files'] / estimated_total) * 100, 2)

        # Mark complete if we've reached the target
        if index['total_files'] >= estimated_total * 0.99:  # 99% threshold
            index['scan_complete'] = True

        # Save index
        if self.write_file_directly(self.index_file, json.dumps(index, indent=2)):
            print(f"\n   ✓ Master Index saved: {self.index_file}")
            print(f"   📊 Files indexed THIS RUN: {files_added_this_run:,}")
            print(f"   📊 TOTAL files in catalog: {index['total_files']:,}")
            print(f"   📊 HTML projects: {len(index['html_projects'])}")
            print(f"   📊 Progress: {index['progress_percentage']}%")
            print(f"   💾 Total size: {index['total_size'] / (1024**3):.2f} GB")

            if index['scan_complete']:
                print(f"   🎉 SCAN COMPLETE! All files cataloged!")

            # Print category breakdown
            print(f"\n   📂 Categories:")
            for cat, count in sorted(index['categories'].items(), key=lambda x: -x[1])[:10]:
                print(f"      {cat}: {count:,}")

        return True

    async def incremental_update(self):
        """Update index with new/modified files since last run"""
        print("\n🔄 Incremental Index Update...")

        # Load existing index
        if self.index_file.exists():
            try:
                with open(self.index_file, 'r') as f:
                    index = json.load(f)
                print(f"   📖 Loaded existing index: {index['total_files']:,} files")
            except Exception as e:
                print(f"   ⚠ Could not load index: {e}")
                return await self.build_master_index()
        else:
            print("   ℹ️  No existing index found, building from scratch...")
            return await self.build_master_index()

        # Continue scanning where we left off
        # This is a simplified incremental update
        # In production, you'd track which files were already indexed

        return await self.build_master_index()

    async def create_index_report(self):
        """Create human-readable report from index"""
        print("\n📝 Creating index report...")

        if not self.index_file.exists():
            print("   ⚠ No index found")
            return False

        try:
            with open(self.index_file, 'r') as f:
                index = json.load(f)

            report = {
                'timestamp': datetime.now().isoformat(),
                'summary': {
                    'total_files': index['total_files'],
                    'html_projects': len(index.get('html_projects', [])),
                    'progress': index.get('progress_percentage', 0),
                    'total_size_gb': round(index.get('total_size', 0) / (1024**3), 2)
                },
                'categories': index.get('categories', {}),
                'html_by_tags': {}
            }

            # Categorize HTML by tags
            for html_file in index.get('html_projects', []):
                tags = html_file.get('tags', ['untagged'])
                for tag in tags:
                    if tag not in report['html_by_tags']:
                        report['html_by_tags'][tag] = []
                    report['html_by_tags'][tag].append({
                        'name': html_file['name'],
                        'path': html_file['path'],
                        'title': html_file.get('title', html_file['name'])
                    })

            # Save report
            report_file = self.pod_root / 'index_report.json'
            if self.write_file_directly(report_file, json.dumps(report, indent=2)):
                print(f"   ✓ Report saved: {report_file}")

            return True

        except Exception as e:
            print(f"   ✗ Error creating report: {e}")
            return False

    async def run_indexing_session(self):
        """Run complete indexing session"""
        print("\n" + "="*60)
        print("🗂️  Master Indexer Starting...")
        print("   Building SINGLE SOURCE OF TRUTH for entire Pod")
        print("="*60)

        # Task 1: Build/update master index
        await self.run_task(
            self.build_master_index,
            "build_index"
        )

        # Task 2: Create report
        await self.run_task(
            self.create_index_report,
            "create_report"
        )

        # Print final stats
        self.print_stats()
        print(f"\n📊 Indexing Summary:")
        print(f"   Files indexed: {self.stats['files_indexed']:,}")
        print(f"   HTML projects: {self.stats['html_files']:,}")
        print(f"   Code files: {self.stats['code_files']:,}")
        print(f"   Data files: {self.stats['data_files']:,}")
        print(f"   Image files: {self.stats['image_files']:,}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = IndexerGardener()
    await gardener.run_indexing_session()


if __name__ == '__main__':
    asyncio.run(main())
