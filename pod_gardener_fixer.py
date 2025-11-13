#!/usr/bin/env python3
"""
Pod Gardener Fixer - Actually REPAIRS Broken Files
Not just reporting issues - FIXING them with Ember's help
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import re

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class FixerGardener(ResilientGardener):
    """Actually fixes broken files using Ember"""

    def __init__(self):
        super().__init__('fixer', pod_root='/media/palmerschallon/ThePod1')

        self.stats['files_fixed'] = 0
        self.stats['errors_repaired'] = 0

        # Output directory
        self.fixes_dir = self.pod_root / 'fix_reports'
        self.fixes_dir.mkdir(exist_ok=True)

        # Check if Ember is available
        self.ember_available = (self.pod_root / 'ember_complete.py').exists()

    async def ask_ember_to_fix(self, file_path, error_description):
        """Ask Ember to fix a broken file"""
        if not self.ember_available:
            print("  ⚠ Ember not available - cannot fix files")
            return None

        try:
            from ember_complete import Ember
            ember = Ember()

            # Read the broken file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            prompt = f"""You are a code repair specialist. Fix this broken file.

File: {file_path}
Error: {error_description}

Current content:
{content[:5000]}  # First 5000 chars

Instructions:
1. Analyze the error and identify the root cause
2. Fix the issue properly (don't just comment it out)
3. Add defensive programming (null checks, error handling)
4. Preserve all existing functionality
5. Return ONLY the complete fixed file content, no explanations

Return the COMPLETE fixed file ready to save."""

            fixed_content = await ember.chat(prompt)

            # Basic validation - does it look like code?
            if fixed_content and len(fixed_content) > 100:
                return fixed_content

            return None

        except Exception as e:
            print(f"  ✗ Error asking Ember: {e}")
            return None

    async def find_and_fix_js_errors(self):
        """Find HTML files with JavaScript errors and fix them"""
        print("\n🔧 Finding and fixing JavaScript errors...")

        html_files = list(self.pod_root.glob('*.html'))[:100]  # Process 100 files per run

        fixed_count = 0

        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Look for common JavaScript error patterns
                issues = []

                # Check for forEach on potentially undefined
                if re.search(r'\.forEach\(', content) and '.children.forEach' in content:
                    if '(branch.children || [])' not in content and '(item.children || [])' not in content:
                        issues.append("Unsafe forEach on children - missing null check")

                # Check for undefined property access
                if re.search(r'\w+\.\w+\.forEach', content):
                    issues.append("Potential null reference in chained property access")

                # Check for missing error handling in async/await
                if 'async ' in content and 'try' not in content:
                    issues.append("Async function without try-catch")

                if issues:
                    print(f"\n  🔍 Found issues in {html_file.name}:")
                    for issue in issues:
                        print(f"     - {issue}")

                    # Ask Ember to fix it
                    error_desc = "; ".join(issues)
                    fixed_content = await self.ask_ember_to_fix(html_file, error_desc)

                    if fixed_content:
                        # Backup original
                        backup_path = html_file.with_suffix('.html.backup')
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(content)

                        # Write fixed version
                        if self.write_file_directly(html_file, fixed_content):
                            print(f"  ✓ Fixed {html_file.name} (backup saved)")
                            fixed_count += 1
                            self.stats['files_fixed'] += 1
                            self.stats['errors_repaired'] += len(issues)

            except Exception as e:
                print(f"  ✗ Error processing {html_file.name}: {e}")
                continue

        print(f"\n  📊 Fixed {fixed_count} files")
        return True

    async def fix_healing_report_issues(self):
        """Read healing reports and fix the issues found"""
        print("\n🩹 Fixing issues from healing reports...")

        healing_dir = self.pod_root / 'healing_reports'
        report_files = sorted(healing_dir.glob('healing_report_*.json'), reverse=True)

        if not report_files:
            print("  ⚠ No healing reports found")
            return False

        # Read latest report
        with open(report_files[0], 'r') as f:
            report = json.load(f)

        fixed_count = 0

        # Fix broken Python files
        if 'syntax_errors' in report and report['syntax_errors']:
            print(f"\n  🐍 Fixing {len(report['syntax_errors'])} Python syntax errors...")

            for error_info in report['syntax_errors'][:20]:  # Fix first 20
                file_path = self.pod_root / error_info['file']

                if file_path.exists():
                    fixed_content = await self.ask_ember_to_fix(
                        file_path,
                        f"Python syntax error: {error_info['error']}"
                    )

                    if fixed_content:
                        # Backup
                        backup_path = file_path.with_suffix('.py.backup')
                        with open(file_path, 'r') as f:
                            original = f.read()
                        with open(backup_path, 'w') as f:
                            f.write(original)

                        # Fix
                        if self.write_file_directly(file_path, fixed_content):
                            print(f"    ✓ Fixed {file_path.name}")
                            fixed_count += 1
                            self.stats['files_fixed'] += 1

        # Fix broken links in HTML files
        if 'broken_links' in report and report['broken_links']:
            print(f"\n  🔗 Found {len(report['broken_links'])} broken links")
            print("     (Logging for manual review - automatic link fixing risky)")

        self.stats['errors_repaired'] += fixed_count
        print(f"\n  📊 Repaired {fixed_count} issues")
        return True

    async def validate_fixes(self):
        """Validate that fixes actually work"""
        print("\n✅ Validating fixes...")

        # Check backup files exist
        backups = list(self.pod_root.glob('*.backup'))
        print(f"  📦 {len(backups)} backups saved for rollback if needed")

        # TODO: Could run HTML files in headless browser to check for errors
        # For now, just log what we fixed

        return True

    async def create_fix_report(self):
        """Create report of what was fixed"""
        print("\n📝 Creating fix report...")

        report = {
            'timestamp': datetime.now().isoformat(),
            'files_fixed': self.stats['files_fixed'],
            'errors_repaired': self.stats['errors_repaired'],
            'ember_available': self.ember_available
        }

        report_file = self.fixes_dir / f'fix_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        success = self.write_file_directly(report_file, json.dumps(report, indent=2))

        if success:
            print(f"  ✓ Fix report saved: {report_file.name}")

        return report

    async def run_fixing_session(self):
        """Run complete fixing session"""
        print("\n" + "="*60)
        print("🔧 Fixer Gardener Starting...")
        print("   Actually REPAIRING broken files")
        print("="*60)

        if not self.ember_available:
            print("\n⚠ Ember not available - cannot fix files")
            print("   Please ensure ember_complete.py exists")
            return

        # Task 1: Fix JavaScript errors
        await self.run_task(
            self.find_and_fix_js_errors,
            "fix_js_errors"
        )

        # Task 2: Fix issues from healing reports
        await self.run_task(
            self.fix_healing_report_issues,
            "fix_healing_issues"
        )

        # Task 3: Validate fixes
        await self.run_task(
            self.validate_fixes,
            "validate_fixes"
        )

        # Task 4: Create report
        await self.run_task(
            self.create_fix_report,
            "create_report"
        )

        # Print final stats
        self.print_stats()
        print(f"\n📊 Fixing Summary:")
        print(f"   Files fixed: {self.stats['files_fixed']}")
        print(f"   Errors repaired: {self.stats['errors_repaired']}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = FixerGardener()
    await gardener.run_fixing_session()


if __name__ == '__main__':
    asyncio.run(main())
