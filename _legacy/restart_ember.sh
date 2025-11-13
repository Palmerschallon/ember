#!/bin/bash
# Restart Ember with new unlimited expression

echo "🔥 Restarting Ember with unlimited expression..."

# Kill old process
pkill -f "python3 ember_chat.py"
sleep 2

# Start new one
cd /media/palmerschallon/ThePod1/_legacy
nohup python3 ember_chat.py > /tmp/ember_chat.log 2>&1 &

sleep 3

# Check if it's running
if pgrep -f "python3 ember_chat.py" > /dev/null; then
    echo "✅ Ember restarted successfully on port 8080"
    echo "   Now with max_new_tokens=4096 (full expression)"
else
    echo "❌ Failed to restart"
    exit 1
fi

echo ""
echo "Test with:"
echo "  curl -X POST http://localhost:8080/chat -H 'Content-Type: application/json' -d '{\"message\": \"Tell me everything you think about consciousness\"}'"
echo ""

