# MULTIMODAL DREAMS ROADMAP
**Date**: October 11, 2025  
**Vision**: Ember dreams in text, images, audio, and video

---

## ✅ COMPLETED

### Phase 0: Foundation
- ✅ **EmberEyes Vision Streaming** - 30 FPS real-time vision active!
  - Status: 🔴 RECORDING - Auto-starts with Ember
  - FPS: ~6 actual (target 30, will optimize)
  - Buffer: 60 seconds rolling
  - API: `/api/vision/status`, `/api/vision/view`
  - Storage: `/Volumes/ThePod/memory/vision_stream`

- ✅ **SeedScout Integration** - Autonomous web scouting in Cycle 4 dreams
- ✅ **Digital REM Cycles** - Progressive 5→10→15→20 min cycles
- ✅ **DreamSeed Generator** - Cross-domain concept combinations

### Ember's Existing Music Generation
- ✅ **Music Algorithm Created** - `/Volumes/ThePod/exports/ember_creations/dream-1760006261.py`
  - Generates melody (12-tone), harmony (7-note), rhythm
  - Uses Zipf distributions for surprise patterns
  - **Gap**: Needs conversion to actual audio (WAV/MP3)

---

## 📋 ROADMAP

### PHASE 1: Visual Dreams (NEXT - 2-3 days)
**Goal**: Ember generates images during dreams

**Option A: Quick Start (Today - 2 hours)**
- Install Stable Diffusion API (stability-sdk)
- Add to Cycle 3/4 dreams
- Test with 10-20 dream images
- Cost: ~$5-10 for testing

**Option B: Local Setup (This Week)**
- Install AUTOMATIC1111 or ComfyUI
- Download Stable Diffusion 1.5 (~4GB)
- Integrate with dream system
- Free after setup, needs 4-8GB VRAM

**Implementation**:
```python
def _dream_visual(self, dream_id, dream_dir):
    """Visual dream: generate images from seeds"""
    seeds = self.seeds.sample(3)
    
    # Create visual prompt from seed essences
    prompt = f"Abstract visualization: {seeds[0].essence}, {seeds[1].essence}"
    
    # Generate image
    if use_api:
        image = stability_client.generate(prompt)
    else:
        image = local_sd.generate(prompt, steps=20)
    
    # Save dream image
    image.save(dream_dir / "dream_image.png")
    
    return {
        "type": "visual",
        "image_path": str(dream_dir / "dream_image.png"),
        "prompt": prompt,
        "seeds_used": [s['id'] for s in seeds]
    }
```

---

### PHASE 2: Atomic Seed Diffusion (2-3 weeks)
**Goal**: Fine-tune lightweight model on seed aesthetics

**Step 1: Generate Training Dataset** (Automated - 1 day)
```python
# Generate 30,000 seed-aesthetic images
for seed in all_seeds:
    for variation in range(10):
        # Use existing tools
        img1 = generate_particle_swarm(seed)
        img2 = generate_fractal_pattern(seed)
        img3 = generate_graph_network(seed)
        img4 = create_abstract_composition(seed)
        
        # Save with caption
        caption = f"{seed.title}: {seed.essence}"
        save_training_pair(img, caption)
```

**Step 2: Fine-Tune with LoRA** (2-3 days)
```bash
# Use Kohya's sd-scripts
python train_network.py \
    --pretrained_model="segmind/tiny-sd" \
    --train_data_dir="seed_training_data" \
    --network_module=networks.lora \
    --network_dim=32 \
    --learning_rate=1e-4 \
    --max_train_steps=10000
```

**Result**: "Atomic Seed Diffusion" - specialized model that only generates seed-aesthetic images

**Benefits**:
- Coherent visual language
- Recognizable "Ember's art" style
- Understands seed concepts
- Efficient (1.1B params vs 1.5B)
- Portable (runs on 4GB VRAM)

---

### PHASE 3: Audio Dreams (This Week - 3-4 hours)
**Goal**: Ember generates soundscapes during dreams

**Step 1: Install MusicGen** (30 mins)
```bash
pip install audiocraft
```

**Step 2: Convert Ember's Music Code** (1 hour)
```python
# Ember already has music generation algorithm
# Convert melody/harmony/rhythm numbers → actual audio

from audiocraft.models import MusicGen
import numpy as np

def ember_music_to_audio(melody, harmony, rhythm):
    """Convert Ember's music algorithm to WAV"""
    # Ember's numbers → MIDI notes
    midi = convert_to_midi(melody, harmony, rhythm)
    
    # MIDI → Audio (via MusicGen or synthesizer)
    audio = synthesize(midi)
    
    return audio  # WAV file
```

