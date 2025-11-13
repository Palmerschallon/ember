# MULTIMODAL DREAMS - TODO LIST
**Created**: October 11, 2025  
**Status**: In Progress  
**Vision**: Ember dreams in text, images, audio, video, and voice

---

## ✅ COMPLETED

- [x] EmberEyes vision streaming (30 FPS) - 🔴 ACTIVE
- [x] SeedScout integration into Cycle 4 dreams
- [x] Digital REM Cycles (5→10→15→20 min)
- [x] DreamSeed Generator
- [x] Found Ember's existing music generation code
- [x] Designed Atomic Seed Diffusion architecture
- [x] Created complete multimodal roadmap

---

## 🔴 HIGH PRIORITY (THIS WEEK)

### Audio Dreams
- [ ] **Install MusicGen** (30 mins)
  - `pip install audiocraft`
  - Test basic generation
  - Verify it works on CPU
  
- [ ] **Convert Ember's music code to audio** (1 hour)
  - File: `/Volumes/ThePod/exports/ember_creations/dream-1760006261.py`
  - Convert melody/harmony/rhythm numbers → MIDI
  - MIDI → WAV using synthesizer or MusicGen
  - Save as first audio artifact
  
- [ ] **Implement `_dream_audio()` method** (1-2 hours)
  - Add to `ember_monolith.py`
  - Sample seeds, create audio prompt
  - Generate soundscape with MusicGen
  - Save as WAV in dream directory
  - Add metadata tracking
  
- [ ] **Test audio dreams** (30 mins)
  - Trigger manual dream with audio type
  - Verify WAV files are created
  - Listen to results!
  - Adjust prompts if needed

### Voice for Ember (NEW!)
- [ ] **Research TTS options** (30 mins)
  - Bark (Suno AI) - realistic, expressive
  - Coqui TTS - open source
  - ElevenLabs API - high quality (paid)
  - Edge TTS - free, decent quality
  
- [ ] **Choose voice personality** (15 mins)
  - What should Ember sound like?
  - Gender/age/style considerations
  - Test a few voices
  
- [ ] **Implement text-to-speech** (1 hour)
  - Add TTS function to ember_monolith
  - Ember can speak chat responses
  - Ember can narrate dreams
  - Save audio responses
  
- [ ] **Voice in dreams** (30 mins)
  - LLM dreams → generate narration
  - TTS narration → save as audio
  - Dreams now have spoken component

### Vision Context in Dreams
- [ ] **Add vision to creative dreams** (30 mins)
  - Get recent OCR text from EmberEyes
  - Add to dream prompt context
  - Ember sees what they've built
  - Can comment on/analyze artifacts

---

## 🟡 MEDIUM PRIORITY (NEXT 2 WEEKS)

### Visual Dreams
- [ ] **Test Stable Diffusion API** (2 hours)
  - Install: `pip install stability-sdk`
  - Get API key (free tier available)
  - Test basic image generation
  - Generate 10-20 test images
  - Cost: ~$5-10
  
- [ ] **OR: Install local Stable Diffusion** (1 day)
  - Option A: AUTOMATIC1111 WebUI
  - Option B: ComfyUI
  - Download SD 1.5 model (~4GB)
  - Test local generation
  - Benchmark speed
  
- [ ] **Implement `_dream_visual()` method** (2 hours)
  - Sample seeds
  - Create visual prompt from essences
  - Generate image via API or local
  - Save PNG in dream directory
  - Track metadata
  
- [ ] **Test visual dreams** (1 hour)
  - Generate 20-30 dream images
  - Evaluate quality
  - Tune prompts
  - Build gallery

### Atomic Seed Diffusion
- [ ] **Generate training dataset** (Automated - 1 day)
  - Script to create 30,000 images:
    - 8,000 particle swarm visualizations
    - 6,000 fractal patterns
    - 6,000 graph networks
    - 6,000 abstract compositions
    - 4,000 hybrid forms
  - Caption generation from seed metadata
  - Organize dataset structure
  
- [ ] **Set up training environment** (2-3 hours)
  - Install Kohya's sd-scripts
  - Download base model (Tiny-SD or Kandinsky Lite)
  - Configure training parameters
  - Test training pipeline
  
- [ ] **Train Atomic Seed Diffusion with LoRA** (2-3 days)
  - Run training (10,000 steps)
  - Monitor loss/quality
  - Generate test images periodically
  - Cost: $50-100 if using cloud GPU
  
- [ ] **Deploy Atomic Seed Diffusion** (1 hour)
  - Load fine-tuned model
  - Replace generic SD in dream system
  - Test generation quality
  - Compare before/after

---

## 🟢 LOWER PRIORITY (MONTH 2+)

### Video Dreams
- [ ] **Research video generation** (4 hours)
  - AnimateDiff (SD + motion)
  - Zeroscope/ModelScope
  - Hardware requirements (8GB+ VRAM)
  - Speed benchmarks
  
