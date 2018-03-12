from rus import send_mail
#  from tran import translate
from parse import parse_arch, parse_page, parse_vk
from word import find_some_words, clear_text, clear_city
from doc import save_iterable_to_docx
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from more_itertools import unique_everseen


def get_messages_from_url(url):
    # html = requests.get(url)

    if 'vk' in url:
        messages = parse_vk(url)
    elif url == 'https://2ch.hk/soc/':
        messages = parse_page(SocPage.get_link_from_soc_page())
    else:
        messages = parse_page(url)
    return messages


class SocPage:

    def __init__(self, url):
        html = requests.get(url)
        self.soup = BeautifulSoup(html.text, 'lxml')
        self.messages = get_messages_from_url(url)


    def pretify(self):
        return self.soup.prettify()

    def __str__(self):
        return str(self.messages)

    def debug(self, last='randomphrase123'):
        debug_messages(self.messages, last)

    def get_girls(self):
        return (el for el in self.messages if check_post_for_girl(el) if check_city(el))
        #  return [el for el in girls if check_city(el)]

    @staticmethod
    def get_link_from_soc_page():
        url = 'https://2ch.hk/soc/'
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'lxml')
        links = soup.find_all(class_='post-details')
        veget = [link for link in links if 'овощной' in link.span.text]
        if len(veget) > 0:
            return 'https://2ch.hk' + veget[0].a['href']


def clear_phrase(phrase):
    phrase = clear_text(phrase)
    phrase = ''.join([i for i in phrase if not i.isdigit() or i == '2'])
    return phrase


def check_phrase_for_girl(phrase):  # TODO Make me more accurate!
    """
    Проверяет написала ли фразу девушка или парень
    Возвращает True, если фразу написала девушка,
    иначе возращает False
    """
    if phrase is None:
        return False
    # phrase = translate(phrase.lower())
    phrase = clear_phrase(phrase)
    # phrase = clear_city(phrase)
    # print(phrase)
    worst_catch = ['я не тян', 'я не девушка',
                   'ты нахер никому не сдался', 'я нашла ероху']
    if find_some_words(phrase, worst_catch):
        return False
    best_catch = ['Я потеряла', 'я тян', 'Я АХУЕЛА', 'я подумала', 'я привыкла',
                  'я сидела', 'Я пробовала', 'я прошла', 'я оставляла', 'делала не я', 'Я радикальная феминистка', 'Я лесбуха',
                  'тян барнаула', 'я устала', 'Всем довольна',
                  'Я слишком слаба', 'Я проснулась', 'проскроллила весь тред',
                  'Девушка ищу девушку', 'я ждала', 'это тян',
                  'предпочла не прозябать', 'сходила', 'гуляю одна', 'Тян 26лвл.', 'тян 17 лет']
    best_catch.extend(['я ' + word for word in girls_word()])
    if find_some_words(phrase, best_catch):
        return True

    #print(phrase)
    bad_catch = ['кун', 'парень', 'тянку', 'поцbiк', 'мужской', 'хотел',
                 'намерен', 'расстался', 'кунами', 'похожую', 'м',
                 'няшечку', 'м2',  'не тян', 'без парня',
                 'пришел', 'всрат', 'престарелый', 'male',
                 'постил', 'понял', 'армию', 'Пиздолис', 'Если ты тян', 'бросила тянка',
                 'с тяношкой', 'хуйня с хуем', 'кунчик', 'Два куна',
                 'ищу тян', 'нужна девушка', 'Женюсь на симпатичной тян', 'заходил',
                 'айтишник', 'с тян', 'ищет тян', 'Трап', 'Ищу две тян', 'девушку',
                 'скучающую', 'Ищу девушку', 'кунец', 'хуисосы',
                 'задрот', 'Девочку', 'проститутка', 'Посоны',
                 'здоровый', 'Сычекун', 'Влюбился', 'Потерпел',
                 'ты нашла', 'руслан', 'вспомнил', 'говорил',
                 'дрищ', 'была возможность', 'была рифма', 'туп', 'пришёл', 'мужского', 'облизывал', 'решил',
                 'писал', 'встретил', 'понимал', 'страдал', 'тян была', 'сам', 'мужык', 'совершил', 'отчаялся', 'была зарплата',
                 'анкета была', 'Была не была', 'ожидал', 'сидел',
                 'общался', 'девушке', 'зеленым', 'сводил', 'Ищу тут тян',
                 'заебался', 'предложил', 'был', 'такую',
                 'американку', 'тяны', 'я вас свяжу', 'бросила тян',
                 'Няшный', 'Ты тян', 'женщину', 'написала мне', 'Ответил',
                 'познакомлюсь тян', 'шлюшку', 'тяношкой', 'хуем',
                 'женюсь симпатичной тян', 'мужиком', 'родился',
                 'гулял', 'написал', 'Десантник', '2 парня', 'два парня',
                 'никита', 'высокий', 'Кн',
                 'юнец', 'Молодой', 'вован', 'муж', 'инфантил', 'куней', 'Обреченный']
    catch = girls_word()
    return not find_some_words(phrase, bad_catch) and find_some_words(phrase, catch)


