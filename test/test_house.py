import pytest

from src.dice import Dice
from src.dice import DiceValues as DV
from src.house import House


house_list1 = ['I I I I I I I I',
               'I E E M I E I I',
               'I E D E E E E I',
               'I E B I E E E I',
               'I E E E M E E I',
               'I E I E E I I I',
               'I I I I I I I I']

house_list2 = ['I I I I I I I I',
               'I E E E I E I I',
               'I B B Y E E E I',
               'I E E I E E E I',
               'I H Y Y D B B I',
               'I P I P P I I I',
               'I I I I I I I I']

house_str_pattern = '''
          7/3           
     9/5   |   8/4      
6/4   |   6__   |       
 |   6__   |   6__      
5__   |   5__   |   3/2 
 |   5__   |   5__   |  
 |    |   4__   |   4__ 
 |   4__   |   4__   |  
3__   |    |    |   3__ 
 |   3__   |   3__   |  
2__   |   2__   |    |  
 |   2__   |   2__   |  
1__   |   1__   |   1__ 
 |   1__   |   1__   |  
 |    |    |    |    |  
 =    =    =    =    ='''

house_str_1 = '''
          7/3           
     9/5   |   8/4      
6/4   |   6__   |       
 |   6__   |   6__      
5__   |   5__   |   3/2 
 |   5__   |   5__   |  
 |    |   4__   |   4__ 
 |   4__   |   4_M   |  
3_M   |    |    |   3__ 
 |   3__   |   3__   |  
2__   |   2_B   |    |  
 |   2_D   |   2__   |  
1__   |   1__   |   1__ 
 |   1__   |   1__   |  
 |    |    |    |    |  
 =    =    =    =    ='''

def test_init():
    house1 = House(None)
    house2 = House(house_list1)
    # Тест шаблонного дома
    assert house1.field[1][4] == Dice(DV.INVALID)
    assert house1.field[4][2] == Dice(DV.EMPTY)
    for i in range(8):
        assert house1.field[0][i] == Dice(DV.INVALID)
    # Тест определённого дома
    assert house2.field[1][3] == Dice(DV.MOUSE)
    assert house2.field[3][2] == Dice(DV.BUTTERFLY)
    assert house2.field[3][3] == Dice(DV.INVALID)

def test_eq():
    house1 = House(None)
    house2 = House(None)
    house3 = House(house_list1)
    assert house1 == house2
    assert house1 != house3

def test_save():
    house1 = House(None)
    house2 = House(house_list1)
    assert house1.save() == House.PATTERN
    assert house2.save() == house_list1

def test_load():
    house1 = House(house_list1)
    house2 = House.load(house_list1)
    assert house1 == house2

def test_place():
    house = House(None)
    house.place(Dice(DV.PILLOW), 4, 2)
    assert house.field[4][2] == Dice(DV.PILLOW)

    with pytest.raises(ValueError):
        house.place(Dice(DV.PILLOW), 5, 2)

    with pytest.raises(ValueError):
        house.place(Dice(DV.PILLOW), 4, 2)

def test_get_item():
    house = House(house_list1)
    assert house.get_item(1, 3) == Dice(DV.MOUSE)
    assert house.get_item(2, 2) == Dice(DV.DISH)
    assert house.get_item(3, 2) == Dice(DV.BUTTERFLY)

def test_count_filled_columns():
    house1 = House(None)
    house2 = House(house_list1)
    house3 = House(house_list2)
    assert house1.count_filled_columns() == 0
    assert house2.count_filled_columns() == 0
    assert house3.count_filled_columns() == 2

def test_count_yarns():
    house = House(house_list2)
    assert house.count_yarns() == [0, 1, 0, 2, 0]

def test_house_score():
    pass

def test_yarn_score():
    house = House(house_list2)
    y_max1 = [2, 2, 2, 2, 2]
    y_max2 = [3, 3, 3, 3, 3]
    y_max3 = [0, 1, 0, 2, 0]
    assert house.yarn_score(y_max1) == 11
    assert house.yarn_score(y_max2) == 6
    assert house.yarn_score(y_max3) == 16

def test_butterfly_score():
    house = House(house_list2)
    assert house.butterfly_score() == 12

def test_dish_score():
    pass

def test_pillow_score():
    house = House(house_list2)
    assert house.pillow_score() == 8

def test_mouse_score():
    pass

def test_tower_score():
    house1 = House(house_list1)
    house2 = House(house_list2)
    assert house1.tower_score() == 0
    assert house2.tower_score() == 6

def test_count_final_score():
    pass

def test_valid_pairs():
    dice1 = Dice(DV.YARN)
    dice2 = Dice(DV.PILLOW)
    house = House(house_list1)
    assert house.valid_pairs(4, dice1, dice2) == [[2, 5], [5, 2]]
    assert house.valid_pairs(2, dice1, dice2) == [[2, 5]]

def test_neighbors():
    pass

def test_print():
    house1 = House(None)
    house2 = House(house_list1)
    assert house1.print() == house_str_pattern
    assert house2.print() == house_str_1