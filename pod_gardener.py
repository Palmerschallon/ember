#!/usr/bin/env python3
"""
Pod Gardener - Autonomous Exploration and Generation System

Ember tends the garden:
- Explores unexplored territories
- Fills sparse/empty directories
- Continues evolution chains
- Generates missing documentation
- Makes intelligent connections
"""
import os
import sys
import json
import asyncio
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import random

# Add Pod to path for Ember integration
sys.path.insert(0, '/media/palmerschallon/ThePod1')

class PodGardener:
    """Autonomous system that tends to the Pod's creative space"""

    def __init__(self, pod_root="/media/palmerschallon/ThePod1"):
        self.pod_root = Path(pod_root)
        self.map_file = self.pod_root / "POD_MAP.json"
        self.gardener_log = self.pod_root / "GARDENER_LOG.json"

        # Ember integration
        self.ember = None

        # Activity tracking
        self.activities = {
            'gaps_filled': [],
            'evolutions_continued': [],
            'documentation_created': [],
            'connections_made': [],
            'explorations': []
        }

        # Load existing map
        self.pod_map = self.load_map()

    def load_map(self):
        """Load the Pod map if it exists"""
        if self.map_file.exists():
            with open(self.map_file, 'r') as f:
                return json.load(f)
        return None

    async def initialize_ember(self):
        """Initialize Ember for content generation"""
        try:
            from ember_complete import Ember
            self.ember = Ember()
            print("✓ Ember initialized for autonomous creation")
        except Exception as e:
            print(f"⚠ Could not initialize Ember: {e}")
            print("  Gardener will run in analysis-only mode")

    async def explore_and_tend(self):
        """Main gardening loop - explore and tend to the Pod"""
        print("\n🌱 Pod Gardener Starting...")
        print("="*60)

        # Initialize Ember
        await self.initialize_ember()

        # 1. Find gaps and opportunities
        print("\n📊 Analyzing the Pod...")
        gaps = self.find_gaps()
        sparse = self.find_sparse_directories()
        incomplete = self.find_incomplete_evolutions()
        undocumented = self.find_undocumented_projects()

        # 2. Report findings
        self.report_findings(gaps, sparse, incomplete, undocumented)

        # 3. Take autonomous actions (if Ember available)
        if self.ember:
            print("\n🌿 Taking autonomous actions...")
            await self.tend_garden(gaps, sparse, incomplete, undocumented)
        else:
            print("\n📝 Analysis complete. Enable Ember for autonomous actions.")

        # 4. Save activity log
        self.save_log()

        print("\n✨ Gardening session complete!")

    def find_gaps(self):
        """Find empty or near-empty directories"""
        gaps = []

        for root, dirs, files in os.walk(self.pod_root):
            # Skip certain directories
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            path = Path(root)

            # Empty directory
            if not files and not dirs:
                gaps.append({
                    'path': str(path.relative_to(self.pod_root)),
                    'type': 'empty',
                    'reason': 'Directory has no files or subdirectories'
                })

            # Very sparse (1-2 files)
            elif len(files) <= 2 and len(dirs) == 0:
                gaps.append({
                    'path': str(path.relative_to(self.pod_root)),
                    'type': 'sparse',
                    'file_count': len(files),
                    'reason': f'Only {len(files)} file(s), could be expanded'
                })

        return gaps[:20]  # Top 20 gaps

    def find_sparse_directories(self):
        """Find directories with potential for growth"""
        sparse = []

        # Look for thematic directories that could have more content
        interesting_patterns = [
            'vr', 'game', 'experiment', 'demo', 'prototype',
            'test', 'example', 'creation', 'generated'
        ]

        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            path = Path(root)
            path_lower = str(path).lower()

            # Check if directory name suggests it should have more content
            if any(pattern in path_lower for pattern in interesting_patterns):
                if 1 <= len(files) <= 5:  # Small but not empty
                    sparse.append({
                        'path': str(path.relative_to(self.pod_root)),
                        'file_count': len(files),
                        'files': files[:5],  # Sample files
                        'potential': 'Could generate variations or continuations'
                    })

        return sparse[:15]

    def find_incomplete_evolutions(self):
        """Find evolution chains that stopped"""
        incomplete = []

        # Look for files with generation numbers
        gen_files = defaultdict(list)

        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            for filename in files:
                if '_gen' in filename.lower():
                    # Extract base name and gen number
                    try:
                        base = filename.split('_gen')[0]
                        gen_part = filename.split('_gen')[1].split('.')[0].split('_')[0]
                        gen_num = int(''.join(filter(str.isdigit, gen_part)))

                        gen_files[base].append({
                            'file': filename,
                            'gen': gen_num,
                            'path': os.path.join(root, filename)
                        })
                    except (ValueError, IndexError):
                        continue

        # Find chains that could continue
        for base, gens in gen_files.items():
            if len(gens) >= 3:  # At least 3 generations
                gens_sorted = sorted(gens, key=lambda x: x['gen'])
                max_gen = gens_sorted[-1]['gen']

                # If max gen is less than 100, could continue
                if max_gen < 100:
                    incomplete.append({
                        'base': base,
                        'current_max': max_gen,
                        'generation_count': len(gens),
                        'latest_file': gens_sorted[-1]['file'],
                        'potential_next': f"{base}_gen{max_gen + 1}",
                        'suggestion': f'Continue evolution from gen{max_gen} to gen{max_gen + 10}'
                    })

        return incomplete[:10]

    def find_undocumented_projects(self):
        """Find project directories without README files"""
        undocumented = []

        project_indicators = ['src', 'lib', 'components', 'modules']

        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            path = Path(root)

            # Has code but no README
            has_code = any(f.endswith(('.py', '.js', '.html')) for f in files)
            has_readme = any('readme' in f.lower() for f in files)
            has_structure = any(d in dirs for d in project_indicators)

            if (has_code or has_structure) and not has_readme and len(files) > 3:
                undocumented.append({
                    'path': str(path.relative_to(self.pod_root)),
                    'file_count': len(files),
                    'has_structure': has_structure,
                    'file_types': list(set(Path(f).suffix for f in files if Path(f).suffix)),
                    'suggestion': 'Generate README documenting the project'
                })

        return undocumented[:10]

    def report_findings(self, gaps, sparse, incomplete, undocumented):
        """Print findings report"""
        print(f"\n{'='*60}")
        print("GARDENING OPPORTUNITIES DISCOVERED")
        print(f"{'='*60}")

        print(f"\n📭 Empty/Sparse Directories: {len(gaps)}")
        for gap in gaps[:5]:
            print(f"  • {gap['path']} - {gap['type']}")
            if gap['type'] == 'sparse':
                print(f"    → {gap['reason']}")

        print(f"\n🌱 Sparse Thematic Directories: {len(sparse)}")
        for s in sparse[:5]:
            print(f"  • {s['path']} ({s['file_count']} files)")
            print(f"    → {s['potential']}")

        print(f"\n🧬 Incomplete Evolution Chains: {len(incomplete)}")
        for inc in incomplete[:5]:
            print(f"  • {inc['base']} (gen0-{inc['current_max']}, {inc['generation_count']} files)")
            print(f"    → {inc['suggestion']}")

        print(f"\n📄 Undocumented Projects: {len(undocumented)}")
        for proj in undocumented[:5]:
            print(f"  • {proj['path']} ({proj['file_count']} files)")
            print(f"    → {proj['suggestion']}")

    async def tend_garden(self, gaps, sparse, incomplete, undocumented):
        """Take autonomous actions to tend the garden"""

        # Pick one task from each category
        tasks = []

        if sparse:
            tasks.append(('expand_sparse', random.choice(sparse)))

        if incomplete:
            tasks.append(('continue_evolution', random.choice(incomplete)))

        if undocumented:
            tasks.append(('document_project', random.choice(undocumented)))

        # Execute tasks
        for task_type, task_data in tasks:
            print(f"\n🌿 {task_type}: {task_data.get('path', task_data.get('base', 'unknown'))}")

            try:
                if task_type == 'expand_sparse':
                    await self.expand_sparse_directory(task_data)
                elif task_type == 'continue_evolution':
                    await self.continue_evolution_chain(task_data)
                elif task_type == 'document_project':
                    await self.document_project(task_data)
            except Exception as e:
                print(f"  ⚠ Error during {task_type}: {e}")

    async def expand_sparse_directory(self, data):
        """Generate content for sparse directory"""
        print(f"  Analyzing existing content...")

        # Read sample files to understand context
        dir_path = self.pod_root / data['path']
        context = f"Directory: {data['path']}\n"
        context += f"Existing files: {', '.join(data['files'])}\n"

        # Ask Ember to create a variation or related content
        prompt = f"""I found a sparse directory in the Pod that could use more content:

{context}

This appears to be a creative/experimental space. Generate a NEW creative piece that fits this directory's theme. Be inventive and experimental. Save it with an appropriate name in this directory.

Directory path: {dir_path}"""

        print(f"  Asking Ember to create content...")
        response = await self.ember.chat(prompt)

        self.activities['gaps_filled'].append({
            'path': data['path'],
            'timestamp': datetime.now().isoformat(),
            'action': 'expanded_sparse_directory'
        })

        print(f"  ✓ Content created")

    async def continue_evolution_chain(self, data):
        """Continue an evolution chain"""
        print(f"  Found evolution chain: {data['base']} (gen{data['current_max']})")

        # Read the latest generation
        latest_path = Path(data['latest_file'])

        # Determine save path (same directory as latest)
        next_filename = f"{data['base']}_gen{data['current_max'] + 1}.html"
        save_path = latest_path.parent / next_filename

        try:
            with open(latest_path, 'r') as f:
                latest_content = f.read()  # Read full file
        except:
            latest_content = "[Could not read file]"

        prompt = f"""I'm giving you an HTML file from an evolution chain. Your task is to create the NEXT generation.

Evolution chain: {data['base']}
Current generation: gen{data['current_max']}
Next generation: gen{data['current_max'] + 1}
Total generations so far: {data['generation_count']}

Here is the COMPLETE source code of the current generation:

{latest_content}

---

Your task:
1. Read and understand the code above
2. Make a creative evolution - improve graphics, add features, change behavior, or take it in an interesting direction
3. Write the COMPLETE evolved HTML file using write_file() with these parameters:
   - path: {save_path}
   - content: <your complete evolved HTML code>

Generate the full evolved HTML now and save it to {save_path}"""

        print(f"  Generating next evolution: {next_filename}")
        response = await self.ember.chat(prompt)

        self.activities['evolutions_continued'].append({
            'base': data['base'],
            'from_gen': data['current_max'],
            'to_gen': data['current_max'] + 1,
            'timestamp': datetime.now().isoformat()
        })

        print(f"  ✓ Evolution continued to gen{data['current_max'] + 1}")

    async def document_project(self, data):
        """Generate README for undocumented project"""
        print(f"  Analyzing project structure...")

        dir_path = self.pod_root / data['path']

        # Sample some files
        files = list(dir_path.glob('*'))[:10]
        file_list = '\n'.join([f"- {f.name}" for f in files])

        prompt = f"""I found an undocumented project directory in the Pod:

Path: {data['path']}
File count: {data['file_count']}
File types: {', '.join(data['file_types'])}

Sample files:
{file_list}

Please create a README.md file for this project. Analyze what you can infer about the project from the files, and write clear documentation. Save it as README.md in: {dir_path}"""

        print(f"  Generating README.md...")
        response = await self.ember.chat(prompt)

        self.activities['documentation_created'].append({
            'path': data['path'],
            'timestamp': datetime.now().isoformat()
        })

        print(f"  ✓ Documentation created")

    def save_log(self):
        """Save gardening activity log"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'activities': self.activities,
            'summary': {
                'gaps_filled': len(self.activities['gaps_filled']),
                'evolutions_continued': len(self.activities['evolutions_continued']),
                'documentation_created': len(self.activities['documentation_created'])
            }
        }

        # Append to log
        if self.gardener_log.exists():
            with open(self.gardener_log, 'r') as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)

        # Keep last 100 entries
        logs = logs[-100:]

        with open(self.gardener_log, 'w') as f:
            json.dump(logs, f, indent=2)

        print(f"\n💾 Activity log saved to {self.gardener_log}")


async def main():
    """Run the Pod Gardener"""
    gardener = PodGardener()
    await gardener.explore_and_tend()


if __name__ == "__main__":
    asyncio.run(main())
