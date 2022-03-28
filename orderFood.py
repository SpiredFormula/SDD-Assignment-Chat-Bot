from Avatar import Avatar
from Menu import Menu
from fuzzywuzzy import process
import json


class OrderFood:
    def __init__(self):
        self.waiter = Avatar()
        self.m = Menu()

    def loadItems(self):
        menu = json.loads(open("Json\Menu.json", "r").read())
        possible_dishes = []

        for course in menu:
            items = menu[course]

            for item in items:
                possible_dishes.append(item)

        return possible_dishes

    def addOrder(self, name, order, ordernum):
        filename = 'Json\People.json'

        # 1. Read file contents
        with open(filename, "r") as f:
            data = json.load(f)
            print("----------------")
            print(data)

        # 2. Update json object
        preorders = data[name]
        preorders[ordernum] = order
        print(data)

        # 3. Write json file
        with open(filename, "w") as fi:
            json.dump(data, fi)

    def order(self, name):
        choices = self.loadItems()
        action = self.waiter.listen(
            "What do you want to order? you need at least 3 items: ")
        results = process.extract(action, choices)
        ordered = []
        for(match, confidence) in results:

            if confidence >= 80:
                ordered.append(match)
            else:
                pass
        print(ordered)
        try:
            with open("Json\People.json") as p:
                data = p.read()
                people = json.loads(data)

                ordernum = people[name]
                ordernumlist = list(people[name].keys())
                print(ordernumlist)
                ordernumber = str(len(ordernumlist) + 1)
            print(ordernumber)
        except:
            ordernumber = "1"

        with open("Json\Menu.json") as d:
            data = d.read()
            menu = json.loads(data)
            print(menu)
        courses = self.m.loadcourses()
        orderDictionary = {}

        for course in courses:
            currentcourse = menu[course]
            print("------------------")
            print(currentcourse)
            for orders in ordered:
                if orders in currentcourse:
                    price = currentcourse[orders]
                    orderDictionary[orders] = price
                    print(orderDictionary)
                else:
                    print("pass")
        print('''----------
        done!''')
        print(orderDictionary)

        self.addOrder(name, orderDictionary, ordernumber)


if __name__ == "__main__":
    o = OrderFood()
    # o.addOrder("Jim", {"1": {"pie": "$1.00"}})

    o.order("Michael")
