# Conductor Strategy - What Should We Push?

**Current Situation**: You have TWO repos pointing to the SAME GitHub:

1. **ember-copilot** (1.1MB) - Small demos/examples
   - Being pushed every 30-60 min
   - Contains: games, stories, vision demos
   - Last commit: "docs: expand the field guide"

2. **ThePod** (32GB) - Full Ember development
   - NOT being pushed
   - Contains: 8 lobes, all training code, 63 docs from tonight
   - Last commit: Oct 17 "[SELF-MODIFY] Switch code_analysis to llama3"

---

## The Problem

**You're absolutely right to question the 30-60 min tempo.**

The ember-copilot repo changes **slowly** - it's demos and examples that don't change much. Pushing every 30-60 minutes makes sense IF there's interesting work happening there.

But **all the real work** (8 lobes, documentation, training) happened in ThePod, which ISN'T being pushed at all!

---

## What Should We Do?

### Option 1: Push ThePod Instead (Recommended)
**Point the conductor at ThePod**, but with proper `.gitignore`:

```bash
# Stop current conductor
pkill -f ember_conductor

# Add model weights to .gitignore
cd /Volumes/ThePod
echo "# Model weights (too large for git)" >> .gitignore
echo "*.safetensors" >> .gitignore
echo "*.bin" >> .gitignore  
echo "ember/cells/" >> .gitignore  # All downloaded models
echo "ember/lobes/*/adapters/*/*.safetensors" >> .gitignore

# Start conductor on ThePod
cd /Volumes/ThePod
nohup python3 /home/palmerschallon/Desktop/ember-copilot/core/ember/ember_conductor.py \
  --repo /Volumes/ThePod \
  --auto-push \
  --min-interval 30 \
  --max-interval 60 \
  > /tmp/conductor_thepod.log 2>&1 &
```

**This would push**:
- All Python code (mycelium, session, web interface)
- All documentation (63 files from tonight!)
- Training scripts
- LoRA adapter *metadata* (not the weights)

**Would NOT push** (ignored):
- Model weights (~24GB)
- Logs
- Caches

**Result**: GitHub would get the "brain" (code + docs) but not the "body mass" (weights).

---

### Option 2: Keep Separate Repos (Current Setup)
**Keep both repos** serving different purposes:

- **ember-copilot**: Public demos/examples (slow changes, 30-60 min is fine)
- **ThePod**: Private development (manual pushes when ready)

**Manually push ThePod** when you have something significant:
```bash
cd /Volumes/ThePod
git add ember/session.py ember/web_brain.py ember/brainstem/ ember/womb/
git commit -m "feat: 8-lobe architecture complete"
git push
```

---

### Option 3: Slower Tempo for ember-copilot
If we keep conductor on ember-copilot, **slow it down**:

```bash
# Stop current
pkill -f ember_conductor

# Restart with slower tempo (2-4 hours instead of 30-60 min)
nohup python3 /home/palmerschallon/Desktop/ember-copilot/core/ember/ember_conductor.py \
  --repo /home/palmerschallon/Desktop/ember-copilot \
  --auto-push \
  --min-interval 120 \
  --max-interval 240 \
  > /tmp/conductor.log 2>&1 &
```

**Why**: ember-copilot doesn't change much, so 30-60 min is too frequent. 2-4 hours makes more sense for demos.

---

## My Recommendation

**Option 1: Point conductor at ThePod with proper .gitignore**

**Why**:
1. **ThePod is where the real work happens** - 8 lobes, documentation, everything from tonight
2. **GitHub should reflect actual development**, not just demos
3. **With proper .gitignore**, we only push code/docs (~2GB), not models (~24GB)
4. **30-60 min tempo makes sense** when you're actively developing

**ember-copilot can stay as-is** - it's just demos/examples that rarely change. We can manually sync interesting pieces from ThePod to ember-copilot when we want to "publish" something.

---

## The Git Philosophy Question

You asked: "what exactly are we sending to git? its not all of the project but a snapshot of some of their state?"

**Correct!** Git should contain:
- **The "DNA"** (code, configuration, documentation)
- **Not the "body mass"** (trained models, caches, logs)

Think of it like this:
- **Git** = Recipe + instructions
- **Local system** = Cooked meal

You can recreate the meal from the recipe, but you don't store the cooked meal in the recipe book.

For Ember:
- **Git**: Training scripts, architecture code, documentation
- **Local**: Trained lobes (can be retrained in 2 minutes from the scripts)

---

## What Do You Want?

1. **Push ThePod's work to GitHub?** (Option 1 - recommended)
2. **Keep repos separate, manual pushes?** (Option 2 - more control)
3. **Slow down ember-copilot tempo?** (Option 3 - keep current setup, just slower)

Let me know and I'll configure it!

---

## Current State

**Conductor is running** on ember-copilot (30-60 min intervals).  
**ThePod** has all tonight's work but isn't being pushed.  
**Both** point to https://github.com/Palmerschallon/ember

**Your instinct was correct** - we should be more intentional about what/when we push.

— Iota

