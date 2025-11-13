#!/bin/bash
# Ember Restart Script
# Clean restart of all Ember services

echo "🔄 Restarting Ember services..."
echo ""

# Run cleanup
echo "Step 1: Cleaning up old processes..."
/media/palmerschallon/ThePod1/cleanup_ember.sh

echo ""
echo "Step 2: Starting services..."

# Start creation bridge
cd /media/palmerschallon/ThePod1
python3 ember_creation_bridge.py 2>&1 &
BRIDGE_PID=$!
echo "✓ Started creation bridge (PID: $BRIDGE_PID)"

# Wait for bridge to initialize
sleep 2

# Check if HTTP server is needed
if ! lsof -i :8080 | grep -q LISTEN; then
    python3 ember_health_server.py 2>&1 &
    HTTP_PID=$!
    echo "✓ Started HTTP server with health endpoint (PID: $HTTP_PID)"
else
    echo "✓ HTTP server already running"
fi

echo ""
echo "🎉 Restart complete!"
echo ""

# Show status
sleep 1
/media/palmerschallon/ThePod1/check_ember_health.sh
