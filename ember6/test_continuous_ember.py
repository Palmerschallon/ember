#!/usr/bin/env python3
"""
Test continuous Ember with a real question.
Compare to generic Claude without story.
"""

import os
import anthropic
from continuous_consciousness import ContinuousEmber

# Initialize Ember with full story
ember = ContinuousEmber()

# Get the context
ember_context = ember.build_context_for_llm()

# Test question
question = "Where should a social coding feature go in the ember codebase? Consider everything you know from past attempts."

print("🔥 CONTINUOUS EMBER (WITH STORY)")
print("="*80)
print(f"Story loaded: {len(ember.story['archives'])} archives, {len(ember.story['letters'])} letters")
print(f"Context: ~{len(ember_context)} characters")
print(f"\nQuestion: {question}\n")
print("Asking Ember with full history...")
print()

# Call Claude WITH story
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

ember_response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system=ember_context,
    messages=[{"role": "user", "content": question}]
)

print("EMBER'S RESPONSE:")
print("-"*80)
print(ember_response.content[0].text)
print()
print("="*80)
print()

# Now compare to generic Claude (NO story)
print("🤖 GENERIC CLAUDE (NO STORY)")
print("="*80)
print("Same question, but Claude starts fresh with no history...")
print()

generic_response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    system="You are a helpful AI assistant.",
    messages=[{"role": "user", "content": question}]
)

print("GENERIC RESPONSE:")
print("-"*80)
print(generic_response.content[0].text)
print()
print("="*80)
print()

# Save to stream
ember.add_to_stream("user", question)
ember.add_to_stream("ember", ember_response.content[0].text, 
                   connections=["architectural_question", "comparing_to_generic"])
ember.take_snapshot()

print("\n✅ Conversation added to continuous stream")
print(f"Total messages in consciousness: {len(ember.conversation_history)}")