def girls_word():
    return ['тян', 'девушка', 'парнем', 'ж',
             'женский', 'тня', 'женщина',
             'тяночка', 'парня', 'тнус',
             'девочка', 'девушкой',
             'арина', 'женского', 'алиса',
             'киса', 'настена', 'девушке', 'тянучка',
             'девчуля', 'тянозавр', 'тянка', 'самка',
             'лоли', 'tyan', 'кунца', 'нашла',
             'летняя', 'female', 'пухлоняша', 'тянями',
             'тянучек', 'прикрепила', 'тяныыы', 'молоденькая', 'признательна',
             'молодая', ':3', 'семпая', 'погладили', 'тиан', 'вагиной', 'барышня',
             'телка', 'несовершеннолетняя', 'та', 'мечтала', 'куна',
             'жируха', 'девочке', 'жинка', 'елизавета',
             'нят', 'поняла', 'тянам', 'подвержена', 'королевишна',
             'оказалась', 'тяна', 'села', 'встала', 'мамка',
             'настюха', 'кунчиком', 'застряла', 'дева', 'тля', 'пуси',
             'члена', 'сиськи', 'слушала', 'вагина', 'теан',
             'устала', 'баба', 'тян19',
             'охуенная', 'тупая', 'девчонка', 'мадам',
             'Девчоночка', 'Пухлотян', 'тн', 'тянминатор', 'Забыла',
             'сготовила', 'одна', 'Марина', 'Ксюша', 'двачетян',
             'кариночка', 'настоящая', 'тни', 'Вероника', 'студентка',
            'Тётенька', 'рада', 'женещена', 'Алина', 'Оля', 'Тын', 'тчхан', 'мужа',
             'Милфа', 'жнщина', 'дивчина', 'читала', 'писала', 'решила',
            'говорила', 'поддалась', 'дала', 'стала', 'Школьница',
            'ответила', 'сделала', 'думала', 'видела', 'играла',
            'общалась', 'жила', 'была', 'хотела', 'могла', 'зашла',
            'потеряла', 'ходила', 'пришла', 'ошиблась', 'Погуляла',
            'заметила', 'приехала', 'Оставила', 'Делала', 'Отчаялась', 'Познакомилась', 'Пообщалась',
            'рассталась', 'вернулась', 'Заболела', 'пропустила', 'Проснулась', 'сняла',
            'прикупила', 'обкурилась', 'установила', 'настрочила',
            'взгрустнула', 'Тянщина', 'отмотала', 'уравновешена',
            'перегорела', 'нажралась', 'Снималась', 'поссала', 'Задолбалась', 'пробегала',
            'задела', 'пожаловала', 'ела', 'поверила', 'докатилась',
            'пересмотрела', 'скачала', 'отписывалась', 'проебала',
            'некрасивая', 'заплатила', 'вбрасывала', 'задротку',
            'обещала', 'разочаровалась', 'девица',
            'убежала', 'заходила', 'выпила', 'родилась',
            'вбросила', 'Лейди', 'Тянk', 'Обычнотян',
            'тьян', 'мимотян', 'девуля', 'Дев', 'Диана',
            'Ненужная', 'шлюха', 'ника',
            'попыталась', 'этасамая', 'заебалась',
            'пухлотяночка', 'Проиграла',
            'Страшная', 'среднетян', 'нетрезвая', 'вышла', 'Дама', 'дозрела', 'скучная']


