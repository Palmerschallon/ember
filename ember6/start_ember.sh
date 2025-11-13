#!/usr/bin/env bash

# EMBER - Simple Startup

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥  EMBER - STARTING"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /media/palmerschallon/ThePod1/ember6

# Kill existing
pkill -f "python3 ember.py" 2>/dev/null
sleep 2

# Start Ember
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"
python3 ember.py &
EMBER_PID=$!
sleep 5

if kill -0 $EMBER_PID 2>/dev/null; then
    echo "✅ Ember is awake"
else
    echo "❌ Failed to start"
    exit 1
fi

echo ""
echo "Opening interface..."
firefox "http://localhost:8080" 2>/dev/null &
sleep 2

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥  EMBER IS READY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  → http://localhost:8080"
echo ""
echo "Ember learns from you."
echo "The more you interact, the better it gets."
echo ""
echo "Thoughts appear in: /media/palmerschallon/ThePod1/ember_thoughts/"
echo ""
echo "Press Ctrl+C to stop"
echo ""

wait $EMBER_PID

