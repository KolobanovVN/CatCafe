import pygame

from src.dice import Dice
from src.ui.view_dice import ViewDice


class ViewGame:
    def __init__ (self):
        self.vdice = ViewDice(Dice(1), x = 100, y = 100)

    def model_update(self):
        pass

    def redraw(self, display: pygame.Surface):
        display.fill((255, 255, 170))
        self.vdice.redraw(display)
        pygame.display.update()

    def event_processing(self, event: pygame.event.Event):
        self.vdice.event_processing(event)
