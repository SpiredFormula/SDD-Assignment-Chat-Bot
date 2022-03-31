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

        # 2. Update json object
        preorders = data[name]
        preorders[ordernum] = order

        # 3. Write json file
        with open(filename, "w") as fi:
            json.dump(data, fi)

    def order(self, name):
        choices = self.loadItems()
        choices.append("exit order")
        choices.append("see the menu")
        print(choices)
        print("Ask to exit order at anytime to cancel. Ask to see the menu to see the menu again")
        self.waiter.say(
            "Ask to exit order at anytime to cancel. Ask to see the menu to see the menu again")
        action = self.waiter.listen(
            "What do you want to order? you need at least 3 items: ")
        if action == False:
            self.waiter.say("lets try that again")
            self.order(name)
        results = process.extract(action, choices)
        ordered = []

        for(match, confidence) in results:
            print(f'{match}: {confidence}')
            if match != 'exit order' and match != "see the menu" and confidence >= 80:
                ordered.append(match)
            elif match == "exit order" and confidence >= 70:
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.actions(name)
            elif match == "see the menu" and confidence >= 60:
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.seeMenu()
                self.order(name)
        orderlength = len(ordered)
        print(orderlength)
        if orderlength <= 2:
            print("sorry your order needs to be at least 3 or more items")
            self.waiter.say(
                "sorry your order needs to be at least 3 or more items")
            self.order(name)
        try:
            with open("Json\People.json") as p:
                data = p.read()
                people = json.loads(data)
                if name not in people:
                    people[name] = {}
                    with open("Json\People.json", "w") as fil:
                        json.dump(people, fil)
                ordernum = people[name]
                ordernumlist = list(people[name].keys())
                ordernumber = str(len(ordernumlist) + 1)

        except:
            ordernumber = "1"

        with open("Json\Menu.json") as d:
            data = d.read()
            menu = json.loads(data)
        courses = self.m.loadcourses()
        orderDictionary = {}
        pricedictionary = []
        totalprice = []
        for course in courses:
            currentcourse = menu[course]
            for orders in ordered:
                if orders in currentcourse:
                    price = currentcourse[orders]
                    orderDictionary[orders] = price
                    totalprice.append(price)
                    pricedictionary.append(price)
                else:
                    pass
        num = 0
        for t in totalprice:
            total = num + t
            num = total

        print("This is your final order:")
        self.waiter.say("This is your final order:")
        for finalorder in orderDictionary:
            print(f"{finalorder}: ${str(orderDictionary[finalorder])}")
            self.waiter.say(
                f"{finalorder}: ${str(orderDictionary[finalorder])} and cents")
        print(f"Order Number: {ordernumber}")
        self.waiter.say(f"Order Number: {ordernumber}")
        print(f'Total Price: {num}')
        self.waiter.say(f'Total Price: ${num} and cents')
        self.Q1(name, orderDictionary, ordernumber)

    def Q1(self, name, orderDictionary, ordernumber):
        responce = self.waiter.listen(
            "Is this what you ordered? (yes or no): ")
        if responce == False:
            self.waiter.say("lets try that again")
            self.Q1(name, orderDictionary, ordernumber)
        choice = ['yes', 'no']
        choice.append("see the menu")
        results2 = process.extract(responce, choice)
        for (match, confidence) in results2:
            if match == 'yes' and confidence >= 70:
                self.addOrder(name, orderDictionary, ordernumber)
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.actions(name)
            elif match == 'no' and confidence >= 70:
                self.Q2(name)
            elif match == "see the menu" and confidence >= 60:
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.seeMenu()
                self.Q1(name, orderDictionary, ordernumber)
            else:
                self.Q1(name, orderDictionary, ordernumber)

    def Q2(self, name):
        responce2 = self.waiter.listen(
            "Ok do you wish to order again? (yes or no): ")
        if responce2 == False:
            self.waiter.say("lets try that again")
            self.Q2(name)
        choice2 = ['yes', 'no', 'see the menu']
        results3 = process.extract(responce2, choice2)
        for (match, confidence) in results3:
            if match == 'yes' and confidence >= 70:
                self.order(name)
            elif match == 'no' and confidence >= 70:
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.actions(name)
            elif match == "see the menu" and confidence >= 60:
                from chatBot import Chat_Bot
                chat = Chat_Bot()
                chat.seeMenu()
                self.Q1(name, orderDictionary, ordernumber)
            else:
                print("sorry did not understand")
                self.waiter.say("sorry did not understand")
                self.Q2(name)


if __name__ == "__main__":
    o = OrderFood()
    o.order("jim")
