#!/usr/bin/env python3
"""
Pod Portal Enhancer - INCREMENTAL improvement approach
Instead of rebuilding from scratch, this ADDS TO and ENHANCES the existing portal
Preserves all working features while gradually evolving the portal
"""

import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime
import os
import re
from bs4 import BeautifulSoup

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener
from ember_complete import Ember

try:
    from tavily import TavilyClient
    TAVILY_AVAILABLE = True
except ImportError:
    TAVILY_AVAILABLE = False


class PortalEnhancer(ResilientGardener):
    """Enhances the Pod Portal incrementally without destroying existing work"""

    def __init__(self):
        super().__init__('portal_enhancer', pod_root='/media/palmerschallon/ThePod1')

        self.portal_file = self.pod_root / 'the_pod_portal.html'
        self.backup_dir = self.pod_root / 'portal_backups'
        self.backup_dir.mkdir(exist_ok=True)

        # Tavily setup
        tavily_key = os.getenv('TAVILY_API_KEY')
        if tavily_key and TAVILY_AVAILABLE:
            self.tavily = TavilyClient(api_key=tavily_key)
            print("  ✓ Tavily web search enabled!")
        else:
            self.tavily = None

        # Ember AI
        self.ember = Ember()

        # Discovered content
        self.viz_dir = self.pod_root / 'visualizations'
        self.maps_dir = self.pod_root / 'pod_maps'

        # Enhancement tracking
        self.enhancements = []
        self.web_insights = []

    async def backup_portal(self):
        """Create timestamped backup of current portal"""
        if not self.portal_file.exists():
            print("  ⚠️  No existing portal to backup")
            return None

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'portal_backup_{timestamp}.html'

        try:
            content = self.portal_file.read_text()
            backup_path.write_text(content)
            print(f"  ✓ Portal backed up to {backup_path.name}")
            return backup_path
        except Exception as e:
            print(f"  ⚠️  Backup failed: {e}")
            return None

    async def analyze_existing_portal(self):
        """Parse existing portal to understand what's already there"""
        print("\n🔍 Analyzing existing portal...")

        if not self.portal_file.exists():
            print("  ⚠️  No existing portal found")
            return {}

        try:
            content = self.portal_file.read_text()
            soup = BeautifulSoup(content, 'html.parser')

            analysis = {
                'has_build_button': bool(soup.find(class_='build-button')),
                'has_websocket': 'WebSocket' in content,
                'has_timer': 'buildTimer' in content or 'progressFill' in content,
                'sections': [],
                'scripts': len(soup.find_all('script')),
                'styles': bool(soup.find('style')),
            }

            # Find all sections
            for section in soup.find_all(class_='section'):
                title_elem = section.find(class_='section-title')
                if title_elem:
                    analysis['sections'].append(title_elem.get_text(strip=True))

            print(f"  ✓ Current Portal State:")
            print(f"    - BUILD button: {'✓' if analysis['has_build_button'] else '✗'}")
            print(f"    - WebSocket: {'✓' if analysis['has_websocket'] else '✗'}")
            print(f"    - Timer/Progress: {'✓' if analysis['has_timer'] else '✗'}")
            print(f"    - Sections: {len(analysis['sections'])}")
            print(f"    - Scripts: {analysis['scripts']}")

            return analysis

        except Exception as e:
            print(f"  ⚠️  Analysis failed: {e}")
            return {}

    async def gather_new_content(self):
        """Find new content that should be added to portal"""
        print("\n📊 Gathering new content...")

        new_content = {
            'visualizations': [],
            'html_projects': [],
            'total_files': 0
        }

        # Find latest visualizations
        if self.viz_dir.exists():
            viz_files = sorted(self.viz_dir.glob('*.html'), key=lambda f: f.stat().st_mtime, reverse=True)
            new_content['visualizations'] = [
                {
                    'name': f.stem,
                    'path': str(f.relative_to(self.pod_root)),
                    'modified': datetime.fromtimestamp(f.stat().st_mtime).isoformat()
                }
                for f in viz_files[:5]  # Latest 5
            ]

        # Find latest HTML projects
        html_files = sorted(
            [f for f in self.pod_root.glob('*.html') if f.name != 'the_pod_portal.html'],
            key=lambda f: f.stat().st_mtime,
            reverse=True
        )
        new_content['html_projects'] = [
            {'name': f.stem, 'path': f.name}
            for f in html_files[:10]  # Latest 10
        ]

        # Get map data if available
        map_files = sorted(self.maps_dir.glob('pod_map_*.json'), reverse=True)
        if map_files:
            with open(map_files[0], 'r') as f:
                map_data = json.load(f)
                new_content['total_files'] = map_data.get('total_files', 0)

        print(f"  ✓ Found {len(new_content['visualizations'])} new visualizations")
        print(f"  ✓ Found {len(new_content['html_projects'])} recent HTML projects")
        print(f"  ✓ Total files in Pod: {new_content['total_files']}")

        return new_content

    async def search_web_for_ideas(self):
        """Quick web search for 1-2 fresh ideas"""
        if not self.tavily:
            print("  ⏭ Skipping web search (Tavily not configured)")
            return []

        print("\n🌐 Quick web search for fresh ideas...")

        try:
            # Just 1-2 searches to keep it fast
            query = "innovative web portal design ideas 2025"
            response = self.tavily.search(query=query, search_depth="basic", max_results=2)

            insights = []
            for result in response.get('results', []):
                insights.append({
                    'title': result.get('title', ''),
                    'content': result.get('content', '')[:200]
                })
                print(f"  ✓ {result.get('title', 'Unknown')[:60]}...")

            return insights

        except Exception as e:
            print(f"  ⚠️  Web search failed: {e}")
            return []

    async def ask_ember_for_enhancement(self, current_state, new_content, web_insights):
        """Ask Ember how to enhance (not replace!) the portal"""
        print("\n💡 Asking Ember for enhancement ideas...")

        prompt = f"""You're enhancing an EXISTING Pod Portal. DO NOT rebuild from scratch!

Current Portal State:
- BUILD button working: {current_state.get('has_build_button')}
- WebSocket connected: {current_state.get('has_websocket')}
- Has timer/progress: {current_state.get('has_timer')}
- Existing sections: {current_state.get('sections', [])}

New Content to Add:
- {len(new_content.get('visualizations', []))} new visualizations
- {len(new_content.get('html_projects', []))} recent HTML projects
- {new_content.get('total_files', 0)} total files

Web Insights:
{chr(10).join([f"- {i['title']}" for i in web_insights[:2]])}

Suggest 2-3 SMALL ENHANCEMENTS that can be added WITHOUT breaking existing features:
1. A new section to add (not replace)
2. A visual improvement (CSS only)
3. A small interactive feature

Keep it INCREMENTAL. Preserve what works. Format as JSON:
{{"enhancements": [{{"type": "section|style|feature", "description": "...", "priority": "high|medium|low"}}]}}
"""

        try:
            response = await self.ember.chat(prompt)

            # Try to parse JSON
            try:
                ideas = json.loads(response)
                enhancements = ideas.get('enhancements', [])
                print(f"  ✓ Ember suggested {len(enhancements)} enhancements")
                for e in enhancements:
                    print(f"    - {e.get('description', 'Unknown')[:60]}")
                return enhancements
            except:
                print("  📝 Ember provided text suggestions (not JSON)")
                return []

        except Exception as e:
            print(f"  ⚠️  Ember enhancement failed: {e}")
            return []

    async def apply_safe_enhancements(self, current_state, new_content):
        """Apply ONLY safe, incremental updates"""
        print("\n✨ Applying safe enhancements...")

        if not self.portal_file.exists():
            print("  ⚠️  No portal to enhance - create one first")
            return False

        try:
            content = self.portal_file.read_text()
            soup = BeautifulSoup(content, 'html.parser')

            # Enhancement 1: Update stats if stats bar exists
            stats_bar = soup.find(class_='stats-bar')
            if stats_bar and new_content.get('total_files'):
                # Find and update the total files stat
                stat_cards = stats_bar.find_all(class_='stat-card')
                for card in stat_cards:
                    label = card.find(class_='stat-label')
                    if label and 'Total Files' in label.get_text():
                        number_elem = card.find(class_='stat-number')
                        if number_elem:
                            number_elem.string = f"{new_content['total_files']:,}"
                            print("  ✓ Updated total files stat")

            # Enhancement 2: Update last updated timestamp if it exists
            last_updated = soup.find(class_='last-updated')
            if last_updated:
                last_updated.string = f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                print("  ✓ Updated timestamp")

            # Enhancement 3: Add web insights section if not present (SAFE addition)
            if self.web_insights and not soup.find(id='web-insights'):
                container = soup.find(class_='container')
                if container:
                    insights_html = f"""
<div class="section" id="web-insights">
    <h2 class="section-title">🌐 Latest Web Insights</h2>
    <div class="grid">
        {"".join([f'''
        <div class="card">
            <div class="card-title">{insight.get('title', 'Insight')[:50]}</div>
            <p class="card-description">{insight.get('content', '')[:100]}...</p>
        </div>
        ''' for insight in self.web_insights[:3]])}
    </div>
</div>
"""
                    new_section = BeautifulSoup(insights_html, 'html.parser')
                    container.append(new_section)
                    print("  ✓ Added web insights section")

            # Write enhanced portal
            self.write_file_directly(self.portal_file, str(soup))
            print("  ✓ Portal enhanced successfully!")
            return True

        except Exception as e:
            print(f"  ⚠️  Enhancement failed: {e}")
            return False

    async def run_enhancement_session(self):
        """Run a complete enhancement session"""
        print("\n" + "="*60)
        print("🌱 Pod Portal Enhancer Starting...")
        print("   INCREMENTAL approach - preserves existing work!")
        print("="*60)

        # Step 1: Backup
        await self.backup_portal()

        # Step 2: Analyze what's already there
        current_state = await self.run_task(
            self.analyze_existing_portal,
            "analyze_portal"
        )

        # Step 3: Gather new content
        new_content = await self.run_task(
            self.gather_new_content,
            "gather_content"
        )

        # Step 4: Quick web search (1-2 searches only)
        self.web_insights = await self.run_task(
            self.search_web_for_ideas,
            "web_search"
        )

        # Step 5: Ask Ember for safe enhancements
        enhancements = await self.run_task(
            self.ask_ember_for_enhancement(current_state, new_content, self.web_insights),
            "ember_ideas"
        )

        # Step 6: Apply SAFE enhancements only
        await self.run_task(
            self.apply_safe_enhancements(current_state, new_content),
            "apply_enhancements"
        )

        # Print final stats
        self.print_stats()
        print("="*60)


async def main():
    """Main entry point"""
    enhancer = PortalEnhancer()
    await enhancer.run_enhancement_session()


if __name__ == '__main__':
    asyncio.run(main())
