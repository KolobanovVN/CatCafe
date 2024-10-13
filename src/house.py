from src.dice import Dice
from src.dice import DiceValues as DV
import typing

class House:
    """Дом Котокафе"""
    # Nota bene: i - это башня, a j - это этаж!

               #0 1 2 3 4 5 6 7#
    PATTERN = ['I I I I I I I I', #0
               'I E E E I E I I', #1
               'I E E E E E E I', #2
               'I E E I E E E I', #3
               'I E E E E E E I', #4
               'I E I E E I I I', #5
               'I I I I I I I I'] #6

    EVEN = [[0, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
    ODD  = [[0, 1], [1, 1], [1, 0],  [0, -1], [-1, 0],  [-1, 1]]

    SCORES = ['null', 4, 5, 3, 4, 2]

    # Стандартные __init__, __repr__ и __eq__:
    def __init__(self, array: None | list):
        if array is None: array = list(House.PATTERN)
        self.field = [[] for _ in range(len(House.PATTERN))]
        # Проверка массива
        if len(array) != len(House.PATTERN): raise ValueError
        for i in range(len(House.PATTERN)):
            if len(array[i].split()) != len(House.PATTERN[i].split()): raise ValueError
        # Инициализация дома
        for i in range(len(House.PATTERN)):
            tower = array[i].split()
            for j in range(len(tower)):
                self.field[i].append(Dice(Dice.VALUES_SHORT.index(tower[j])))

    def __repr__(self):
        return f'{self.save()}'

    def __eq__(self, other):
        if isinstance(other, list): other = House.load(other)
        return self.field == other.field

    # Методы сохранения и загрузки:
    def save(self) -> list:
        return [(' '.join(Dice.VALUES_SHORT[self.field[i][j].value] for j in range(len(self.field[i])))) \
                for i in range(len(self.field))]
    
    @classmethod
    def load(cls, mas: list) -> typing.Self:
        return cls(mas)

    # Методы размещения и просмотра кости:
    def place(self, dice: Dice, tower: int, floor: int):
        if self.field[tower][floor] != Dice(DV.EMPTY): raise ValueError
        self.field[tower][floor] = dice

    def get_item(self, tower: int, floor: int) -> Dice:
        return self.field[tower][floor]

    # Методы подсчёта заполненных башен и итоговых очков:
    def count_filled_columns(self) -> int:
        fc = 0
        for i in range(1,6):
            if Dice(DV.EMPTY) not in self.field[i]: fc += 1
        return fc

    def count_final_score(self, y_max: list) -> int:
        return self.house_score() + self.yarn_score(y_max) + self.butterfly_score() \
        + self.dish_score() + self.pillow_score() + self.mouse_score() + self.tower_score()

    # Методы вычисления очков для отдельных предметов:
    def house_score(self) -> int:
        return 0

    def yarn_score(self, max_values: list) -> int:
        values = self.count_yarns()
        score = 0
        for i in range(5):
            if values[i] == max_values[i]:  score += 8
            elif values[i] > 0:             score += 3
            elif values[i] == 0:            score += 0
            else: raise ValueError
        return score

    def butterfly_score(self) -> int:
        score = 0
        for i in range(1, 6):
            for j in range(1, 7):
                if self.field[i][j] == Dice(DV.BUTTERFLY):
                    score += 3
        return score

    def dish_score(self) -> int:
        return 0

    def pillow_score(self) -> int:
        score = 0
        for i in range(1, 6):
            for j in range(1, 7):
                if self.field[i][j] == Dice(DV.PILLOW):
                    score += j
        return score

    def mouse_score(self) -> int:
        return 0

    def tower_score(self) -> int:
        score = 0
        for i in range(1,6):
            if Dice(DV.EMPTY) not in self.field[i]:
                score += self.SCORES[i]
        return score

    # Методы подсчёта клубков, вычисления соседей:
    def count_yarns(self) -> list:
        num_of_yarns = [0 for _ in range(5)]
        for i in range(1, 6):
            for j in range(1, 7):
                if self.field[i][j] == Dice(DV.YARN): num_of_yarns[i-1] += 1
        return num_of_yarns
