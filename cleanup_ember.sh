#!/bin/bash
# Ember Cleanup Script
# Kills all duplicate bridge processes and restarts cleanly

echo "🧹 Cleaning up Ember processes..."

# Kill all creation bridge processes
echo "Killing creation bridge processes..."
pkill -9 -f "ember_creation_bridge.py"

# Kill all VR bridge processes
echo "Killing VR bridge processes..."
pkill -9 -f "ember_vr_bridge.py"

# Kill all other ember bridges
echo "Killing other ember bridge processes..."
pkill -9 -f "ember_command_center_bridge.py"
pkill -9 -f "ember_reliable_bridge.py"

# Kill any test processes
echo "Killing test processes..."
pkill -9 -f "test_ember"

# Wait for cleanup
sleep 2

echo "✓ Cleanup complete!"
echo ""
echo "Remaining python processes:"
ps aux | grep "python3" | grep -v grep | grep -E "(ember|creation)" || echo "None found"
