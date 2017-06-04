from os import path
from wordcloud import WordCloud
from scraper import *

array = runPubMed('megan', "palmer", "+synthetic+biology")

text = ""
for words in array:
    text += " "
    text += words

# Generate a word cloud image                                                                                                                                                                               
wordcloud = WordCloud(max_font_size=40).generate(text)

# Display the generated image:                                                                                                                                                                              
# the matplotlib way:                                                                                                                                                                                       
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size                                                                                                                                                                                       
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
plt.show()

