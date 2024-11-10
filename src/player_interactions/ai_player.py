from random import *

from src.dice import Dice
from src.house import House
from src.player_interaction import PlayerInteraction

class DummyAI(PlayerInteraction):

    @classmethod
    def choose_dice(cls, dices):
        return choice([dice.value for dice in dices])

    @classmethod
    def draw_object(cls, house: House, player_dice: Dice, centre_dice: Dice):
        for tower in range(House.SAFE_TOWER):
            valid_pairs = house.valid_pairs(tower, player_dice, centre_dice)
            if len(valid_pairs) > 0: return tower, valid_pairs.index(choice(valid_pairs)) + 1
        return None

    @classmethod
    def inform_dice_chosen(cls):
        pass

    @classmethod
    def inform_object_drawn(cls):
        pass
