from random import randrange

from src.player_interaction import PlayerInteraction

class Bot(PlayerInteraction):

    @classmethod
    def choose_dice(cls, dices): # Упрости!
        random_index = randrange(len(dices))
        choice_dice = dices[random_index].value
        return choice_dice

    @classmethod
    def draw_object(cls, valid_pairs): # Упрости!
        if len(valid_pairs) == 0:
            choice_pair = -1
        elif len(valid_pairs) == 1:
            choice_pair = 1
        else:
            choice_pair = randrange(1, 3)
        return choice_pair

    @classmethod
    def inform_dice_chosen(cls):
        pass

    @classmethod
    def inform_object_drawn(cls):
        pass
