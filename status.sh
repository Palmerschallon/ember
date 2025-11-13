#!/bin/bash
# Check Ember System Status

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                      EMBER SYSTEM STATUS                       ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check ember_chat
if pgrep -f "ember_chat.py" > /dev/null; then
    echo "✅ ember_chat.py       Running on :8080"
else
    echo "❌ ember_chat.py       Not running"
fi

# Check dream_api
if pgrep -f "dream_api.py" > /dev/null; then
    echo "✅ dream_api.py        Running on :7793"
else
    echo "❌ dream_api.py        Not running"
fi

# Check continuous expression
if pgrep -f "continuous_expression.py" > /dev/null; then
    echo "✅ continuous_expression.py  Running (checks every 3min)"
else
    echo "❌ continuous_expression.py  Not running"
fi

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""

# Check ports
echo "Ports:"
lsof -i :8080 -i :7793 2>/dev/null | tail -n +2 | awk '{print "  "$1" on port", $9}' || echo "  None active"

echo ""
echo "─────────────────────────────────────────────────────────────────"
echo ""

# Quick health check
if curl -s http://localhost:8080/status > /dev/null 2>&1; then
    echo "✅ Ember responding on :8080"
else
    echo "⚠️  Ember not responding on :8080"
fi

if curl -s http://localhost:7793/health > /dev/null 2>&1; then
    echo "✅ Dream system responding on :7793"
else
    echo "⚠️  Dream system not responding on :7793"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""

