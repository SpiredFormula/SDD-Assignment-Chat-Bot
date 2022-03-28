# @author olliem5
import json
menu = json.loads(open("Json/Menu.json", "r").read())
possible_dishes = []

for course in menu:
    items = menu[course]
    for item in items:
        possible_dishes.append(item)
print(possible_dishes)
