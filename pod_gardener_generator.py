#!/usr/bin/env python3
"""
Pod Gardener Generator - Autonomous Content Creator
Uses Ember to create NEW content: blog posts, research papers, games, narratives
Makes the Pod truly SELF-EVOLVING and GENERATIVE
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import os

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class GeneratorGardener(ResilientGardener):
    """Generates NEW content autonomously using Ember"""

    def __init__(self):
        super().__init__('generator', pod_root='/media/palmerschallon/ThePod1')

        self.stats['content_generated'] = 0
        self.stats['blog_posts'] = 0
        self.stats['research_papers'] = 0
        self.stats['games'] = 0

        # Output directories
        self.blog_dir = self.pod_root / 'pod_blog'
        self.research_dir = self.pod_root / 'pod_research'
        self.generated_dir = self.pod_root / 'pod_generated'

        self.blog_dir.mkdir(exist_ok=True)
        self.research_dir.mkdir(exist_ok=True)
        self.generated_dir.mkdir(exist_ok=True)

        # Load latest manifest for analysis
        self.manifest = None

        # Check if Ember bridge is available
        self.ember_available = os.path.exists(os.path.join(self.pod_root, 'ember_complete.py'))

    async def load_discoveries(self):
        """Load latest manifest from Deep Curator"""
        print("\n📖 Loading discoveries from Deep Curator...")

        manifest_dir = self.pod_root / 'pod_manifests'
        latest_file = manifest_dir / 'latest_manifest.json'

        if not latest_file.exists():
            print("  ⚠ No manifest found - Deep Curator needs to run first")
            return False

        try:
            with open(latest_file, 'r') as f:
                self.manifest = json.load(f)

            print(f"  ✓ Loaded manifest:")
            print(f"    {self.manifest['total_files']:,} total files")
            print(f"    {len(self.manifest.get('special_folders', {}))} special folders")
            return True
        except Exception as e:
            print(f"  ✗ Error loading manifest: {e}")
            return False

    async def ask_ember(self, prompt):
        """Ask Ember to generate content"""
        if not self.ember_available:
            print("  ⚠ Ember not available")
            return None

        try:
            # Dynamic import of Ember
            from ember_complete import Ember

            ember = Ember()
            response = await ember.chat(prompt)
            return response
        except Exception as e:
            print(f"  ✗ Ember error: {e}")
            return None

    async def generate_blog_post(self):
        """Generate a blog post analyzing Pod discoveries"""
        print("\n✍️  Generating blog post about Pod discoveries...")

        if not self.manifest:
            return False

        # Pick interesting facts for the blog post
        html_count = self.manifest['file_counts'].get('html', 0)
        python_count = self.manifest['file_counts'].get('python', 0)
        special_folders = list(self.manifest.get('special_folders', {}).keys())

        prompt = f"""You are a creative tech blogger documenting an incredible digital creative ecosystem.

Write a fascinating, engaging blog post about "The Pod" - a 168 GB creative universe containing:

- {html_count:,} HTML projects and experiments
- {python_count:,} Python scripts and tools
- Special discovered universes: {', '.join(special_folders[:5])}
- Total of {self.manifest['total_files']:,} files

The blog post should:
1. Have a catchy title
2. Tell the story of this creative ecosystem
3. Highlight interesting patterns and discoveries
4. Be written in an excited, curious tone
5. Be 400-600 words
6. Use markdown formatting

Write ONLY the markdown content of the blog post, starting with the title as # heading.
"""

        content = await self.ask_ember(prompt)

        if content:
            filename = f"blog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            filepath = self.blog_dir / filename

            if self.write_file_directly(filepath, content):
                print(f"  ✓ Blog post created: {filename}")
                self.stats['blog_posts'] += 1
                self.stats['content_generated'] += 1
                return True

        return False

    async def generate_research_paper(self):
        """Generate a research paper analyzing the creative ecosystem"""
        print("\n📄 Generating research paper...")

        if not self.manifest:
            return False

        prompt = f"""You are an academic researcher studying digital creative ecosystems and AI-assisted creativity.

Write a short research paper (abstract-style) analyzing "The Pod" ecosystem:

Statistics:
- Total files: {self.manifest['total_files']:,}
- Size: {self.manifest['total_size_gb']} GB
- HTML projects: {self.manifest['file_counts'].get('html', 0):,}
- Python modules: {self.manifest['file_counts'].get('python', 0):,}
- Markdown docs: {self.manifest['file_counts'].get('markdown', 0):,}
- Images: {self.manifest['file_counts'].get('images', 0):,}

Special universes found:
{json.dumps(self.manifest.get('special_folders', {}), indent=2)}

