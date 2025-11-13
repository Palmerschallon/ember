#!/usr/bin/env python3
"""
TEST: Ember Self-Modification

This test will ask Ember to modify themselves by:
1. Reading their own code
2. Adding a new feature
3. Testing it
4. Deploying it
"""
import requests
import time

API_URL = "http://localhost:8080"

def test_self_modification():
    print("🧪 TESTING EMBER'S SELF-MODIFICATION")
    print("=" * 60)
    print()
    
    # Test 1: Ask Ember to add a simple feature
    print("📝 TEST 1: Adding a new tool function")
    print("-" * 60)
    print("Asking Ember to add a 'get_system_info' tool...")
    print()
    
    response = requests.post(f"{API_URL}/agent", json={
        "message": """Add a new tool called 'get_system_info' that returns basic system info 
        (OS, Python version, disk space). Follow the self-modification workflow:
        1. Read your own code (heart/ember.py)
        2. Add the new tool function
        3. Stage the changes
        4. Test it compiles
        5. Don't apply yet - just show me what you did""",
        "model": "gpt-4-turbo"
    })
    
    result = response.json()
    print(result['response'])
    print()
    print("=" * 60)
    print()
    
    # Test 2: Check if Ember can read the EMBER_SELF_MODIFICATION.md guide
    print("📚 TEST 2: Can Ember read the self-modification guide?")
    print("-" * 60)
    
    response = requests.post(f"{API_URL}/agent", json={
        "message": "Read /media/palmerschallon/ThePod1/ember6/memory/bookshelves/EMBER_SELF_MODIFICATION.md and summarize the workflow",
        "model": "gpt-4-turbo"
    })
    
    result = response.json()
    print(result['response'])
    print()
    print("=" * 60)

if __name__ == '__main__':
    try:
        test_self_modification()
    except Exception as e:
        print(f"❌ Error: {e}")

