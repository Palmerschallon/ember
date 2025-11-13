#!/usr/bin/env python3
"""
Pod Gardener Visualizer - Discover & Showcase EVERYTHING
Finds Python, notebooks, data, images - generates beautiful HTML visualizations
Inherits error-resistance from ResilientGardener
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime
import json

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener

# Import Ember
try:
    from ember_multi_claude import EmberMultiClaude
    EMBER_AVAILABLE = True
except:
    EMBER_AVAILABLE = False
    print("⚠️ Ember not available, will work in discovery-only mode")


class VisualizerGardener(ResilientGardener):
    """Discovers and visualizes ALL content types in the Pod"""

    def __init__(self):
        super().__init__('visualizer', pod_root='/media/palmerschallon/ThePod1')

        # Output directory
        self.viz_dir = self.pod_root / 'visualizations'
        self.viz_dir.mkdir(exist_ok=True)

        # Content types to discover
        self.content_types = {
            'python': ['.py'],
            'notebooks': ['.ipynb'],
            'data': ['.csv', '.json', '.yaml', '.yml', '.pkl', '.parquet'],
            'images': ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp'],
            'markdown': ['.md'],
            'configs': ['.toml', '.ini', '.conf', '.cfg'],
            'logs': ['.log']
        }

        # Discovery stats
        self.discovered = {category: [] for category in self.content_types.keys()}

        # Ember instance (if available)
        self.ember = None
        if EMBER_AVAILABLE:
            try:
                self.ember = EmberMultiClaude(
                    working_dir=str(self.pod_root),
                    model_name='claude-sonnet-4'
                )
            except Exception as e:
                print(f"⚠️ Could not initialize Ember: {e}")

    async def discover_all_content(self):
        """Discover all content types throughout the Pod"""
        print("\n🔍 Discovering content across the Pod...")

        for category, extensions in self.content_types.items():
            print(f"\n  🔹 Scanning for {category}...")
            files = self.discover_files_by_extension(extensions, max_files=500)
            self.discovered[category] = files
            print(f"    Found {len(files)} {category} files")

        # Save discovery results
        discovery_log = self.logs_dir / 'visualizer_discovery.json'
        with open(discovery_log, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'discovered': {k: len(v) for k, v in self.discovered.items()},
                'total_files': sum(len(v) for v in self.discovered.values())
            }, f, indent=2)

        print(f"\n✓ Discovery complete! Total files: {sum(len(v) for v in self.discovered.values())}")
        return self.discovered

    async def visualize_python_file(self, filepath):
        """Create HTML visualization of a Python file"""
        if not self.ember:
            return None

        try:
            # Read the Python file
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()

            # Get Ember to generate HTML visualization
            prompt = f"""Create a beautiful HTML page showcasing this Python file: {Path(filepath).name}

Include:
1. Syntax-highlighted code display
2. Brief description of what the file does
3. Key functions/classes with descriptions
4. Dependencies/imports
5. Nice styling with dark theme

The code:
```python
{code[:5000]}  # First 5000 chars
```

Return ONLY the complete HTML, no explanations."""

            response = await self.ember.async_prompt(prompt)
            html_content = response.get('response', '')

            # Extract HTML if wrapped in markdown code blocks
            if '```html' in html_content:
                html_content = html_content.split('```html')[1].split('```')[0]
            elif '```' in html_content:
                html_content = html_content.split('```')[1].split('```')[0]

            return html_content.strip()

        except Exception as e:
            print(f"    ⚠️ Failed to read {filepath}: {e}")
            return None

    async def visualize_notebook(self, filepath):
        """Create HTML visualization of a Jupyter notebook"""
        if not self.ember:
            return None

        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                notebook = json.load(f)

            # Get basic notebook info
            cell_count = len(notebook.get('cells', []))
            code_cells = sum(1 for c in notebook.get('cells', []) if c.get('cell_type') == 'code')

            prompt = f"""Create a beautiful HTML page showcasing this Jupyter notebook: {Path(filepath).name}

Notebook has {cell_count} cells ({code_cells} code cells).

Include:
1. Title and description
2. Cell count and types
3. Preview of first few cells
4. Nice styling with dark theme

Return ONLY the complete HTML, no explanations."""

            response = await self.ember.async_prompt(prompt)
            html_content = response.get('response', '')

            if '```html' in html_content:
                html_content = html_content.split('```html')[1].split('```')[0]
            elif '```' in html_content:
                html_content = html_content.split('```')[1].split('```')[0]

            return html_content.strip()

        except Exception as e:
            print(f"    ⚠️ Failed to process notebook {filepath}: {e}")
            return None

    async def create_category_index(self, category, files):
        """Create an index page for a content category"""
        if not self.ember or not files:
            return None

        # Sample files for the index
        sample_files = files[:50]  # First 50 files
        file_list = '\n'.join([f"- {Path(f).name} ({Path(f).parent})" for f in sample_files])

        prompt = f"""Create a beautiful HTML index page for {category} files in the Pod.

