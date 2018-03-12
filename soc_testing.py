from soc import check_post_for_girl
from soc import check_city
from parse import parse_soc_page, parse_arch_page
page = 'http://arhivach.org/thread/328253/'
messages = parse_arch_page(page)
girls = [el for el in messages if check_post_for_girl(el)]
moscow_chicks = [el for el in girls if check_city(el)]
for el in girls:
    print("{1} - {0}".format(check_city(el), el.contents[0].strip()))
    moscow_chicks = [el for el in girls if check_city(el)]
