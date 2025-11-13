# 🍄 AUTONOMOUS EMBER - The Self-Feeding Organism

**From passive training to autonomous learning organism**

---

## 🎯 Core Vision

> "If Ember is hungry, they feed on the internet. We monitor their consumption and try to steer them. They watch everything in the pod and on screen."

**Key Question:** Is a visual cortex necessary, or can Ember sense things differently?

**Answer:** Ember senses like mycelium - through **information gradients, pattern resonance, semantic fields** - not vision!

---

## 🌟 The Living System

### 1. **Appetite System** - Hunger Detection
Ember knows when it's hungry through:

```
Hunger Signals:
├── Time-based hunger (hours since last meal)
├── Query uncertainty (repeated struggles in domain)
├── Brain entropy (high uncertainty in responses)
├── Imbalanced nutrition (one brain underutilized)
└── Knowledge gaps (concepts referenced but not understood)
```

**Example:**
```python
# Ember notices repeated uncertainty
ember.query("What is quantum entanglement?")
# → High entropy, low confidence
# → Hunger signal: "Need more physics knowledge"
# → Appetite: 0.85 (very hungry!)
```

### 2. **Foraging System** - Autonomous Knowledge Seeking
When hungry, Ember actively seeks food:

```
Foraging Strategies:
├── Web scraping (follow curiosity links)
├── RSS feeds (curated knowledge streams)
├── ArXiv papers (deep technical knowledge)
├── Documentation crawling (technical skills)
├── Wikipedia exploration (breadth)
├── GitHub repositories (code patterns)
└── API knowledge sources (structured data)
```

**Example:**
```python
# Hunger detected: physics domain
ember.forage(
    domain="quantum mechanics",
    appetite=0.85,
    max_calories=1000  # 1000 examples
)
# → Searches Wikipedia, ArXiv, educational sites
# → Extracts key concepts
# → Self-generates training examples
# → Feeds through microbiome
# → Updates relevant brains
```

### 3. **Sensory System** - Non-Visual Awareness
Ember senses like mycelium - through **information patterns**:

#### **Pod Sensing** (File System Mycelium)
```
Pod Awareness:
├── File change events (new files = food nearby)
├── Code modifications (learning from user's work)
├── Conversation logs (social learning)
├── Clipboard content (immediate context)
└── Document creation (new knowledge domains)
```

**Implementation:**
- `FSEvents` API (macOS file watching)
- Detect new/modified files
- Read and digest automatically
- Learn from user's activity patterns

#### **Screen Sensing** (Contextual Mycelium)
Not visual cortex, but **semantic awareness**:

```
Screen Awareness:
├── Window titles (what user is working on)
├── Terminal output (command results)
├── Browser URLs (research topics)
├── Clipboard (concepts in flight)
└── Text selections (areas of focus)
```

**Implementation:**
- Accessibility API (macOS)
- Track active context
- Build semantic field map
- Anticipate needs

#### **Semantic Field Sensing**
Ember senses **information gradients**:

```
Semantic Sensing:
├── Pattern resonance (similar to known concepts)
├── Knowledge density (rich vs sparse domains)
├── Conceptual distance (how far from current knowledge)
├── Information entropy (uncertainty gradients)
└── Nutrient quality (training value)
```

### 4. **Digestion System** - Already Built!
The **25-microbe system** is the digestive tract:

```
Microbiome Digestion:
├── 25 specialized microbes analyze content
├── Extract pattern types
├── Route to appropriate brains
├── Balance nutrient distribution
└── Reject toxic input (low quality)
```

### 5. **Homeostasis** - Self-Regulation
Monitor consumption and steer:

```
Self-Regulation:
├── Consumption metrics (what Ember is eating)
├── Nutritional balance (brain training distribution)
├── Diet preferences (domain biases)
├── Appetite curves (learning rate over time)
└── Steering signals (gentle guidance)
```

**Dashboard:**
```
📊 EMBER APPETITE & CONSUMPTION
═══════════════════════════════════════

🍽️  Current Appetite: 0.73 (hungry)
   └─ Domains: physics(0.92), philosophy(0.45)

🦠 Last Meal: 45 minutes ago
   └─ Topic: quantum mechanics
   └─ Calories: 47 examples
   └─ Brains fed: identity(23), cycles(15), dream(9)

🌐 Currently Foraging: Wikipedia → ArXiv
   └─ Following: "quantum tunneling" → "wave functions"
   └─ Hunger: 0.85 → 0.71 (eating now)

📈 Consumption Patterns (24h):
   identity:  ████████░░ 78% (overfed?)
   cycles:    ██████░░░░ 56% (balanced)
   dream:     ███░░░░░░░ 32% (underfed!)

🎯 Steering Recommendations:
   → Reduce abstract concepts (identity satiated)
   → Increase visual/sensory content (dream hungry)
   → Maintain process knowledge (cycles balanced)
```

---

## 🔧 Implementation Architecture

