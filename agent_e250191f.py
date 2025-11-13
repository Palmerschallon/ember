import matplotlib.pyplot as plt
from wordcloud import WordCloud
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

# Generating word cloud
wordcloud = WordCloud(width = 800, height = 800, background_color ='white').generate_from_frequencies(word_counts)

# Display the word cloud
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis('off')
plt.tight_layout(pad = 0)

plt.show()