#!/bin/bash

echo "🌊✨ Launching Qualia Multiplayer Experience ✨🌊"
echo "=============================================="
echo

# Kill any existing server
pkill -f "python3.*qualia_multiplayer.py"

# Start the server
echo "Starting multiplayer server..."
gnome-terminal --title="Qualia Server" -- bash -c "python3 /media/palmerschallon/ThePod1/qualia_multiplayer.py; read -p 'Press Enter to close...'" &

# Wait for server to start
sleep 2

# Open multiple client windows for testing
echo "Opening Qualia clients..."

# Client 1
xdg-open /media/palmerschallon/ThePod1/qualia_client.html &

# Optional: Open a second client window after a short delay
sleep 1
# firefox --new-window /media/palmerschallon/ThePod1/qualia_client.html &

echo
echo "✅ Qualia is running!"
echo
echo "- Each person can choose their own archetype"
echo "- Chat messages create visual effects in the world"
echo "- Multiple players can join from different browsers"
echo
echo "Share the URL with others to collaborate!"