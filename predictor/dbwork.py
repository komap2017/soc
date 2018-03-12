import pandas as pd


def get_samples(path='genders.csv'):
    df = pd.read_csv(path)
    return list(df['Сообщение']), list(df['Пол'])


def main():
    path = 'genders.csv'
    x, y = get_samples(path)
    for el in y:
        # print(el)
        print(type(el))

if __name__ == '__main__':
    main()
