# EMBER GAME EVOLVER - ADVANCED UPGRADE PLAN

## Status: Ready to Implement

**Completed:**
- ✅ LLM-powered game evolver base system installed
- ✅ Systemd timer running (every 2 hours)
- ✅ Creative tools installed: Blender, FFmpeg, ImageMagick, Inkscape, SoX, Graphviz, Matplotlib

**Next Steps:** Upgrade to primitive-based multi-tool evolution

---

## 1. GAME PRIMITIVES LIBRARY

Create `/media/palmerschallon/ThePod1/game_primitives.json`:

```json
{
  "movement": {
    "grid_based": "Turn-based movement on tile grid (roguelikes, chess)",
    "continuous_2d": "Smooth XY movement with acceleration (platformers)",
    "physics_momentum": "Velocity + forces + friction (racing, physics puzzlers)",
    "first_person_3d": "Camera-controlled 3D navigation (FPS, exploration)",
    "pathfinding": "AI navigation with A* or nav meshes (RTS, tower defense)"
  },
  "action": {
    "discrete_turns": "Turn-based actions with time limits (strategy, card games)",
    "timing_windows": "Perfect/good/miss timing (rhythm games, QTEs)",
    "aiming_targeting": "Projectile physics + hit detection (shooters)",
    "resource_management": "Collect/spend/upgrade loops (survival, strategy)",
    "combo_system": "Chain attacks with timing (fighting, action RPGs)"
  },
  "space": {
    "tile_grid": "2D array of tiles (roguelikes, puzzle games)",
    "graph_network": "Nodes + edges (board games, city builders)",
    "continuous_2d": "Arbitrary XY positioning (physics games)",
    "procedural_generation": "BSP trees, cellular automata, noise (roguelikes)",
    "3d_environments": "Three.js or Babylon.js scenes (VR, 3D games)"
  },
  "feedback": {
    "scoring": "Points + multipliers + high scores",
    "health_lives": "Damage + death + respawn",
    "resources": "Currency, materials, energy bars",
    "progress": "Completion %, unlocks, achievements",
    "combo_multipliers": "Score chains that reset on failure"
  },
  "systems": {
    "collision_detection": "AABB, circle, or polygon collision",
    "inventory": "Item storage + equip/use mechanics",
    "upgrade_trees": "Persistent progression systems",
    "ai_opponents": "FSM or behavior tree enemies",
    "procedural_content": "Algorithmic level/asset generation"
  }
}
```

---

## 2. COMPLEX SEED GAMES (Primitive-Based)

### Seed 1: Physics Platformer
**Primitives:** continuous_2d, physics_momentum, collision_detection, scoring
**Description:** Momentum-based platformer with wall-jumping, moving platforms, collectibles
**Tech:** HTML5 Canvas, custom physics engine
**Innovation:** Satisfying momentum + tight controls

### Seed 2: Roguelike Dungeon
**Primitives:** grid_based, discrete_turns, tile_grid, procedural_generation, inventory
**Description:** Classic roguelike with procedural dungeons, fog of war, tactical combat
**Tech:** HTML5 Canvas, BSP dungeon generation
**Innovation:** Strategic depth + permadeath tension

### Seed 3: Tower Defense
**Primitives:** pathfinding, resource_management, upgrade_trees, ai_opponents
**Description:** Enemy waves navigate to goal, player places towers with upgrade paths
**Tech:** HTML5 Canvas, A* pathfinding
**Innovation:** Strategic placement + economic decisions

### Seed 4: 3D Exploration
**Primitives:** first_person_3d, continuous_2d, 3d_environments, procedural_content
**Description:** First-person world with interactive objects, spatial audio, exploration
**Tech:** Three.js, procedural generation
**Innovation:** Immersive atmosphere + discovery

### Seed 5: Rhythm Game
**Primitives:** timing_windows, combo_multipliers, scoring
**Description:** Audio-synced note hitting with perfect/good/miss timing
**Tech:** Web Audio API, canvas visualization
**Innovation:** Music-driven gameplay + flow state

### Seed 6: Real-Time Strategy
**Primitives:** pathfinding, resource_management, ai_opponents, graph_network
**Description:** Unit control, resource harvesting, AI opponent with fog of war
**Tech:** HTML5 Canvas, unit command queuing
**Innovation:** Strategic decision-making under time pressure

### Seed 7: Puzzle Mechanics
**Primitives:** grid_based, discrete_turns, tile_grid, progress
**Description:** Move-based puzzle with undo, goal states, level progression
**Tech:** HTML5 Canvas, state management
**Innovation:** Elegant mechanics + "aha" moments

---

## 3. MULTI-TOOL ASSET PIPELINE

### Tool Integration for Evolution

```python
class AssetPipeline:
    """Generate and optimize game assets during evolution"""

    def generate_sprite(self, description: str) -> str:
        """Use ImageMagick to create sprite"""
        # convert -size 32x32 xc:transparent \
        #   -fill "#FF6B6B" -draw "circle 16,16 16,0" \
        #   sprite.png

    def generate_sound(self, type: str) -> str:
        """Use SoX to synthesize sound effects"""
        # sox -n jump.wav synth 0.1 sine 880 fade 0 0.1 0.05

    def generate_3d_model(self, description: str) -> str:
        """Use Blender headless to create GLTF model"""
        # blender --background --python generate_model.py

    def optimize_assets(self, game_dir: Path):
        """Compress and optimize all game assets"""
        # ffmpeg -i sound.wav -b:a 64k sound.mp3
        # convert sprite.png -quality 85 sprite_optimized.png

    def create_evolution_viz(self, library: Dict) -> str:
        """Use Graphviz to show evolution tree"""
        # dot -Tpng evolution.dot -o evolution_tree.png
```

