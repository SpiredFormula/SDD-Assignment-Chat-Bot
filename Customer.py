# importing necessary packages
import spacy
from Avatar import Avatar
import json


class CustomerClass:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.waiter = Avatar()

    # Grabs the previous customers and returns them as a string
    def loadPeople(self):
        try:
            with open("Json\People.json") as p:
                data = p.read()
                self.people = json.loads(data)
                self.peopleNames = list(self.people.keys())
                self.peopleNames = ' '.join(self.peopleNames)
                return self.people
        except:
            print("error")

    # This will read the user's input and grabs all the names in it
    def getName(self, speech):
        name = []
        doc = self.nlp(speech.title()+" And")

        # Parts of Speech (POS) Tagging
        for token in doc:
            #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
            if token.pos_ in ["PROPN"]:
                #print("found one")
                name.append(token.text)

        name = " ".join(name)
        #print(f" 2: {name}")
        return name

    # Asks the user for their name and will run the getName function and return the result
    def askName(self, ask):
        self.customerName = self.waiter.listen(ask)
        if self.customerName == False:
            return self.customerName
        else:

            self.customerName = self.getName(self.customerName)

            return self.customerName
