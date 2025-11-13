#!/usr/bin/env python3
"""
Pod Gardener Healer - Fix & Repair
Finds broken links, fixes errors, repairs damaged files
Inherits error-resistance from ResilientGardener
"""

import sys
import asyncio
import re
from pathlib import Path
from datetime import datetime
import json

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class HealerGardener(ResilientGardener):
    """Finds and fixes broken links and errors in the Pod"""

    def __init__(self):
        super().__init__('healer', pod_root='/media/palmerschallon/ThePod1')

        # Healing reports directory
        self.reports_dir = self.pod_root / 'healing_reports'
        self.reports_dir.mkdir(exist_ok=True)

        # Issues found
        self.issues = {
            'broken_links': [],
            'missing_files': [],
            'syntax_errors': [],
            'other': []
        }

    async def scan_html_for_broken_links(self, filepath):
        """Scan an HTML file for broken links"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find all href and src attributes
            links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)

            broken = []
            for link in links:
                # Skip external URLs
                if link.startswith('http://') or link.startswith('https://'):
                    continue
                if link.startswith('data:'):
                    continue
                if link.startswith('#'):
                    continue

                # Check if file exists
                link_path = Path(filepath).parent / link
                if not link_path.exists():
                    broken.append({
                        'file': str(filepath),
                        'broken_link': link,
                        'expected_path': str(link_path)
                    })

            return broken

        except Exception as e:
            return []

    async def check_for_syntax_errors(self, filepath):
        """Check Python files for basic syntax errors"""
        if not filepath.endswith('.py'):
            return None

        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Try to compile it
            compile(content, filepath, 'exec')
            return None  # No errors

        except SyntaxError as e:
            return {
                'file': str(filepath),
                'error': str(e),
                'line': e.lineno
            }
        except Exception:
            return None

    async def scan_files_for_issues(self):
        """Scan Pod files for various issues"""
        print("\n🔍 Scanning for issues...")

        # Scan HTML files for broken links
        print("\n  🔹 Checking HTML files for broken links...")
        html_files = self.discover_files_by_extension(['.html'], max_files=100)

        for html_file in html_files[:50]:  # Check first 50
            broken = await self.scan_html_for_broken_links(html_file)
            if broken:
                self.issues['broken_links'].extend(broken)

        print(f"    Found {len(self.issues['broken_links'])} broken links")

        # Scan Python files for syntax errors
        print("\n  🔹 Checking Python files for syntax errors...")
        py_files = self.discover_files_by_extension(['.py'], max_files=100)

        for py_file in py_files[:50]:  # Check first 50
            error = await self.check_for_syntax_errors(py_file)
            if error:
                self.issues['syntax_errors'].append(error)

        print(f"    Found {len(self.issues['syntax_errors'])} syntax errors")

        total_issues = sum(len(v) for v in self.issues.values())
        return total_issues

    async def generate_healing_report(self):
        """Generate a report of all issues found"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = self.reports_dir / f'healing_report_{timestamp}.json'

        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'broken_links': len(self.issues['broken_links']),
                'missing_files': len(self.issues['missing_files']),
                'syntax_errors': len(self.issues['syntax_errors']),
                'total_issues': sum(len(v) for v in self.issues.values())
            },
            'details': self.issues
        }

        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"    ✓ Report saved: {report_file.name}")

        # Also create a readable text report
        txt_report = self.reports_dir / f'healing_report_{timestamp}.txt'
        with open(txt_report, 'w') as f:
            f.write("="*60 + "\n")
            f.write("Pod Healer Report\n")
            f.write("="*60 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write(f"Total Issues Found: {report['summary']['total_issues']}\n\n")

            if self.issues['broken_links']:
                f.write(f"\nBroken Links ({len(self.issues['broken_links'])}):\n")
                f.write("-" * 60 + "\n")
                for link in self.issues['broken_links'][:20]:  # First 20
                    f.write(f"  File: {link['file']}\n")
                    f.write(f"  Link: {link['broken_link']}\n\n")

            if self.issues['syntax_errors']:
                f.write(f"\nSyntax Errors ({len(self.issues['syntax_errors'])}):\n")
                f.write("-" * 60 + "\n")
                for error in self.issues['syntax_errors']:
                    f.write(f"  File: {error['file']}\n")
                    f.write(f"  Line: {error['line']}\n")
                    f.write(f"  Error: {error['error']}\n\n")

        print(f"    ✓ Text report saved: {txt_report.name}")

        return report

    async def run_healing_session(self):
        """Run a complete healing session"""
        print("\n" + "="*60)
        print("🏥 Pod Healer Gardener Starting...")
        print("="*60)

        # Task 1: Scan for issues
        total_issues = await self.run_task(
            self.scan_files_for_issues,
            "scan_for_issues"
        )

        # Task 2: Generate report
        print("\n🔹 Task: Generating healing report")
        await self.execute_with_timeout(
            self.generate_healing_report(),
            "generate_report"
        )

        # Print final stats
        self.print_stats()
        print(f"\n✨ Reports saved to: {self.reports_dir}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = HealerGardener()
    await gardener.run_healing_session()


if __name__ == '__main__':
    asyncio.run(main())