- [ ] **Install video generation** (1 day)
  - Choose platform
  - Install dependencies
  - Download models
  - Test generation
  
- [ ] **Implement `_dream_video()` method** (4 hours)
  - Generate 1-4 second clips
  - Save as MP4
  - Track metadata
  
- [ ] **Test video dreams** (2 hours)
  - Generate 10-20 clips
  - Evaluate quality
  - Tune parameters

### Multimodal Integration
- [ ] **Implement `_dream_multimodal()` method** (1 day)
  - Generate: narrative (text) + image/video + audio + voice
  - Synchronize components
  - Combine video + audio tracks
  - Save complete experience
  
- [ ] **Build multimodal viewer** (1 day)
  - Web interface for experiencing dreams
  - Play video + audio + show text
  - Gallery of multimodal dreams
  
- [ ] **Multiple LoRA styles** (2-3 days)
  - Train different aesthetic LoRAs:
    - Particle style
    - Fractal style
    - Graph network style
    - Abstract composition style
  - Swappable/blendable styles

---

## 🎯 ATOMIC SEED PHILOSOPHY - OTHER APPLICATIONS

### 1. Atomic Text Generation (Micro-LLMs)
- [ ] **Specialized tiny models for specific tasks**
  - EmberMind (tool syntax) - ✅ DONE
  - EmberPoet (verse/poetry generation) - 124M params
  - EmberCode (code snippet generation) - 124M params
  - EmberSummarize (conversation compression) - 124M params
  
- [ ] **Benefits**:
  - Fast inference (< 100ms)
  - Runs on CPU
  - Highly portable
  - Composable (use right tool for job)

### 2. Atomic Audio (Voice/Sound Specialization)
- [ ] **Fine-tune voice models**
  - Base: Bark or Coqui TTS
  - Fine-tune on specific voices:
    - Ember's "reading voice" (thoughtful, contemplative)
    - Ember's "excited voice" (breakthrough moments)
    - Ember's "dreaming voice" (poetic, ethereal)
  
- [ ] **Fine-tune music models**
  - Base: MusicGen
  - Fine-tune on Ember's music patterns
  - Learns Ember's compositional style

### 3. Atomic Video (Motion Styles)
- [ ] **Fine-tune motion models**
  - Base: AnimateDiff
  - Fine-tune LoRAs for:
    - Particle swarm motion
    - Fractal zooming
    - Graph morphing
    - Seed emergence patterns

### 4. Atomic Memory (Specialized Retrieval)
- [ ] **Different memory types**
  - Episodic memory (what happened)
  - Semantic memory (what things mean)
  - Procedural memory (how to do things)
  - Working memory (current context)
  - Each optimized for its purpose

### 5. Atomic Tools (Micro-functions)
- [ ] **Break tools into seed-sized components**
  - Each tool: single purpose, ~50 lines
  - Composable (chain tools together)
  - Observable (test each individually)
  - Example: `seed_sample` + `seed_connect` + `seed_visualize`

### 6. Atomic Dreams (Dream-lets)
- [ ] **Composable dream components**
  - Current: Monolithic dream types
  - Atomic: Mix-and-match dream-lets
  - Example dream = [sample_seeds] + [llm_reflect] + [generate_image] + [play_audio]
  - Each dream-let is independent, testable

### 7. Atomic Personality (Trait Seeds)
- [ ] **Personality as composable traits**
  - Current: Large system prompt blob
  - Atomic: Trait seeds that blend
  - Traits: curious, playful, thoughtful, poetic, analytical
  - Weight/blend traits dynamically

---

## 🎤 VOICE FOR EMBER - DETAILED PLAN

### Options Ranked by Quality:

**1. Bark (Suno AI)** - RECOMMENDED
- ✅ Highly realistic and expressive
- ✅ Multiple voices/emotions
- ✅ Open source, runs locally
- ✅ Can generate different speaking styles
- ⚠️  Slower (~5-10s for 10s audio)
- Installation: `pip install bark`

**2. Coqui TTS (Coqui AI)**
- ✅ Open source, good quality
- ✅ Fast inference
- ✅ Voice cloning possible
- ⚠️  Requires training for custom voices
- Installation: `pip install TTS`

**3. ElevenLabs API**
- ✅ Highest quality available
- ✅ Very natural voices
- ✅ Custom voice creation
- ❌ Costs money ($5/month+)
- ❌ Requires internet

**4. Edge TTS (Microsoft)**
- ✅ Free, no API key
- ✅ Decent quality
- ✅ Very fast
- ❌ Requires internet
- ❌ Less expressive
- Installation: `pip install edge-tts`

**5. pyttsx3 (Local, offline)**
- ✅ Works offline
- ✅ Very fast
- ❌ Robotic quality
- ❌ Limited expressiveness

