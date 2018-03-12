from soc import check_post_for_girl, check_city
from bs4 import BeautifulSoup
import requests
import re


def get_contacts(post):
    regex = r'@[a-z0-9]+'
    matches = re.findall(regex, post.text)
    regex = r'(id[0-9]+)'
    matches.extend(re.findall(regex, post.text))
    for el in matches:
        print(el)
    if not len(matches):
        print('Контактов не найдено')


page = requests.get('http://arhivach.org/thread/328253/')
soup = BeautifulSoup(page.text, 'html.parser')
messages = soup.find_all('div', class_="post_comment_body")
#messages = list(set(messages))
girls = [el for el in messages if check_post_for_girl(el)]
for el in girls:
    print(check_city(el))

