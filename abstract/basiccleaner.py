from abc import ABC, abstractmethod


class BasicCleaner(ABC):

    @abstractmethod
    def __init__(self, messages):
        self.messages = messages

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def get_messages(self, cleared=False):
        return self.messages

    @staticmethod
    @abstractmethod
    def clear(text):
        pass


def main():
    try:
        BasicCleaner('text')
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
