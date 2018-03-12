import json
with open('output.json', encoding='utf-8') as file:
    data = json.load(file)
good = [el for el in data if 'овощной' in el['name']]
for el in good:
    print(el)
print(len(good))