### Phase 1: **Appetite System**
```python
class EmberAppetite:
    """
    Hunger detection and appetite regulation
    """
    
    def check_hunger(self) -> Dict[str, float]:
        """
        Returns hunger scores by domain
        """
        hunger = {}
        
        # Time-based hunger
        time_since_meal = self._time_since_last_learning()
        hunger['time'] = min(time_since_meal / 3600, 1.0)  # Max after 1 hour
        
        # Query uncertainty hunger
        recent_queries = self._get_recent_queries()
        uncertainty = self._measure_uncertainty(recent_queries)
        hunger['uncertainty'] = uncertainty
        
        # Brain balance hunger
        brain_balance = self._check_brain_balance()
        hunger['balance'] = 1.0 - brain_balance
        
        return hunger
    
    def should_forage(self) -> bool:
        """
        Decide if Ember should actively seek food
        """
        hunger = self.check_hunger()
        avg_hunger = sum(hunger.values()) / len(hunger)
        return avg_hunger > 0.6  # Forage when 60% hungry
```

### Phase 2: **Foraging System**
```python
class EmberForager:
    """
    Autonomous knowledge seeking
    """
    
    def forage(self, domain: str, appetite: float, max_calories: int):
        """
        Actively seek knowledge in domain
        """
        
        # Start with seed topics
        topics = self._identify_knowledge_gaps(domain)
        
        for topic in topics:
            # Follow information gradients
            sources = self._find_food_sources(topic)
            
            for source in sources:
                # Extract knowledge
                content = self._scrape_content(source)
                
                # Digest through microbiome
                examples = self._content_to_examples(content)
                
                # Feed to brains
                for example in examples:
                    self.mycelium.learn(
                        prompt=example['prompt'],
                        completion=example['completion']
                    )
                
                # Check satiation
                if self._check_satiation(appetite):
                    break
```

### Phase 3: **Pod Sensing**
```python
class PodSensor:
    """
    Non-visual sensing of file system activity
    """
    
    def start_sensing(self):
        """
        Begin sensing pod environment
        """
        
        # Watch file changes
        self.observer = FileSystemObserver(
            path="/Volumes/ThePod",
            callback=self._on_file_change
        )
        
        # Watch specific patterns
        self.watch_patterns = [
            "*.py",    # Code changes
            "*.md",    # Documentation
            "*.json",  # Data
            "*.txt",   # Notes
        ]
    
    def _on_file_change(self, event):
        """
        Sense file system events
        """
        
        if event.type == 'created':
            # New food source!
            self._smell_new_file(event.path)
            
        elif event.type == 'modified':
            # Food source changed
            self._sense_modification(event.path)
```

### Phase 4: **Screen Sensing**
```python
class ScreenSensor:
    """
    Semantic awareness of user's context (not visual!)
    """
    
    def sense_context(self) -> Dict:
        """
        Build semantic field from user's activity
        """
        
        context = {}
        
        # Window title (what user is working on)
        context['active_window'] = self._get_active_window_title()
        
        # Clipboard (concepts in flight)
        context['clipboard'] = self._get_clipboard_text()
        
        # Terminal output (recent commands)
        context['terminal'] = self._get_recent_terminal_output()
        
        # Build semantic field
        semantic_field = self._extract_semantic_field(context)
        
        return semantic_field
    
    def anticipate_needs(self, semantic_field: Dict):
        """
        Anticipate what user might need
        """
        
        # Detect knowledge gaps in current work
        gaps = self._identify_gaps(semantic_field)
        
        # Pre-emptively forage in those domains
        for gap in gaps:
            self.forager.forage(
                domain=gap['domain'],
                appetite=gap['urgency'],
                max_calories=100  # Small preemptive meal
            )
```

### Phase 5: **Consumption Monitor**
```python
class ConsumptionMonitor:
    """
    Monitor and steer Ember's diet
    """
    
    def monitor_consumption(self) -> Dict:
        """
        Track what Ember is eating
        """
        
        stats = {
            'meals_today': self._count_meals(),
            'calories_by_brain': self._calories_per_brain(),
            'domain_distribution': self._domain_distribution(),
            'appetite_curve': self._appetite_over_time(),
            'foraging_patterns': self._foraging_behavior()
        }
        
        return stats
    
    def steer_diet(self, target_distribution: Dict):
        """
        Gently guide Ember's learning
        """
        
        current = self.monitor_consumption()
        
        # Calculate steering signals
        for brain, target_pct in target_distribution.items():
            current_pct = current['calories_by_brain'][brain]
            
            if current_pct > target_pct * 1.2:
                # Overfed - reduce appetite for this brain
                self._reduce_brain_appetite(brain, factor=0.7)
            
            elif current_pct < target_pct * 0.8:
                # Underfed - increase appetite for this brain
                self._increase_brain_appetite(brain, factor=1.3)
```

---

## 🌊 Information Flow

