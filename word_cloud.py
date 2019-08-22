"""
Python script to generate word cloud image.
Author - Anurag Rana
Read more on - https://www.pythoncircle.com
"""

from wordcloud import WordCloud

# image configurations
background_color = "#101010"
height = 720
width = 1080

with open("stopwords.txt", "r") as f:
    stop_words = f.read().split()

# Read a text file and calculate frequency of words in it
with open("/tmp/sample_text.txt", "r") as f:
    words = f.read().split()

data = dict()

for word in words:
    word = word.lower()
    if word in stop_words:
        continue

    data[word] = data.get(word, 0) + 1

word_cloud = WordCloud(
    background_color=background_color,
    width=width,
    height=height
)

word_cloud.generate_from_frequencies(data)
word_cloud.to_file('image.png')
