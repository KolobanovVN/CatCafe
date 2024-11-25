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
        actions = house.valid_actions(player_dice, centre_dice)
        if len(actions) == 0: return None
        return choice(actions)
