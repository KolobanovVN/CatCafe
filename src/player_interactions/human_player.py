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
                elif len(valid_pairs) == 1:
                    print(f'Вы можете разместить {valid_pairs[0][0].word} на {valid_pairs[0][1].value} этаж')
                    answer = int(input('Нарисовать предмет (введите 1) или пропуск хода (введите 2)? '))
                    if answer == 1: return tower, answer
                    elif answer == 2: return None
                    else: raise ValueError
                elif len(valid_pairs) == 2:
                    answer = int(input(
                        f'Выберите действие: {valid_pairs[0][0].word} на {valid_pairs[0][1].value} этаж (введите 1)'
                        f'Или {valid_pairs[1][0].word} на {valid_pairs[1][1].value} (введите 2): '))
                    if 0 < answer <= len(valid_pairs):
                        answer = int(input('Нарисовать предмет (введите 1) или пропуск хода (введите 2)? '))
                        if answer == 1: return tower, answer
                        elif answer == 2: return None
                        else: raise ValueError
                    else: raise ValueError
            except ValueError:
                print("Ошибка ввода, повторите ещё раз")
