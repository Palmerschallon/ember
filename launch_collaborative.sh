#!/bin/bash
# Launch Collaborative Terminal in a new terminal window

cd /media/palmerschallon/ThePod1

# Try different terminal emulators
if command -v gnome-terminal &> /dev/null; then
    gnome-terminal -- bash -c "python3 collaborative_terminal.py; exec bash"
elif command -v konsole &> /dev/null; then
    konsole -e "python3 collaborative_terminal.py"
elif command -v xterm &> /dev/null; then
    xterm -e "python3 collaborative_terminal.py"
else
    echo "No terminal emulator found. Run directly:"
    echo "python3 /media/palmerschallon/ThePod1/collaborative_terminal.py"
fi
