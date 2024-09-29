from random import randrange
import typing

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

    # Стандартные __init__, __repr__ и __eq__:
    def __init__(self, value = 0):
        if value not in range(0,8):
            raise ValueError
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value

    # Методы сохранения и загрузки:
    def save(self):
        return int(repr(self))

    @classmethod
    def load(cls, num: int) -> typing.Self:
        return cls(num)

    # Методы броска, вывода символа и вывода слова:
    def roll(self):
        self.value = randrange(1, 7)

    def char(self):
        return f'{Dice.VALUES_SHORT[self.value]}'

    def word(self):
        return f'{Dice.VALUES[self.value]}'
