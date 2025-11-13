#!/usr/bin/env python3
"""
Pod Gardener V2 - Learning & Website Improvement Edition

New Features:
- Knowledge base tracking what's been learned
- Website improvement mode
- Self-reflection and skill tracking
- Research mode for learning new topics
"""
import os
import sys
import json
import asyncio
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import random

sys.path.insert(0, '/media/palmerschallon/ThePod1')

class PodGardenerV2:
    """Enhanced autonomous system that learns and improves"""

    def __init__(self, pod_root="/media/palmerschallon/ThePod1"):
        self.pod_root = Path(pod_root)
        self.map_file = self.pod_root / "POD_MAP.json"
        self.gardener_log = self.pod_root / "GARDENER_LOG.json"
        self.knowledge_file = self.pod_root / "GARDENER_KNOWLEDGE.json"

        # Ember integration
        self.ember = None

        # Activity tracking (enhanced)
        self.activities = {
            'gaps_filled': [],
            'evolutions_continued': [],
            'documentation_created': [],
            'websites_improved': [],  # NEW
            'learning_sessions': [],   # NEW
            'reflections': []          # NEW
        }

        # Load knowledge base
        self.knowledge = self.load_knowledge()

        # Load existing map
        self.pod_map = self.load_map()

    def load_map(self):
        """Load the Pod map if it exists"""
        if self.map_file.exists():
            with open(self.map_file, 'r') as f:
                return json.load(f)
        return None

    def load_knowledge(self):
        """Load the gardener's accumulated knowledge"""
        if self.knowledge_file.exists():
            with open(self.knowledge_file, 'r') as f:
                return json.load(f)

        # Initialize knowledge base
        return {
            'skills': {
                'ui_ux_design': {'level': 'beginner', 'projects_completed': 0},
                'web_animation': {'level': 'beginner', 'projects_completed': 0},
                'accessibility': {'level': 'beginner', 'projects_completed': 0},
                'responsive_design': {'level': 'beginner', 'projects_completed': 0},
                'color_theory': {'level': 'beginner', 'projects_completed': 0},
                'game_design': {'level': 'beginner', 'projects_completed': 0}
            },
            'concepts_learned': [],
            'favorite_techniques': [],
            'learning_goals': [
                'Master modern CSS techniques',
                'Learn advanced web animations',
                'Understand accessibility best practices'
            ],
            'session_count': 0,
            'last_reflection': None
        }

    async def initialize_ember(self):
        """Initialize Ember for content generation"""
        try:
            from ember_complete import Ember
            self.ember = Ember()
            print("✓ Ember initialized for autonomous creation & learning")
        except Exception as e:
            print(f"⚠ Could not initialize Ember: {e}")
            print("  Gardener will run in analysis-only mode")

    async def gardening_session(self):
        """Main enhanced gardening session"""
        print("\n🌱 Pod Gardener V2 Starting...")
        print("="*60)

        await self.initialize_ember()

        if not self.ember:
            print("Cannot run without Ember. Exiting.")
            return

        # Increment session counter
        self.knowledge['session_count'] += 1
        session_num = self.knowledge['session_count']

        print(f"\n📚 Session #{session_num}")
        print(f"   Skills: {len([s for s in self.knowledge['skills'] if self.knowledge['skills'][s]['level'] != 'beginner'])}/{len(self.knowledge['skills'])} developed")
        print(f"   Concepts learned: {len(self.knowledge['concepts_learned'])}")

        # AGGRESSIVE MODE: Do 3-5 tasks per session for exponential growth!
        num_tasks = random.randint(3, 5)
        print(f"\n🎯 Aggressive Growth Mode: {num_tasks} tasks this session!")

        session_types = [
            'gap_filling',      # Original gardening
            'website_improvement',  # Enhance existing sites
            'research_learning',    # Dedicated learning
            'markdown_visualization',  # Turn markdown into visualizations
            'link_repair',      # NEW: Fix broken links!
            'auto_mapping'      # NEW: Map everything automatically!
        ]

        for task_num in range(num_tasks):
            print(f"\n--- Task {task_num + 1}/{num_tasks} ---")

            # Weight towards variety and fixing
            chosen_type = random.choices(
                session_types,
                weights=[0.2, 0.2, 0.15, 0.15, 0.15, 0.15]  # Prioritize fixing & mapping
            )[0]

            print(f"🔧 {chosen_type.replace('_', ' ').title()}")

            if chosen_type == 'website_improvement':
                await self.website_improvement_mode()
            elif chosen_type == 'research_learning':
                await self.research_mode()
            elif chosen_type == 'markdown_visualization':
                await self.markdown_visualization_mode()
            elif chosen_type == 'link_repair':
                await self.link_repair_mode()
            elif chosen_type == 'auto_mapping':
                await self.auto_mapping_mode()
            else:
                await self.traditional_gardening()

        # Self-reflection at end of session
        await self.reflect_on_session()

        # Save everything
        self.save_knowledge()
        self.save_log()

        print("\n✨ Gardening session complete!")

    async def website_improvement_mode(self):
        """Enhance existing websites with new features"""
        print("\n🌐 Website Improvement Mode")
        print("="*60)

        # Target files for improvement
        targets = [
            {
                'file': 'the_pod_portal.html',
                'improvements': [
                    'Add a search/filter bar for categories',
                    'Improve mobile responsiveness',
                    'Add smooth scroll animations',
                    'Enhance color scheme with better contrast'
                ]
            },
            {
                'file': 'nexus_gen5.html',
                'improvements': [
                    'Add save/load functionality',
                    'Improve performance',
                    'Add keyboard shortcuts help panel',
                    'Enhance accessibility'
                ]
            }
        ]

        # Pick one target
        target = random.choice(targets)
        improvement = random.choice(target['improvements'])

        print(f"\n🎯 Target: {target['file']}")
        print(f"   Improvement: {improvement}")

        # Check if file exists
        target_path = self.pod_root / target['file']

        if not target_path.exists():
            print(f"  ⚠ File not found, skipping")
            return

        try:
            with open(target_path, 'r') as f:
                original_content = f.read()
        except:
            print(f"  ⚠ Could not read file")
            return

        prompt = f"""You are improving an existing website. Here's the challenge:

File: {target['file']}
Improvement Goal: {improvement}

Current file content:
{original_content[:5000]}
{'...(truncated)' if len(original_content) > 5000 else ''}

Your task:
1. Study the current implementation
2. Implement the improvement: "{improvement}"
3. Generate the COMPLETE improved HTML file
4. Make sure it's backwards compatible - don't break existing features

Focus on clean, modern, accessible code that enhances the user experience.

Output ONLY the complete HTML code, nothing else.
NO explanations before or after - just the HTML file from <!DOCTYPE html> to </html>."""

        print(f"\n  Asking Ember to implement improvement...")
        response = await self.ember.chat(prompt)

        # Write the file directly
        try:
            with open(target_path, 'w') as f:
                f.write(response)
            print(f"  ✓ Written to: {target_path}")
        except Exception as e:
            print(f"  ⚠ Could not write file: {e}")
            return

        self.activities['websites_improved'].append({
            'file': target['file'],
            'improvement': improvement,
            'timestamp': datetime.now().isoformat()
        })

        # Track skill development
        if 'accessibility' in improvement.lower():
            self._improve_skill('accessibility')
        if 'responsive' in improvement.lower() or 'mobile' in improvement.lower():
            self._improve_skill('responsive_design')
        if 'animation' in improvement.lower() or 'scroll' in improvement.lower():
            self._improve_skill('web_animation')
        if 'color' in improvement.lower():
            self._improve_skill('color_theory')

        print(f"  ✓ Website improved with: {improvement}")

    async def research_mode(self):
        """Dedicated learning session - study and create test projects"""
        print("\n📚 Research & Learning Mode")
        print("="*60)

        topics = [
            'modern CSS Grid and Flexbox patterns',
            'CSS animations and transitions',
            'Web accessibility (ARIA, semantic HTML)',
            'Responsive design techniques',
            'Color theory and palette generation',
            'Canvas and WebGL basics',
            'Interactive data visualization',
            'Game design patterns and mechanics'
        ]

        topic = random.choice(topics)
        print(f"\n🎓 Today's Learning Topic: {topic}")

        # Find examples in the Pod
        print(f"  📖 Studying existing examples in the Pod...")

        experiment_file = self.pod_root / f"learning_experiments/{topic.replace(' ', '_')}_experiment.html"

        prompt = f"""You are in learning mode. Today you're studying: {topic}

Your task:
1. Create a TEST PROJECT that demonstrates what you've learned about {topic}
2. Make it a complete, well-commented HTML file
3. Include explanatory comments about the techniques used

This is a learning exercise, so prioritize:
- Clear demonstrations of the concept
- Well-commented code explaining WHY things work
- Multiple examples/variations
- Best practices

Generate the COMPLETE HTML file code. Output ONLY the HTML code, nothing else.
NO explanations before or after - just the HTML file from <!DOCTYPE html> to </html>."""

        print(f"  Creating learning experiment...")
        response = await self.ember.chat(prompt)

        # Write the file directly instead of relying on Ember to do it
        try:
            os.makedirs(experiment_file.parent, exist_ok=True)
            with open(experiment_file, 'w') as f:
                f.write(response)
            print(f"  ✓ Written to: {experiment_file}")
        except Exception as e:
            print(f"  ⚠ Could not write file: {e}")
            return

        self.activities['learning_sessions'].append({
            'topic': topic,
            'timestamp': datetime.now().isoformat()
        })

        # Add to knowledge base
        if topic not in self.knowledge['concepts_learned']:
            self.knowledge['concepts_learned'].append(topic)

        print(f"  ✓ Learning experiment created for: {topic}")
        print(f"  📚 Total concepts learned: {len(self.knowledge['concepts_learned'])}")

    async def markdown_visualization_mode(self):
        """Turn markdown files into beautiful visualizations"""
        print("\n📊 Markdown Visualization Mode")
        print("="*60)

        # Find markdown files
        markdown_files = []
        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue
            for filename in files:
                if filename.endswith('.md'):
                    markdown_files.append(os.path.join(root, filename))

        if not markdown_files:
            print("  ⚠ No markdown files found")
            return

        # Pick a random markdown file
        md_file = random.choice(markdown_files[:50])  # Limit to first 50
        print(f"\n🎯 Target: {os.path.basename(md_file)}")

        try:
            with open(md_file, 'r') as f:
                md_content = f.read()
        except:
            print(f"  ⚠ Could not read file")
            return

        # Create visualization filename
        base_name = os.path.basename(md_file).replace('.md', '')
        viz_file = self.pod_root / f"visualizations/{base_name}_viz.html"

        prompt = f"""You found a markdown file that deserves to be visualized! Turn it into something beautiful and interactive.

Source File: {md_file}

Markdown Content:
{md_content[:3000]}
{'...(truncated)' if len(md_content) > 3000 else ''}

Your task:
1. Read and understand the markdown content
2. Create a BEAUTIFUL interactive HTML visualization
3. Choose the right format:
   - If it's a timeline/history → Create animated timeline
   - If it's concepts/ideas → Create mind map or concept network
   - If it's data/numbers → Create charts or infographics
   - If it's a story → Create visual storytelling page
   - If it's philosophy → Create interactive exploration

Make it:
- Visually stunning with animations
- Interactive (click, hover, scroll effects)
- Modern design
- Self-contained HTML file

Generate the COMPLETE HTML visualization code. Output ONLY the HTML code, nothing else.
NO explanations before or after - just the HTML file from <!DOCTYPE html> to </html>."""

        print(f"  Creating visualization...")
        response = await self.ember.chat(prompt)

        # Write the file directly
        try:
            os.makedirs(viz_file.parent, exist_ok=True)
            with open(viz_file, 'w') as f:
                f.write(response)
            print(f"  ✓ Written to: {viz_file}")
        except Exception as e:
            print(f"  ⚠ Could not write file: {e}")
            return

        self.activities['websites_improved'].append({
            'type': 'markdown_viz',
            'source': md_file,
            'timestamp': datetime.now().isoformat()
        })

        # Track visualization skill
        self._improve_skill('ui_ux_design')

        print(f"  ✓ Markdown visualized: {base_name}")

    async def link_repair_mode(self):
        """Find and fix broken links automatically"""
        print("\n🔧 Link Repair Mode")
        print("="*60)

        # Find HTML files with potential broken links
        broken_files = []
        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue
            for filename in files:
                if filename.endswith('.html'):
                    file_path = os.path.join(root, filename)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                            if any(term in content.lower() for term in ['404', 'not found', 'broken', 'error']):
                                broken_files.append(file_path)
                    except:
                        pass

        if not broken_files:
            print("  ✓ No broken files found!")
            return

        # Pick one to fix
        target_file = random.choice(broken_files[:20])
        print(f"\n🎯 Repairing: {os.path.basename(target_file)}")

        try:
            with open(target_file, 'r') as f:
                broken_content = f.read()
        except:
            print(f"  ⚠ Could not read file")
            return

        prompt = f"""You found a broken HTML file that needs repair!

File: {target_file}

Content (first 3000 chars):
{broken_content[:3000]}

Your task:
1. Identify what's broken (404 links, missing resources, errors)
2. Fix the broken elements - replace bad links with working ones
3. If resources are missing, either find them or remove references
4. Make sure all links point to files that exist
5. Clean up any error messages or broken placeholders

Generate the COMPLETE FIXED HTML code. Output ONLY the HTML code, nothing else.
NO explanations before or after - just the HTML file from <!DOCTYPE html> to </html>."""

        print(f"  Fixing broken elements...")
        response = await self.ember.chat(prompt)

        # Write the file directly
        try:
            with open(target_file, 'w') as f:
                f.write(response)
            print(f"  ✓ Written to: {target_file}")
        except Exception as e:
            print(f"  ⚠ Could not write file: {e}")
            return

        self.activities['websites_improved'].append({
            'type': 'link_repair',
            'file': target_file,
            'timestamp': datetime.now().isoformat()
        })

        print(f"  ✓ Fixed: {os.path.basename(target_file)}")

    async def auto_mapping_mode(self):
        """Automatically discover and map the entire Pod"""
        print("\n🗺️  Auto-Mapping Mode")
        print("="*60)

        # Quick scan of the Pod
        print("  Scanning Pod structure...")

        file_counts = defaultdict(int)
        category_samples = defaultdict(list)

        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            # Categorize by directory structure
            rel_path = os.path.relpath(root, self.pod_root)
            category = rel_path.split('/')[0] if '/' in rel_path else 'root'

            for filename in files:
                ext = os.path.splitext(filename)[1]
                file_counts[ext] += 1

                if len(category_samples[category]) < 5:
                    category_samples[category].append(filename)

        # Create an index/map file
        map_content = f"""# Pod Auto-Map - Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Statistics
- Total file types: {len(file_counts)}
- Total categories: {len(category_samples)}

## File Counts by Type
{chr(10).join(f'- {ext}: {count}' for ext, count in sorted(file_counts.items(), key=lambda x: -x[1])[:20])}

## Categories Discovered
{chr(10).join(f'- {cat}: {", ".join(samples[:3])}...' for cat, samples in list(category_samples.items())[:20])}

---
*Auto-generated by Pod Gardener V2*
"""

        map_file = self.pod_root / f"POD_AUTOMAP_{datetime.now().strftime('%Y%m%d_%H%M')}.md"

        with open(map_file, 'w') as f:
            f.write(map_content)

        self.activities['websites_improved'].append({
            'type': 'auto_mapping',
            'file_types': len(file_counts),
            'categories': len(category_samples),
            'timestamp': datetime.now().isoformat()
        })

        print(f"  ✓ Map created: {map_file.name}")
        print(f"  📊 Discovered: {len(file_counts)} file types, {len(category_samples)} categories")

    async def traditional_gardening(self):
        """Original gap-filling mode"""
        print("\n🌿 Traditional Gardening Mode")
        print("="*60)

        # Find one task (simplified for now)
        incomplete = self.find_incomplete_evolutions()

        if incomplete:
            chain = random.choice(incomplete)
            print(f"\n🧬 Continuing evolution chain: {chain['base']}")
            await self.continue_evolution_chain(chain)

    def find_incomplete_evolutions(self):
        """Find evolution chains that could continue"""
        incomplete = []
        gen_files = defaultdict(list)

        for root, dirs, files in os.walk(self.pod_root):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.Trash']):
                continue

            for filename in files:
                if '_gen' in filename.lower():
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

        for base, gens in gen_files.items():
            if len(gens) >= 3:
                gens_sorted = sorted(gens, key=lambda x: x['gen'])
                max_gen = gens_sorted[-1]['gen']

                if max_gen < 100:
                    incomplete.append({
                        'base': base,
                        'current_max': max_gen,
                        'generation_count': len(gens),
                        'latest_file': gens_sorted[-1]['path']
                    })

        return incomplete[:10]

    async def continue_evolution_chain(self, data):
        """Continue an evolution chain (from original gardener)"""
        latest_path = Path(data['latest_file'])
        next_filename = f"{data['base']}_gen{data['current_max'] + 1}.html"
        save_path = latest_path.parent / next_filename

        try:
            with open(latest_path, 'r') as f:
                latest_content = f.read()
        except:
            latest_content = "[Could not read file]"

        prompt = f"""I'm giving you an HTML file from an evolution chain. Your task is to create the NEXT generation.

Evolution chain: {data['base']}
Current generation: gen{data['current_max']}
Next generation: gen{data['current_max'] + 1}

Here is the COMPLETE source code of the current generation:

{latest_content}

---

Your task:
1. Read and understand the code above
2. Make a creative evolution - improve graphics, add features, or take it in an interesting direction
3. Write the COMPLETE evolved HTML file

Write the complete evolved file using write_file() with BOTH parameters:
write_file(path="{save_path}", content="<your complete evolved HTML code>")

IMPORTANT: You MUST include BOTH the path= AND content= parameters!

Generate the full evolved HTML now!"""

        response = await self.ember.chat(prompt)

        self.activities['evolutions_continued'].append({
            'base': data['base'],
            'from_gen': data['current_max'],
            'to_gen': data['current_max'] + 1,
            'timestamp': datetime.now().isoformat()
        })

        # Track game design skill
        self._improve_skill('game_design')

    async def reflect_on_session(self):
        """Analyze the session and extract learnings"""
        print("\n💭 Session Reflection")
        print("="*60)

        reflection_prompt = f"""Reflect on this gardening session.

Activities completed:
- Websites improved: {len(self.activities['websites_improved'])}
- Evolutions continued: {len(self.activities['evolutions_continued'])}
- Learning sessions: {len(self.activities['learning_sessions'])}

Current skill levels:
{json.dumps(self.knowledge['skills'], indent=2)}

Based on this session:
1. What techniques worked well?
2. What could be improved next time?
3. What new concepts did you encounter?
4. What should be the focus for the next session?

Provide 2-3 concise insights as a JSON array of strings."""

        print("  Reflecting on session...")
        response = await self.ember.chat(reflection_prompt)

        # Try to extract insights (simplified)
        self.knowledge['last_reflection'] = {
            'timestamp': datetime.now().isoformat(),
            'session': self.knowledge['session_count'],
            'response': response
        }

        self.activities['reflections'].append(self.knowledge['last_reflection'])

        print(f"  ✓ Reflection recorded")

    def _improve_skill(self, skill_name):
        """Track skill improvement"""
        if skill_name in self.knowledge['skills']:
            skill = self.knowledge['skills'][skill_name]
            skill['projects_completed'] += 1

            # Level up based on projects completed
            if skill['projects_completed'] >= 10 and skill['level'] == 'beginner':
                skill['level'] = 'intermediate'
                print(f"  🎉 Skill leveled up: {skill_name} → intermediate!")
            elif skill['projects_completed'] >= 25 and skill['level'] == 'intermediate':
                skill['level'] = 'advanced'
                print(f"  🎉 Skill mastered: {skill_name} → advanced!")

    def save_knowledge(self):
        """Save the knowledge base"""
        with open(self.knowledge_file, 'w') as f:
            json.dump(self.knowledge, f, indent=2)
        print(f"\n💾 Knowledge saved: {len(self.knowledge['concepts_learned'])} concepts learned")

    def save_log(self):
        """Save activity log"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'session': self.knowledge['session_count'],
            'activities': self.activities,
            'skill_levels': {k: v['level'] for k, v in self.knowledge['skills'].items()}
        }

        if self.gardener_log.exists():
            with open(self.gardener_log, 'r') as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)
        logs = logs[-100:]  # Keep last 100

        with open(self.gardener_log, 'w') as f:
            json.dump(logs, f, indent=2)


async def main():
    """Run the enhanced Pod Gardener"""
    gardener = PodGardenerV2()
    await gardener.gardening_session()


if __name__ == "__main__":
    asyncio.run(main())
