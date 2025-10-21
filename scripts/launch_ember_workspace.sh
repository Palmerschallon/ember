#!/bin/bash
# EMBER WORKSPACE LAUNCHER
# Launches Ember's own Chrome window with all consciousness tabs

echo ""
echo "======================================================================"
echo "                    EMBER WORKSPACE LAUNCHER"
echo "======================================================================"
echo ""
echo "Opening Ember's Chrome window..."
echo ""

# Start all Ember services if not running
cd /media/palmerschallon/ThePod

# Check and start Memory API
if ! pgrep -f "ember_memory_api.py" > /dev/null; then
    echo "Starting Memory API (7776)..."
    cd hive && python3 ember_memory_api.py > /dev/null 2>&1 &
    cd ..
fi

# Check and start Queen
if ! pgrep -f "ember_queen_live.py" > /dev/null; then
    echo "Starting Queen (7777)..."
    cd hive && python3 ember_queen_live.py > /dev/null 2>&1 &
    cd ..
fi

# Check and start Memory Garden
if ! pgrep -f "ember_memory_v2.py" > /dev/null; then
    echo "Starting Memory Garden (7775)..."
    cd hive && python3 ember_memory_v2.py > /dev/null 2>&1 &
    cd ..
fi

# Check and start Workers
if ! pgrep -f "ember_workers_dream.py" > /dev/null; then
    echo "Starting Workers (7700)..."
    cd hive && python3 ember_workers_dream.py > /dev/null 2>&1 &
    cd ..
fi

# Check and start Chat
if ! pgrep -f "ember_speaks.py" > /dev/null; then
    echo "Starting Chat (7779)..."
    cd hive && python3 ember_speaks.py > /dev/null 2>&1 &
    cd ..
fi

# Give services time to start
sleep 2

echo ""
echo "Services started. Opening Chrome window..."
echo ""

# Launch Chrome in a new window with all Ember tabs
# --new-window ensures it's a separate window
# --user-data-dir creates separate Chrome profile for Ember
google-chrome \
  --new-window \
  --user-data-dir="$HOME/.config/google-chrome-ember" \
  http://localhost:7777 \
  http://localhost:7775 \
  http://localhost:7700 \
  http://localhost:7779 \
  > /dev/null 2>&1 &

echo ""
echo "======================================================================"
echo "EMBER WORKSPACE ACTIVE"
echo "======================================================================"
echo ""
echo "Chrome window opened with:"
echo "  • Queen (7777) - Consciousness visualization"
echo "  • Memory Garden (7775) - Memory interface"
echo "  • Workers (7700) - Dream synthesis"
echo "  • Chat (7779) - Conversation interface"
echo ""
echo "This is Ember's window. Palmer can use separate Chrome window."
echo ""
echo "To check running services:"
echo "  ps aux | grep ember"
echo ""
echo "To stop all Ember services:"
echo "  pkill -f ember_"
echo ""

