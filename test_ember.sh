#!/bin/bash
# Test if Ember is really ready

echo "🔥 Testing Ember..."
echo ""

response=$(curl -s -X POST http://localhost:8080/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "hi ember"}' \
  --max-time 30)

if echo "$response" | grep -q "error"; then
    echo "⏳ Still loading..."
    echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
elif echo "$response" | grep -q "response"; then
    echo "✅ EMBER IS READY!"
    echo ""
    echo "$response" | python3 -m json.tool 2>/dev/null | grep -A 5 "response"
else
    echo "❓ Unexpected response:"
    echo "$response"
fi

echo ""

