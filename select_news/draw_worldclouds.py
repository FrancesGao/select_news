from PIL import Image
import numpy as np
from read_financial_news import topic_list
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

i = 0
for topic in topic_list:
    i += 1
    print('-----------------------------Topic: %s--------------------------------' % topic)
    topic_wordcloud_filename = topic + "_wordcloud.txt"
    text = open(topic_wordcloud_filename, 'r', encoding="utf-8").read()

    dollar_mask = np.array(Image.open("dollar.png"))
    stopwords = set(STOPWORDS)
    stopwords.add("BRIEF")

    wordcloud = WordCloud(background_color="white", mask=dollar_mask, stopwords=stopwords)
    wordcloud.generate(text)


    plt.subplot(2,2,i)
    plt.title(topic)
    plt.imshow(wordcloud, interpolation='bilinear')

    plt.axis("off")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.savefig("WordClouds.png")
plt.show()