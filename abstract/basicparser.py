from abc import ABC, abstractmethod


class BasicParser(ABC):

    @abstractmethod
    def __init__(self):
        """Конструктор класса Parser"""
        link = self.get_soc_link()
        self.messages = self.parse(link)


    @staticmethod
    @abstractmethod
    def get_soc_link():
        pass

    @abstractmethod
    def get_messages(self):
        return self.messages

    @staticmethod
    @abstractmethod
    def parse(link):
        pass


def main():
    try:
        BasicParser('er')
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
