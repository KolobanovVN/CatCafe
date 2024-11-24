import pytest

from src.dice import Dice
from src.house import House
from src.player import Player

alice_house = ["I I I I I I I I",
               "I E E M I E I I",
               "I E D E E E E I",
               "I E B I E E E I",
               "I E E E M E E I",
               "I E I E E I I I",
               "I I I I I I I I"]

alice_data = {"name": "Alice",
      "dice": 6,
      "score": 0,
      "house":
      [
        "I I I I I I I I",
        "I E E M I E I I",
        "I E D E E E E I",
        "I E B I E E E I",
        "I E E E M E E I",
        "I E I E E I I I",
        "I I I I I I I I"
      ],}

def test_init():
    h = House.load(alice_house)
    p = Player(name = "Alice", dice = Dice(6), score = 0, house = h)
    assert p.name == "Alice"
    assert p.dice == Dice(6)
    assert p.score == 0
    assert p.house == h

def test_str():
    h = House.load(alice_house)
    p = Player(name = "Alice", dice = Dice(6), score = 0, house = h)
    assert str(p) == '''
Игрок: Alice
Кубик: 6
Очки:  0
Игровое поле: 
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
 =    =    =    =    =
'''

def test_eq():
    h1 = House.load(alice_house)
    h2 = House.load(alice_house)
    p1 = Player(name = "Alice", dice = Dice(6), score = 0, house = h1)
    p2 = Player(name = "Alice", dice = Dice(6), score = 0, house = h2)
    assert p1 == p2

def test_save():
    h = House.load(alice_house)
    p = Player(name = "Alice", dice = Dice(6), score = 0, house = h)
    assert p.save() == alice_data

def test_load():
    data = alice_data
    h = House.load(alice_house)
    p = Player(name = "Alice", dice = Dice(6), score = 0, house = h)
    p_from_data = Player.load(data)
    assert p == p_from_data
