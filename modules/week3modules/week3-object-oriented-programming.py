import string 
class TextContainer():

    def __init__(self, text):
        self.text = text

    def countwords(self):
        print(len(self.text.split()))

tc = TextContainer("very cool! :)")
tc.countwords