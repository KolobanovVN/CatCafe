from random import choice

from src.player_interaction import PlayerInteraction

class DummyAI(PlayerInteraction):

    @classmethod
    def choose_dice(cls, dices):
        return choice([dice.value for dice in dices])

    @classmethod
    def draw_object(cls, valid_pairs):
        if len(valid_pairs) == 0: return None
        else: return choice(range(1,6)), valid_pairs.index(choice(valid_pairs)) + 1

    @classmethod
    def inform_dice_chosen(cls):
        pass

    @classmethod
    def inform_object_drawn(cls):
        pass
