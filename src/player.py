import hashlib
import typing

from src.dice import Dice, DiceValues
from src.house import House


class Player:
    """Игрок Котокафе"""

    # Стандартные __init__, __str__ и __eq__:
    def __init__(self, name: str, dice: Dice = None, score: int = 0, house: House = None):
        if dice is None: dice = Dice()
        if house is None: house = House(None)
        self.name = name
        self.dice = dice
        self.score = score
        self.house = house

    def __str__(self):
         return f'''
Игрок: {self.name}
Кубик: {self.dice}
Очки:  {self.score}
Игровое поле: {self.house.print()}
'''

    def __eq__(self, other: typing.Self | dict):
        if isinstance(other, dict):
            other = self.load(other)
        return self.name == other.name          \
               and self.dice == other.dice      \
               and self.score == other.score    \
               and self.house == other.house

    # Метод хеша
    def __hash__(self) -> int:
        return int(hashlib.sha1(self.name.encode("utf-8")).hexdigest(), 16) % (10**8)

    # Методы сохранения и загрузки:
    def save(self) -> dict:
        return \
        {
            'name': self.name,
            'dice': self.dice.save(),
            'score': self.score,
            'house': self.house.save(),
        }

    @classmethod
    def load(cls, data: dict):
        return cls(name = data['name'], dice = Dice.load(data['dice']),
                   score = int(data['score']), house = House.load(data['house']))
