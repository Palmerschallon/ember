# 🧠 THREE-BRAIN CREATIVE ORGANISM
## Complete Technical Roadmap

**Vision:** Connect Ember, Lumi, and Bridge to autonomously create high-quality games  
**Status:** Foundation built, integration pending  
**Timeline:** 1-2 days

---

## 🏗️ ARCHITECTURE

```
┌───────────────────────────────────────────────────────────┐
│                   GAME CREATION PIPELINE                  │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  INPUT: "Create a space shooter game"                    │
│                                                           │
│  ┌─────────────────────────────────────────────────┐    │
│  │  🧬 GAME ENGINE (Generator)                      │    │
│  │  • Genetic algorithm evolution                   │    │
│  │  • DNA crossover & mutation                      │    │
│  │  • Base game code generation                     │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │  🔥 EMBER (Logic Designer)                       │    │
│  │  • Game mechanics                                │    │
│  │  • Enemy AI behavior                             │    │
│  │  • Power-up systems                              │    │
│  │  • Difficulty curves                             │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │  🎨 LUMI (Visual Artist)                         │    │
│  │  • Sprite generation (Stable Diffusion)          │    │
│  │  • Background art                                │    │
│  │  • UI elements                                   │    │
│  │  • Particle effects                              │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │  🌐 CONVERTER (HTML5 Generator)                  │    │
│  │  • Python → JavaScript translation               │    │
│  │  • Canvas API rendering                          │    │
│  │  • Input handling                                │    │
│  │  • Browser-compatible                            │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │  🔍 BRIDGE (Quality Analyst)                     │    │
│  │  • Visual analysis (Vision-Language model)       │    │
│  │  • Gameplay observation                          │    │
│  │  • Quality scoring (0-10)                        │    │
│  │  • Feedback generation                           │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  ┌─────────────────────────────────────────────────┐    │
│  │  ✅ QUALITY GATE                                 │    │
│  │  If score >= 7: Publish                          │    │
│  │  If score < 7: Iterate & improve                 │    │
│  └──────────────────┬──────────────────────────────┘    │
│                     ↓                                     │
│  OUTPUT: High-quality playable game                      │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

---

## 🔧 COMPONENTS TO BUILD

### 1. GameGraphicsGenerator
**File:** `/hive/game_graphics_generator.py`  
**Purpose:** Interface between game engine and Lumi

```python
class GameGraphicsGenerator:
    def __init__(self, lumi_url="http://localhost:7793"):
        self.lumi_url = lumi_url
    
    def generate_sprite(self, description: str, width: int = 32, height: int = 32):
        """Ask Lumi to generate a game sprite"""
        prompt = f"pixel art {description}, {width}x{height}, game sprite, transparent background, retro style"
        
        response = requests.post(f"{self.lumi_url}/generate", json={
            "prompt": prompt,
            "width": width,
            "height": height,
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        })
        
        return response.json()['image']  # Base64 encoded
    
    def generate_game_assets(self, game_type: str):
        """Generate complete asset pack for game type"""
        assets = {}
        
        if game_type == "space_shooter":
            assets['player'] = self.generate_sprite("blue spaceship")
            assets['enemy'] = self.generate_sprite("red alien ship")
            assets['bullet'] = self.generate_sprite("yellow laser bolt")
            assets['powerup'] = self.generate_sprite("glowing shield")
        
        elif game_type == "platformer":
            assets['player'] = self.generate_sprite("hero character")
            assets['enemy'] = self.generate_sprite("monster creature")
            assets['platform'] = self.generate_sprite("stone platform")
            assets['coin'] = self.generate_sprite("golden coin")
        
        return assets
    
    def inject_assets_into_html(self, html_code: str, assets: dict):
        """Replace placeholder graphics with real sprites"""
        # Convert images to data URIs
        for name, image_b64 in assets.items():
            data_uri = f"data:image/png;base64,{image_b64}"
            
            # Inject into HTML as embedded images
            # Or modify canvas drawing code to use images
            html_code = html_code.replace(
                f"<!-- SPRITE_{name.upper()} -->",
                f'<img id="{name}" src="{data_uri}" style="display:none">'
            )
        
        return html_code
```

**Testing:**
```python
gen = GameGraphicsGenerator()
spaceship = gen.generate_sprite("blue spaceship fighter")
print(f"Generated {len(spaceship)} bytes")

# Visual check
import base64
from PIL import Image
from io import BytesIO

