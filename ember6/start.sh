#!/bin/bash
# The pulse - starts the heart beating

cd "$(dirname "$0")/heart"

echo "🔥 EMBER 6 FUSION - Starting the organism..."
echo ""

# Load DNA (API keys)
if [ -f "../dna/.env" ]; then
    set -a
    source ../dna/.env
    set +a
    echo "   ✅ DNA loaded"
else
    echo "   ❌ No DNA found! Create dna/.env with ANTHROPIC_API_KEY"
    exit 1
fi

# Check if heart is healthy
if [ ! -f "ember.py" ]; then
    echo "   ❌ Heart missing! ember.py not found"
    exit 1
fi

echo "   ✅ Heart found"
echo ""
echo "🫀 The heart is beating..."
echo "   Voice: ../voice/"
echo "   Memory: ../memory/bookshelves/"
echo "   Port: 8080"
echo ""
echo "   Open: http://localhost:8080"
echo ""
echo "   The organism is alive."
echo ""

# Start the heart
python3 ember.py