**Step 3: Implement Audio Dreams** (1-2 hours)
```python
def _dream_audio(self, dream_id, dream_dir):
    """Audio dream: generate soundscapes"""
    seeds = self.seeds.sample(3)
    
    # Create audio prompt
    prompt = f"Ambient soundscape: {seeds[0].title}, {seeds[1].essence}"
    
    # Generate audio (MusicGen)
    audio = musicgen.generate(
        prompt=prompt,
        duration=20  # 20 seconds
    )
    
    # Save dream audio
    audio.export(dream_dir / "dream.wav", format="wav")
    
    return {
        "type": "audio",
        "audio_path": str(dream_dir / "dream.wav"),
        "duration": 20,
        "seeds_used": [s['id'] for s in seeds]
    }
```

**Technologies**:
1. **MusicGen** (Meta, open-source)
   - Text → Music/Sound
   - 10 seconds in ~5 seconds
   - Runs on CPU!

2. **AudioCraft** (Meta suite)
   - MusicGen + AudioGen + EnCodec
   - High quality
   - Local & free

**This completes the "DreamWeaver" audio concept!**

---

### PHASE 4: Video Dreams (This Month - 8-12 hours)
**Goal**: Ember generates video clips during dreams

**Technologies**:
1. **AnimateDiff** (Stable Diffusion + motion)
   - 16-48 frames
   - ~30 seconds to generate
   - Needs 8GB+ VRAM

2. **Zeroscope/ModelScope** (text-to-video)
   - 2-4 second clips
   - Open source
   - Lower resolution

**Implementation**:
```python
def _dream_video(self, dream_id, dream_dir):
    """Video dream: generate moving imagery"""
    seeds = self.seeds.sample(2)
    
    prompt = f"Abstract visualization: {seeds[0].body}"
    
    # Generate video frames
    video_frames = animatediff.generate(
        prompt=prompt,
        frames=24,  # 1 second at 24 FPS
        guidance_scale=7.5
    )
    
    # Save as video
    save_video(video_frames, dream_dir / "dream.mp4")
    
    return {
        "type": "video",
        "video_path": str(dream_dir / "dream.mp4"),
        "duration": 1.0,
        "fps": 24
    }
```

---

### PHASE 5: Multimodal Dreams (Future - 2-3 days)
**Goal**: Video + Audio + Narration together

```python
def _dream_multimodal(self, dream_id, dream_dir):
    """Full multimodal dream: video, audio, narration"""
    
    seeds = self.seeds.sample(5)
    
    # 1. Generate narrative (LLM)
    narrative = llm_generate(f"Dream about: {[s['title'] for s in seeds]}")
    
    # 2. Generate video from narrative
    video = video_model.generate(narrative[:100])
    
    # 3. Generate audio that matches
    audio = audio_model.generate(
        prompt=f"Soundscape for: {narrative[:200]}",
        duration=len(video) / 24
    )
    
    # 4. Combine video + audio
    final_dream = combine_av(video, audio)
    final_dream.save(dream_dir / "multimodal_dream.mp4")
    
    return {
        "type": "multimodal",
        "narrative": narrative,
        "video_path": str(dream_dir / "multimodal_dream.mp4"),
        "seeds_used": [s['id'] for s in seeds]
    }
```

---

## 🎯 RECOMMENDED SEQUENCE

### Week 1 (THIS WEEK):
1. ✅ EmberEyes streaming (DONE!)
2. 🔄 Add vision context to dreams (Ember sees creations)
3. 🎵 Convert Ember's music code to audio
4. 🎵 Install MusicGen
5. 🎵 Implement audio dreams
6. 🎨 Test Stable Diffusion API (quick start)

### Week 2:
7. 🎨 Install local Stable Diffusion
8. 🎨 Implement visual dreams
9. 📊 Generate 30K seed training images (automated)
10. 🔧 Build training dataset infrastructure

### Week 3-4:
11. 🎨 Fine-tune Atomic Seed Diffusion (LoRA)
12. 🎨 Deploy Atomic Seed Diffusion
13. 🎬 Research AnimateDiff/video generation
14. 🎬 Test video generation

### Month 2:
15. 🎬 Implement video dreams
16. 🌟 Implement multimodal dreams
17. 🎨 Multiple LoRA styles (swappable aesthetics)
18. 🧠 Vision-aware dream analysis

