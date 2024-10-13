from random import randrange
import typing
import enum

class DiceValues(enum.IntEnum):
    EMPTY = 0
    HOUSE = 1
    YARN = 2
    BUTTERFLY = 3
    DISH = 4
    PILLOW = 5
    MOUSE = 6
    INVALID = 7

class Dice:
    """Кубики Котокафе"""

    # Стандартные __init__, __repr__ и __eq__:
    def __init__(self, value = DiceValues.EMPTY):
        if value not in range(DiceValues.EMPTY,DiceValues.INVALID + 1):
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
        self.value = randrange(DiceValues.HOUSE, DiceValues.MOUSE + 1)

    def char(self):
        return f'{DiceValues(self.value).name[0]}'

    def word(self):
        return f'{DiceValues(self.value).name}'
