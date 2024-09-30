import pytest

from src.dice import Dice
from src.house import House


house_list1 = ['I I I I I I I I',
               'I E E M I E I I',
               'I E D E E E E I',
               'I E B I E E E I',
               'I E E E M E E I',
               'I E I E E I I I',
               'I I I I I I I I']

def test_init():
    house1 = House(None)
    house2 = House(house_list1)
    # Тест шаблонного дома
    assert house1.field[1][4] == Dice(Dice.INVALID)
    assert house1.field[4][2] == Dice(Dice.EMPTY)
    for i in range(8):
        assert house1.field[0][i] == Dice(Dice.INVALID)
    # Тест определённого дома
    assert house2.field[1][3] == Dice(Dice.MOUSE)
    assert house2.field[3][2] == Dice(Dice.BUTTERFLY)
    assert house2.field[3][3] == Dice(Dice.INVALID)

def test_eq():
    house1 = House(None)
    house2 = House(None)
    house3 = House(house_list1)

    assert house1 == house2
    assert house1 != house3

def test_save():
    house1 = House(None)
    house2 = House(house_list1)
    assert house1.save == House.PATTERN
    assert house2.save == house_list1

def test_load():
    house1 = House(house_list1)
    house2 = House.load(house_list1)
    assert house1 == house2

def test_place():
    house = House(None)
    house.place(Dice(Dice.PILLOW), 4, 2)
    assert house.field[4][2] == Dice(Dice.PILLOW)

    with pytest.raises(ValueError):
        house.place(Dice(Dice.PILLOW), 5, 2)
