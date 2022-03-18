
# Importing all the packages required
from Menu import Menu
from Avatar import Avatar
import json
from fuzzywuzzy import process
import spacy
from Customer import CustomerClass
from viewPrevOrders import ViewPrev

# defining the class


class Chat_Bot:
    def __init__(self):
        self.waiter = Avatar()
        self.Customer = CustomerClass()
        self.previouscustomers = self.Customer.loadPeople()
        self.orders = ViewPrev()

    # Greets the user
    def greet(self):
        print(
            f"Hello my name is {self.waiter.name} and I'll be serving you today")
        self.waiter.say(
            f"Hello my name is {self.waiter.name} and I'll be serving you today")

        self.orderHistory("Before we start may i take your name?")

    # This function will check to see if the user had ordered before
    def orderHistory(self, ask):
        self.customerName = self.Customer.askName(
            ask)
        # if they have ordered before
        if self.customerName in self.previouscustomers:
            print(
                f"I can see you have ordered with us before.  Welcome back {self.customerName}")
            self.waiter.say(
                f"I can see you have ordered with us before.  Welcome back {self.customerName}")
            self.orderedBefore = True
            self.actions()
        # if it can not undersand the user
        if self.customerName == False:
            print("Let's try that again.  What is your name? ")
            self.orderHistory("let's try that again What is Your name")
        # if it is their first time
        else:
            print(
                f"I can see this is your first time ordering with us. welcome {self.customerName}")
            self.waiter.say(
                f"I can see this is your first time ordering with us. welcome {self.customerName}")
            self.actions()
            self.orderedBefore = False

    # this asks the user what they want to do
    def actions(self):
        print("Here are your options")
        self.waiter.say("here are your options")

        choices = ["Order food", "View previous orders",
                   "See the menu", "Exit the system"]
        for i in choices:
            print(i)
            self.waiter.say(i)

        action = self.waiter.listen("What do you want to do? ")

        results = process.extract(action, choices)

        for (match, confidence) in results:

            if match == "Exit the system" and confidence >= 60:
                print("exit!!!")
                quit()
            elif match == "View previous orders" and confidence >= 60:
                print("viewing prev orders")
                self.orders.loadOrders(self.customerName)
                self.actions()
            elif match == "See the menu" and confidence >= 60:
                print("See the menu")
            elif match == "Order food" and confidence >= 60:
                print("Order food")
            else:
                print("sorry did not understand")
                self.actions()


if __name__ == "__main__":
    bot = Chat_Bot()
    bot.greet()
