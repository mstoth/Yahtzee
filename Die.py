import random
from tkinter import *

class Die:
    active = True
    number_of_sides: int
    def __init__(self,n):
        self.number_of_sides = n
        self.last_value = 0

    def roll(self):
        if self.active:
            self.last_value = round(random.uniform(1,self.number_of_sides)+0.5)
            return self.last_value
        else:
            return self.last_value