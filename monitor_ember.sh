#!/bin/bash
# Ember Monitor Script
# Real-time monitoring of Ember services

echo "📊 Ember Monitor - Press Ctrl+C to exit"
echo "========================================"
echo ""

while true; do
    clear
    echo "📊 Ember Real-Time Monitor"
    echo "========================================"
    echo "Updated: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""

    # Creation Bridge Stats
    if lsof -i :8083 | grep -q LISTEN; then
        BRIDGE_PID=$(lsof -t -i:8083)
        CONNECTIONS=$(lsof -i :8083 | grep ESTABLISHED | wc -l)
        MEMORY=$(ps -p $BRIDGE_PID -o rss= | awk '{print int($1/1024)"MB"}')
        CPU=$(ps -p $BRIDGE_PID -o %cpu= | awk '{print $1"%"}')

        echo "🔥 Creation Bridge (PID: $BRIDGE_PID)"
        echo "   Status: RUNNING"
        echo "   Active Connections: $CONNECTIONS"
        echo "   Memory: $MEMORY"
        echo "   CPU: $CPU"
    else
        echo "🔥 Creation Bridge"
        echo "   Status: NOT RUNNING ❌"
    fi

    echo ""

    # HTTP Server Stats
    if lsof -i :8080 | grep -q LISTEN; then
        HTTP_PID=$(lsof -t -i:8080)
        HTTP_MEMORY=$(ps -p $HTTP_PID -o rss= | awk '{print int($1/1024)"MB"}')
        HTTP_CPU=$(ps -p $HTTP_PID -o %cpu= | awk '{print $1"%"}')

        echo "🌐 HTTP Server (PID: $HTTP_PID)"
        echo "   Status: RUNNING"
        echo "   Memory: $HTTP_MEMORY"
        echo "   CPU: $HTTP_CPU"
    else
        echo "🌐 HTTP Server"
        echo "   Status: NOT RUNNING ❌"
    fi

    echo ""
    echo "========================================"
    echo "Press Ctrl+C to exit"

    sleep 3
done
