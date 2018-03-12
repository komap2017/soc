from soc import get_arch_messages_from_thread
from soc import check_post_for_girl, check_city
last_girls_check = 5
last_city_check = 1
for message in list(set(get_arch_messages_from_thread(last_city_check))):
    if len(message.contents[0]) != 1:
        print(message.getText(separator=' '))
        print(check_city(message))
