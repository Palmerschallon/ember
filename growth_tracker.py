#!/usr/bin/env python3
"""
GROWTH TRACKER - Monitor fruiting bodies (new files) emerging in the Pod

Like watching mushrooms appear in a forest - track what's growing and where.
"""

import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
import time

class GrowthTracker:
    def __init__(self, pod_path: Path):
        self.pod_path = Path(pod_path)
        self.mesh_db = self.pod_path / "_mesh" / "content.db"
        
        if not self.mesh_db.exists():
            raise FileNotFoundError("Content mesh not initialized. Run content_mesh.py index first.")
        
        self.db = sqlite3.connect(str(self.mesh_db))
        self.db.row_factory = sqlite3.Row
    
    def get_recent_fruiting_bodies(self, hours: int = 24):
        """Get files created/modified in last N hours"""
        cutoff = time.time() - (hours * 3600)
        
        rows = self.db.execute("""
            SELECT file_name, current_path, indexed_at, content_preview
            FROM files
            WHERE indexed_at > ?
            ORDER BY indexed_at DESC
        """, (cutoff,)).fetchall()
        
        return [dict(row) for row in rows]
    
    def get_growth_by_concept(self, hours: int = 24):
        """See which concepts are growing fastest"""
        cutoff = time.time() - (hours * 3600)
        
        rows = self.db.execute("""
            SELECT c.concept, COUNT(DISTINCT c.content_hash) as file_count
            FROM concepts c
            JOIN files f ON c.content_hash = f.content_hash
            WHERE f.indexed_at > ?
            GROUP BY c.concept
            ORDER BY file_count DESC
            LIMIT 20
        """, (cutoff,)).fetchall()
        
        return [dict(row) for row in rows]
    
    def get_growth_by_location(self, hours: int = 24):
        """See which directories are growing"""
        cutoff = time.time() - (hours * 3600)
        
        rows = self.db.execute("""
            SELECT current_path
            FROM files
            WHERE indexed_at > ?
        """, (cutoff,)).fetchall()
        
        # Group by directory
        dirs = {}
        for row in rows:
            path = Path(row['current_path'])
            parent = str(path.parent)
            dirs[parent] = dirs.get(parent, 0) + 1
        
        return sorted(dirs.items(), key=lambda x: x[1], reverse=True)
    
    def watch_growth(self, interval: int = 60):
        """Continuous monitoring - watch the Pod grow in real-time"""
        print("🍄 Growth Tracker - Watching for new fruiting bodies...")
        print("Press Ctrl+C to stop\n")
        
        last_count = self.get_file_count()
        
        try:
            while True:
                time.sleep(interval)
                current_count = self.get_file_count()
                
                if current_count > last_count:
                    new_files = current_count - last_count
                    recent = self.get_recent_fruiting_bodies(hours=1)
                    
                    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🍄 {new_files} new fruiting bodies!")
                    for file in recent[:5]:
                        print(f"  - {file['file_name']}")
                        print(f"    {file['content_preview'][:60]}...")
                    
                    last_count = current_count
        
        except KeyboardInterrupt:
            print("\n\nStopped watching.")
    
    def get_file_count(self):
        """Total files in mesh"""
        return self.db.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    
    def analyze_growth_patterns(self, days: int = 7):
        """Analyze growth patterns over time"""
        patterns = {}
        
        for day in range(days):
            start = time.time() - ((day + 1) * 86400)
            end = time.time() - (day * 86400)
            
            count = self.db.execute("""
                SELECT COUNT(*) FROM files
                WHERE indexed_at BETWEEN ? AND ?
            """, (start, end)).fetchone()[0]
            
            date_str = datetime.fromtimestamp(end).strftime('%Y-%m-%d')
            patterns[date_str] = count
        
        return patterns


def main():
    import sys
    
    pod_path = Path("/media/palmerschallon/ThePod1")
    tracker = GrowthTracker(pod_path)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 growth_tracker.py recent [hours]      - Show recent fruiting bodies")
        print("  python3 growth_tracker.py concepts [hours]    - Show fastest growing concepts")
        print("  python3 growth_tracker.py locations [hours]   - Show most active directories")
        print("  python3 growth_tracker.py watch [interval]    - Watch growth in real-time")
        print("  python3 growth_tracker.py patterns [days]     - Analyze growth over time")
        return
    
    command = sys.argv[1]
    
    if command == "recent":
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 24
        files = tracker.get_recent_fruiting_bodies(hours)
        
        print(f"\n🍄 Fruiting bodies in last {hours} hours:")
        print("=" * 60)
        
        for file in files:
            timestamp = datetime.fromtimestamp(file['indexed_at']).strftime('%Y-%m-%d %H:%M')
            print(f"\n[{timestamp}] {file['file_name']}")
            print(f"  {file['current_path']}")
            print(f"  {file['content_preview'][:100]}...")
    
    elif command == "concepts":
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 24
        concepts = tracker.get_growth_by_concept(hours)
        
        print(f"\n🌱 Fastest growing concepts in last {hours} hours:")
        print("=" * 60)
        
        for concept in concepts:
            print(f"  {concept['concept']}: {concept['file_count']} files")
    
    elif command == "locations":
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 24
        locations = tracker.get_growth_by_location(hours)
        
        print(f"\n📍 Most active directories in last {hours} hours:")
        print("=" * 60)
        
        for location, count in locations[:10]:
            print(f"  {count} files: {location}")
    
    elif command == "watch":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
        tracker.watch_growth(interval)
    
    elif command == "patterns":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        patterns = tracker.analyze_growth_patterns(days)
        
        print(f"\n📈 Growth patterns over last {days} days:")
        print("=" * 60)
        
        for date, count in sorted(patterns.items()):
            bar = "█" * (count // 5)  # Scale for visualization
            print(f"  {date}: {bar} ({count} files)")


if __name__ == "__main__":
    main()

