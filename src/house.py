from itertools import count

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

    SAFE_TOWER = range(1, 6)
    SAFE_FLOOR = range(1, 7)

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
        for i in House.SAFE_TOWER:
            if Dice(DV.EMPTY) not in self.field[i]: fc += 1
        return fc

    def count_final_score(self, y_max: list) -> int:
        return self.house_score() + self.yarn_score(y_max) + self.butterfly_score() \
        + self.dish_score() + self.pillow_score() + self.mouse_score() + self.tower_score()

    # Методы вычисления очков для отдельных предметов:
    def house_score(self) -> int:
        score = 0
        count_h = 0
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.EMPTY):      score += 0
                elif self.field[i][j] == Dice(DV.INVALID):  score += 0
                elif self.field[i][j] == Dice(DV.MOUSE):    score += -2
                elif self.field[i][j] == Dice(DV.HOUSE):    score += 2; count_h += 1
                else: score += 1
        if count_h == 0:
            score = 0
        return score

    def yarn_score(self, max_values: list) -> int:
        values = self.count_yarns()
        score = 0
        for i in range(len(House.SAFE_TOWER)):
            if values[i] == 0:                  score += 0
            elif values[i] == max_values[i]:    score += 8
            elif values[i] > 0:                 score += 3
            else: raise ValueError
        return score

    def butterfly_score(self) -> int:
        score = 0
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.BUTTERFLY): score += 3
        return score

    def dish_score(self) -> int:
        score = 0
        unique_items = [Dice(i) for i in range(DV.HOUSE, DV.MOUSE + 1)]
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.DISH):
                    current_neighbors = self.neighbors(i, j)
                    current_unique_items = unique_items.copy()
                    for k in range(len(current_neighbors)):
                        if self.field[current_neighbors[k][0]][current_neighbors[k][1]] in current_unique_items:
                            score += 1
                            del_dice = self.field[current_neighbors[k][0]][current_neighbors[k][1]]
                            current_unique_items.remove(del_dice)
        return score

    def pillow_score(self) -> int:
        score = 0
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.PILLOW): score += j
        return score

    def mouse_score(self) -> int:
        score = 0
        remaining_mice = []
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.MOUSE): remaining_mice.append([i, j])
        while remaining_mice:
            mouse = remaining_mice.pop()
            mice = self.get_all_connected_mice(mouse, remaining_mice)
            if mice == 1: score += 2
            if mice == 2: score += 6
            if mice == 3: score += 12
            if mice == 4: score += 20
        return score

    def tower_score(self) -> int:
        score = 0
        for i in House.SAFE_TOWER:
            if Dice(DV.EMPTY) not in self.field[i]: score += self.SCORES[i]
        return score

    # Методы подсчёта клубков, вычисления действительных пар, вычисления соседей и печати:
    def count_yarns(self) -> list:
        num_of_yarns = [0 for _ in range(len(House.SAFE_TOWER))]
        for i in House.SAFE_TOWER:
            for j in House.SAFE_FLOOR:
                if self.field[i][j] == Dice(DV.YARN): num_of_yarns[i-1] += 1
        return num_of_yarns

    def valid_pairs(self, tower: int, player_dice: Dice, centre_dice: Dice) -> list:
        pairs = []
        i = player_dice.value
        j = centre_dice.value
        if self.field[tower][j] == Dice(DV.EMPTY): pairs.append([i, j])
        if self.field[tower][i] == Dice(DV.EMPTY): pairs.append([j, i])
        return pairs

    def neighbors(self, tower: int, floor: int)  -> list:
        neighbors_list = []
        if self.field[tower][floor] == Dice(DV.INVALID): raise ValueError
        if tower % 2 == 1:
            neighbors_list = [[tower + House.ODD[i][0], floor + House.ODD[i][1]] for i in range(len(House.ODD))]
        if tower % 2 == 0:
            neighbors_list = [[tower + House.EVEN[i][0], floor + House.EVEN[i][1]] for i in range(len(House.EVEN))]
        return neighbors_list

    def print(self):
        return f'''
          7/3           
     9/5   |   8/4      
6/4   |   6_{self.field[3][6].char()}   |       
 |   6_{self.field[2][6].char()}   |   6_{self.field[4][6].char()}      
5_{self.field[1][5].char()}   |   5_{self.field[3][5].char()}   |   3/2 
 |   5_{self.field[2][5].char()}   |   5_{self.field[4][5].char()}   |  
 |    |   4_{self.field[3][4].char()}   |   4_{self.field[5][4].char()} 
 |   4_{self.field[2][4].char()}   |   4_{self.field[4][4].char()}   |  
3_{self.field[1][3].char()}   |    |    |   3_{self.field[5][3].char()} 
 |   3_{self.field[2][3].char()}   |   3_{self.field[4][3].char()}   |  
2_{self.field[1][2].char()}   |   2_{self.field[3][2].char()}   |    |  
 |   2_{self.field[2][2].char()}   |   2_{self.field[4][2].char()}   |  
1_{self.field[1][1].char()}   |   1_{self.field[3][1].char()}   |   1_{self.field[5][1].char()} 
 |   1_{self.field[2][1].char()}   |   1_{self.field[4][1].char()}   |  
 |    |    |    |    |  
 =    =    =    =    ='''

    # Специальный метод для метода mouse_score()
    def get_all_connected_mice(self, mouse, remaining_mice):
        count = 1
        for neighbor in self.neighbors(mouse[0], mouse[1]):
            if neighbor in remaining_mice:
                neighbor_selected = neighbor
                remaining_mice.remove(neighbor_selected)
                count += self.get_all_connected_mice(neighbor_selected, remaining_mice)
        return count
