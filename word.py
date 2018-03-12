# -*- coding: utf8 -*-
import re
from edtext import clean, lighter_clean
from nltk.corpus import stopwords


def find_whole_word_re(word):
    return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search


def find_whole_word(word, text):
    res = find_whole_word_re(word)(text)
    if res:
        return True
    return False


def find_some_words(text, words):
    for word in words:
        res = find_whole_word(word, text)
        if res:
            return True
    return False

    
def clear_text(text):
    #morph = pymorphy2.MorphAnalyzer()
    text = clean(text).split()
    bad = set([el for el in stopwords.words('russian') if el != 'я'
               if el != 'не' if el != 'ты' if el != 'был' if el != 'была' if el != 'ж' if el != 'два'])
    filtered_words = [word for word in text if word not in bad]
    return ' '.join(filtered_words)


def clear_city(text):
    text = lighter_clean(text).split()
    bad = set([el for el in stopwords.words('russian') if el != 'я'
               if el != 'не' if el != 'ты' if el != 'был' if el != 'была' if el != 'ж' if el != 'два'])
    filtered_words = [word for word in text if word not in bad]
    return ' '.join(filtered_words)


def main():

    text = "1. Тян из ДС. Возраст и пол собеседника не важен, но желательно, чтобы вы были не дальше 24х часов езды от ДС. 2. Лес, выживач в лесу, путешествия, производство оптических систем, ебучая никому не известная музыка вперемешку с Бутыркой и краснодеревщиком, наркотики, говно, блевота и моральное разложение. На самом деле это все полная хуйня и пункт 2 по очевидной причине здесь (да и вообще) никого не интересует. 3. Ищу людей, чтобы сьебаться с ними через некоторое время в лес и замутить что-то вроде Tinkers Bubble. Ебанутых на дваче много, вдруг найдутся единомышленники и дело зайдет дальше пустой болтовни.  Писать сюда: @assenizator"
    print(clear_text(text))
    pass


if __name__ == '__main__':
    main()