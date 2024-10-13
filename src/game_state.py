import typing

from src.dice import Dice
from src.house import House
from src.player import Player


class GameState:

    # Стандартные __init__, __eq__:
    def __init__(self):
        pass

    def __eq__(self, other):
        pass

    # Методы сохранения и загрузки:
    def save(self) -> dict:
        pass

    @classmethod
    def load(cls, data: dict):
        pass

    # Другие методы:
    def current_player(self) -> Player:
        pass

    def next_player(self):
        pass

    def take_dice(self):
        pass

    def draw_object(self):
        pass
