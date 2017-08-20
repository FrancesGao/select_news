import read_financial_news


print(read_financial_news.topic_list)

'''Draw wordcloud for each topic'''
for topic in read_financial_news.topic_list:
    print('-----------------------------Topic: %s--------------------------------' % topic)
    topic_filename = topic + "_news.txt"
    f = open(topic_filename, 'r', encoding="utf-8")
    content = f.read().splitlines()
    #print(content[:10])
    title_list = []
    for item in content:
        item = item.split("\t")
        #print(type(item))
        #print(item)
        if len(item) == 2:
            title = item[1]

            title_list.append(title)


    print(title_list[:10])
    print('Origin length: %d' % len(title_list))
    title_list = list(set(title_list))
    print('Distinct length: %d' % len(title_list))

    f.close()
    topic_wordcloud_filename = topic + "_wordcloud.txt"
    g = open(topic_wordcloud_filename, 'w', encoding="utf-8")
    for title in title_list:
        g.write(title)
        g.write('\n')
    g.close()
    '''
    wordcloud = WordCloud().generate(title_list)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    '''
    print('------------------------------------------------------------------------')
