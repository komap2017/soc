from soc import SocPage




def main():
    url = 'https://2ch.hk/soc/'
    last = 'Ищу людей с факультета компьютерных наук ВШЭ @azisas'
    page = SocPage(url)
    page.debug()
    """ Донецк, 17 лвл, парень. 2. Депрессивный меланхолик без чувства """


if __name__ == '__main__':
    main()

