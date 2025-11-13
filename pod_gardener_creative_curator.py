#!/usr/bin/env python3
"""
Pod Gardener CREATIVE Curator - Web-Searching, Idea-Generating Portal Builder
- Explores the Pod and gets INSPIRED by what it finds
- Uses Tavily web search to bring in latest creative coding trends
- Uses Ember AI to generate creative interactive features
- Adds WebSocket-connected BUILD buttons, timers, progress bars
- Makes the portal a LIVING, CREATIVE showcase that grows smarter
"""

import sys
import asyncio
import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import random

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener
from ember_complete import Ember

# Tavily setup
try:
    from tavily import TavilyClient
    TAVILY_AVAILABLE = True
except ImportError:
    TAVILY_AVAILABLE = False
    print("⚠️  Tavily not available - install with: pip install tavily-python")


class CreativeCurator(ResilientGardener):
    """Creative, web-searching, AI-powered portal curator"""

    def __init__(self):
        super().__init__('creative_curator', pod_root='/media/palmerschallon/ThePod1')

        # Initialize Ember for creative thinking
        self.ember = Ember()

        # Initialize Tavily if API key available
        self.tavily = None
        tavily_key = os.getenv('TAVILY_API_KEY')
        if TAVILY_AVAILABLE and tavily_key:
            self.tavily = TavilyClient(api_key=tavily_key)
            print("✓ Tavily web search enabled!")
        else:
            print("⚠️  Tavily API key not found in .env - add TAVILY_API_KEY for web search")

        # Reinitialize stats with custom fields
        self.stats['last_updated'] = datetime.now().isoformat()
        self.stats['web_searches_performed'] = 0
        self.stats['creative_ideas_generated'] = 0

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
            'html_projects': [],
            'notebooks': [],
            'images': [],
            'data_files': []
        }

        # Creative insights from web search
        self.web_insights = []

        # Creative ideas from Ember
        self.creative_ideas = []

        # Add custom fields to inherited stats
        self.stats['total_files'] = 0
        self.stats['categories'] = {}

    async def search_web_for_inspiration(self):
        """Use Tavily to search for creative coding trends and ideas"""
        if not self.tavily:
            print("  ⏭ Skipping web search (Tavily not configured)")
            return []

        print("\n🌐 Searching web for creative inspiration...")

        search_queries = [
            "creative coding interactive experiences 2025",
            "best web animation techniques Three.js",
            "innovative data visualization ideas",
            "creative WebGL shader effects",
            "interactive generative art web",
        ]

        # Use up to 5 searches per run (we have 100/day available!)
        num_searches = min(5, len(search_queries))
        insights = []

        for query in search_queries[:num_searches]:
            try:
                print(f"  🔍 Searching: {query}")
                response = self.tavily.search(
                    query=query,
                    search_depth="basic",
                    max_results=2
                )

                for result in response.get('results', []):
                    insights.append({
                        'query': query,
                        'title': result.get('title', ''),
                        'content': result.get('content', '')[:300],  # First 300 chars
                        'url': result.get('url', '')
                    })
                    print(f"    ✓ Found: {result.get('title', 'Unknown')[:60]}...")

                self.stats['web_searches_performed'] += 1
                await asyncio.sleep(0.5)  # Rate limit

            except Exception as e:
                print(f"    ⚠️  Search failed: {str(e)[:100]}")
                continue

        print(f"  ✓ Gathered {len(insights)} insights from the web")
        return insights

    async def generate_creative_ideas(self):
        """Use Ember to analyze the Pod and generate creative ideas"""
        print("\n💡 Asking Ember for creative portal ideas...")

        # Prepare context about what's in the Pod
        context = f"""You're exploring a creative ecosystem called The Pod - 168GB with {self.stats.get('total_files', 30000)} files including:

Pod Contents:
- {len(self.content['html_projects'])} HTML projects and interactive experiences
- {len(self.content['visualizations'])} data visualizations
- {len(self.content['experiments'])} learning experiments
- {len(self.content['python_files'])} Python scripts
- {self.stats['categories'].get('images', 0)} images
- {self.stats['categories'].get('code', 0)} code files
- VR worlds, games, generative art, animations

Recent Web Insights:
{chr(10).join([f"- {insight['title']}" for insight in self.web_insights[:5]])}

Generate 5 CREATIVE IDEAS for interactive features to add to the Pod Portal. Think:
- WebSocket-connected live creation buttons
- Real-time progress meters and animations
- Interactive data visualizations that update live
- Creative navigation patterns (spatial, temporal, semantic)
- Gamification elements (achievements, exploration rewards)
- AI-powered recommendations and discovery
- Collaborative features

Be SPECIFIC and INNOVATIVE. Each idea should include:
1. Feature name
2. What it does
3. Why it's exciting
4. How users interact with it

Format as JSON array of objects with keys: name, description, excitement, interaction"""

        try:
            response = await self.ember.chat(context)
            print(f"  ✓ Ember generated creative ideas!")

            # Try to parse JSON, fall back to text
            try:
                ideas = json.loads(response)
                if isinstance(ideas, list):
                    self.creative_ideas = ideas
                    self.stats['creative_ideas_generated'] = len(ideas)
                    return ideas
            except:
                # If not JSON, treat as text and extract ideas
                print("  📝 Ideas generated as text (not JSON)")
                return [{'name': 'Creative Ideas', 'description': response[:500]}]

        except Exception as e:
            print(f"  ⚠️  Idea generation failed: {str(e)[:100]}")
            return []

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
                print(f"  ✓ Loaded map: {self.stats['total_files']:,} files across {len(self.stats['categories'])} categories")

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

    async def build_creative_portal(self):
        """Build portal with creative interactive features"""
        print("\n🎨 Building CREATIVE Pod Portal...")

        # Pick a random creative idea to feature
        featured_idea = random.choice(self.creative_ideas) if self.creative_ideas else None

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
            position: relative;
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

        .ai-badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(0, 217, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            border: 1px solid #00d9ff;
            font-size: 0.85rem;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.6; }}
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
            cursor: pointer;
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

        .build-section {{
            margin: 3rem 2rem;
            padding: 3rem;
            background: linear-gradient(135deg, rgba(123, 44, 191, 0.2), rgba(0, 217, 255, 0.2));
            border-radius: 20px;
            border: 2px solid rgba(0, 217, 255, 0.4);
            text-align: center;
        }}

        .build-button {{
            background: linear-gradient(135deg, #00d9ff, #7b2cbf);
            color: white;
            border: none;
            padding: 1.5rem 3rem;
            font-size: 1.5rem;
            font-weight: bold;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 8px 30px rgba(0, 217, 255, 0.4);
            position: relative;
            overflow: hidden;
        }}

        .build-button:hover {{
            transform: scale(1.05);
            box-shadow: 0 12px 40px rgba(0, 217, 255, 0.6);
        }}

        .build-button:active {{
            transform: scale(0.98);
        }}

        .build-button::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }}

        .build-button:hover::before {{
            width: 300px;
            height: 300px;
        }}

        #buildLog {{
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s;
        }}

        #buildLog.active {{
            max-height: 500px;
        }}

        .log-entry {{
            padding: 0.5rem;
            margin: 0.3rem 0;
            border-radius: 5px;
            animation: slideIn 0.3s;
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateX(-20px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}

        .log-entry.info {{ background: rgba(0, 217, 255, 0.2); }}
        .log-entry.success {{ background: rgba(76, 175, 80, 0.2); }}
        .log-entry.error {{ background: rgba(244, 67, 54, 0.2); }}

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
            cursor: pointer;
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

        .card-description {{
            color: #a0a0a0;
            font-size: 0.9rem;
            margin-bottom: 0.8rem;
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

        .idea-spotlight {{
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 107, 0, 0.1));
            border: 2px dashed rgba(255, 215, 0, 0.5);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
        }}

        .idea-spotlight h3 {{
            color: #ffd700;
            margin-bottom: 1rem;
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

        .web-insight {{
            background: rgba(0, 255, 157, 0.1);
            border-left: 3px solid #00ff9d;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 5px;
        }}

        .web-insight-title {{
            color: #00ff9d;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="ai-badge">🤖 AI-Curated • {self.stats.get('web_searches_performed', 0)} Web Searches • {self.stats.get('creative_ideas_generated', 0)} Ideas Generated</div>
        <h1>🌱 The Pod Portal</h1>
        <p>Living Creative Ecosystem - 168 GB of Innovation</p>
        <p class="last-updated">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p class="self-healing">⚡ SELF-HEALING & SELF-IMPROVING Every 30 Minutes! ⚡</p>
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

    <!-- BUILD SOMETHING AMAZING Section with WebSocket Connection -->
    <div class="build-section">
        <h2 style="color: #00d9ff; margin-bottom: 1rem;">✨ CREATE WITH EMBER AI ✨</h2>
        <p style="margin-bottom: 2rem; color: #a0a0a0;">Let Ember imagine and build something amazing for you</p>
        <button class="build-button" onclick="buildSomething()">
            <span style="position: relative; z-index: 1;">🔥 BUILD SOMETHING AMAZING</span>
        </button>
        <div id="buildLog"></div>
    </div>

    <div class="container">
"""

        # Featured Creative Idea (if available)
        if featured_idea:
            html += f"""
        <div class="idea-spotlight">
            <h3>💡 Latest AI-Generated Idea: {featured_idea.get('name', 'Creative Feature')}</h3>
            <p>{featured_idea.get('description', 'An innovative new feature concept')[:300]}...</p>
            <span class="badge">Generated by Ember</span>
        </div>
"""

        # Web Insights Section (if available)
        if self.web_insights:
            html += """
        <div class="section">
            <h2 class="section-title">🌐 Latest Web Trends & Inspiration</h2>
            <div class="grid">
"""
            for insight in self.web_insights[:6]:
                html += f"""
                <div class="web-insight">
                    <div class="web-insight-title">{insight['title'][:80]}</div>
                    <p style="color: #a0a0a0; font-size: 0.85rem;">{insight['content'][:150]}...</p>
                    <a href="{insight['url']}" target="_blank" class="card-link">Read More →</a>
                </div>
"""
            html += """
            </div>
        </div>
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

        # WebSocket BUILD functionality
        html += f"""
    </div>

    <div class="footer">
        <p>🌱 Pod Gardener Fleet Active - Discovering, Healing, Learning, Mapping</p>
        <p>🌐 Web-Searching • 🤖 AI-Powered • 💡 Idea-Generating</p>
        <p>Next Update: 30 minutes | Managed by error-resistant AI gardeners</p>
        <p style="margin-top: 1rem; color: #666;">
            Total Ecosystem: {self.stats['total_files']:,} files | 168 GB Creative Universe
        </p>
        <p style="margin-top: 0.5rem; color: #00ff9d; font-size: 0.85rem;">
            This portal was curated with {self.stats['web_searches_performed']} web searches bringing in the latest trends
        </p>
    </div>

    <script>
        // WebSocket connection to Ember creation bridge
        let ws = null;

        function buildSomething() {{
            const button = document.querySelector('.build-button');
            const log = document.getElementById('buildLog');

            button.disabled = true;
            button.textContent = '🔄 Connecting to Ember...';
            log.classList.add('active');
            log.innerHTML = '';

            // Add timer and progress bar
            const timerEl = document.createElement('div');
            timerEl.id = 'buildTimer';
            timerEl.style.cssText = 'font-size: 2em; color: #667eea; margin: 15px 0; font-weight: bold; text-align: center;';
            timerEl.textContent = '⏱️ 0s';
            log.appendChild(timerEl);

            const progressBarWrap = document.createElement('div');
            progressBarWrap.style.cssText = 'background: rgba(255,255,255,0.1); height: 8px; border-radius: 4px; margin: 10px 0; overflow: hidden;';
            const progressBarFill = document.createElement('div');
            progressBarFill.id = 'progressFill';
            progressBarFill.style.cssText = 'background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; width: 0%; transition: width 0.5s ease;';
            progressBarWrap.appendChild(progressBarFill);
            log.appendChild(progressBarWrap);

            // Start timer
            let startTime = Date.now();
            const timerInterval = setInterval(() => {{
                const elapsed = Math.floor((Date.now() - startTime) / 1000);
                timerEl.textContent = `⏱️ ${{elapsed}}s`;

                // Progress bar fills over expected 60 second duration
                const progress = Math.min((elapsed / 60) * 100, 95);
                progressBarFill.style.width = `${{progress}}%`;
            }}, 100);

            window.currentBuildTimer = timerInterval;

            // Connect to WebSocket
            ws = new WebSocket('ws://localhost:8083');

            ws.onopen = () => {{
                addLog('🚀 Connected to Ember AI!', 'info');

                // Request a random creation
                const themes = ['particle-system', 'fractal-art', 'data-viz', 'interactive-story', 'generative-music'];
                const theme = themes[Math.floor(Math.random() * themes.length)];

                ws.send(JSON.stringify({{
                    type: 'create',
                    creation_type: theme,
                    params: {{}}
                }}));
            }};

            ws.onmessage = (event) => {{
                const data = JSON.parse(event.data);

                if (data.type === 'progress') {{
                    addLog(data.message, 'info');
                }} else if (data.type === 'creation_complete') {{
                    clearInterval(window.currentBuildTimer);
                    progressBarFill.style.width = '100%';

                    addLog(`✅ Created: ${{data.filename}}`, 'success');
                    addLog('🎉 Opening your creation...', 'success');

                    // Open the file
                    setTimeout(() => {{
                        window.open(data.filename, '_blank');
                        button.disabled = false;
                        button.innerHTML = '<span style="position: relative; z-index: 1;">🔥 BUILD SOMETHING AMAZING</span>';
                    }}, 1000);

                    ws.close();
                }} else if (data.type === 'error') {{
                    clearInterval(window.currentBuildTimer);
                    addLog(`❌ Error: ${{data.message}}`, 'error');
                    button.disabled = false;
                    button.innerHTML = '<span style="position: relative; z-index: 1;">🔥 TRY AGAIN</span>';
                    ws.close();
                }}
            }};

            ws.onerror = () => {{
                clearInterval(window.currentBuildTimer);
                addLog('❌ Connection failed. Is Ember running on port 8083?', 'error');
                button.disabled = false;
                button.innerHTML = '<span style="position: relative; z-index: 1;">🔥 TRY AGAIN</span>';
            }};

            ws.onclose = () => {{
                if (button.disabled) {{
                    clearInterval(window.currentBuildTimer);
                    addLog('Connection closed', 'info');
                    button.disabled = false;
                    button.innerHTML = '<span style="position: relative; z-index: 1;">🔥 BUILD SOMETHING AMAZING</span>';
                }}
            }};
        }}

        function addLog(message, type = 'info') {{
            const log = document.getElementById('buildLog');
            const entry = document.createElement('div');
            entry.className = `log-entry ${{type}}`;
            entry.textContent = message;
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
        }}

        // Make stats clickable for fun
        document.querySelectorAll('.stat-card').forEach(card => {{
            card.addEventListener('click', () => {{
                card.style.transform = 'rotate(360deg) scale(1.1)';
                setTimeout(() => {{
                    card.style.transform = '';
                }}, 600);
            }});
        }});
    </script>
</body>
</html>
"""

        return html

    async def update_portal(self):
        """Update the Pod Portal with fresh, creative content"""
        html = await self.execute_with_timeout(
            self.build_creative_portal(),
            "build_creative_portal",
            timeout=90
        )

        if html:
            success = self.write_file_directly(self.portal_file, html)
            if success:
                print(f"\n✨ CREATIVE Pod Portal dynamically rebuilt!")
                print(f"   {self.stats['total_files']:,} files indexed")
                print(f"   {len(self.content['visualizations'])} visualizations linked")
                print(f"   {len(self.content.get('html_projects', []))} projects featured")
                print(f"   {self.stats['web_searches_performed']} web searches performed")
                print(f"   {self.stats['creative_ideas_generated']} creative ideas generated")
                return True
        return False

    async def run_creative_curation_session(self):
        """Run a complete CREATIVE curation session"""
        print("\n" + "="*70)
        print("🎭 CREATIVE Pod Curator Gardener Starting...")
        print("   Web-Searching • Idea-Generating • AI-Powered")
        print("="*70)

        # Task 1: Search web for inspiration
        self.web_insights = await self.run_task(
            self.search_web_for_inspiration,
            "search_web_inspiration"
        ) or []

        # Task 2: Gather discoveries
        await self.run_task(
            self.gather_discoveries,
            "gather_discoveries"
        )

        # Task 3: Generate creative ideas with Ember
        await self.run_task(
            self.generate_creative_ideas,
            "generate_creative_ideas"
        )

        # Task 4: Update portal with all the creativity
        print("\n🔹 Task: Updating Creative Pod Portal")
        await self.execute_with_timeout(
            self.update_portal(),
            "update_portal"
        )

        # Print final stats
        self.print_stats()
        print("="*70)


async def main():
    """Main entry point"""
    gardener = CreativeCurator()
    await gardener.run_creative_curation_session()


if __name__ == '__main__':
    asyncio.run(main())