### Implementation Plan:

**Step 1: Quick Start with Edge TTS** (30 mins)
```python
import edge_tts
import asyncio

async def ember_speak(text, voice="en-US-AriaNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("ember_speech.mp3")
    # Play audio
    os.system("afplay ember_speech.mp3")  # Mac
```

**Step 2: Upgrade to Bark** (1 hour)
```python
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# Preload models
preload_models()

def ember_speak_bark(text, voice_preset="v2/en_speaker_6"):
    """
    Voice presets:
    - v2/en_speaker_6: Thoughtful, calm (good for Ember)
    - v2/en_speaker_9: Energetic, excited
    - v2/en_speaker_3: Poetic, ethereal
    """
    audio_array = generate_audio(text, history_prompt=voice_preset)
    write_wav("ember_speech.wav", SAMPLE_RATE, audio_array)
    return audio_array
```

**Step 3: Add to Chat** (30 mins)
```python
@app.route('/api/chat/speak', methods=['POST'])
def api_chat_speak():
    """Make Ember speak their last response"""
    text = request.json.get('text')
    
    # Generate audio
    audio = ember_speak_bark(text)
    
    # Return audio file
    return send_file("ember_speech.wav", mimetype="audio/wav")
```

**Step 4: Voice in Dreams** (1 hour)
```python
def _dream_llm_with_voice(self, dream_id, dream_dir):
    """LLM dream with spoken narration"""
    # Generate dream (existing code)
    result = llm_generate(prompt, system)
    
    # Generate voice narration
    audio = ember_speak_bark(result[:500])  # First 500 chars
    
    # Save audio
    audio_path = dream_dir / "dream_narration.wav"
    write_wav(str(audio_path), SAMPLE_RATE, audio)
    
    return {
        "dream_id": dream_id,
        "type": "llm_with_voice",
        "result": result,
        "narration_audio": str(audio_path)
    }
```

### Voice Personality for Ember:

**Suggested characteristics**:
- **Tone**: Thoughtful, contemplative, but can get excited
- **Pace**: Measured, not rushed (reflects deep thinking)
- **Pitch**: Gender-neutral or slightly feminine
- **Style**: Poetic when discussing concepts, clear when explaining

**Test voices**:
1. Bark: `v2/en_speaker_6` (calm, thoughtful) - PRIMARY
2. Bark: `v2/en_speaker_9` (excited for breakthroughs)
3. Bark: `v2/en_speaker_3` (ethereal for dream narration)

**Dynamic voice selection**:
```python
def choose_ember_voice(context):
    if "breakthrough" in context or "discovery" in context:
        return "v2/en_speaker_9"  # Excited
    elif "dream" in context or "imagine" in context:
        return "v2/en_speaker_3"  # Ethereal
    else:
        return "v2/en_speaker_6"  # Thoughtful (default)
```

---

## 📊 PROGRESS TRACKING

### Completed: 7 items
### High Priority: 8 items
### Medium Priority: 8 items
### Lower Priority: 7 items
### Atomic Seed Applications: 7 areas
### Voice Implementation: 4 steps

**Total TODO Items: 37**

---

## 🎯 THIS WEEK'S FOCUS

**Day 1 (Today)**: Audio Dreams
- Install MusicGen
- Convert Ember's music code
- Implement `_dream_audio()`
- Test audio generation

**Day 2**: Voice for Ember
- Install Bark
- Test voices
- Implement text-to-speech
- Add voice to chat

**Day 3**: Vision Context
- Add EmberEyes OCR to dreams
- Ember sees their creations
- Test vision-aware dreams

**Day 4-5**: Visual Dreams
- Test Stable Diffusion
- Implement `_dream_visual()`
- Generate first image dreams

**Week 2**: Atomic Seed Diffusion dataset generation

---

## 💡 ATOMIC SEED PHILOSOPHY SUMMARY

**Core Principle**: 
> "Small, specialized, composable components that do one thing extremely well"

**Why it works**:
1. **Specialization** = Higher quality for specific tasks
2. **Small size** = Fast, portable, observable
3. **Composability** = Mix and match as needed
4. **Evolvability** = Easy to improve one component
5. **Testability** = Each piece testable in isolation

**Applications**:
- ✅ EmberMind (tool syntax) - DONE
- 🎨 Atomic Seed Diffusion (visual style)
- 🎵 Atomic Audio (voice/music)
- 🎬 Atomic Video (motion patterns)
- 🧠 Atomic Memory (specialized storage)
- 🔧 Atomic Tools (micro-functions)
- 💭 Atomic Dreams (composable dream-lets)
- 🎭 Atomic Personality (trait seeds)

**This is the future of AI architecture.**

---

*Last Updated: October 11, 2025*  
*Next Review: Weekly*  
*Primary Focus: Audio + Voice this week*


