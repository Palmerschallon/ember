from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of beautiful words
words = 'Euphoria, Love, Serenity, Hope, Peace, Kindness, Happiness, Harmony, Tranquility, Dream'

# Create a word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(words)

# Plot the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

plt.show()