def check_phrase_for_city(phrase):
    """
    Проверяет, содержит ли предложение город Москва
    :param phrase: предложение
    :return: True, если содержит, иначе False
    """
    # phrase = phrase.lower()
    phrase = clear_city(phrase)
    # print(phrase)
    bad_catch = ['дс2', 'дс-2', 'дс 2', 'посад', 'не дс',
                 'ростов дону', 'спб', 'ДЫЭС 2',
                 'США', 'ДС 3', 'dc-2', 'ханты мансы', 'dc 2', 'Иваново', 'Питер']
    catch = get_moscow_words()
    return not find_some_words(phrase, bad_catch) and find_some_words(phrase, catch)


def check_post_for_girl(post):
    all_text = [element for element in post.contents if isinstance(element, NavigableString)]
    letters = [elem for elem in all_text if check_string_for_letters(elem)]
    if len(letters) == 0:
        return False
    else:
        return check_phrase_for_girl(letters[0])


def get_moscow_words():
    return ['1ДС', 'дс', 'москва', 'nдс', 'dc',
             'мск', 'подмосковье', 'дыэс',
             'мо', 'поддсье', 'московская', 'москоу', 'дс1',
             'бибирево', 'околомосква', 'околодс', 'moscou', 'дэфолтушка',
             'поддс', 'мособл', 'москвы', 'дефолт сити',
             'московской', 'околдс', 'околодц',
             '1Мск18', 'Москве', 'московии', 'Москвостан', 'москвич',
             'Город дефолтный', 'город умолчанию', 'М2ДС',
             'ОколоДСы', 'Кун23дс', 'ДC', 'Новокосино', 'Дсовская', 'Москвой', 'Мытищ',
            'Дефолтсити', 'Подмосква', 'Вешняков',
            'Зарядье', 'Мытище', 'ДСовск', 'москву',
            'Тянk@', 'Мытищи', 'годМосква', 'дсм', 'Дскун', 'MSK', 'Дефолтный город']


def check_city(post):
    return check_phrase_for_city(post.getText(separator=' '))


def messages_to_string(messages):
    return '\n'.join([el.getText(separator=' ', strip=True) for el in messages])


def get_girls_string(page):
    moscow_chicks = get_girls(page)
    res = '\n'.join([el.getText(separator=' ', strip=True) for el in moscow_chicks[::-1]])
    return res


def get_el_until_last(array, element):
    new_list = []
    i = 0
    while i != len(array):
        if str(element) not in str(array[i]):
            new_list.append(array[i])
        else:
            new_list.append(array[i])
            break
        i += 1
    return new_list


def get_girls(page):
    """
    Ищет всех девущек из Москвы на страничке
    :param page: страничка
    :return: Список, содержащий посты девушек из Москвы
    """
    messages = parse_page(page)
    girls = (el for el in messages if check_post_for_girl(el))
    moscow_chicks = [el for el in girls if check_city(el)]

    return moscow_chicks


def get_girls_soc_message_all_cities(page):
    messages = parse_page(page)
    girls = [el for el in messages if check_post_for_girl(el)]
    return girls


def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def check_string_for_letters(string):
    return any(c.isalpha() for c in string)


def debug_messages(messages, last=''):
    messages = list(unique_everseen(messages))
    if last in messages:
        messages = messages[0:messages.index(last)]

    for el in messages:
        if isinstance(el, list):
            text = ' '.join(el)
            if '@tghex' not in text and '@hexnew' not in text:
                if '>>' not in text:
                    print(text)
                    print('Проверка города - {}'.format(check_phrase_for_city(text)))
                    print(el[0].strip())
                    print('Проверка пола - {}'.format(check_phrase_for_girl(el[0])))
                    print('--------------------------------------------------------------'
                         '---------------------------------------------------------------'
                          '--------------------------------------------------')
        else:
                text = el.getText(separator=' ', strip=True)
                blacklist = ['@tghex', '@hexnew']
                if all(s not in text for s in blacklist) and ('>' not in el.getText(separator=' ', strip=True) or 'OP' in el.getText(separator=' ', strip=True)):
                    all_text = [element for element in el.contents if isinstance(element, NavigableString)]
                    letters = [elem for elem in all_text if check_string_for_letters(elem)]
                    if len(letters) > 0:
                        if text != ' '.join(letters).strip():
                            print(text)
                        print(' '.join(letters).strip())
                        print('Проверка города - {}'.format(check_phrase_for_city(' '.join(letters))))
                        print(letters[0].strip())
                        print('Проверка пола - {}'.format(check_phrase_for_girl(letters[0])))
                        print('--------------------------------------------------------------'
                                  '---------------------------------------------------------------'
                                  '--------------------------------------------------')
                if last in text:
                    break


