import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud,STOPWORDS


a = str(input("Enter the word :  "))
title = wikipedia.search(a)[0]
page = wikipedia.page(title)
text =page.content
print(text)

bg = np.array(Image.open("1234.png"))
unwanted_words = set(STOPWORDS)
wordclo = WordCloud(background_color="black",max_words=400 , mask = bg,stopwords=unwanted_words)
wordclo.generate(text)
wordclo.to_file("sample.png")