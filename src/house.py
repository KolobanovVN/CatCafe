from src.dice import Dice
import typing

class House:
    """Дом Котокафе"""
    
               #0 1 2 3 4 5 6 7#
    PATTERN = ["I I I I I I I I", #0
               "I E E E I E I I", #1
               "I E E E E E E I", #2
               "I E E I E E E I", #3
               "I E E E E E E I", #4
               "I E I E E I I I", #5
               "I I I I I I I I"] #6

    #Стандартные __init__, __repr__ и __eq__:
    def __init__(self, massive: None | list):
        if massive is None:
            massive = list(House.PATTERN)
        self.field = [[] for _ in range(7)]
        #Проверка массива
        if len(massive) != 7:
            raise Exception
        for i in range(7):
            if len(massive[i].split()) != 8:
                raise Exception
        #Инициализация дома
        for i in range(7):
            tower = massive[i].split()
            for j in range(8):
                self.field[i].append(Dice(Dice.VALUES_SHORT.index(tower[j])))
            tower = None

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        pass

    #Методы сохранения и загрузки:
    def save(self) -> list:
        pass
    
    @classmethod
    def load(cls, mas: list) -> typing.Self:
        pass

    #Методы размещения и просмотра кости:
    def place(self):
        pass

    def get_item(self):
        pass

    #Методы подсчёта заполненных башен и итоговых очков:
    def count_filled_columns(self) -> int:
        pass

    def count_final_score(self) -> int:
        pass

    #Методы вычисления очков для отдельных предметов:
    def count_house_score(self) -> int:
        pass

    def count_yarn_score(self) -> int:
        pass

    def count_butterfly_score(self) -> int:
        pass

    def count_dish_score(self) -> int:
        pass

    def count_pillow_score(self) -> int:
        pass

    def count_mouse_score(self) -> int:
        pass