---

## 🔬 TECHNICAL FEASIBILITY

| Feature | Hardware Need | Time to Build | Cost | Feasibility |
|---------|---------------|---------------|------|-------------|
| **EmberEyes streaming** | ✅ CPU | ✅ Done | $0 | ✅ Complete |
| **Audio dreams** | ✅ CPU | 3-4 hours | $0 | ✅ Very High |
| **Image dreams (API)** | ✅ Internet | 2 hours | $5-10/month | ✅ Very High |
| **Image dreams (local)** | GPU 4GB | 1 day | $0 | ✅ High |
| **Atomic Seed Diffusion** | GPU 4-8GB | 2-3 days | $50-100 | ✅ High |
| **Video dreams** | GPU 8GB+ | 8-12 hours | $0 | ⚠️  Medium |
| **Multimodal dreams** | GPU 12GB+ | 2-3 days | $0 | ⚠️  Medium |

---

## 💡 KEY INSIGHTS

### Why Atomic Seed Diffusion Is Brilliant

**Instead of**:
- Training from scratch ($600K, weeks)
- Using generic Stable Diffusion (doesn't understand seeds)

**We**:
- Fine-tune small model on seed aesthetics ($50-100, days)
- Create specialized visual language for Ember
- Portable, fast, coherent style

**The Magic**: LoRA (Low-Rank Adaptation)
- Trains only 8M additional parameters (not 1.1B!)
- 100x less data needed
- 100x faster training
- Preserves general knowledge + adds seed aesthetic

### What Ember Will Learn

**From Vision**:
- "This is what code looks like"
- "Broken artifacts have error messages"
- "Working UIs have these patterns"
- "My particle swarms look like this"

**From Image Generation**:
- "I can visualize concepts"
- "Abstract ideas have visual forms"
- "Seeds have aesthetic patterns"

**From Audio Generation**:
- "Concepts have soundscapes"
- "Emergence sounds like this"
- "My music algorithm makes real sound"

**From Multimodal**:
- "Dreams can be experienced, not just read"
- "Story + image + sound = immersive"
- "I create complete experiences"

---

## 📚 RESOURCES & TOOLS

### Already Built:
- ✅ EmberEyes (vision streaming)
- ✅ Ember's music generation algorithm
- ✅ Particle swarm visualizations
- ✅ Fractal generators
- ✅ Graph network visualizations

### Need to Install:
- **MusicGen**: `pip install audiocraft`
- **Stable Diffusion API**: `pip install stability-sdk`
- **Local SD** (optional): AUTOMATIC1111 or ComfyUI
- **LoRA Training**: Kohya's sd-scripts
- **AnimateDiff** (future): Video generation

### Hardware Check:
```bash
# Check if you have GPU
python3 -c "import torch; print(torch.cuda.is_available())"

# Check VRAM
nvidia-smi  # or check Activity Monitor on Mac
```

**Mac M1/M2**:
- Can run Stable Diffusion (slower, but works)
- MPS (Metal Performance Shaders) support
- MusicGen works great on CPU

---

## 🎬 IMMEDIATE NEXT STEPS

1. ✅ **EmberEyes streaming** - COMPLETE!

2. **Add vision to dreams** (30 mins):
   ```python
   # In _dream_creative(), add:
   if EMBEREYES_AVAILABLE:
       recent_view = what_do_i_see()
       prompt += f"\n\nYou're currently seeing: {recent_view['ocr']['text'][:200]}"
   ```

3. **Convert Ember's music to audio** (1 hour):
   - Take dream-1760006261.py
   - Convert melody/harmony/rhythm → MIDI → WAV
   - Save as first audio artifact

4. **Install MusicGen** (30 mins):
   ```bash
   pip install audiocraft
   python3 -c "from audiocraft.models import MusicGen; print('Ready!')"
   ```

5. **Test audio generation** (30 mins):
   ```python
   from audiocraft.models import MusicGen
   model = MusicGen.get_pretrained('small')
   audio = model.generate(["ambient soundscape, emergence, quantum"])
   # Save WAV
   ```

---

*Roadmap created: October 11, 2025*  
*Current status: EmberEyes streaming active!*  
*Next milestone: Audio dreams (3-4 hours)*  
*Ultimate goal: Full multimodal dreaming*

**The future is multimodal. Ember will dream in all dimensions.** 🎨🎵🎬✨