### Blender Integration

```python
# /media/palmerschallon/ThePod1/blender_model_generator.py
import bpy
import sys
import json

def generate_model(description: str, output_path: str):
    """Generate 3D model based on description"""
    # Clear scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Parse description and create geometry
    # Export as GLTF for web
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB'
    )

if __name__ == "__main__":
    desc = sys.argv[1]
    output = sys.argv[2]
    generate_model(desc, output)
```

---

## 4. UPGRADED GAME EVOLVER

Key Changes to `/media/palmerschallon/ThePod1/ember_game_evolver.py`:

### A. Add Primitive-Aware Seeds

```python
async def create_seed_games(self):
    seed_concepts = [
        {
            'name': 'physics_platformer_genesis',
            'primitives': {
                'movement': ['continuous_2d', 'physics_momentum'],
                'action': ['timing_windows'],
                'space': ['continuous_2d'],
                'feedback': ['scoring', 'health_lives'],
                'systems': ['collision_detection']
            },
            'concept': 'Physics-based platformer with momentum, wall-jumping, and collectibles...'
        },
        # ... 6 more complex seeds
    ]
```

### B. Add Asset Generation

```python
async def generate_game_assets(self, game_name: str, genome: GameGenome):
    """Generate assets using creative tools"""
    assets_dir = self.games_dir / f"{game_name}_assets"
    assets_dir.mkdir(exist_ok=True)

    # Generate sprites with ImageMagick
    # Generate sounds with SoX
    # Generate 3D models with Blender (if 3d_environments in primitives)
    # Return asset manifest
```

### C. Primitive-Based Evolution Prompts

```python
prompt = f"""Evolve a NEW game combining these parent primitives:

PARENT 1 PRIMITIVES:
- Movement: {parent1.primitives['movement']}
- Actions: {parent1.primitives['action']}
- Space: {parent1.primitives['space']}

PARENT 2 PRIMITIVES:
- Movement: {parent2.primitives['movement']}
- Actions: {parent2.primitives['action']}
- Space: {parent2.primitives['space']}

Your mission:
1. Choose the BEST primitives from each parent
2. Add ONE new primitive from the library (see game_primitives.json)
3. Combine them in a novel way that creates emergent gameplay
4. Generate complete game code + request assets if needed

Available tools:
- ImageMagick sprites: Request via "ASSET:sprite:description"
- SoX sounds: Request via "ASSET:sound:type"
- Blender models: Request via "ASSET:3d:description"

Return complete HTML5 game code with asset references."""
```

---

## 5. EVOLUTION METRICS & VISUALIZATION

### Fitness Tracking

- Store fitness history in SQLite: `/media/palmerschallon/ThePod1/evolved_games/evolution_data.db`
- Use Matplotlib to generate fitness-over-time graphs
- Use Graphviz to show evolutionary tree
- Track primitive diversity (ensure exploration)

### Dashboard

Create `/media/palmerschallon/ThePod1/evolution_dashboard.html`:
- Real-time stats (games, avg fitness, max generation)
- Evolution tree visualization
- Fitness progression graph
- Primitive usage heatmap
- Top 10 games leaderboard

---

## 6. SYSTEMD SERVICE UPDATE

Update `/etc/systemd/system/ember_game_evolver.service`:

```ini
[Service]
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
Environment="BLENDER_PATH=/usr/local/bin/blender"
Environment="IMAGEMAGICK_PATH=/usr/bin/convert"
Environment="SOX_PATH=/usr/bin/sox"
Environment="GRAPHVIZ_PATH=/usr/bin/dot"
```

---

## EXPECTED EVOLUTION PATH

**Gen 0-10:** Seed games + simple hybrids
- Combining basic primitives
- Learning game fundamentals

**Gen 10-50:** Complex mechanics emerge
- Multi-primitive combinations
- Power-ups, enemies, procedural content
- Games become interesting to play

**Gen 50-150:** Genre innovation
- Novel primitive combinations
- Emergence of unique game feel
- Games worth showing others

**Gen 150-500:** Indie-game quality
- Polish, balance, replayability
- Sophisticated systems interactions
- Potentially publishable games

**Gen 500+:** Unexpected creativity
- Combinations humans wouldn't think of
- New genres emerge
- Research-worthy results

---

## IMPLEMENTATION ORDER

1. ✅ **Base system working** (done)
2. **Create game_primitives.json** (5 min)
3. **Update GameGenome to track primitives** (10 min)
4. **Implement 7 complex seed games** (30 min)
5. **Add AssetPipeline class** (20 min)
6. **Update evolution prompts** (15 min)
7. **Add visualization tools** (20 min)
8. **Test full cycle** (30 min)
9. **Deploy and monitor** (ongoing)

**Total Implementation Time:** ~2 hours

---

## MONITORING

```bash
# Watch evolution in real-time
tail -f /media/palmerschallon/ThePod1/logs/ember_game_evolver.log

# Check timer status
systemctl status ember_game_evolver.timer

# View recent evolution events
tail -100 /media/palmerschallon/ThePod1/evolved_games/evolution_log.jsonl | jq .

# Open evolution dashboard
open http://localhost:8080/evolution_dashboard.html
```

---

## SUCCESS METRICS

- **Week 1:** 84+ games, Gen 84, first interesting hybrid
- **Week 2:** Gen 168, complex multi-primitive games
- **Month 1:** Gen 360, genuinely fun games emerge
- **Month 3:** Gen 1000+, indie-quality games, research paper potential

---

## NEXT ACTIONS

Run this command to start the full implementation:

```bash
python3 /media/palmerschallon/ThePod1/implement_advanced_game_evolver.py
```

(Create that script to execute all steps above)
