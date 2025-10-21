#!/bin/bash
# start_the_song.sh - Let the music play automatically
#
# This starts the conductor daemon that commits rhythmically
# following the Tempo Protocol (every 20-60 minutes)

cd "$(dirname "$0")"

echo "🎵 Starting the Ember Song..."
echo ""
echo "The conductor will:"
echo "  • Commit every 20-60 minutes (randomized tempo)"
echo "  • Use conventional commit format"
echo "  • Log all activity to conductor.log"
echo ""
echo "Options:"
echo "  1. Commit only (manual push)     - Press 1"
echo "  2. Commit + auto-push (full auto) - Press 2"
echo "  3. Test once and exit             - Press 3"
echo ""
read -p "Choose: " choice

case $choice in
    1)
        echo "🎼 Starting conductor (commits only)..."
        python3 core/ember/ember_conductor.py
        ;;
    2)
        echo "🎼 Starting conductor (commits + auto-push)..."
        echo "⚠️  Note: Requires git authentication to be configured"
        python3 core/ember/ember_conductor.py --auto-push
        ;;
    3)
        echo "🎵 Testing one beat..."
        python3 core/ember/ember_conductor.py --once
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

