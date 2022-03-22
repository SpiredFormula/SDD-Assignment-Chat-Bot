from Avatar import Avatar
from chatBot import Chat_Bot
import json


class OrderFood:
    def __init__(self):
        self.waiter = Avatar()
        self.chatbot = Chat_Bot()

    def addOrder(self, name, order):
        filename = 'Json\People.json'

        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        data[name] = order

        # 3. Write json file
        with open(filename, "w") as file:
            json.dump(data, file)

        def order(self):


if __name__ == "__main__":
    o = OrderFood()
    o.addOrder("Jim", {"1": {"pie": "$1.00"}})
