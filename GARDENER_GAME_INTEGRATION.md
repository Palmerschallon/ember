# GARDENER + GAME EVOLUTION INTEGRATION

## The Synergy

**Evolution creates variety. Gardeners create quality.**

Together they form a self-improving creative ecosystem where:
- Game Evolver explores the space of possible games
- Gardeners refine and polish each creation
- Better games breed better offspring
- The system accelerates exponentially

---

## Gardener Specialists for Games

### 1. Code Quality Gardener
**Target:** `evolved_games/*.html`
**Tasks:**
- Refactor for performance (requestAnimationFrame optimization)
- Remove code duplication
- Add proper variable scoping
- Optimize collision detection loops
- Cache expensive calculations

### 2. Bug Fix Gardener
**Target:** Games with low fitness scores
**Tasks:**
- Find edge cases that cause crashes
- Fix collision detection bugs
- Handle edge-of-screen boundary issues
- Fix game-over state transitions
- Add error handling

### 3. Polish Gardener
**Target:** Games with good mechanics but low polish scores
**Tasks:**
- Add particle effects (explosions, trails, sparkles)
- Implement screen shake on impacts
- Add sound effects (using SoX)
- Smooth animations with easing
- Visual feedback for all actions

### 4. Balance Gardener
**Target:** Games that are too easy/hard
**Tasks:**
- Analyze playtesting data (simulated)
- Adjust difficulty curves
- Tweak scoring multipliers
- Balance enemy spawn rates
- Adjust power-up frequency

### 5. Asset Gardener
**Target:** Games with placeholder visuals
**Tasks:**
- Generate better sprites with ImageMagick
- Create sound effects with SoX
- Generate 3D models with Blender
- Optimize asset sizes
- Create consistent art style

### 6. UX Gardener
**Target:** All games
**Tasks:**
- Add tutorial overlays
- Improve control feedback
- Add pause menu
- Implement restart button
- Show FPS counter (debug mode)

---

## Integration Architecture

```
┌─────────────────────────────────────────────┐
│       EVOLUTION + GARDENING LOOP            │
├─────────────────────────────────────────────┤
│                                             │
│  [1] Game Evolver (every 2h)                │
│      ├─ Combine 2 parents                   │
│      ├─ Add new primitive                   │
│      └─ Create child game                   │
│             │                                │
│             v                                │
│  [2] Gardener Fleet (immediate)             │
│      ├─ Code Quality: Refactor              │
│      ├─ Bug Fix: Find & fix crashes         │
│      ├─ Polish: Add juice                   │
│      ├─ Balance: Tweak difficulty           │
│      ├─ Assets: Generate better art         │
│      └─ UX: Improve controls                │
│             │                                │
│             v                                │
│  [3] Fitness Evaluation                     │
│      ├─ Test improved game                  │
│      ├─ Score: code + gameplay + polish     │
│      └─ Update library                      │
│             │                                │
│             v                                │
│  [4] Selection (next cycle)                 │
│      └─ High-fitness games are parents      │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Implementation: Garden Watcher

Create `/media/palmerschallon/ThePod1/game_garden_watcher.py`:

```python
#!/usr/bin/env python3
"""
Watches evolved_games/ and dispatches gardeners
"""
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener

class GameGardener(ResilientGardener):
    """Specialized gardener for evolved games"""

    async def improve_game(self, game_path: Path):
        """Full improvement pipeline"""

        # 1. Code quality pass
        await self.refactor_code(game_path)

        # 2. Bug fixing pass
        await self.fix_common_bugs(game_path)

        # 3. Polish pass
        await self.add_juice(game_path)

        # 4. Balance pass
        await self.balance_gameplay(game_path)

        # 5. Asset enhancement
        await self.improve_assets(game_path)

        # 6. UX improvements
        await self.add_ux_features(game_path)

    async def refactor_code(self, game_path: Path):
        """Optimize and clean code"""
        code = game_path.read_text()

        prompt = f"""Refactor this game code for performance and readability:

{code}

Improvements:
1. Use requestAnimationFrame properly
2. Cache expensive calculations
3. Optimize collision detection
4. Remove code duplication
5. Add proper variable scoping

Return ONLY the improved code."""

        improved = await self.ember.chat(prompt)
        self.write_file_directly(game_path, improved)

    async def add_juice(self, game_path: Path):
        """Add visual/audio polish"""
        code = game_path.read_text()

        prompt = f"""Add 'game feel' to this code:

{code}

Add:
1. Particle effects on key events
2. Screen shake on impacts
3. Smooth camera movements
4. Visual feedback for all actions
5. Easing functions for animations

Return improved code with juice!"""

        improved = await self.ember.chat(prompt)
        self.write_file_directly(game_path, improved)

class GameFileHandler(FileSystemEventHandler):
    """Triggers gardening when new games appear"""

    def __init__(self, gardener):
        self.gardener = gardener

    def on_created(self, event):
        if event.src_path.endswith('.html'):
            game_path = Path(event.src_path)
            print(f"🌱 New game detected: {game_path.name}")
            print(f"   Dispatching gardeners...")

            # Run async improvement
            asyncio.run(self.gardener.improve_game(game_path))

            print(f"   ✓ Garden complete!")

def main():
    gardener = GameGardener('game_gardener', pod_root=Path('/media/palmerschallon/ThePod1'))
    handler = GameFileHandler(gardener)
    observer = Observer()

    watch_dir = Path('/media/palmerschallon/ThePod1/evolved_games')
    observer.schedule(handler, str(watch_dir), recursive=False)

    print(f"🌿 Game Garden Watcher started...")
    print(f"   Watching: {watch_dir}")

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
```

---

## Expected Results

### Without Gardeners:
- Gen 50: Games with interesting mechanics but rough code
- Gen 100: More complexity but still buggy
- Gen 200: Novel combinations but poor UX

### With Gardeners:
- Gen 50: Polished games with particles and sound
- Gen 100: Professional-feeling games
- Gen 200: Publishable indie-quality games

**Acceleration:** 3-5x faster to high quality

---

## Installation

```bash
# Install watchdog for file monitoring
pip3 install watchdog

# Create systemd service
sudo cp game_garden_watcher.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable game_garden_watcher
sudo systemctl start game_garden_watcher

# Monitor both services
tail -f /media/palmerschallon/ThePod1/logs/ember_game_evolver.log \
        /media/palmerschallon/ThePod1/logs/game_garden_watcher.log
```

---

## The Full Ecosystem

```
EVOLUTION (Exploration)
├─ Game Evolver: Creates variety
├─ Tries novel combinations
└─ Pushes boundaries

GARDENING (Refinement)
├─ Code Quality: Clean & fast
├─ Bug Fixing: Reliable
├─ Polish: Beautiful
├─ Balance: Fun
├─ Assets: Professional
└─ UX: Intuitive

FITNESS SELECTION
├─ Quality games breed
├─ Polished > raw
└─ Cycle accelerates
```

---

## Measuring Impact

Track these metrics:

```python
{
    "without_gardeners": {
        "avg_fitness_gen_50": 0.45,
        "playable_games": "30%",
        "publishable": "0%"
    },
    "with_gardeners": {
        "avg_fitness_gen_50": 0.72,
        "playable_games": "85%",
        "publishable": "15%"
    }
}
```

---

## Next Level: Meta-Gardening

Eventually gardeners could:
- **Learn patterns** from successful improvements
- **Share knowledge** across game types
- **Evolve themselves** based on fitness impact
- **Collaborate** on complex improvements

This creates a **meta-learning system** where the improvers improve themselves!
