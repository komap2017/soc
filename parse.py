from bs4 import BeautifulSoup
import requests
import json


def parse_soc_page(page):
    page = requests.get(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    messages = soup.find_all('blockquote')
    return messages


def parse_arch_page(page):
    page = requests.get(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    messages = soup.find_all('div', class_="post_comment_body")
    return messages


def parse_arch():
    """
    Ищет ссылочки под тегом 'овощной' на архиваче
    :return: список ссылочек
    """
    page = 'http://arhivach.org/?tags=2758'
    page = requests.get(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    threads = soup.find_all('a', style='display:block;')
    tree = 'http://arhivach.org'
    threads_adress = []
    for el in threads:
        threads_adress.append(tree + el.get('href'))
    return threads_adress


def check_site(page):
    if 'soc' in page:
        return True
    else:
        return False


def save_list_to_file_in_json(list, filename='data.json'):
    with open(filename, 'w') as outfile:
        json.dump(list, outfile, ensure_ascii=False)


def read_data_from_file_with_json(filename='data.json'):
    with open(filename) as data_file:
        data = json.load(data_file)
    print(data)


def parse_vk(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.prettify())
    """
    posts = soup.find_all('div', class_='pi_text')
    for post in posts:
        print(post.getText(separator=' '))
    """


def parse_page(page):
    if check_site(page):
        return parse_soc_page(page)
    else:
        return parse_arch_page(page)


if __name__ == '__main__':
    save_list_to_file_in_json(['какая-то', 'инфа'])
    read_data_from_file_with_json()