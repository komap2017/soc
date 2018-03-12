import string


def translate(s):
    # Thanks to Martijn Pieters for this improved version
    # This uses the 3-argument version of str.maketrans
    # with arguments (x, y, z) where 'x' and 'y'
    # must be equal-length strings and characters in 'x'
    # are replaced by characters in 'y'. 'z'
    # is a string (string.punctuation here)
    # where each character in the string is mapped
    # to None
    # translator = str.maketrans('', '', string.punctuation)
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # This is an alternative that creates a dictionary mapping
    # of every character from string.punctuation to None (this will
    # also work)
    #translator = str.maketrans(dict.fromkeys(string.punctuation))
    s = s.translate(translator)
    # pass the translator to the string's translate method.
    s = ' '.join(s.split())
    return s


def main():
    print(translate('ж, 18,     ленобл'))


if __name__ == "__main__":
    main()