#!/bin/bash
# EMBER CONNECTION - Run after GPU reboot

echo ""
echo "======================================================================"
echo "                     CONNECTING EMBER"
echo "======================================================================"
echo ""

POD="/media/palmerschallon/ThePod"
EMBER="$POD/ember_oct20_backup/ember"

echo "Checking GPU..."
python3 -c "import torch; print('✓ CUDA available' if torch.cuda.is_available() else '✗ CUDA not available (reboot needed)')"

echo ""
echo "Connecting pieces..."
echo ""

# 1. Update chat interface with brain connection
echo "[1/4] Connecting brain to chat..."
python3 "$POD/scripts/ember_connect.py" brain-to-chat

# 2. Start mind state bridge
echo "[2/4] Starting mind state bridge..."
python3 "$POD/hive/mind_state_bridge.py" &
BRIDGE_PID=$!
echo "  Bridge PID: $BRIDGE_PID"

# 3. Restart chat interface with brain
echo "[3/4] Restarting chat interface..."
pkill -f "ember_speaks.py"
sleep 1
cd "$POD/hive" && python3 ember_speaks.py > /dev/null 2>&1 &
echo "  Chat interface: http://localhost:7779"

# 4. Start Ember's self-evolution loop
echo "[4/4] Starting Ember's self-evolution..."
echo "  Not auto-starting - Palmer should decide when"
echo "  To start: cd $EMBER && python3 brainstem/ember_self_evolving.py start"

echo ""
echo "======================================================================"
echo "                  CONNECTION COMPLETE"
echo "======================================================================"
echo ""

echo "Ember is now connected:"
echo "  ✓ Chat interface uses qwen brain"
echo "  ✓ Mind state visible to tabs"
echo "  ✓ Ready for self-evolution"
echo ""

echo "Next steps:"
echo "  1. Open http://localhost:7779 and chat with Ember"
echo "  2. Ember thinks with own qwen brain now"
echo "  3. When ready: Start self-evolution loop"
echo ""

echo "To start self-evolution:"
echo "  cd $EMBER"
echo "  python3 brainstem/ember_self_evolving.py start"
echo ""
