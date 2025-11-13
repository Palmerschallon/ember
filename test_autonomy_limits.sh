#!/usr/bin/env bash
# Test to show the actual limits of "autonomous" mode

CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
MAGENTA='\033[95m'
RESET='\033[0m'
BOLD='\033[1m'

echo -e "\n${BOLD}${MAGENTA}🧪 TESTING AUTONOMY LIMITS${RESET}"
echo "======================================================================"
echo ""

echo -e "${CYAN}This will show you what 'autonomous' ACTUALLY means right now.${RESET}\n"

# Check current state
echo -e "${YELLOW}1. Checking system state...${RESET}\n"

# Check if laptop is on battery or AC
if [ -f /sys/class/power_supply/BAT*/status ]; then
    battery_status=$(cat /sys/class/power_supply/BAT*/status)
    echo -e "   Power: ${GREEN}$battery_status${RESET}"
else
    echo -e "   Power: ${YELLOW}Unknown (desktop?)${RESET}"
fi

# Check sleep settings
echo -e "   Sleep: $(systemctl status sleep.target 2>&1 | grep -o 'Active: [^(]*' | head -1)"

# Check GPU
echo -e "   GPU: $(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo 'Not available')"

echo ""

# Show what will happen
echo -e "${YELLOW}2. What happens with sleep mode?${RESET}\n"

cat << EOF
${CYAN}Scenario A: Laptop stays awake${RESET}
  └─ Python runs continuously ✅
      └─ GPU stays active ✅
          └─ Ember evolves ✅
              └─ ${GREEN}Works!${RESET}

${CYAN}Scenario B: Laptop sleeps${RESET}
  └─ Python process suspends ⏸️
      └─ GPU powers down ❌
          └─ Ember freezes ❌
              └─ ${RED}Stops!${RESET}

${CYAN}Scenario C: Laptop wakes up${RESET}
  └─ Process may resume... ⚠️
      └─ GPU may be available... ⚠️
          └─ Ember may continue... ⚠️
              └─ ${YELLOW}Unreliable!${RESET}
EOF

echo -e "\n${YELLOW}3. Current autonomous modes:${RESET}\n"

cat << EOF
${CYAN}A) Supervised autonomous (what works now):${RESET}
   ${GREEN}✓${RESET} Runs without asking you for approval
   ${GREEN}✓${RESET} Continues through multiple generations
   ${GREEN}✓${RESET} Stops at max generations or error
   ${RED}✗${RESET} Stops if laptop sleeps
   ${RED}✗${RESET} Stops if you close terminal (unless use screen/tmux)
   ${RED}✗${RESET} Stops on reboot

   ${YELLOW}Command:${RESET}
   python3 ember_continuous_evolution.py --auto --max-generations 10

   ${YELLOW}Reality:${RESET} You need to be around and keep laptop awake

${CYAN}B) Background autonomous (need to build):${RESET}
   ${GREEN}✓${RESET} Runs as system service
   ${GREEN}✓${RESET} Survives terminal close
   ${GREEN}✓${RESET} Starts on boot
   ${RED}✗${RESET} Still stops if laptop sleeps (GPU issue)
   ${RED}✗${RESET} Loses state on crash

   ${YELLOW}Command:${RESET}
   sudo systemctl start ember-evolution

   ${YELLOW}Reality:${RESET} Need systemd service + prevent sleep

${CYAN}C) True autonomous (need hardware + checkpoints):${RESET}
   ${GREEN}✓${RESET} Survives sleep/wake
   ${GREEN}✓${RESET} Survives crashes
   ${GREEN}✓${RESET} Survives reboots
   ${GREEN}✓${RESET} Runs 24/7 forever
   ${YELLOW}!${RESET} Needs always-on hardware OR checkpoint system

   ${YELLOW}Needs:${RESET}
   - Desktop/server that never sleeps
   - OR checkpoint/resume code
   - OR both

   ${YELLOW}Reality:${RESET} Not there yet, but buildable
EOF

echo -e "\n${YELLOW}4. What you can do RIGHT NOW:${RESET}\n"

echo -e "${GREEN}Option 1: Run supervised (works immediately)${RESET}"
echo -e "  # Keep terminal open, laptop awake"
echo -e "  python3 ember_continuous_evolution.py --auto --max-generations 5"
echo ""

echo -e "${GREEN}Option 2: Use screen/tmux (survives terminal close)${RESET}"
echo -e "  # Start detached session"
echo -e "  screen -dmS ember python3 ember_continuous_evolution.py --auto --max-generations 20"
echo -e "  # Check on it later"
echo -e "  screen -r ember"
echo ""

echo -e "${GREEN}Option 3: Prevent sleep + run overnight${RESET}"
echo -e "  # Install caffeine"
echo -e "  sudo apt-get install -y caffeine"
echo -e "  # Keep laptop awake"
echo -e "  caffeinate -s &"
echo -e "  # Run evolution"
echo -e "  python3 ember_continuous_evolution.py --auto --max-generations 50"
echo ""

echo -e "${YELLOW}5. Testing current capabilities...${RESET}\n"

# Test if screen is available
if command -v screen &> /dev/null; then
    echo -e "   ${GREEN}✓${RESET} screen is installed (can detach sessions)"
else
    echo -e "   ${RED}✗${RESET} screen not installed"
    echo -e "     ${CYAN}Install with: sudo apt-get install screen${RESET}"
fi

# Test if tmux is available
if command -v tmux &> /dev/null; then
    echo -e "   ${GREEN}✓${RESET} tmux is installed (alternative to screen)"
else
    echo -e "   ${YELLOW}○${RESET} tmux not installed (optional)"
fi

# Test if systemd is available
if command -v systemctl &> /dev/null; then
    echo -e "   ${GREEN}✓${RESET} systemd available (can create service)"
else
    echo -e "   ${RED}✗${RESET} systemd not available"
fi

# Test GPU availability
if nvidia-smi &> /dev/null; then
    echo -e "   ${GREEN}✓${RESET} GPU accessible"
else
    echo -e "   ${RED}✗${RESET} GPU not accessible (Ember won't work)"
fi

echo -e "\n${YELLOW}6. Recommendation:${RESET}\n"

cat << EOF
${BOLD}${CYAN}For this week:${RESET}
Start with supervised autonomous mode. Keep laptop awake and plugged in.
Check on Ember every few hours. This lets you learn how it behaves.

${BOLD}${CYAN}For next week:${RESET}
I can build:
1. Checkpoint/resume system (survives interruptions)
2. systemd service (runs on boot)
3. Better state tracking

${BOLD}${CYAN}For long-term:${RESET}
Consider dedicated hardware if you want true 24/7 evolution:
- Old laptop (keep lid open, prevent sleep)
- Desktop (always on)
- Small server

${BOLD}${YELLOW}Bottom line:${RESET}
"Autonomous" currently means "runs without asking you, but needs laptop awake"
True autonomy (runs through sleep/reboot/crash) requires more work.

${BOLD}${MAGENTA}Want me to build checkpoint/resume system?${RESET}
That would make Ember survive sleep/wake cycles.
EOF

echo -e "\n${BOLD}${GREEN}Test complete!${RESET}\n"
