from abc import ABC, abstractmethod


class BasicDeterminant(ABC):

    @abstractmethod
    def __init__(self, clean_messages, messages, model):
        self.clean_messages = clean_messages
        self.messages = messages
        self.model = model

    @staticmethod
    @abstractmethod
    def check_phrase_for_girl(phrase):
        """returns: check : Boolean"""

    @staticmethod
    @abstractmethod
    def check_phrase_for_city(phrase):
        """returns: check : Boolean"""

    @abstractmethod
    def get_girls(self):
        """returns: messages : list"""


def main():
    try:
        BasicDeterminant('aer', 'aer')
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
