import wordcloud
import os
import glob

def generate_pattern(topic):
    return '*' + topic + '.txt'


topic_list = ['Deals', 'Finance', 'Market News', 'Top News']
financial_news_path = 'C:/Users/StationA/PycharmProjects/select_news/financial_related_news/'


if __name__ == '__main__':
    print(glob.glob(os.path.join(financial_news_path,'*Deals.txt')))

    string_pattern_list = [generate_pattern(topic) for topic in topic_list]

    for topic in topic_list:
        all_financial_news = []
        print('------------------------------------------------------------------------------------------------------------------------')
        string_pattern = generate_pattern(topic)
        print(string_pattern)
        for filename in glob.glob(os.path.join(financial_news_path, string_pattern)):
            try:
                print('======')
                f = open(filename, 'r', encoding='utf-8')
                content = f.read().splitlines()
            except:
                print('filename: ' + filename)
                print('non-utf8 encoding')
            else:
                print('filename: ' + filename)
                print('Read %d lines.' % len(content))
                all_financial_news.append(content)
            finally:
                f.close()
                print('======')

        news_flat_list = [item for sublist in all_financial_news for item in sublist]

        output_filename = topic + '_news.txt'
        print(output_filename)
        print('Total %d lines.' % len(news_flat_list))
        print('------------------------------------------------------------------------------------------------------------------------')

        g = open(output_filename, 'w', encoding='utf-8')
        for line in news_flat_list:
            g.write(line)
            g.write('\n')
        g.close()

        '''
        g = open('news_flat_list.txt', 'w', encoding='utf-8')
        for line in news_flat_list:
            g.write(line)
            g.write('\n')
        g.close()
        '''