import random

class Card:
    def __init__(self) -> None:
        self.value = 0
        self.isGreater = True
        self.suite = ""
        self.suiteMap = ["Spades","Hearts","Clubs","Diamonds"]

    def draw_card(self):
        new = random.randrange(1,13)
        if new > self.value:
            self.isGreater = True
        else:
            self.isGreater = False
        self.value = new
        self.suite = self.suiteMap[random.randrange(0,3)]


    def get_value(self):
        return self.value