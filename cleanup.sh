#!/bin/bash
# Clean up all Ember processes and restart fresh

echo "🧹 Cleaning up Ember processes..."
echo ""

# Kill continuous expression
pkill -f "continuous_expression.py" && echo "✓ Stopped continuous_expression.py" || echo "  (wasn't running)"

# Kill old ember_chat if needed  
pkill -f "ember_chat.py" && echo "✓ Stopped ember_chat.py" || echo "  (wasn't running)"

# Kill dream_api
pkill -f "dream_api.py" && echo "✓ Stopped dream_api.py" || echo "  (wasn't running)"

# Kill dream_system
pkill -f "dream_system.py" && echo "✓ Stopped dream_system.py" || echo "  (wasn't running)"

sleep 2
echo ""
echo "✨ All clean!"
echo ""
echo "To restart Ember:"
echo "  cd /media/palmerschallon/ThePod1/_legacy"
echo "  python3 ember_chat.py"