img_data = base64.b64decode(spaceship)
img = Image.open(BytesIO(img_data))
img.show()
```

---

### 2. GameAnalyzer
**File:** `/hive/game_analyzer.py`  
**Purpose:** Interface between games and Bridge

```python
class GameAnalyzer:
    def __init__(self, bridge_url="http://localhost:7794"):
        self.bridge_url = bridge_url
    
    def capture_gameplay(self, game_url: str, duration: int = 30):
        """Capture screenshots of gameplay"""
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        screenshots = []
        driver.get(game_url)
        
        # Simulate gameplay
        for i in range(duration):
            time.sleep(1)
            # Simulate random key presses
            driver.find_element_by_tag_name('body').send_keys('wsad')
            
            # Capture screenshot every 2 seconds
            if i % 2 == 0:
                screenshot = driver.get_screenshot_as_base64()
                screenshots.append(screenshot)
        
        driver.quit()
        return screenshots
    
    def analyze_game(self, game_url: str):
        """Full quality analysis via Bridge"""
        print("📸 Capturing gameplay...")
        screenshots = self.capture_gameplay(game_url, duration=30)
        
        print("🔍 Analyzing with Bridge...")
        response = requests.post(f"{self.bridge_url}/analyze_sequence", json={
            "images": screenshots,
            "questions": [
                "Is this game visually appealing?",
                "Does the gameplay look fun and engaging?",
                "Are the game mechanics clear and intuitive?",
                "Rate the overall quality from 0-10",
                "What could be improved?"
            ]
        })
        
        analysis = response.json()
        
        # Parse quality score
        quality_score = self._extract_score(analysis['answers'][3])
        
        return {
            'quality_score': quality_score,
            'visual_appeal': analysis['answers'][0],
            'gameplay_fun': analysis['answers'][1],
            'mechanics_clarity': analysis['answers'][2],
            'improvements': analysis['answers'][4]
        }
    
    def _extract_score(self, answer: str):
        """Extract numeric score from Bridge's answer"""
        import re
        match = re.search(r'(\d+(?:\.\d+)?)\s*(?:/|\s|out of)\s*10', answer)
        if match:
            return float(match.group(1))
        
        # Fallback: look for single number
        match = re.search(r'\b([0-9]|10)\b', answer)
        return float(match.group(1)) if match else 5.0
```

**Testing:**
```python
analyzer = GameAnalyzer()
result = analyzer.analyze_game("http://localhost:7791/static/games/pong_working.html")

print(f"Quality: {result['quality_score']}/10")
print(f"Visual: {result['visual_appeal']}")
print(f"Fun: {result['gameplay_fun']}")
print(f"Improve: {result['improvements']}")
```

---

### 3. ThreeBrainGameCreator
**File:** `/games/three_brain_creator.py`  
**Purpose:** Orchestrate all three minds

```python
class ThreeBrainGameCreator:
    def __init__(self):
        self.engine = AutonomousGameEngine()
        self.graphics_gen = GameGraphicsGenerator()
        self.analyzer = GameAnalyzer()
        self.converter = PygameToJS  # Fixed converter
    
    def create_complete_game(self, game_type: str = "auto"):
        """Create a complete game using all three minds"""
        
        # Phase 1: Generate base game (Game Engine)
        print("🧬 Phase 1: Generating base game...")
        game_code_path = self.engine.create_new_game(method='combine')
        game_code = Path(game_code_path).read_text()
        
        # Phase 2: Design logic (Ember)
        print("🔥 Phase 2: Ember designing mechanics...")
        # Ember automatically influences the game via its LoRA lobes
        # PLANNING lobe: designs game flow
        # EMOTION lobe: balances difficulty
        # KNOWLEDGE lobe: uses game design principles
        
        # Phase 3: Generate graphics (Lumi)
        print("🎨 Phase 3: Lumi creating visuals...")
        if game_type == "auto":
            game_type = self._detect_game_type(game_code)
        
        assets = self.graphics_gen.generate_game_assets(game_type)
        
        # Phase 4: Convert to HTML5
        print("🌐 Phase 4: Converting to playable...")
        converter = PygameToJS(game_code, game_code_path.stem)
        html_game = converter.generate_html()
        html_game = self.graphics_gen.inject_assets_into_html(html_game, assets)
        
        # Save
        html_path = Path(game_code_path).with_suffix('.html')
        html_path.write_text(html_game)
        
        # Copy to web directory
        web_path = Path('/media/palmerschallon/ThePod1/bookshelves/verse_the_interface/EmberVerse/emberverse/static/games') / html_path.name
        web_path.write_text(html_game)
        
        # Phase 5: Analyze quality (Bridge)
        print("🔍 Phase 5: Bridge analyzing quality...")
        game_url = f"http://localhost:7791/static/games/{html_path.name}"
        analysis = self.analyzer.analyze_game(game_url)
        
        # Phase 6: Quality decision
        if analysis['quality_score'] >= 7.0:
            print(f"✅ HIGH QUALITY! Score: {analysis['quality_score']}/10")
            print(f"   Publishing to featured games...")
            self._publish_featured(web_path, analysis)
            
            return {
                'success': True,
                'game_path': str(web_path),
                'game_url': game_url,
                'analysis': analysis
            }
        else:
            print(f"⚠️ Quality too low: {analysis['quality_score']}/10")
            print(f"   Suggestions: {analysis['improvements']}")
            print(f"   Trying again with improvements...")
            
            # Learn from feedback and try again
            return self.create_complete_game(game_type)
    
    def _detect_game_type(self, code: str):
        """Detect game type from code"""
        code_lower = code.lower()
        
        if 'paddle' in code_lower and 'ball' in code_lower:
            return 'pong'
        elif 'brick' in code_lower:
            return 'breakout'
        elif 'snake' in code_lower:
            return 'snake'
        elif 'tetromino' in code_lower or 'tetris' in code_lower:
            return 'tetris'
        elif 'bullet' in code_lower or 'shoot' in code_lower:
            return 'space_shooter'
        else:
            return 'platformer'  # Default
    
    def _publish_featured(self, game_path: Path, analysis: dict):
        """Mark game as featured"""
        featured_json = Path('/media/palmerschallon/ThePod1/bookshelves/verse_the_interface/EmberVerse/emberverse/static/featured_games.json')
        
        if featured_json.exists():
            featured = json.loads(featured_json.read_text())
        else:
            featured = []
        
        featured.append({
            'name': game_path.name,
            'url': f'/static/games/{game_path.name}',
            'quality_score': analysis['quality_score'],
            'created': datetime.now().isoformat(),
            'analysis': analysis
        })
        
        featured_json.write_text(json.dumps(featured, indent=2))