Found {len(files)} {category} files. Here are some examples:
{file_list}

Include:
1. Category title and description
2. File count
3. List of files with links
4. Search/filter functionality
5. Beautiful dark theme styling

Return ONLY the complete HTML, no explanations."""

        try:
            response = await self.ember.async_prompt(prompt)
            html_content = response.get('response', '')

            if '```html' in html_content:
                html_content = html_content.split('```html')[1].split('```')[0]
            elif '```' in html_content:
                html_content = html_content.split('```')[1].split('```')[0]

            return html_content.strip()
        except Exception as e:
            print(f"    ⚠️ Failed to create index for {category}: {e}")
            return None

    async def create_master_index(self):
        """Create master index of all discovered content"""
        if not self.ember:
            return None

        stats = {cat: len(files) for cat, files in self.discovered.items()}
        total = sum(stats.values())

        prompt = f"""Create a beautiful master HTML index for the Pod Visualizer.

Discovered content:
{json.dumps(stats, indent=2)}

Total files: {total}

Include:
1. Big bold title: "Pod Content Visualizer"
2. Total file count
3. Category breakdown with counts
4. Links to each category index
5. Last updated timestamp
6. Beautiful dark theme with gradients
7. Responsive design

Return ONLY the complete HTML, no explanations."""

        try:
            response = await self.ember.async_prompt(prompt)
            html_content = response.get('response', '')

            if '```html' in html_content:
                html_content = html_content.split('```html')[1].split('```')[0]
            elif '```' in html_content:
                html_content = html_content.split('```')[1].split('```')[0]

            return html_content.strip()
        except Exception as e:
            print(f"    ⚠️ Failed to create master index: {e}")
            return None

    async def run_visualization_session(self):
        """Run a complete visualization session"""
        print("\n" + "="*60)
        print("🎨 Pod Visualizer Gardener Starting...")
        print("="*60)

        # Task 1: Discover all content
        await self.run_task(
            self.discover_all_content,
            "discover_content"
        )

        # Task 2: Create master index
        if self.ember:
            print("\n🔹 Task: Creating master index")
            master_html = await self.execute_with_timeout(
                self.create_master_index(),
                "create_master_index"
            )
            if master_html:
                self.write_file_directly(
                    self.viz_dir / 'index.html',
                    master_html
                )

        # Task 3: Create category indexes
        if self.ember:
            for category, files in self.discovered.items():
                if not files:
                    continue

                print(f"\n🔹 Task: Creating {category} index")
                index_html = await self.execute_with_timeout(
                    self.create_category_index(category, files),
                    f"create_{category}_index"
                )
                if index_html:
                    self.write_file_directly(
                        self.viz_dir / f'{category}_index.html',
                        index_html
                    )

        # Task 4: Visualize sample Python files (5 most recent)
        if self.ember and self.discovered['python']:
            print("\n🔹 Task: Visualizing sample Python files")
            python_files = sorted(
                self.discovered['python'],
                key=lambda f: self.get_file_age_days(f)
            )[:5]

            for py_file in python_files:
                task_id = f"visualize_python_{Path(py_file).name}"
                print(f"\n  Processing {Path(py_file).name}...")
                html = await self.execute_with_timeout(
                    self.visualize_python_file(py_file),
                    task_id,
                    timeout=180  # 3 minutes for Python viz
                )
                if html:
                    output_name = Path(py_file).stem + '_viz.html'
                    self.write_file_directly(
                        self.viz_dir / output_name,
                        html
                    )

        # Task 5: Visualize sample notebooks (3 most recent)
        if self.ember and self.discovered['notebooks']:
            print("\n🔹 Task: Visualizing sample notebooks")
            notebooks = sorted(
                self.discovered['notebooks'],
                key=lambda f: self.get_file_age_days(f)
            )[:3]

            for nb_file in notebooks:
                task_id = f"visualize_notebook_{Path(nb_file).name}"
                print(f"\n  Processing {Path(nb_file).name}...")
                html = await self.execute_with_timeout(
                    self.visualize_notebook(nb_file),
                    task_id,
                    timeout=180
                )
                if html:
                    output_name = Path(nb_file).stem + '_viz.html'
                    self.write_file_directly(
                        self.viz_dir / output_name,
                        html
                    )

        # Print final stats
        self.print_stats()
        print(f"\n✨ Visualizations saved to: {self.viz_dir}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = VisualizerGardener()
    await gardener.run_visualization_session()


if __name__ == '__main__':
    asyncio.run(main())
