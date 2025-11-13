#!/usr/bin/env python3
"""
GAME GARDEN WATCHER
===================
Watches evolved_games/ and automatically improves new games with gardeners.

Features:
- Code quality refactoring
- Bug fixing
- Polish (particles, screen shake, juice)
- Balance tweaking
- Asset enhancement
- UX improvements
"""

import sys
import asyncio
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from gardener_base import ResilientGardener
from ember_complete import Ember


class GameGardener(ResilientGardener):
    """Specialized gardener for evolved games"""

    def __init__(self):
        super().__init__('game_gardener', pod_root=Path('/media/palmerschallon/ThePod1'))
        self.ember = Ember()
        self.games_dir = self.pod_root / 'evolved_games'

    async def improve_game(self, game_path: Path):
        """Full improvement pipeline"""
        print(f"\n🌱 Gardening: {game_path.name}")

        # Read original
        original_code = game_path.read_text()

        # Run improvement passes
        code = original_code
        code = await self.refactor_code(code, game_path.name)
        code = await self.fix_bugs(code, game_path.name)
        code = await self.add_juice(code, game_path.name)
        code = await self.improve_ux(code, game_path.name)

        # Save improved version
        self.write_file_directly(game_path, code)
        print(f"  ✓ Garden complete for {game_path.name}")

    async def refactor_code(self, code: str, game_name: str) -> str:
        """Optimize and clean code"""
        print(f"    🔧 Refactoring...")

        prompt = f"""Refactor this game code for performance and readability:

{code[:3000]}... (truncated)

Improvements to make:
1. Use requestAnimationFrame properly
2. Cache expensive calculations
3. Optimize collision detection loops
4. Remove code duplication
5. Add proper variable scoping
6. Extract magic numbers to constants

Return ONLY the improved code, no explanation."""

        improved = await self.ember.chat(prompt)
        return improved if len(improved) > 100 else code

    async def fix_bugs(self, code: str, game_name: str) -> str:
        """Find and fix common bugs"""
        print(f"    🐛 Fixing bugs...")

        prompt = f"""Fix common bugs in this game code:

{code[:3000]}... (truncated)

Look for and fix:
1. Edge-of-screen boundary issues
2. Division by zero
3. Null reference errors
4. Game-over state bugs
5. Collision detection edge cases
6. Missing error handling

Return ONLY the fixed code, no explanation."""

        fixed = await self.ember.chat(prompt)
        return fixed if len(fixed) > 100 else code

    async def add_juice(self, code: str, game_name: str) -> str:
        """Add visual/audio polish (game feel)"""
        print(f"    ✨ Adding juice...")

        prompt = f"""Add "game feel" polish to this code:

{code[:3000]}... (truncated)

Add:
1. Particle effects on key events (explosions, trails, sparkles)
2. Screen shake on impacts
3. Smooth camera movements with lerp
4. Visual feedback for ALL player actions
5. Easing functions for animations (ease-out, ease-in-out)
6. Color flashes on damage/success
7. Trail effects for moving objects

Make it feel JUICY and satisfying to play!

Return ONLY the improved code with juice, no explanation."""

        juicy = await self.ember.chat(prompt)
        return juicy if len(juicy) > 100 else code

    async def improve_ux(self, code: str, game_name: str) -> str:
        """Improve user experience"""
        print(f"    🎯 Improving UX...")

        prompt = f"""Improve the UX of this game:

{code[:3000]}... (truncated)

Add/improve:
1. Tutorial overlay on first play (skip with space)
2. Better control feedback (show key presses)
3. Pause menu (P key)
4. Restart button (R key)
5. Score display improvements
6. Clear visual hierarchy
7. Responsive feedback to all inputs

Return ONLY the improved code, no explanation."""

        improved_ux = await self.ember.chat(prompt)
        return improved_ux if len(improved_ux) > 100 else code


class GameFileHandler(FileSystemEventHandler):
    """Triggers gardening when new games appear"""

    def __init__(self, gardener):
        self.gardener = gardener
        self.processing = set()

    def on_created(self, event):
        if event.src_path.endswith('.html') and not event.is_directory:
            game_path = Path(event.src_path)

            # Avoid re-processing
            if game_path in self.processing:
                return

            # Skip library files
            if 'library' in str(game_path) or 'index' in str(game_path):
                return

            print(f"\n🌿 New game detected: {game_path.name}")
            print(f"   Dispatching gardeners...")

            self.processing.add(game_path)

            try:
                # Run async improvement
                asyncio.run(self.gardener.improve_game(game_path))
            except Exception as e:
                print(f"   ✗ Gardening failed: {e}")
            finally:
                self.processing.discard(game_path)


async def main():
    """Main entry point"""
    gardener = GameGardener()
    handler = GameFileHandler(gardener)
    observer = Observer()

    watch_dir = Path('/media/palmerschallon/ThePod1/evolved_games')
    watch_dir.mkdir(exist_ok=True)

    observer.schedule(handler, str(watch_dir), recursive=False)

    print(f"🌿 Game Garden Watcher started...")
    print(f"   Watching: {watch_dir}")
    print(f"   Waiting for new games to garden...")

    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    asyncio.run(main())
