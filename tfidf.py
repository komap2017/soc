from sklearn.feature_extraction.text import TfidfVectorizer


class Analyzer:

    def __init__(self, table):
        self.table = table
        self.vector = TfidfVectorizer(ngram_range=(1, 3))

    def transform(self, questions=None):
        if questions is None:
            questions = self.table
            transformed = self.vector.fit_transform(questions)
        else:
            questions = [text.lower() for text in questions]
            transformed = self.vector.transform(questions)
        return transformed


def main():
    phrases = 'Как дела?,Привет,Йоу'.split(',')
    clean = Analyzer(phrases)
    print(clean.transform())


if __name__ == '__main__':
    main()
