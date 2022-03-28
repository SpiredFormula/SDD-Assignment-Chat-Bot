# Importing all the packages required
from Menu import Menu
from Avatar import Avatar
import json
from fuzzywuzzy import process
import spacy
from Customer import CustomerClass
from viewPrevOrders import ViewPrev
from orderFood import OrderFood


# defining the class
class Chat_Bot:
    def __init__(self):
        self.waiter = Avatar()
        self.Customer = CustomerClass()
        self.previouscustomers = self.Customer.loadPeople()
        self.orders = ViewPrev()
        self.viewmenu = Menu()
        self.foodorder = OrderFood()

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

    # This asks the user what they want to do
    def actions(self):
        print("Here are your options")
        self.waiter.say("here are your options")

        choices = ["Order food", "View previous orders",
                   "See the menu", "Exit the system"]
        for i in choices:
            print(i)
            self.waiter.say(i)

        # Asks the user what they want to do
        action = self.waiter.listen("What do you want to do? ")

        results = process.extract(action, choices)

        for (match, confidence) in results:
            # If they want to exit the system exit the system duh...
            if match == "Exit the system" and confidence >= 60:
                self.waiter.say(
                    "So sad to see you go lol just kidding i'm a robot and i don't have feelings eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee lol among us xd poopy piss lol among us funny joke bye")
                quit()

            # Views previous orders by grabbing it form the json file People.json
            elif match == "View previous orders" and confidence >= 60:
                print("viewing prev orders")
                self.orders.loadOrders(self.customerName)
                self.actions()

            # Shows the user the menu
            elif match == "See the menu" and confidence >= 60:
                self.seeMenu()
                self.actions()

            # Ask the use what they want to order
            elif match == "Order food" and confidence >= 60:
                choices3 = ['yes', 'no']
                actions3 = self.waiter.listen(
                    "would you like to see the menu?")
                results = process.extract(actions3, choices3)
                for (match, confidence) in results:
                    if match == "yes" and confidence >= 60:
                        self.seeMenu()
                        self.foodorder.order(self.customerName)
                    elif match == "no" and confidence >= 60:
                        self.foodorder.order(self.customerName)

                # print this if it does not undersand the user
            else:
                print("sorry did not understand")
                self.actions()

    def seeMenu(self):
        choices2 = ['see the full menu',
                    'see a specific course']
        action2 = self.waiter.listen(
            "Would you like to see the full menu or a specific course?")
        results = process.extract(action2, choices2)
        for (match, confidence) in results:

            # Shows the user the full menu
            if match == 'see the full menu' and confidence >= 60:
                self.viewmenu.showMenu()
                self.actions()

                # Asks the user what course they want to see
            elif match == 'see a specific course' and confidence >= 60:
                courses = self.viewmenu.loadcourses()
                for i in courses:
                    print(i)
                    self.waiter.say(i)
                ans = self.waiter.listen("what course do you want to see?")
                self.viewmenu.showMenu(ans)


if __name__ == "__main__":
    bot = Chat_Bot()
    bot.greet()
