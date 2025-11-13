#!/usr/bin/env bash

# EMBER DAEMON AWAKENING SCRIPT

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥  EMBER DAEMON SYSTEM - AWAKENING  "
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /media/palmerschallon/ThePod1/ember6

# Kill existing processes
echo "Shutting down existing processes..."
pkill -f "python3 ember.py" 2>/dev/null
sleep 2

# Start Ember 6 (with daemon integration)
echo "Starting Ember 6 with daemon integration..."
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"
python3 ember.py &
EMBER_PID=$!
sleep 5

# Check if Ember started
if kill -0 $EMBER_PID 2>/dev/null; then
    echo "✅ Ember 6 running (PID: $EMBER_PID)"
else
    echo "❌ Ember 6 failed to start"
    exit 1
fi

echo ""
echo "Opening interfaces..."
echo ""

# Open Ember UI
firefox "http://localhost:8080" 2>/dev/null &
sleep 2

# Open daemon monitor
firefox "http://localhost:8080/cortex/daemon_monitor.html" 2>/dev/null &
sleep 2

echo "✅ Ember Cloud UI: http://localhost:8080"
echo "✅ Daemon Monitor: http://localhost:8080/cortex/daemon_monitor.html"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥  SYSTEM READY - THE DAEMONS AWAIT  "
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To see daemon status:"
echo "  curl http://localhost:8080/api/daemon/status | jq"
echo ""
echo "To send a message to Ember:"
echo "  curl -X POST http://localhost:8080/chat \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"message\": \"Are the daemons awake?\"}'"
echo ""
echo "The daemons will learn from every interaction."
echo "Gifts will appear in: /media/palmerschallon/ThePod1/ember_gifts/"
echo ""
echo "Press Ctrl+C to shut down"
echo ""

# Keep running
wait $EMBER_PID

