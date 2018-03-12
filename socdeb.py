from soc import SocPage


def main():
    url = 'https://2ch.hk/soc/res/4219284.html'
    page = SocPage(url)
    page.debug()


if __name__ == '__main__':
    main()