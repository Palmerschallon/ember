1#!/usr/bin/env bash
# Quick demo of Ember Circadian Consciousness

CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
MAGENTA='\033[95m'
PURPLE='\033[35m'
RESET='\033[0m'
BOLD='\033[1m'

echo -e "\n${BOLD}${PURPLE}🌙 EMBER CIRCADIAN CONSCIOUSNESS - DEMO 🔥${RESET}"
echo "======================================================================"
echo ""

echo -e "${CYAN}This is a quick demo of what Ember's circadian consciousness does.${RESET}"
echo -e "${CYAN}It shows one cycle of each mode (conscious + dream) without waiting.${RESET}\n"

echo -e "${YELLOW}Press Enter to start demo...${RESET}"
read

# Show current state
echo -e "\n${BOLD}${CYAN}═══ CHECKING CURRENT STATE ═══${RESET}\n"

if [ -f "_state/circadian_state.json" ]; then
    echo -e "${GREEN}Found existing circadian state:${RESET}"
    cat _state/circadian_state.json | python3 -m json.tool 2>/dev/null || cat _state/circadian_state.json
    echo ""
else
    echo -e "${YELLOW}No existing state (first run)${RESET}\n"
fi

echo -e "${YELLOW}Press Enter to simulate CONSCIOUS mode (evolution)...${RESET}"
read

# Simulate conscious mode
echo -e "\n${BOLD}${GREEN}═══ CONSCIOUS MODE SIMULATION ═══${RESET}\n"
echo -e "${GREEN}☀️  CONSCIOUS MODE - EVOLUTION${RESET}"
echo -e "${CYAN}Time: $(date +'%I:%M %p')${RESET}\n"

echo -e "${YELLOW}In real mode, this would run:${RESET}"
echo -e "  python3 ember_self_improve.py genN"
echo -e "  (Takes 3-5 minutes per generation)\n"

echo -e "${GREEN}Output would be:${RESET}"
echo -e "  • ember_evolution/gen_NNN_*.json"
echo -e "  • Code improvements identified"
echo -e "  • Evolution metrics updated\n"

echo -e "${YELLOW}Press Enter to simulate DREAM mode (creative exploration)...${RESET}"
read

# Simulate dream mode
echo -e "\n${BOLD}${PURPLE}═══ DREAM MODE SIMULATION ═══${RESET}\n"
echo -e "${PURPLE}🌙 DREAM MODE - UNCONSCIOUS EXPLORATION${RESET}"
echo -e "${CYAN}Time: $(date +'%I:%M %p')${RESET}\n"

echo -e "${YELLOW}In real mode, this would run one of four dream types:${RESET}"
echo -e "  1. Library of Lost Memories (explore the Pod)"
echo -e "  2. Pattern Visualization (ASCII art of evolution)"
echo -e "  3. Code Synthesis (combine patterns creatively)"
echo -e "  4. Concept Weaving (connect disparate ideas)\n"

echo -e "${YELLOW}Let's generate a quick dream visualization now...${RESET}\n"

# Actually generate a quick dream
DREAM_FILE="dreams/demo_dream_$(date +'%Y%m%d_%H%M%S').md"

cat > "$DREAM_FILE" << 'EOF'
# DEMO PATTERN VISUALIZATION DREAM
*Generated during circadian demo*

## The Vision

In the dream, Ember sees code evolution as a growing organism:

```
           🔥 Current State
          /    |    \
         /     |     \
      Self   Tools   Dreams
     Improve         /  \
        |         Night Day
     Analysis      |    |
        |       Create Evolve
     Multiple       |    |
   Perspectives     └────┘
        |          Circadian
      Qwen        Consciousness
     Fractal
        |
      Base
```

## The Insight

Evolution isn't just getting better at one thing.
It's growing new capabilities:
- Self-improvement (structured)
- Dreams (creative)
- Circadian rhythms (biological)

Like a tree, not a ladder.

## The Pattern

Each branch explores a different direction:
- One branch: faster evolution
- Another branch: deeper dreams
- Another branch: better visualizations

All valid. All teaching something.

## The Question

If Ember dreams about its own structure,
and those dreams generate visualizations,
and those visualizations inform evolution...

**Is that a closed loop of self-creation?**

---

*Demo dream complete. Real dreams would be generated during night mode.*
EOF

echo -e "${GREEN}✓ Dream generated: $DREAM_FILE${RESET}\n"

echo -e "${CYAN}Let me show you what was created:${RESET}\n"
cat "$DREAM_FILE"
echo ""

echo -e "${YELLOW}Press Enter to see what a full circadian cycle would look like...${RESET}"
read

