#!/usr/bin/env python3
"""
Pod Gardener Researcher - Learn & Experiment
Studies patterns, creates learning experiments, discovers new techniques
Inherits error-resistance from ResilientGardener
"""

import sys
import asyncio
from pathlib import Path
from datetime import datetime
import random

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener

# Import Ember
try:
    from ember_multi_claude import EmberMultiClaude
    EMBER_AVAILABLE = True
except:
    EMBER_AVAILABLE = False


class ResearcherGardener(ResilientGardener):
    """Learns from the Pod and creates experimental projects"""

    def __init__(self):
        super().__init__('researcher', pod_root='/media/palmerschallon/ThePod1')

        # Experiment directory
        self.experiments_dir = self.pod_root / 'learning_experiments'
        self.experiments_dir.mkdir(exist_ok=True)

        # Learning topics
        self.topics = [
            'advanced CSS animations and transitions',
            'WebGL shaders and 3D graphics',
            'interactive data visualizations with D3.js',
            'generative art algorithms',
            'audio synthesis and visualization',
            'particle systems and physics',
            'procedural generation techniques',
            'creative coding with Canvas API',
            'responsive design patterns',
            'accessibility best practices'
        ]

        # Ember instance
        self.ember = None
        if EMBER_AVAILABLE:
            try:
                self.ember = EmberMultiClaude(
                    working_dir=str(self.pod_root),
                    model_name='claude-sonnet-4'
                )
            except Exception as e:
                print(f"⚠️ Could not initialize Ember: {e}")

    async def study_existing_work(self, topic):
        """Study existing examples in the Pod related to a topic"""
        print(f"  📚 Studying existing work on: {topic}")

        # Find relevant files
        html_files = self.discover_files_by_extension(['.html'], max_files=50)

        # Sample a few to study
        sample_size = min(5, len(html_files))
        samples = random.sample(html_files, sample_size)

        print(f"    Found {len(html_files)} HTML files, studying {sample_size} examples")

        return {
            'topic': topic,
            'total_files': len(html_files),
            'studied_samples': samples
        }

    async def create_learning_experiment(self, topic):
        """Create a new experimental project based on learning"""
        if not self.ember:
            print("    ⚠️ Ember not available, skipping experiment creation")
            return None

        try:
            prompt = f"""Create an experimental learning project focused on: {topic}

Make it:
1. Educational - demonstrates the concept clearly
2. Interactive - user can play with parameters
3. Well-commented - explains what's happening
4. Visually interesting - engaging to explore
5. Self-contained - single HTML file with inline CSS/JS

Include controls/sliders to adjust parameters and see the effects in real-time.

Return ONLY the complete HTML, no explanations."""

            response = await self.ember.async_prompt(prompt)
            html_content = response.get('response', '')

            # Extract HTML if wrapped
            if '```html' in html_content:
                html_content = html_content.split('```html')[1].split('```')[0]
            elif '```' in html_content:
                html_content = html_content.split('```')[1].split('```')[0]

            return html_content.strip()

        except Exception as e:
            print(f"    ⚠️ Failed to create experiment: {e}")
            return None

    async def document_learning(self, topic, experiment_path):
        """Document what was learned from this experiment"""
        if not self.ember:
            return None

        try:
            prompt = f"""Create a brief learning summary for the experiment on: {topic}

Include:
1. Key concepts demonstrated
2. Techniques used
3. Interesting discoveries
4. Ideas for future experiments

Keep it concise (2-3 paragraphs). Return plain text, no markdown."""

            response = await self.ember.async_prompt(prompt)
            learning_notes = response.get('response', '').strip()

            return learning_notes

        except Exception as e:
            print(f"    ⚠️ Failed to document learning: {e}")
            return None

    async def run_research_session(self):
        """Run a complete research & learning session"""
        print("\n" + "="*60)
        print("🎓 Pod Researcher Gardener Starting...")
        print("="*60)

        # Pick 3 random topics to explore
        topics_to_explore = random.sample(self.topics, min(3, len(self.topics)))

        for i, topic in enumerate(topics_to_explore, 1):
            print(f"\n\n{'='*60}")
            print(f"Learning Session {i}/{len(topics_to_explore)}: {topic}")
            print("="*60)

            # Task 1: Study existing work
            study_results = await self.run_task(
                self.study_existing_work,
                f"study_{topic[:30]}",
                topic
            )

            # Task 2: Create experiment
            if self.ember:
                print(f"\n🔹 Task: Creating learning experiment")
                html_content = await self.execute_with_timeout(
                    self.create_learning_experiment(topic),
                    f"create_experiment_{topic[:30]}",
                    timeout=180
                )

                if html_content:
                    # Save experiment
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    safe_name = topic.replace(' ', '_')[:40]
                    filename = f'{timestamp}_{safe_name}.html'
                    filepath = self.experiments_dir / filename

                    self.write_file_directly(filepath, html_content)
                    print(f"    ✓ Experiment saved: {filename}")

                    # Task 3: Document learning
                    print(f"\n🔹 Task: Documenting learning")
                    learning_notes = await self.execute_with_timeout(
                        self.document_learning(topic, filepath),
                        f"document_{topic[:30]}",
                        timeout=60
                    )

                    if learning_notes:
                        notes_file = filepath.with_suffix('.txt')
                        self.write_file_directly(notes_file, learning_notes)
                        print(f"    ✓ Learning notes saved")

        # Print final stats
        self.print_stats()
        print(f"\n✨ Experiments saved to: {self.experiments_dir}")
        print("="*60)


async def main():
    """Main entry point"""
    gardener = ResearcherGardener()
    await gardener.run_research_session()


if __name__ == '__main__':
    asyncio.run(main())
