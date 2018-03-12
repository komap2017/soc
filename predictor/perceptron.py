from sklearn.linear_model import Perceptron
from tfidf import Analyzer
from predictor.dbwork import get_samples
import pickle


class Predictor:

    def __init__(self, transformer, model):
        transformer.transform()
        self.transformer = transformer
        self.network = model

    def check_gender(self, phrase):
        result = None
        if isinstance(phrase, str):
            phrase = [phrase]
            result = self.network.predict(self.transformer.transform(phrase))
            result = result[0]
        return result


def main():
    # predictor = load_model()
    train()


def load(path=r'C:\Users\nikit\OneDrive\Рабочий стол\Codding\Python\tv\predictor\weights.h5'):
    network = load_model(path)
    if not isinstance(network, Perceptron):
        raise TypeError
    x, y = get_samples('genders.csv')
    transformer = Analyzer(x)
    predictor = Predictor(transformer, network)
    return predictor
    # transformer.transform()
    # transformer = Analyzer(x)
    # print(network.predict(transformer.transform(['тян', 'тяночка из москвы', 'кун'])))


def train():
    network = Perceptron(max_iter=100000)
    x,y = get_samples('genders.csv')
    transformer = Analyzer(x)
    network.fit(transformer.transform(), y)
    print(network.predict(transformer.transform(['1. Дс, 19, тян 2. Игры, аниме, музыка, фильмы, книги 3. Хорошего и интересного друга 4. Телега @cypr123'])))
    pickle.dump(network, open('latest_weights.h5', 'wb'))


def load_model(path=r'C:\Users\nikit\OneDrive\Рабочий стол\Codding\Python\tv\predictor\weights.h5'):
    return pickle.load(open(path, 'rb'))


if __name__ == '__main__':
    main()
