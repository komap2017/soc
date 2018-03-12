# -*- coding: utf8 -*-
import re
import string

def clean(string):  # From Vinko's solution, with fix.
    return re.sub('\W+',' ', string.lower())
    #return regex.sub('', string.lower())


def lighter_clean(string_to_clear):
    symbols = set(string.punctuation)
    symbols.remove('.')
    symbols.remove(',')
    for char in symbols:
        string_to_clear = string_to_clear.replace(char, ' ')
    string_to_clear = ''.join([i for i in string_to_clear
                               if not i.isdigit() or i == '2' or i == '3'])
    return string_to_clear

def main():
    text = "1. Тян из ДС. Возраст и пол собеседника не важен, но желательно, чтобы вы были не дальше 24х часов езды от ДС. 2. Лес, выживач в лесу, путешествия, производство оптических систем, ебучая никому не известная музыка вперемешку с Бутыркой и краснодеревщиком, наркотики, говно, блевота и моральное разложение. На самом деле это все полная хуйня и пункт 2 по очевидной причине здесь (да и вообще) никого не интересует. 3. Ищу людей, чтобы сьебаться с ними через некоторое время в лес и замутить что-то вроде Tinkers Bubble. Ебанутых на дваче много, вдруг найдутся единомышленники и дело зайдет дальше пустой болтовни.  Писать сюда: @assenizator"
    print(repr(text))
    print(repr(lighter_clean(text)))


if __name__ == "__main__":
    main()


