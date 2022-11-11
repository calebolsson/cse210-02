import random

class Card:
    def __init__(self) -> None:
        self.value = 0
        self.is_greater = True
        self.suite = ""
        self.suite_map = ["Spades","Hearts","Clubs","Diamonds"]

    def draw_card(self):
        new = random.randrange(1,13)
        if new > self.value:
            self.is_greater = True
        else:
            self.is_greater = False
        self.value = new
        self.suite = self.suite_map[random.randrange(0,3)]


    def get_value(self):
        return self.value