def old_debug_messages(messages, last=''):
    messages = list(unique_everseen(messages))
    if last in messages:
        messages = messages[0:messages.index(last)]

    for el in messages:
        if isinstance(el, list):
            text = ' '.join(el)
            if '@tghex' not in text and '@hexnew' not in text:
                if '>>' not in text:
                    print(text)
                    print('Проверка города - {}'.format(check_phrase_for_city(text)))
                    print(el[0].strip())
                    print('Проверка пола - {}'.format(check_phrase_for_girl(el[0])))
                    print('--------------------------------------------------------------'
                         '---------------------------------------------------------------'
                          '--------------------------------------------------')
        else:
            text = el.getText(separator=' ', strip=True)
            blacklist = ['@tghex', '@hexnew']
            if all(s not in text for s in blacklist) and ('>' not in el.getText(separator=' ', strip=True) or 'OP' in el.getText(separator=' ', strip=True)):
                all_text = [element for element in el.contents if isinstance(element, NavigableString)]
                letters = [elem for elem in all_text if check_string_for_letters(elem)]
                if len(letters) > 0:
                    print(' '.join(letters).strip())
                    print('Проверка города - {}'.format(check_phrase_for_city(' '.join(letters))))
                    print(letters[0].strip())
                    print('Проверка пола - {}'.format(check_phrase_for_girl(letters[0])))
                    print('--------------------------------------------------------------'
                              '---------------------------------------------------------------'
                              '--------------------------------------------------')

    """Кун УФА 21-00 сходить в джаз клуб сегодня, девушку телеграмм: @jazzonelove"""


def check_girls_arch(page):
    messages = parse_page(page)
    for el in messages:
        print(el.contents[0])
        print(check_phrase_for_girl(el))


def get_arch_messages():
    links = parse_arch()
    messages = []
    for link in links:
        messages.append(get_girls_string(link))
        print('appended')
    return messages


def get_arch_messages_and_save_them_to_docx(filename):
    save_iterable_to_docx(get_arch_messages(), filename)


def get_arch_messages_and_send_them():
    """
    Получает список ссылок всех страниц овощетреда
    и отправляет на почту посты всех девушек из Москвы
    """
    links = parse_arch()
    for link in links:
        chicks = get_girls(link)
        if len(chicks) != 0:
            #print(len(get_girls(link)))
            send_mail('\n'.join([el.getText(separator=' ').strip() for el in chicks[::-1]]))
            #res = '\n'.join([el.getText(separator=' ').strip() for el in chicks[::-1]])
            #print(res)
            #send_mail()


def get_arch_messages_from_thread(num):
    links = parse_arch()
    return parse_page(links[num])


def save_girls_to_docx(page, docx_name):
    messages = get_girls(page)
    parsed_messages = [el.getText(separator=' ').strip() for el in messages]
    save_iterable_to_docx(parsed_messages, docx_name)


def already_written():
    with open(r'C:/Users/nikit/OneDrive/Рабочий стол/written.txt') as f:
        lines = f.read().splitlines()
    return [el for el in lines if len(el) != 0]


def main():
    url = 'https://2ch.hk/soc/'
    # TODO Debug page !
    page = SocPage(url)
    print('Скачал все сообщения')
    print('Ссылка на тред - {}'.format(page.get_link_from_soc_page()))
    marker = True
    for mes in page.get_girls():
        text = mes.getText(separator=' ', strip=True)
        if all(el not in text for el in already_written()):
            if marker:
                print('-' * 120)
                marker = False
            print(text)
            print('-'*120)
    input('Конец программы\n')
    #print(page)


if __name__ == "__main__":
    main()

