from random import randrange

class Dice:
    """Кубики Котокафе"""
    EMPTY = 0
    HOUSE = 1
    YARN = 2
    BUTTERFLY = 3
    DISH = 4
    PILLOW = 5
    MOUSE = 6
    INVALID = 7

    VALUES = ['EMPTY', 'HOUSE', 'YARN', 'BUTTERFLY', 'DISH', 'PILLOW', 'MOUSE', 'INVALID']
    VALUES_SHORT = ['E', 'H', 'Y', 'B', 'D', 'P', 'M', 'I']

    def __init__(self, value = 0):
        if value not in range(0,8):
            raise ValueError
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value

    def save(self):
        return int(repr(self))

    @staticmethod
    def load(num: int):
        return Dice(num)

    def roll(self):
        self.value = randrange(1, 7)

    def char(self):
        return f'{Dice.VALUES_SHORT[self.value]}'

    def word(self):
        return f'{Dice.VALUES[self.value]}'