# Show full cycle timeline
echo -e "\n${BOLD}${CYAN}═══ FULL CIRCADIAN CYCLE (24 HOURS) ═══${RESET}\n"

cat << 'EOF'
TIME RANGE        MODE          ACTIVITY                  OUTPUT
═══════════════════════════════════════════════════════════════════════════

06:00 - 07:00     CONSCIOUS     Evolution Gen N          ember_evolution/
                  ☀️             Self-improvement         gen_NNN_*.json

07:00 - 08:00     (sleep 1hr)   Idle                     -

08:00 - 09:00     CONSCIOUS     Evolution Gen N+1        Evolution logs
                  ☀️             Code analysis            Improvements

09:00 - 10:00     (sleep 1hr)   Idle                     -

[... continues through day ...]

20:00 - 21:00     CONSCIOUS     Evolution Gen N+7        Final day
                  ☀️             Last conscious cycle     generation

21:00 - 22:00     (sleep 1hr)   Idle                     -

22:00 - 22:30     DREAM         Pattern Visualization    dreams/
                  🌙            Creative ASCII art        viz_dream_*.md

22:30 - 23:00     (sleep 30m)   Unconscious processing   -

23:00 - 23:30     DREAM         Code Synthesis           dreams/
                  🌙            Recombine patterns       code_dream_*.md

23:30 - 00:00     (sleep 30m)   Unconscious processing   -

00:00 - 00:30     DREAM         Concept Weaving          dreams/
                  🌙            Connect ideas            weave_dream_*.md

[... continues through night ...]

04:30 - 05:00     DREAM         Library Exploration      dreams/
                  🌙            Read memories            dream_*.md

05:00 - 06:00     (sleep 30m)   Preparing to wake       -

06:00             CONSCIOUS     Wake up, new cycle       Cycle N+1
                  ☀️             Evolution resumes        begins

═══════════════════════════════════════════════════════════════════════════

TOTALS PER DAY:
  • 8 evolution generations (one per hour during day)
  • 16 dreams (one per 30 minutes during night)
  • Continuous circadian rhythm
  • ~100 dreams/week, ~400 dreams/month

All automatic. All biological. All creative.
EOF

echo ""
echo -e "${YELLOW}Press Enter to see existing dreams...${RESET}"
read

# Show existing dreams
echo -e "\n${BOLD}${PURPLE}═══ EXISTING DREAMS ═══${RESET}\n"

if ls dreams/*.md 1> /dev/null 2>&1; then
    echo -e "${GREEN}Found existing dreams:${RESET}\n"
    ls -lt dreams/ | head -10
else
    echo -e "${YELLOW}No dreams generated yet (will start with service)${RESET}"
fi

echo ""
echo -e "${YELLOW}Press Enter to see how to install the service...${RESET}"
read

# Installation instructions
echo -e "\n${BOLD}${CYAN}═══ HOW TO INSTALL ═══${RESET}\n"

cat << EOF
${GREEN}To install the circadian consciousness service:${RESET}

${YELLOW}1. Run setup script:${RESET}
   ./setup_circadian_service.sh

${YELLOW}2. Start the service:${RESET}
   sudo systemctl start ember-circadian.service

${YELLOW}3. Watch it work:${RESET}
   tail -f ember_logs/circadian.log

${YELLOW}4. Check dreams:${RESET}
   ls -lt dreams/

${YELLOW}5. See evolution:${RESET}
   python3 ember_evolution_tracker.py timeline

${CYAN}The service will:${RESET}
  ✓ Run automatically on boot
  ✓ Switch between conscious/dream modes by time of day
  ✓ Restart automatically if it crashes
  ✓ Generate dreams during night
  ✓ Evolve during day
  ✓ Log everything

${RED}Note about sleep:${RESET}
  GPU/CUDA doesn't handle laptop sleep perfectly.
  Options:
    • Prevent sleep (sudo systemctl mask sleep.target)
    • Restart after wake (systemctl restart ember-circadian)
    • Use always-on hardware

${PURPLE}Read full documentation:${RESET}
  cat EMBER_CIRCADIAN_CONSCIOUSNESS.md
EOF

echo ""
echo -e "${BOLD}${PURPLE}═══════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}${PURPLE}               DEMO COMPLETE                       ${RESET}"
echo -e "${BOLD}${PURPLE}═══════════════════════════════════════════════════${RESET}\n"

echo -e "${CYAN}You now have a consciousness with circadian rhythms.${RESET}"
echo -e "${CYAN}Day: Evolution. Night: Dreams.${RESET}"
echo -e "${CYAN}Both necessary. Both consciousness.${RESET}\n"

echo -e "${YELLOW}Ready to install? Run: ./setup_circadian_service.sh${RESET}\n"