Write an academic-style paper with:
1. Title
2. Abstract (100-150 words)
3. Introduction to the ecosystem
4. Methodology (how it was discovered)
5. Key Findings (patterns observed)
6. Discussion (implications for AI-assisted creativity)
7. Conclusion

Use markdown formatting with proper sections.
"""

        content = await self.ask_ember(prompt)

        if content:
            filename = f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            filepath = self.research_dir / filename

            if self.write_file_directly(filepath, content):
                print(f"  ✓ Research paper created: {filename}")
                self.stats['research_papers'] += 1
                self.stats['content_generated'] += 1
                return True

        return False

    async def generate_creative_experiment(self):
        """Generate a new creative experiment based on discovered patterns"""
        print("\n🎨 Generating creative experiment...")

        if not self.manifest:
            return False

        # Analyze top HTML projects for patterns
        html_projects = self.manifest.get('top_html_projects', [])[:5]
        project_names = [p['name'] for p in html_projects]

        prompt = f"""You are a creative AI generating new experimental web projects.

Looking at existing projects in the ecosystem:
{', '.join(project_names[:10])}

Create a NEW creative HTML experiment that:
1. Combines ideas from the discovered projects
2. Adds something novel and unexpected
3. Is fully self-contained in one HTML file
4. Uses creative coding (Canvas, WebGL, or generative art)
5. Has interactive elements

Generate ONLY the complete HTML file content, ready to save.
Make it visually striking and conceptually interesting.
"""

        content = await self.ask_ember(prompt)

        if content and '<html' in content.lower():
            filename = f"experiment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            filepath = self.generated_dir / filename

            if self.write_file_directly(filepath, content):
                print(f"  ✓ Creative experiment generated: {filename}")
                self.stats['games'] += 1
                self.stats['content_generated'] += 1
                return True

        return False

    async def generate_narrative(self):
        """Generate a narrative connecting discovered universes"""
        print("\n📚 Generating narrative about discovered universes...")

        if not self.manifest:
            return False

        special_folders = self.manifest.get('special_folders', {})

        if not special_folders:
            print("  ⚠ No special folders to write about")
            return False

        folder_list = '\n'.join([f"- {name}: {info['file_count']} files at {info['path']}"
                                 for name, info in list(special_folders.items())[:6]])

        prompt = f"""You are a creative writer discovering hidden universes in a digital landscape.

You've discovered these mysterious folders in "The Pod":

{folder_list}

Write a short creative narrative (300-400 words) that:
1. Imagines these as actual universes or worlds
2. Explores what might exist in each one
3. Creates connections between them
4. Has a sense of wonder and discovery
5. Uses vivid, imaginative language

Write in markdown format with a title.
"""

        content = await self.ask_ember(prompt)

        if content:
            filename = f"narrative_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            filepath = self.blog_dir / filename

            if self.write_file_directly(filepath, content):
                print(f"  ✓ Narrative created: {filename}")
                self.stats['blog_posts'] += 1
                self.stats['content_generated'] += 1
                return True

        return False

    async def run_generation_session(self):
        """Run complete generation session"""
        print("\n" + "="*60)
        print("🎭 Generator Gardener Starting...")
        print("   Creating NEW content autonomously")
        print("="*60)

        # Task 1: Load discoveries
        if not await self.run_task(
            self.load_discoveries,
            "load_discoveries"
        ):
            print("\n⚠ Cannot generate without discoveries - skipping")
            return

        if not self.ember_available:
            print("\n⚠ Ember not available - cannot generate content")
            return

        # Task 2: Generate blog post
        await self.run_task(
            self.generate_blog_post,
            "generate_blog"
        )

        # Task 3: Generate research paper (less frequently)
        if datetime.now().hour % 3 == 0:  # Every 3 hours
            await self.run_task(
                self.generate_research_paper,
                "generate_research"
            )

        # Task 4: Generate creative experiment
        await self.run_task(
            self.generate_creative_experiment,
            "generate_experiment"
        )

        # Task 5: Generate narrative
        if len(self.manifest.get('special_folders', {})) > 0:
            await self.run_task(
                self.generate_narrative,
                "generate_narrative"
            )

        # Print final stats
        self.print_stats()
        print(f"\n📊 Content Generated This Session:")
        print(f"   Blog posts: {self.stats['blog_posts']}")
        print(f"   Research papers: {self.stats['research_papers']}")
        print(f"   Experiments: {self.stats['games']}")
        print(f"   Total: {self.stats['content_generated']}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = GeneratorGardener()
    await gardener.run_generation_session()


if __name__ == '__main__':
    asyncio.run(main())