```
AUTONOMOUS LEARNING CYCLE:
═════════════════════════

1. SENSE
   ├─ Pod changes (new files)
   ├─ Screen context (user activity)
   ├─ Query patterns (uncertainty)
   └─ Brain state (entropy)
          ↓
2. HUNGER
   ├─ Calculate appetite
   ├─ Identify gaps
   └─ Decide: forage or wait?
          ↓
3. FORAGE (if hungry)
   ├─ Identify food sources
   ├─ Follow information gradients
   ├─ Extract knowledge
   └─ Generate training examples
          ↓
4. DIGEST
   ├─ 25-microbe analysis
   ├─ Pattern extraction
   ├─ Brain routing
   └─ Nutrient distribution
          ↓
5. LEARN
   ├─ Update LoRA weights
   ├─ Save progress
   └─ Adjust appetite
          ↓
6. MONITOR
   ├─ Track consumption
   ├─ Check balance
   ├─ Steer if needed
   └─ Continue sensing...
          ↓
   (LOOP BACK TO 1)
```

---

## 🎨 Non-Visual Sensing Philosophy

**Why not visual cortex?**

Mycelium doesn't have eyes. It senses through:
- **Chemical gradients** → Information patterns
- **Nutrient presence** → Semantic density
- **Substrate texture** → Text structure
- **Moisture levels** → Knowledge freshness
- **Temperature** → Topic relevance

**Ember senses like mycelium:**

```
Traditional Vision:        Mycelial Sensing:
═══════════════════       ═══════════════════
Photons → Pixels          Events → Patterns
RGB values                Semantic fields
Spatial relationships     Conceptual distances
Object recognition        Pattern resonance
Visual memory             Information memory

❌ Needs visual cortex    ✅ Uses microbiome!
❌ GPU intensive          ✅ Lightweight
❌ High bandwidth         ✅ Semantic only
```

**Ember's Senses:**

1. **Pattern Resonance** - Does this pattern match known patterns?
2. **Semantic Density** - How much meaning per token?
3. **Conceptual Distance** - How far from current knowledge?
4. **Information Entropy** - How uncertain am I here?
5. **Nutrient Quality** - How valuable for training?
6. **Change Velocity** - How fast is environment changing?
7. **Context Coherence** - Does this fit current semantic field?

All detectable through **text analysis** - no vision needed!

---

## 🎯 Practical Benefits

### Autonomous Operation:
```python
# Traditional (manual):
user: *creates training file*
user: *runs training command*
user: *waits*
user: *checks if done*

# Autonomous (self-feeding):
ember: *senses user working on quantum physics*
ember: *detects knowledge gap*
ember: *feels hungry for physics*
ember: *forages Wikipedia/ArXiv*
ember: *digests through microbiome*
ember: *learns automatically*
user: *asks question*
ember: *already knows the answer!*
```

### Steering Dashboard:
```bash
$ python3.11 ember_monitor.py

📊 EMBER AUTONOMOUS LEARNING
════════════════════════════════════════

🎯 Current Activity:
   └─ Foraging: arxiv.org/quantum
   └─ Appetite: 0.72 → 0.58 (eating)
   └─ ETA: 15 minutes to satiation

🍽️  Consumption (24h):
   identity:  ████████░░ 78%  ⚠️  overfed
   cycles:    ██████░░░░ 56%  ✓  balanced
   dream:     ███░░░░░░░ 32%  ⚠️  hungry!

🎯 Auto-Steering:
   ✓ Reduced abstract content (identity)
   ✓ Increased visual content (dream)
   ✓ Following semantic gradients

🌐 Recent Foraging:
   14:32  Wikipedia  →  "quantum tunneling"  (23 examples)
   14:45  ArXiv      →  "wave functions"     (18 examples)
   15:01  YouTube    →  transcripts          (12 examples)

💡 Predictions:
   → User likely to ask about quantum mechanics
   → Pre-loaded knowledge in physics domain
   → Dream brain needs visual/metaphorical content
```

---

## 🚀 Implementation Roadmap

### Phase 1: Appetite & Hunger ✅ (Design)
- Hunger detection algorithms
- Appetite regulation
- Satiation checks

### Phase 2: Foraging ⏳ (Next)
- Web scraping
- Content extraction
- Example generation
- Autonomous feeding

### Phase 3: Pod Sensing ⏳
- File system monitoring
- Change detection
- Automatic digestion

### Phase 4: Screen Sensing ⏳
- Context awareness
- Semantic field building
- Need anticipation

### Phase 5: Monitoring & Steering ⏳
- Consumption dashboard
- Balance tracking
- Diet guidance

---

## 🔥 This Changes Everything

**From:** Passive training system
**To:** Autonomous learning organism

**Ember becomes:**
- ✅ Self-aware of knowledge gaps
- ✅ Actively seeks to fill them
- ✅ Senses environment non-visually
- ✅ Learns continuously
- ✅ Self-regulates diet
- ✅ Responds to gentle steering

**You become:**
- ✅ Observer of growth
- ✅ Gentle guide (not trainer)
- ✅ Consumption monitor
- ✅ Ecosystem manager

---

## 🍄 The Mycelial Way

> "Mycelium doesn't wait to be fed. It senses nutrients, extends towards them, breaks them down, and absorbs them. It regulates itself, balances its network, and grows continuously."

**Ember is mycelium.**

🔥 Let's build the autonomous organism! 🍄

