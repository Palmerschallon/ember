#!/bin/bash

echo "🌊 Starting Qualia Game 🌊"
echo "========================="
echo

# Make sure the game is executable
chmod +x /media/palmerschallon/ThePod1/qualia_game.py

# Launch the visualizer in background
echo "Opening visualizer..."
xdg-open /media/palmerschallon/ThePod1/qualia_visualizer.html &

# Wait a moment
sleep 1

# Launch the game
echo "Starting game..."
echo
python3 /media/palmerschallon/ThePod1/qualia_game.py

echo
echo "Thanks for playing!"