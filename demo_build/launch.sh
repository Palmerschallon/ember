#!/bin/bash
# DEMO LAUNCHER - One command to start everything

echo "🔥 PHOENIX DEMO - Starting..."
echo ""

# Kill any existing demo servers
pkill -f "python3.*demo_build/server.py" 2>/dev/null
pkill -f "python3.*phoenix_demo_server.py" 2>/dev/null

# Start demo server
cd /media/palmerschallon/ThePod1/demo_build
python3 server.py > /tmp/demo_server.log 2>&1 &
SERVER_PID=$!

sleep 3

# Check if server started
if ps -p $SERVER_PID > /dev/null; then
    echo "✅ Demo server running (PID: $SERVER_PID)"
    echo "✅ http://localhost:6000"
    echo ""
    echo "Opening in Firefox..."
    firefox http://localhost:6000 &
    echo ""
    echo "🔥 DEMO IS LIVE"
    echo ""
    echo "To stop: kill $SERVER_PID"
else
    echo "❌ Server failed to start"
    echo "Check: /tmp/demo_server.log"
    exit 1
fi

