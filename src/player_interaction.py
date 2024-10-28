from abc import ABC, abstractmethod

class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_dice(cls, dices):
        pass

    @classmethod
    @abstractmethod
    def draw_object(cls, valid_pairs):
        pass

    @classmethod
    def inform_dice_chosen(cls):
        pass

    @classmethod
    def inform_object_drawn(cls):
        pass
