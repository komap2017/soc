from soc import SocPage, clear_phrase, check_string_for_letters, NavigableString, check_city, already_written
from predictor.perceptron import load


class SocML(SocPage):

    def __init__(self, page, model):
        super().__init__(page)
        # self.messages = get_messages_from_url(page)
        self.model = model

    def check_post_for_girl(self, post):
        all_text = [element for element in post.contents if isinstance(element, NavigableString)]
        letters = [elem for elem in all_text if check_string_for_letters(elem)]
        if len(letters) == 0:
            return False
        else:
            text = clear_phrase(letters[0])
            return self.model.check_gender(text)

    def get_girls(self):
        return (el for el in self.messages if self.check_post_for_girl(el) if check_city(el))


def main():
    url = 'https://2ch.hk/soc/'
    model = load(r'C:\Users\nikit\OneDrive\Рабочий стол\Codding\Python\tv\predictor\weights.h5')
    soc = SocML(url, model)
    marker = True
    for mes in soc.get_girls():
        text = mes.getText(separator=' ', strip=True)
        if all(el not in text for el in already_written()):
            if marker:
                print('-' * 120)
                marker = False
            print(text)
            print('-'*120)
    input('Конец программы\n')

if __name__ == '__main__':
    main()
