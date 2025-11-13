#!/bin/bash
# Ember Health Check Script
# Quick verification that all services are running properly

echo "🏥 Ember Health Check"
echo "===================="
echo ""

# Check creation bridge
if lsof -i :8083 | grep -q LISTEN; then
    BRIDGE_PID=$(lsof -t -i:8083)
    CONNECTIONS=$(lsof -i :8083 | grep ESTABLISHED | wc -l)
    echo "✓ Creation Bridge: RUNNING (PID: $BRIDGE_PID)"
    echo "  └─ Active connections: $CONNECTIONS"
else
    echo "✗ Creation Bridge: NOT RUNNING"
fi

echo ""

# Check HTTP server
if lsof -i :8080 | grep -q LISTEN; then
    HTTP_PID=$(lsof -t -i:8080)
    echo "✓ HTTP Server: RUNNING (PID: $HTTP_PID)"
else
    echo "✗ HTTP Server: NOT RUNNING"
fi

echo ""

# Check .env file
if [ -f "/media/palmerschallon/ThePod1/.env" ]; then
    echo "✓ Configuration: .env file present"
else
    echo "✗ Configuration: .env file MISSING"
fi

echo ""

# Check for duplicate processes
DUPLICATES=$(ps aux | grep -E "python3.*ember.*bridge" | grep -v grep | wc -l)
if [ "$DUPLICATES" -eq 1 ]; then
    echo "✓ Process Count: Clean (1 bridge process)"
elif [ "$DUPLICATES" -eq 0 ]; then
    echo "⚠ Process Count: No bridge processes running"
else
    echo "⚠ Process Count: $DUPLICATES processes (cleanup needed)"
fi

echo ""
echo "===================="