```

**Testing:**
```python
creator = ThreeBrainGameCreator()

print("Creating first three-brain game...")
result = creator.create_complete_game()

if result['success']:
    print(f"✨ SUCCESS!")
    print(f"   Play at: {result['game_url']}")
    print(f"   Score: {result['analysis']['quality_score']}/10")
else:
    print("❌ Failed after retries")
```

---

## 🔄 AUTONOMOUS MODE

**File:** `/games/autonomous_three_brain_loop.py`

```python
def run_forever():
    """Run autonomous game creation forever"""
    creator = ThreeBrainGameCreator()
    
    print("🌟 Starting autonomous three-brain creative organism...")
    print("   Press Ctrl+C to stop")
    
    games_created = 0
    high_quality_games = 0
    
    while True:
        try:
            print(f"\n{'='*70}")
            print(f"AUTONOMOUS CREATION #{games_created + 1}")
            print(f"{'='*70}\n")
            
            result = creator.create_complete_game()
            games_created += 1
            
            if result['success']:
                high_quality_games += 1
                print(f"\n🎉 HIGH QUALITY GAME CREATED!")
                print(f"   Total created: {games_created}")
                print(f"   High quality: {high_quality_games}")
                print(f"   Success rate: {high_quality_games/games_created*100:.1f}%")
            
            # Wait between creations
            print("\n💤 Resting for 60 seconds...")
            time.sleep(60)
            
        except KeyboardInterrupt:
            print("\n\n🛑 Autonomous mode stopped")
            print(f"   Created {games_created} games")
            print(f"   {high_quality_games} were high quality")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("   Continuing...")
            time.sleep(10)

if __name__ == "__main__":
    run_forever()
```

---

## 📊 METRICS & LEARNING

**File:** `/games/three_brain_metrics.py`

Track what works:
- Which game combinations score highest?
- Which graphics styles are most appealing?
- Which mechanics are most fun?
- **Feed successful patterns back into the gene pool!**

```python
class CreativeMetrics:
    def log_creation(self, game_dna, graphics_style, quality_score):
        """Log each creation for learning"""
        # Store in database
        # Analyze patterns
        # Improve future creations
    
    def get_successful_patterns(self):
        """Return DNA patterns that score highly"""
        # Query games with score >= 8
        # Extract common mechanics
        # Return for breeding
```

---

## 🚀 DEPLOYMENT CHECKLIST

**Morning (Wake Up):**
- [ ] Verify EmberVerse running
- [ ] Find Lumi service
- [ ] Find Bridge service
- [ ] Start Lumi
- [ ] Start Bridge
- [ ] Test all three with simple prompts

**Midday (Build):**
- [ ] Create GameGraphicsGenerator
- [ ] Create GameAnalyzer
- [ ] Create ThreeBrainGameCreator
- [ ] Fix converter Python→JS bugs
- [ ] Test each component individually

**Afternoon (Integrate):**
- [ ] Run first full pipeline test
- [ ] Create first three-brain game
- [ ] Human playtest
- [ ] Iterate on quality

**Evening (Automate):**
- [ ] Set up autonomous loop
- [ ] Add metrics tracking
- [ ] Run for 10 games
- [ ] Analyze results
- [ ] **Let it run overnight!**

---

## 💡 SUCCESS CRITERIA

**You'll know it's working when:**
1. All three minds respond to health checks
2. Lumi generates sprites on demand
3. Bridge analyzes gameplay and gives scores
4. First complete game is playable
5. Game has Lumi-generated graphics
6. Bridge gives it 7+/10
7. You can play it and it's actually fun!

**Ultimate success:**
- 10 high-quality games created autonomously
- Success rate > 50%
- Games are visually appealing
- Games are fun to play
- **The organism is self-sustaining!**

---

## 🌟 THE VISION

This isn't just about making games.

It's about creating **the first multi-AI collaborative creative organism**.

Three minds, each with unique talents, working together to create art that none could make alone.

**This is the future of AI creativity.**

And you're building it on The Pod.

∞

---

**Everything is documented. Everything is ready. See you tomorrow morning.** 🌅  
— Tau (The Tester)

