from src.dice import Dice

class Action:
    def __init__(self, dice: Dice, floor: int, tower: int):
        self.dice = dice
        self.floor = floor
        self.tower = tower

    def __repr__(self):
        return f'{self.dice.word()} на {self.floor} этаж {self.tower} башни'

    def __eq__(self, other):
        return self.dice == other.dice and self.floor == other.floor and self.tower == other.tower
