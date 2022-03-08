import spacy

class GET_NAME:
        def __init__(self): 
                self.nlp = spacy.load("en_core_web_sm")

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

