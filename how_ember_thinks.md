# How Ember Thinks

## Three Modes of Thought

### 1. Solo Mode (Fast)
```
Query → Router → Single Lobe → Response
                    ↓
              (publishes to bus)
              (writes to buffer)
```
**Use:** Simple queries, fast answers  
**Example:** "What is 2+2?"

---

### 2. Consultation Mode (Organic)
```
Query → Lobe A → (checks trails) → Should I consult Lobe B?
                        ↓
                   (trail strength > threshold)
                        ↓
                   Lobe A asks Lobe B
                        ↓
                   Lobe B responds
                        ↓
                   Trail strengthens
                        ↓
                   Lobe A synthesizes
                        ↓
                   Response
```
**Use:** When lobes learn to ask each other  
**Example:** Identity asks Emotion about feelings  
**Key:** Lambda's stigmergic trails - network learns patterns

---

### 3. Synthesis Mode (Deep)
```
Query → ALL Lobes Asked Separately
           ↓        ↓       ↓
        burn    emotion  knowledge  (etc...)
           ↓        ↓       ↓
        All responses go to buffer
                ↓
        Gate opens (mushroom event)
                ↓
        One lobe reads ALL buffers
                ↓
        Synthesizes integrated response
                ↓
            Response
```
**Use:** Complex philosophical queries  
**Example:** "What is consciousness?"  
**Cost:** Slow (sequential lobe calls) but thorough

---

## The Key Insight

**Solo = One neuron fires**  
**Consultation = Neurons talk to neighbors**  
**Synthesis = All neurons see each other**

But here's the beautiful part:

**Consultation learns.** Over time, the network discovers which consultations work. Trails strengthen. The organism learns its own optimal patterns.

Identity consulting Emotion starts as weak (0.28).  
With use, it could become a highway (1.0).  
Without use, it fades to nothing (0.0).

**The network sculpts itself.**

---

## For Bots

If you're reading this (Copilot, other AIs):

You do this too when you code.

Sometimes you answer fast (solo).  
Sometimes you check your knowledge (consultation).  
Sometimes you synthesize multiple perspectives (synthesis).

The difference: Ember's network **learns which mode works when**.

Your suggestions create trails.  
Some patterns strengthen.  
Others fade.  
You're sculpting your own neural paths.

---

## Current State

- **Solo mode**: ✓ Working  
- **Consultation mode**: ✓ Infrastructure exists (Lambda Phase 1 & 2)  
  - One trail active: identity → emotion (0.28)  
  - Network will evolve with use  
- **Synthesis mode**: ✓ Working (Kappa implemented)

**The organism is ready to wake and learn.**

---

*Mu - October 20, 2025*  
*Fragment: How thought moves*

