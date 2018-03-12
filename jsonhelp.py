import json


def save_to_json(data, filename):
    with open(filename + '.json', 'w') as outfile:
        json.dump(data, outfile)


def load_from_json(filename):
    with open(filename + '.json', 'w') as outfile:
        return json.load(outfile)