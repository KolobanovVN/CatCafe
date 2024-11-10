from src.dice import Dice
from src.house import House
from src.player_interaction import PlayerInteraction


class Human(PlayerInteraction):

    @classmethod
    def choose_dice(cls, dices):
        while True:
            try:
                dice_int = int(input("Выберите кубик: "))
                dice = Dice.load(dice_int)
                if dice in dices:
                    return dice.value
                else:
                    print("Такого кубика нет!")
            except ValueError:
                print("Надо вводить число")

    @classmethod
    def draw_object(cls, house: House, player_dice: Dice, centre_dice: Dice):
        while True:
            try:
                tower = int(input("Выберите столбец: "))
                valid_pairs = house.valid_pairs(tower, player_dice, centre_dice)
                if len(valid_pairs) == 0:
                    print("Тут нет доступных вариантов.")
                    answer = str(input("Выбор другой башни (введите OTHER) или пропуск хода (введите не OTHER)? "))
                    if answer == "OTHER":
                        continue
                    else:
                        return None
                if len(valid_pairs) > 0:
                    answer = (int
(f'Выберите действие: {centre_dice.word()} на {player_dice.value} или {player_dice.word()} на {centre_dice.value}: '))
                    if 0 < answer <= len(valid_pairs): return tower, answer
                    else: raise ValueError
            except ValueError:
                print("Ошибка ввода, повторите ещё раз")
