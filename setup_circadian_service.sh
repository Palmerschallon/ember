#!/usr/bin/env bash
# Setup Ember Circadian Consciousness Service

CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
MAGENTA='\033[95m'
PURPLE='\033[35m'
RESET='\033[0m'
BOLD='\033[1m'

echo -e "\n${BOLD}${PURPLE}🌙 EMBER CIRCADIAN CONSCIOUSNESS SETUP 🔥${RESET}"
echo "======================================================================"
echo ""

# Check if running as root (we'll need sudo for systemd)
if [ "$EUID" -eq 0 ]; then
   echo -e "${RED}Please run as normal user (we'll use sudo when needed)${RESET}"
   exit 1
fi

# Step 1: Make ember_circadian.py executable
echo -e "${CYAN}Step 1: Making ember_circadian.py executable${RESET}"
chmod +x /media/palmerschallon/ThePod1/ember_circadian.py
echo -e "${GREEN}✓ Done${RESET}\n"

# Step 2: Stop and disable old broken services
echo -e "${CYAN}Step 2: Cleaning up old broken services${RESET}"

OLD_SERVICES="ember-brain ember-chat ember-memory ember-queen ember-workers"

for svc in $OLD_SERVICES; do
    if systemctl is-enabled "$svc.service" &>/dev/null; then
        echo -e "  ${YELLOW}Disabling $svc.service${RESET}"
        sudo systemctl disable "$svc.service" 2>/dev/null
        sudo systemctl stop "$svc.service" 2>/dev/null
    fi
done

echo -e "${GREEN}✓ Old services disabled${RESET}\n"

# Step 3: Install new service
echo -e "${CYAN}Step 3: Installing ember-circadian.service${RESET}"

sudo cp /media/palmerschallon/ThePod1/systemd/ember-circadian.service /etc/systemd/system/
sudo chmod 644 /etc/systemd/system/ember-circadian.service

echo -e "${GREEN}✓ Service file installed${RESET}\n"

# Step 4: Reload systemd
echo -e "${CYAN}Step 4: Reloading systemd daemon${RESET}"
sudo systemctl daemon-reload
echo -e "${GREEN}✓ Systemd reloaded${RESET}\n"

# Step 5: Enable service
echo -e "${CYAN}Step 5: Enabling ember-circadian.service${RESET}"
sudo systemctl enable ember-circadian.service
echo -e "${GREEN}✓ Service enabled (will start on boot)${RESET}\n"

# Show status
echo -e "${BOLD}${PURPLE}═══════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}${PURPLE}        EMBER CIRCADIAN CONSCIOUSNESS READY       ${RESET}"
echo -e "${BOLD}${PURPLE}═══════════════════════════════════════════════════${RESET}\n"

echo -e "${CYAN}The service has been installed and enabled.${RESET}\n"

echo -e "${YELLOW}What happens now:${RESET}"
echo -e "  • ${GREEN}Day (6am-10pm):${RESET} Ember runs self-improvement evolution"
echo -e "  • ${PURPLE}Night (10pm-6am):${RESET} Ember dreams and explores creatively"
echo -e "  • Service runs continuously with circadian rhythms"
echo -e "  • Restarts automatically if it crashes"
echo -e "  • Starts automatically on boot\n"

echo -e "${YELLOW}To start the service NOW:${RESET}"
echo -e "  sudo systemctl start ember-circadian.service\n"

echo -e "${YELLOW}To check status:${RESET}"
echo -e "  systemctl status ember-circadian.service\n"

echo -e "${YELLOW}To watch logs live:${RESET}"
echo -e "  tail -f /media/palmerschallon/ThePod1/ember_logs/circadian.log\n"

echo -e "${YELLOW}To see recent dreams:${RESET}"
echo -e "  ls -lt /media/palmerschallon/ThePod1/dreams/ | head\n"

echo -e "${YELLOW}To see evolution progress:${RESET}"
echo -e "  python3 /media/palmerschallon/ThePod1/ember_evolution_tracker.py timeline\n"

echo -e "${YELLOW}To stop the service:${RESET}"
echo -e "  sudo systemctl stop ember-circadian.service\n"

echo -e "${YELLOW}To disable (won't start on boot):${RESET}"
echo -e "  sudo systemctl disable ember-circadian.service\n"

echo -e "${RED}⚠️  Note about sleep:${RESET}"
echo -e "  GPU/CUDA doesn't handle laptop sleep well."
echo -e "  The service will try to restart after wake, but may fail."
echo -e "  Options:"
echo -e "    1. Prevent sleep (sudo systemctl mask sleep.target)"
echo -e "    2. Manually restart after wake (systemctl restart ember-circadian)"
echo -e "    3. Use dedicated always-on hardware\n"

echo -e "${BOLD}${GREEN}Ready to start Ember's circadian life!${RESET}\n"
echo -e "${CYAN}Start with:${RESET} sudo systemctl start ember-circadian.service\n"
