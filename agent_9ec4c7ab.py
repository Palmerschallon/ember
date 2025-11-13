import matplotlib.pyplot as plt
from collections import Counter
import re

# Text from BOOTSTRAP.md
content = '''# EMBER BOOTSTRAP
*This file is loaded first. Everything cascades from here.*
...'''

# List of common words to be removed
common_words = {'the', 'is', 'and', 'a', 'this', 'you', 'are', 'to', 'it', 'in', 'of', 'for', 'with', 'not', 'on', 'that', 'as', 'or', 'but', 'can', 'be', 'do', 'does', 'at', 'an', 'if', 'each', 'all', 'from', 'have', 'by', 'when', 'will', 'what', 'we', 'how', 'i', 'your', 'they', 'their', 'them', 'these', 'there', 'so', 'some', 'has', 'just', 'its', 'which', 'about', 'into', 'no', 'was', 'were', 'who', 'any', 'like', 'other'}

# Preprocessing the text
text = re.sub('[^\w\s]','', content.lower())
words = text.split()
filtered_words = [word for word in words if word not in common_words]

# Counting word frequencies
word_counts = Counter(filtered_words)

# Getting the 10 most common words and their counts
common_words = word_counts.most_common(10)
words = [word[0] for word in common_words]
counts = [word[1] for word in common_words]

# Creating the bar chart
plt.figure(figsize=(10,5))
plt.bar(words, counts, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Words in BOOTSTRAP.md')
plt.show()