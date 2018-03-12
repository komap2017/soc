from playing import get_all_messages
from soc import girls_word, check_phrase_for_girl
from more_itertools import unique_everseen
from word import find_whole_word


def output(messages_text, word):
    for el in messages_text:
        text = el[0]
        if find_whole_word(word.lower(), text):
            print(text)
            print(check_phrase_for_girl(text))
            print('--------------------------------------------------------------'
                  '---------------------------------------------------------------'
                  '-------------------------------------------------')


def get_messages_with_word_in_it(word):
    messages_json = get_all_messages()
    messages_text = [el['message'] for el in messages_json]
    # word = 'тян'
    words = girls_word()
    words = [el.lower() for el in words]
    strict = False
    if word in words and strict:
        raise ValueError('The word "{}" is alredy in the catch list!'.format(word))
    #chunk = [el for el in messages_text if word in ' '.join(el).lower()]
    #chunk = unique_everseen(chunk)
    messages_text = list(unique_everseen(messages_text))
    # TODO More unittests! Begin with line below. Read from file test_results.json.
    """Прикольная тут у вас сосисочная вечеринка получилась. Как и на СЗ в моём городе. На 10 ребят одна девчёнка.
    True
    получилась"""
    # length = 117499
    start = 0
    output(messages_text, word)


def main():
    get_messages_with_word_in_it('куна')



if __name__ == '__main__':
    main()