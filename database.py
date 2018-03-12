import sqlite3
from soc import check_phrase_for_city, check_phrase_for_girl
from more_itertools import unique_everseen
import pandas as pd
import re


def debug():
    conn = sqlite3.connect(r'C:\Users\nikit\socscrap\scrapedata.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT TEXT from posts ORDER BY post_id DESC')
    res = cursor.fetchall()
    start = 0 + 100 * 107
    alphabet = 'а б в г д е ё ж з и к л м н о п р с т у ф х ц ш щ ъ ы ь э ю я'.split(' ')
    alphabet = set(alphabet)
    last_one = 'ДС, 28, М. Тян от 25, для рилейшенс.  Тг @InfiniteLemons'
    res = list(unique_everseen(res))
    for el in res[start:start + 100]:
        blacklist = ['@tghex']
        if all(name not in el[0] for name in blacklist):
            if any(sign in el[0] for sign in alphabet):
                print(str(el[0]).strip())
                print('Проверка города - {}'.format(check_phrase_for_city(str(el[0]).strip())))
                print('Проверка пола - {}'.format(check_phrase_for_girl(str(el[0]).strip())))
                print('--------------------------------------------------------------'
                      '---------------------------------------------------------------'
                      '--------------------------------------------------')
    print('Выводятся сообщения с {} по {}'.format(start, start + 100))


def get_messages(num_of_messages):
    conn = sqlite3.connect(r'C:\Users\nikit\socscrap\scrapedata.sqlite')
    cursor = conn.cursor()
    command = 'SELECT TEXT from posts ORDER BY post_id DESC LIMIT'
    command += ' {}'.format(str(num_of_messages))
    cursor.execute(command)
    res = cursor.fetchall()
    res = [clean(el[0]) for el in res]

    return res


def get_all_messages_and_save(path):
    conn = sqlite3.connect(r'C:\Users\nikit\socscrap\scrapedata.sqlite')
    cursor = conn.cursor()
    command = 'SELECT TEXT from posts ORDER BY post_id DESC'
    cursor.execute(command)
    res = cursor.fetchall()
    res = [clean(el[0]) for el in res]
    if '.csv' not in path:
        path += '.csv'
    check = check_messages(res)
    df = lists_to_dataframe('Сообщение Пол'.split(), res, check)
    # print(df)
    if '.csv' not in path:
        path += '.csv'
    df.to_csv(path, index=False, encoding='utf-8')


def clean(string):
    return re.sub('\W+',' ', string )


def check_messages(messages):
    return [check_phrase_for_girl(el.strip()) for el in messages]


def lists_to_dataframe(names, *args):
    lst1 = ['какая']
    lst2 = ['то']
    lst3 = ['инфа']
    merged = {key:value for key, value in zip(names, args)}
    dataframe = pd.DataFrame(merged)
    # print(dataframe)
    return dataframe


def read_csv(path='genders.csv'):
    return pd.read_csv(path)


def get_messages_and_save(number_of_messages, path):
    messages = get_messages(number_of_messages)
    check = check_messages(messages)
    df = lists_to_dataframe('Сообщение Пол'.split(), messages, check)
    print(df)
    if '.csv' not in path:
        path += '.csv'
    df.to_csv(path, index=False, encoding='utf-8')


def main():
    # debug()
    pass
    get_all_messages_and_save('newgenders')
    # print(get_messages(1))
    # get_messages_and_save(1000, r'C:\Users\nikit\OneDrive\Рабочий стол\Codding\Python\tv\predictor\genders.csv')
    # df = pd.read_csv('genders.csv')
    # print(df)



if __name__ == '__main__':
    main()
