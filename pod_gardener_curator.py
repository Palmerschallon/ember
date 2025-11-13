#!/usr/bin/env python3
"""
Pod Gardener Curator - Dynamic Portal Builder
Reads all discoveries from other gardeners and rebuilds the Pod Portal dynamically
Makes the portal a LIVING, GROWING showcase of actual content
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import os
from collections import defaultdict

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener


class CuratorGardener(ResilientGardener):
    """Curates and rebuilds the Pod Portal from actual discovered content"""

    def __init__(self):
        super().__init__('curator', pod_root='/media/palmerschallon/ThePod1')

        # Reinitialize stats with our custom fields
        self.stats['last_updated'] = datetime.now().isoformat()

        # Directories to pull from
        self.viz_dir = self.pod_root / 'visualizations'
        self.maps_dir = self.pod_root / 'pod_maps'
        self.healing_dir = self.pod_root / 'healing_reports'
        self.experiments_dir = self.pod_root / 'learning_experiments'

        # Portal file
        self.portal_file = self.pod_root / 'the_pod_portal.html'

        # Discovered content
        self.content = {
            'visualizations': [],
            'maps': [],
            'healing_reports': [],
            'experiments': [],
            'python_files': [],
            'notebooks': [],
            'images': [],
            'data_files': []
        }

        # Add custom fields to inherited stats
        self.stats['total_files'] = 0
        self.stats['categories'] = {}

    async def gather_discoveries(self):
        """Gather all discoveries from other gardeners"""
        print("\n📊 Gathering discoveries from all gardeners...")

        # Read latest map file
        map_files = sorted(self.maps_dir.glob('pod_map_*.json'), reverse=True)
        if map_files:
            with open(map_files[0], 'r') as f:
                map_data = json.load(f)
                self.stats['total_files'] = map_data.get('total_files', 0)
                self.stats['categories'] = map_data.get('categories', {})
                print(f"  ✓ Loaded map: {self.stats['total_files']} files across {len(self.stats['categories'])} categories")

        # Find visualizations
        viz_files = list(self.viz_dir.glob('*.html'))
        self.content['visualizations'] = [
            {
                'name': f.stem,
                'path': str(f.relative_to(self.pod_root)),
                'size': f.stat().st_size,
                'modified': datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            }
            for f in viz_files
        ]
        print(f"  ✓ Found {len(viz_files)} visualizations")

        # Find experiments
        exp_files = list(self.experiments_dir.glob('*.html'))
        self.content['experiments'] = [
            {
                'name': f.stem,
                'path': str(f.relative_to(self.pod_root)),
                'modified': datetime.fromtimestamp(f.stat().st_mtime).isoformat()
            }
            for f in exp_files[:20]  # Latest 20
        ]
        print(f"  ✓ Found {len(exp_files)} learning experiments")

        # Find healing reports
        healing_files = sorted(self.healing_dir.glob('healing_report_*.txt'), reverse=True)
        if healing_files:
            self.content['healing_reports'].append({
                'name': healing_files[0].stem,
                'path': str(healing_files[0].relative_to(self.pod_root))
            })
            print(f"  ✓ Found latest healing report")

        # Discover actual content from Pod
        print("\n  🔍 Scanning Pod for actual content...")

        # Python files (sample)
        py_files = list(self.pod_root.glob('*.py'))[:10]
        self.content['python_files'] = [f.name for f in py_files]

        # HTML projects (sample)
        html_files = [f for f in self.pod_root.glob('*.html') if f.name != 'the_pod_portal.html'][:15]
        self.content['html_projects'] = [
            {'name': f.stem, 'path': f.name} for f in html_files
        ]

        print(f"    Found {len(py_files)} Python files")
        print(f"    Found {len(html_files)} HTML projects")

        return True

    async def build_dynamic_portal(self):
        """Build the Pod Portal dynamically from actual discoveries"""
        print("\n🎨 Building dynamic Pod Portal...")

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Pod Portal - Living Creative Ecosystem</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #e0e0e0;
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
            padding: 3rem 2rem;
            text-align: center;
            border-bottom: 3px solid #00d9ff;
            box-shadow: 0 4px 20px rgba(0, 217, 255, 0.3);
        }}

        .header h1 {{
            font-size: 3.5rem;
            background: linear-gradient(135deg, #00d9ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            animation: glow 2s ease-in-out infinite alternate;
        }}

        @keyframes glow {{
            from {{ text-shadow: 0 0 10px rgba(0, 217, 255, 0.5); }}
            to {{ text-shadow: 0 0 20px rgba(123, 44, 191, 0.8); }}
        }}

        .last-updated {{
            color: #00d9ff;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        .stats-bar {{
            background: rgba(22, 33, 62, 0.8);
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}

        .stat-card {{
            text-align: center;
            padding: 1.5rem;
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(123, 44, 191, 0.1));
            border-radius: 10px;
            border: 1px solid rgba(0, 217, 255, 0.3);
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 217, 255, 0.4);
        }}

        .stat-number {{
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, #00d9ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .stat-label {{
            color: #a0a0a0;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .section {{
            margin: 3rem 0;
        }}

        .section-title {{
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #00d9ff;
            border-left: 4px solid #7b2cbf;
            padding-left: 1rem;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .card {{
            background: rgba(22, 33, 62, 0.6);
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid rgba(0, 217, 255, 0.2);
            transition: all 0.3s;
        }}

        .card:hover {{
            border-color: #00d9ff;
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 217, 255, 0.3);
        }}

        .card-title {{
            font-size: 1.2rem;
            color: #00d9ff;
            margin-bottom: 0.5rem;
        }}

        .card-link {{
            color: #7b2cbf;
            text-decoration: none;
            font-size: 0.9rem;
            display: inline-block;
            margin-top: 0.5rem;
            transition: color 0.3s;
        }}

        .card-link:hover {{
            color: #00d9ff;
        }}

        .badge {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            background: linear-gradient(135deg, #00d9ff, #7b2cbf);
            border-radius: 20px;
            font-size: 0.8rem;
            margin: 0.3rem;
        }}

        .footer {{
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            border-top: 1px solid rgba(0, 217, 255, 0.3);
            color: #a0a0a0;
        }}

        .self-healing {{
            color: #00d9ff;
            font-weight: bold;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌱 The Pod Portal</h1>
        <p>Living Creative Ecosystem - 168 GB of Innovation</p>
        <p class="last-updated">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p class="self-healing">⚡ SELF-HEALING Every 30 Minutes! ⚡</p>
    </div>

    <div class="stats-bar">
        <div class="stat-card">
            <div class="stat-number">{self.stats['total_files']:,}</div>
            <div class="stat-label">Total Files</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{len(self.content['visualizations'])}</div>
            <div class="stat-label">Visualizations</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{len(self.content.get('html_projects', []))}</div>
            <div class="stat-label">HTML Projects</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{len(self.content['experiments'])}</div>
            <div class="stat-label">Learning Experiments</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{self.stats['categories'].get('code', 0)}</div>
            <div class="stat-label">Code Files</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{self.stats['categories'].get('images', 0)}</div>
            <div class="stat-label">Images</div>
        </div>
    </div>

    <div class="container">
"""

        # HTML Projects Section
        if self.content.get('html_projects'):
            html += """
        <div class="section">
            <h2 class="section-title">🎨 HTML Projects & Creations</h2>
            <div class="grid">
"""
            for project in self.content['html_projects'][:12]:
                html += f"""
                <div class="card">
                    <div class="card-title">{project['name']}</div>
                    <a href="{project['path']}" class="card-link" target="_blank">Open Project →</a>
                </div>
"""
            html += """
            </div>
        </div>
"""

        # Visualizations Section
        if self.content['visualizations']:
            html += """
        <div class="section">
            <h2 class="section-title">📊 Content Visualizations</h2>
            <div class="grid">
"""
            for viz in self.content['visualizations'][:9]:
                html += f"""
                <div class="card">
                    <div class="card-title">{viz['name']}</div>
                    <span class="badge">Auto-Generated</span>
                    <a href="{viz['path']}" class="card-link" target="_blank">View Visualization →</a>
                </div>
"""
            html += """
            </div>
        </div>
"""

        # Learning Experiments Section
        if self.content['experiments']:
            html += """
        <div class="section">
            <h2 class="section-title">🧪 Learning Experiments</h2>
            <div class="grid">
"""
            for exp in self.content['experiments'][:6]:
                html += f"""
                <div class="card">
                    <div class="card-title">{exp['name'][:50]}</div>
                    <span class="badge">Research</span>
                    <a href="{exp['path']}" class="card-link" target="_blank">View Experiment →</a>
                </div>
"""
            html += """
            </div>
        </div>
"""

        # Categories Breakdown
        if self.stats['categories']:
            html += """
        <div class="section">
            <h2 class="section-title">📁 Content Categories</h2>
            <div class="grid">
"""
            for category, count in sorted(self.stats['categories'].items(), key=lambda x: x[1], reverse=True):
                html += f"""
                <div class="card">
                    <div class="card-title">{category.upper()}</div>
                    <div class="stat-number">{count:,}</div>
                    <div class="stat-label">files</div>
                </div>
"""
            html += """
            </div>
        </div>
"""

        html += f"""
    </div>

    <div class="footer">
        <p>🌱 Pod Gardener Fleet Active - Discovering, Healing, Learning, Mapping</p>
        <p>Next Update: 30 minutes | Managed by error-resistant AI gardeners</p>
        <p style="margin-top: 1rem; color: #666;">
            Total Ecosystem: {self.stats['total_files']:,} files | 168 GB Creative Universe
        </p>
    </div>
</body>
</html>
"""

        return html

    async def update_portal(self):
        """Update the Pod Portal with fresh content"""
        html = await self.execute_with_timeout(
            self.build_dynamic_portal(),
            "build_portal",
            timeout=60
        )

        if html:
            success = self.write_file_directly(self.portal_file, html)
            if success:
                print(f"\n✨ Pod Portal dynamically rebuilt!")
                print(f"   {self.stats['total_files']:,} files indexed")
                print(f"   {len(self.content['visualizations'])} visualizations linked")
                print(f"   {len(self.content.get('html_projects', []))} projects featured")
                return True
        return False

    async def run_curation_session(self):
        """Run a complete curation session"""
        print("\n" + "="*60)
        print("🎭 Pod Curator Gardener Starting...")
        print("="*60)

        # Task 1: Gather discoveries
        await self.run_task(
            self.gather_discoveries,
            "gather_discoveries"
        )

        # Task 2: Update portal
        print("\n🔹 Task: Updating Pod Portal")
        await self.execute_with_timeout(
            self.update_portal(),
            "update_portal"
        )

        # Print final stats
        self.print_stats()
        print("="*60)


async def main():
    """Main entry point"""
    gardener = CuratorGardener()
    await gardener.run_curation_session()


if __name__ == '__main__':
    asyncio.run(main())
