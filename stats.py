from bs4 import BeautifulSoup
import requests


def gender_check(post):
    phrase = post.contents[0].lower()
    bad_catch = ['кун', 'парень', 'тянку']
    if any(word in phrase for word in bad_catch):
        return 'парень'
    catch = ['тян', 'девушка']
    if any(word in phrase for word in catch):
        return 'девушка'
    return 'пол неопределен'


if __name__ == "__main__":
    page = requests.get('http://arhivach.org/thread/251817/')
    soup = BeautifulSoup(page.text, 'html.parser')
    messages = soup.find_all('div', class_="post_comment_body")
    #messages = list(set(messages))
    genders = []
    for el in messages:
        gen = gender_check(el)
        if gen == 'пол неопределен':
            print(el.text)
        genders.append(gen)
    print(len(genders))
    genders = [gen for gen in genders if gen != 'пол неопределен']
    print(len(genders))
    print('Количество парней: {}'.format(genders.count('парень')))
    print('Количество девушек: {}'.format(genders.count('девушка')))