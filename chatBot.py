
#Importing all the packages required
from Menu import Menu
from Avatar import Avatar
import json
from fuzzywuzzy import process
import spacy
from GetName import GET_NAME


#defining the class
class Chat_Bot:
    def __init__(self):
        self.waiter = Avatar()
        self.name = GET_NAME()
        self.loadPeople()
        

    # Gets the list of previous customers
    def loadPeople(self):
        try:
            with open("People.json") as p:
                data = p.read()
                self.people = json.loads(data)
                self.peopleName = list(self.people.keys())
                self.peopleNam = ' '.join(self.peopleName).lower()
                
                print(self.peopleName)
        # Print's out a error message if it is unable to find the json file        
        except:
            print("unable to find json file")
            y = input("Try again? y/n: ").lower()
            if y == "y":
                self.loadPeople()
        


    # Greets the user
    def greet(self):
        self.waiter.say(f"Hello my name is {self.waiter.name} and I'll be serving you today")
        print(f"Hello my name is {self.waiter.name} and I'll be serving you today")
        self.takeName("Before we start, can I take your name? ")

    # Takes the name of the user
    def takeName(self, ask):
        words = self.waiter.listen(ask)
        name = self.name.getName(words)
        name = name.lower()
        print(name)
        results = process.extract(words, self.peopleName)
        print(results)
        for (match ,confidence)
        # If they have ordered before
        if confidence >= 60:
            self.waiter.say(f"I can see you have ordered with us before.  Welcome back {name}")
            print(f"I can see you have ordered with us before.  Welcome back {name}")
            self.actions()



        # If it could not understand what the user said ask again
        elif words == False:
            self.takeName("could you please repeat that?")
            print("could you please repeat that?")

        # If the user has not ordered before
        else:
            self.waiter.say(f"I can see this is your first time ordering with us. Welcome to VietnamBot, {name}")
            print(f"I can see this is your first time ordering with us. Welcome to VietnamBot, {name}")
            self.actions()
    
    def actions(self):
        self.waiter.say("what would you like to do")
        print("what would you like to do")

        self.waiter.say("Order food")
        print("Order food")

        self.waiter.say("View previous orders")
        print("View previous orders")

        self.waiter.say("See the menu")
        print("See the menu")

        self.waiter.say("Exit the system")
        print("Exit the system")

        action = self.waiter.listen("What do you want to do? ")
        action.lower()

        if "exit" in action:
            self.Exit()
        '''
        elif

        elif

        elif
        '''
        


    def Exit(self):
        return


if __name__ == "__main__":
    bot = Chat_Bot()
    bot.greet()



