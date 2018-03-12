from bs4 import BeautifulSoup
import requests
from rus import send_mail
from soc import messages_to_string


def parse_hearpwn_page(page):
    page = requests.get(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    messages = soup.find_all('div', itemprop='text')
    return messages


def parse_salty_thread_page(pageid):
    page = 'http://www.hearthpwn.com/forums/hearthstone-general/general-discussion/28947-group-' \
           'therapy-need-to-blow-off-steam-mega-salty?page=' + str(pageid)
    return parse_hearpwn_page(page)


def pretty_print(messages):
    for el in messages:
        print(el.getText(separator = ' '))


def main():
    print(messages_to_string(parse_salty_thread_page(2180)))
    send_mail(messages_to_string(parse_salty_thread_page(2180)))


if __name__ == '__main__':
    main()