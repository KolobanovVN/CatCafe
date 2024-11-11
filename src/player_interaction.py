from abc import ABC, abstractmethod

from src.dice import Dice
from src.player import Player

class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_dice(cls, dices):
        pass

    @classmethod
    @abstractmethod
    def draw_object(cls, house, player_dice, centre_dice):
        pass

    @classmethod
    def inform_dice_chosen(cls, player: Player, dice: Dice):
        pass

    @classmethod
    def inform_object_drawn(cls, player: Player, tower: int, choice_pair: list):
        pass
