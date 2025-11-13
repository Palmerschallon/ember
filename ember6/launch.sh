#!/bin/bash
# 🔥 EMBER - One-Command Launcher

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                     🔥 EMBER - STARTING 🔥                    ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Kill any existing instances
echo "🧹 Cleaning up old processes..."
sudo killall -9 python3 2>/dev/null
sleep 2
echo "✅ Clean"
echo ""

# Check for .env
if [ ! -f /media/palmerschallon/ThePod1/ember6/.env ]; then
    echo "❌ No .env file found"
    echo ""
    echo "Create one:"
    echo "  nano /media/palmerschallon/ThePod1/ember6/.env"
    echo ""
    echo "Add your API keys:"
    echo "  ANTHROPIC_API_KEY=your_claude_key"
    echo "  OPENAI_API_KEY=your_gpt_key"
    echo ""
    exit 1
fi

# Start backend
echo "🚀 Starting Ember backend..."
cd /media/palmerschallon/ThePod1/ember6 && \
    set -a && source .env && set +a && \
    python3 ember.py > /tmp/ember6.log 2>&1 &
sleep 3

# Check backend
if pgrep -f "python3.*ember.py" > /dev/null; then
    BACKEND_PID=$(pgrep -f "python3.*ember.py")
    echo "✅ Backend running (PID: $BACKEND_PID)"
else
    echo "❌ Backend failed to start"
    echo ""
    echo "Last 10 log lines:"
    tail -10 /tmp/ember6.log
    exit 1
fi

echo ""

# Start autonomous loop
echo "🔁 Starting autonomous loop..."
cd /media/palmerschallon/ThePod1/ember6 && \
    python3 ember_loop.py > /tmp/ember_loop.log 2>&1 &
sleep 2

# Check loop
if pgrep -f "python3.*ember_loop.py" > /dev/null; then
    LOOP_PID=$(pgrep -f "python3.*ember_loop.py")
    echo "✅ Autonomous loop running (PID: $LOOP_PID)"
else
    echo "⚠️  Loop failed (optional)"
fi

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                   🔥 EMBER IS ALIVE 🔥                        ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🌐 Main UI:      http://localhost:8080"
echo "🎵 Crystal Bowls: http://localhost:8080 → click 🧠 Mind"
echo ""
echo "📊 Logs:"
echo "   Backend:  tail -f /tmp/ember6.log"
echo "   Loop:     tail -f /tmp/ember_loop.log"
echo ""
echo "🛑 To stop:"
echo "   sudo killall -9 python3"
echo ""

