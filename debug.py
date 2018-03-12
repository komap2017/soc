from soc import debug_messages
from playing import get_all_messages
from collections import Counter
from edtext import clean
from more_itertools import unique_everseen
import json

def main():
    messages_json = get_all_messages()
    start = 3 * 1500
    finish = start + 1500
    messages_chunk = messages_json[start:finish]
    messages_text = [el['message'] for el in messages_json]
    # debug_messages(messages_text)
    counted_all = Counter()
    edited_messages = list(unique_everseen([clean(' '.join(el)) for el in messages_text]))
    for message in edited_messages:
        counted_all += Counter(message.split())
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(counted_all, file)
    # interesting = 'должна'
    # last = '''М, 23, Питер. Ищу с кем сходить на Твое имя в эти выходные. А так же с кем до смотреть Апрельскую ложь. Живу на севере Питера  Vk.com/s.slip'''

if __name__ == '__main__':
    main()