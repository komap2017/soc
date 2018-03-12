import json_lines
import json
from collections import Counter
import pymorphy2
from soc import girls_word
from nltk.corpus import stopwords


def converter():
    file = r'C:\Users\nikit\socscrap\messages_take3.jsonlines'
    res = []
    with open(file, encoding='utf-8') as file:
        for item in json_lines.reader(file, broken=True):
            res.append(item)
    with open('all_messages.json', 'w', encoding='utf-8') as file:
            json.dump(res, file)


def get_all_messages():
    with open('all_messages.json', encoding='utf-8') as file:
        res = json.load(file)
    return res


def get_fem_words():
    words = []
    with open('result.json', encoding='utf-8') as file:
        res = Counter(json.load(file))
    morph = pymorphy2.MorphAnalyzer()
    girls = [el.lower() for el in girls_word()]
    for word, count in res.most_common():
        word_type = morph.parse(word)[0].tag.POS
        analize =  morph.parse(word)[0].tag.gender
        if analize == 'femn' and (word_type == 'VERB' or word_type == 'INFN') and word.lower() not in girls:
            #print('{} - {} - {}'.format(word, count, analize))
            words.append((word, count, analize))
    return words


def main():
    get_counter()


def get_counter():
    with open('result.json', encoding='utf-8') as file:
        res = Counter(json.load(file))
    #morph = pymorphy2.MorphAnalyzer()
    stop = [el for el in stopwords.words('russian')]
    stop.extend([str(i) for i in range(1000)])
    stop = set(stop)
    for key, count in res.most_common():
        #word_type = morph.parse(key)[0].tag.POS
        if count > 1000 and key not in stop:
            print('{} - {}'.format(key, count))


if __name__ == '__main__':
    #converter()
    main()

