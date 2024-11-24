from random import choice

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
                valid_actions = house.valid_actions(player_dice, centre_dice)
                if len(valid_actions) == 0:
                    print("Нет доступных вариантов.")
                    return None
                else:
                    print(f'Вы можете сходить следующим образом:')
                    print(f'0. Пропуск хода')
                    number = 1
                    for action in valid_actions:
                        print(f'{number}. Разместить {action}')
                        number += 1
                    choice_action = int(input('Введите номер варианта хода: '))
                    if choice == 0:
                        return None
                    else:
                        return valid_actions[choice_action-1]
            except ValueError:
                print("Ошибка ввода, повторите ещё раз")
            except IndexError:
                print("Ошибка ввода, повторите ещё раз")
