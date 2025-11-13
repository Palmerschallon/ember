#!/usr/bin/env python3
"""
Pod Gardener Modernizer - Rebuilds Old Projects with 2025 Design Standards
Takes crusty old HTML and makes it BEAUTIFUL, MODERN, PROFESSIONAL
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import re

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class ModernizerGardener(ResilientGardener):
    """Completely rebuilds old projects with modern UI/UX"""

    def __init__(self):
        super().__init__('modernizer', pod_root='/media/palmerschallon/ThePod1')

        self.stats['projects_modernized'] = 0
        self.stats['old_files_archived'] = 0

        # Output directory
        self.modernized_dir = self.pod_root / 'modernized_projects'
        self.archive_dir = self.pod_root / 'archived_old_versions'
        self.modernized_dir.mkdir(exist_ok=True)
        self.archive_dir.mkdir(exist_ok=True)

        # Check if Ember is available
        self.ember_available = (self.pod_root / 'ember_complete.py').exists()

    def needs_modernization(self, file_path):
        """Check if file looks old/ugly and needs modernization"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Signs of old/ugly code
            old_indicators = [
                '<table' in content.lower() and 'layout' in content.lower(),  # Table layouts
                'font face=' in content.lower(),  # Old font tags
                '<center>' in content.lower(),  # Center tags
                'bgcolor=' in content.lower(),  # Inline bgcolor
                content.count('<style>') == 0 and content.count('class=') < 3,  # No CSS
                'width="100%"' in content and '<div' not in content,  # Old table-based
                len(content) < 1000 and '<script>' not in content,  # Too simple/minimal
            ]

            # Also modernize if it lacks modern features
            lacks_modern = [
                'viewport' not in content,  # No responsive viewport
                'flex' not in content and 'grid' not in content,  # No modern layout
                'rgba(' not in content and 'hsla(' not in content,  # No modern colors
                '@media' not in content and len(content) > 500,  # No responsive design
            ]

            return sum(old_indicators) >= 2 or sum(lacks_modern) >= 2

        except Exception as e:
            return False

    async def modernize_with_ember(self, file_path):
        """Use Ember to completely rebuild project with modern design"""
        if not self.ember_available:
            print("  ⚠ Ember not available")
            return None

        try:
            from ember_complete import Ember
            ember = Ember()

            # Read the old file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                old_content = f.read()

            # Extract what the project is trying to do
            prompt = f"""You are a modern UI/UX designer rebuilding an old project.

OLD PROJECT: {file_path.name}
{old_content[:3000]}

Your mission: Completely rebuild this project with 2025 design standards.

MODERN DESIGN REQUIREMENTS:
1. **Responsive Layout** - CSS Grid or Flexbox, works on all devices
2. **Modern Color Palette** - Sophisticated colors, good contrast, dark mode support
3. **Typography** - Web fonts, proper hierarchy (h1-h6), readable line-height
4. **Smooth Animations** - Transitions, hover effects, fade-ins
5. **Clean Code** - Semantic HTML5, organized CSS, no inline styles
6. **Accessibility** - ARIA labels, keyboard navigation, screen reader friendly
7. **Performance** - Optimized, fast loading, no unnecessary scripts
8. **Visual Polish** - Shadows, borders, spacing, professional appearance

KEEP THE SAME FUNCTIONALITY but make it look STUNNING and MODERN.

Return ONLY the complete rebuilt HTML file, ready to save."""

            modernized_content = await ember.chat(prompt)

            # Validation - does it look like modern HTML?
            if modernized_content and len(modernized_content) > 500:
                if any(term in modernized_content.lower() for term in ['flex', 'grid', 'viewport', 'rgba']):
                    return modernized_content

            return None

        except Exception as e:
            print(f"  ✗ Ember error: {e}")
            return None

    async def scan_and_modernize(self):
        """Find old/ugly projects and modernize them"""
        print("\n🎨 Scanning for old projects that need modernization...")

        # Get HTML files, prioritize older ones
        html_files = sorted(
            self.pod_root.glob('*.html'),
            key=lambda f: f.stat().st_mtime  # Oldest first
        )[:50]  # Process 50 per run

        modernized_count = 0
        candidates = []

        # First pass - identify candidates
        for html_file in html_files:
            if html_file.name.startswith('modernized_'):
                continue  # Skip already modernized

            if self.needs_modernization(html_file):
                candidates.append(html_file)

        print(f"  📊 Found {len(candidates)} projects needing modernization")

        # Second pass - modernize top candidates
        for html_file in candidates[:10]:  # Modernize 10 per run
            try:
                print(f"\n  🔄 Modernizing {html_file.name}...")

                modernized_content = await self.modernize_with_ember(html_file)

                if modernized_content:
                    # Archive original
                    archive_path = self.archive_dir / f"{html_file.stem}_{datetime.now().strftime('%Y%m%d')}.html"
                    with open(html_file, 'r') as f:
                        original = f.read()
                    with open(archive_path, 'w') as f:
                        f.write(original)

                    # Save modernized version
                    modernized_path = self.modernized_dir / f"modernized_{html_file.name}"
                    if self.write_file_directly(modernized_path, modernized_content):
                        print(f"    ✓ Modernized! Saved to: {modernized_path.name}")
                        print(f"    📦 Original archived: {archive_path.name}")
                        modernized_count += 1
                        self.stats['projects_modernized'] += 1
                        self.stats['old_files_archived'] += 1

                        # Also replace original with modernized version
                        if self.write_file_directly(html_file, modernized_content):
                            print(f"    ✓ Original updated with modern version")

            except Exception as e:
                print(f"  ✗ Error modernizing {html_file.name}: {e}")
                continue

        print(f"\n  📊 Modernized {modernized_count} projects")
        return True

    async def create_modernization_report(self):
        """Create report of modernization progress"""
        print("\n📝 Creating modernization report...")

        # Count files
        total_html = len(list(self.pod_root.glob('*.html')))
        modernized = len(list(self.modernized_dir.glob('*.html')))
        archived = len(list(self.archive_dir.glob('*.html')))

        report = {
            'timestamp': datetime.now().isoformat(),
            'total_html_files': total_html,
            'modernized_count': modernized,
            'archived_count': archived,
            'completion_percentage': round((modernized / total_html * 100) if total_html > 0 else 0, 2),
            'session_stats': {
                'projects_modernized': self.stats['projects_modernized'],
                'old_files_archived': self.stats['old_files_archived']
            }
        }

        report_file = self.modernized_dir / f'modernization_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        success = self.write_file_directly(report_file, json.dumps(report, indent=2))

        if success:
            print(f"  ✓ Modernization report saved")
            print(f"  📊 Progress: {report['completion_percentage']}% of projects modernized")

        return report

    async def run_modernization_session(self):
        """Run complete modernization session"""
        print("\n" + "="*60)
        print("🎨 Modernizer Gardener Starting...")
        print("   Rebuilding old projects with 2025 design standards")
        print("="*60)

        if not self.ember_available:
            print("\n⚠ Ember not available - cannot modernize")
            return

        # Task 1: Scan and modernize
        await self.run_task(
            self.scan_and_modernize,
            "scan_modernize"
        )

        # Task 2: Create report
        await self.run_task(
            self.create_modernization_report,
            "create_report"
        )

        # Print final stats
        self.print_stats()
        print(f"\n📊 Modernization Summary:")
        print(f"   Projects modernized: {self.stats['projects_modernized']}")
        print(f"   Old versions archived: {self.stats['old_files_archived']}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = ModernizerGardener()
    await gardener.run_modernization_session()


if __name__ == '__main__':
    asyncio.run(main())
