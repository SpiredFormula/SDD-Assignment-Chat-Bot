##########################################################################
##########################################################################
#                           RUN THIS FIRST                               #
##########################################################################
##########################################################################

# IMPORTANT!!!!!
# python version: 3.10.2 64-bit
# also the water costing $10.50 is not a typo :)

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

        self.waiter.say(
            f"Hello and welcome to Motherboard Foods. my name is {self.waiter.name} I am totally a normal human being and I'll be serving you today")

        self.orderHistory("Before we start. May I take your name? ")

    # This function will check to see if the user had ordered before
    def orderHistory(self, ask):
        self.customerName = self.Customer.askName(
            ask)

        # if they have ordered before
        if self.customerName in self.previouscustomers:
            self.waiter.say(
                f"I can see you have ordered with us before.  Welcome back To MotherBoard Foods {self.customerName}")
            self.orderedBefore = True
            self.actions(self.customerName)

        # if it can not undersand the user
        elif self.customerName == False or self.customerName == '':
            self.orderHistory("Let's try that again What is Your name")

        # if it is their first time
        else:
            self.waiter.say(
                f"I can see this is your first time ordering with us. Hello {self.customerName} and welcome to MotherBoard Foods")
            self.actions(self.customerName)
            self.orderedBefore = False

    # This asks the user what they want to do
    def actions(self, name):
        self.customerName = name
        print("----------------------------------------------------------")
        self.waiter.say(f"Here are your options {self.customerName}")
        print("----------------------------------------------------------")
        choices = ["Order food", "View previous orders",
                   "See the menu", "Exit the system"]
        for i in choices:

            self.waiter.say(i)
        print("----------------------------------------------------------")
        # Asks the user what they want to do
        action = self.waiter.listen("What do you want to do? ")
        print(f'- {action}')
        print("----------------------------------------------------------")
########################################################################################


########################################################################################
        # if it doesn't understand the user restart the function
########################################################################################
        if action == False or action == '':
            self.waiter.say("Lets's try that again.")
            self.actions(self.customerName)
        results = process.extract(action, choices)

        for (match, confidence) in results:
            ############################################################################
            # If they want to exit the system exit the system
            ############################################################################
            if match == "Exit the system" and confidence >= 60:
                ans = self.waiter.listen(
                    "Are you sure you want to exit? (yes or no): ")
                if ans == False or ans == '':
                    self.waiter.say("Let's try that again")
                yn = ['yes', 'no']
                r = process.extract(ans, yn)
                for (match, confidence) in r:
                    if match == 'yes' and confidence >= 60:

                        self.waiter.say(
                            f"So sad to see you go {self.customerName}. Thank you for choosing MotherBoard Foods , we hope we will see you again")
                        quit()
                    elif match == "no" and confidence >= 60:
                        self.actions(self.customerName)
########################################################################################
            # Views previous orders by grabbing it form the json file People.json
########################################################################################
            elif match == "View previous orders" and confidence >= 60:
                self.waiter.say("Viewing previous orders..............")
                self.orders.loadOrders(self.customerName)
                self.actions(self.customerName)
########################################################################################
            # Shows the user the menu
########################################################################################
            elif match == "See the menu" and confidence >= 60:
                self.seeMenu()
                self.actions(self.customerName)
########################################################################################
            # Ask the use what they want to order
########################################################################################
            elif match == "Order food" and confidence >= 60:

                actions3 = self.waiter.listen(
                    "Would you like to see the menu? (yes or no): ")
                if actions3 == False or actions3 == '':
                    self.actions(self.customerName)
                choices3 = ['yes', 'no']
                results = process.extract(actions3, choices3)
                for (match, confidence) in results:
                    if match == "yes" and confidence >= 60:
                        self.seeMenu()
                        self.foodorder.order(self.customerName)
                        self.actions(self.customerName)
                    elif match == "no" and confidence >= 60:
                        self.foodorder.order(self.customerName)
                        self.actions(self.customerName)
            else:
                self.waiter.say("Let's try that again")
                self.actions(self.customerName)

########################################################################################

    def seeMenu(self):
        choices2 = ['see the full menu',
                    'see a specific course']
        action2 = self.waiter.listen(
            "Would you like to see the full menu or a specific course?")
        if action2 == False or action2 == '':

            self.waiter.say("Lets try that again")
            self.actions(self.customerName)
        results = process.extract(action2, choices2)
        for (match, confidence) in results:

            # Shows the user the full menu
            if match == 'see the full menu' and confidence >= 60:
                self.viewmenu.showMenu()
                return

                # Asks the user what course they want to see
            elif match == 'see a specific course' and confidence >= 60:
                courses = self.viewmenu.loadcourses()
                coursechoices = []
                self.waiter.say("Here are the courses:")
                for i in courses:
                    self.waiter.say(f"- {i}")
                    coursechoices.append(i)
                ans = self.waiter.listen("what course do you want to see?")
                if ans == False or ans == '':
                    self.waiter.say("Let's try that again")
                    self.actions(self.customerName)
                elif ans not in coursechoices:
                    self.waiter.say("That course does not exist")
                    return
                results = process.extract(ans, coursechoices)
                for (match, confidence) in results:
                    if match in coursechoices and confidence >= 60:
                        self.viewmenu.showMenu(ans)
                        return


if __name__ == "__main__":
    bot = Chat_Bot()
    bot.greet()
