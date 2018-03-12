from bs4 import BeautifulSoup
import requests
import json


def load_and_save_female_names():
    page = 'https://kakzovut.ru/woman.html'
    html = requests.get(page)
    soup = BeautifulSoup(html.text, 'lxml')
    names = soup.find_all('div', class_='nameslist')
    fem_names = [name.text for name in names]
    with open('femnames.json', 'w', encoding='utf-8') as file:
        json.dump(fem_names, file)


def get_female_names():
    with open('femnames.json', encoding='utf-8') as file:
        res = json.load(file)
    return res


def main():
    get_female_names()


if __name__ == '__main__':
    main()
