from random import randint as ran
import pandas as pd
import requests as req


class Human(object):
    def __init__(self, age=ran(14, 70), height=ran(140, 220), hair_color=ran(0, 4)):
        self.age = age
        self.height = height
        self.hair_color = hair_color

    @staticmethod
    def select_hair_color(selection):
        hair_colors = ('blonde', 'brown', 'black', 'red', 'grey')
        if isinstance(selection, int) and 0 <= selection <= 4:
            return hair_colors[selection]
        elif isinstance(selection, str) and selection in hair_colors:
            return hair_colors
        else:
            return hair_colors[ran(0, 4)]


