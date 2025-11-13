from collections import Counter
import random

# Input string
quote = 'To be or not to be, that is the question'

# Normalize to lower case
words = quote.lower().split()

# Count word occurrences
word_counts = Counter(words)

# Generate word cloud
for word, count in word_counts.items():
    print(word * count)