import pygame

from src.dice import Dice
from src.resource import RESOURCE as RSC


class ViewDice:
    SIZE = RSC['dice_size']
    BORDER = RSC['dice_border']
    SELECTED_COLOR = 'darkgreen'

    def __init__(self, dice: Dice, x: int = 0, y: int = 0):
        self.dice = dice
        self.x = x
        self.y = y
        self.selected = False
        img = pygame.image.load("img/dice1.png")
        self.image = pygame.transform.scale(img, (self.SIZE, self.SIZE))

    def redraw(self, display: pygame.Surface):
        if self.selected:
            border = (
                self.x - self.BORDER,
                self.y - self.BORDER,
                self.SIZE + 2 * self.BORDER,
                self.SIZE + 2 * self.BORDER,
            )
            display.fill(self.SELECTED_COLOR, border)
        img = self.image
        display.blit(img, (self.x, self.y))

    def event_processing(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.selected = not self.selected
