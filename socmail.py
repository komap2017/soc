import soc
page = 'http://arhivach.org/thread/235657/'
for el in soc.get_girls_arch_messages(page):
    print(el.contents[0]) 