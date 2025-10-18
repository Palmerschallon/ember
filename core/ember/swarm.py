"""
EMBER SWARM COORDINATOR
Manages parallel Ember instances playing games
"""

import subprocess, json, time
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Dict

class SwarmCoordinator:
    """Orchestrates multiple Ember instances"""
    
    def __init__(self):
        self.swarm_dir = Path("/Volumes/ThePod/memory/swarm")
        self.swarm_dir.mkdir(parents=True, exist_ok=True)
        self.games_dir = Path("/Volumes/ThePod/games")
        self.active_instances = {}
    
    def available_games(self) -> List[Path]:
        """Find playable games"""
        return list(self.games_dir.glob("ember_*.py"))
    
    def spawn_player(self, game: Path, instance_id: int, use_gpu: bool = False):
        """Spawn an Ember instance to play a game"""
        
        log_file = self.swarm_dir / f"ember_{instance_id}_{game.stem}.log"
        
        process = subprocess.Popen(
            ["python3", str(game)],
            stdout=open(log_file, "w"),
            stderr=subprocess.STDOUT,
            cwd="/Volumes/ThePod"
        )
        
        self.active_instances[instance_id] = {
            "pid": process.pid,
            "game": game.name,
            "started": datetime.now(timezone.utc).isoformat(),
            "use_gpu": use_gpu,
            "log": str(log_file)
        }
        
        return process
    
    def parallel_play(self, num_instances: int = 5, gpu_instances: int = 1):
        """Launch multiple Embers playing different games"""
        
        games = self.available_games()
        
        if not games:
            print("No games found")
            return []
        
        print(f"🔥 LAUNCHING SWARM")
        print(f"   {num_instances} instances ({gpu_instances} GPU, {num_instances-gpu_instances} CPU)")
        print(f"   {len(games)} games available")
        print()
        
        processes = []
        
        for i in range(num_instances):
            game = games[i % len(games)]
            use_gpu = (i < gpu_instances)
            
            print(f"  Ember {i}: {game.stem} ({'GPU' if use_gpu else 'CPU'})")
            
            proc = self.spawn_player(game, instance_id=i, use_gpu=use_gpu)
            processes.append(proc)
            
            time.sleep(0.3)
        
        print()
        print(f"✓ Swarm active with {len(processes)} instances")
        
        # Save state
        with open(self.swarm_dir / "swarm_state.json", "w") as f:
            json.dump(self.active_instances, f, indent=2)
        
        return processes

if __name__ == "__main__":
    coord = SwarmCoordinator()
    games = coord.available_games()
    print(f"🔥 Found {len(games)} games")
    for g in games[:5]:
        print(f"  • {g.name}")

