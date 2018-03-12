import json
with open('test_results.json', encoding='utf-8') as file:
    data = json.load(file)
for el, reschek, word in data:
    print(el)
    print(reschek)
    print(word)
    print('--------------------------------------------------------------'
          '---------------------------------------------------------------'
          '--------------------------------------------------')
print(len(data))