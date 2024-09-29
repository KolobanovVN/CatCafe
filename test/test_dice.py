import pytest

from src.dice import Dice


def test_init():
    d1 = Dice(5)
    assert d1.value == 5
    d2 = Dice(2)
    assert d2.value == 2
    d3 = Dice()
    assert d3.value == 0

    with pytest.raises(ValueError):
        Dice(-1)
    with pytest.raises(ValueError):
        Dice(8)
    with pytest.raises(ValueError):
        Dice('bug')


def test_eq():
    d1 = Dice(5)
    d2 = Dice(5)
    d3 = Dice(2)
    d4 = Dice(3)
    d5 = Dice(1)

    assert d1 == d2
    assert d1 != d3
    assert d1 != d4
    assert d1 != d5


def test_save():
    d1 = Dice(5)
    assert d1.save() == 5
    d2 = Dice(2)
    assert d2.save() == 2
    d3 = Dice(1)
    assert d3.save() == 1


def test_load():
    n = 5
    d = Dice.load(n)
    assert d == Dice(5)
    n = 1
    d = Dice.load(n)
    assert d == Dice(1)

    with pytest.raises(ValueError):
        n = 'bug'
        Dice.load(n)


def test_roll():
    d = Dice()
    n = [0, 0, 0, 0, 0, 0]
    for i in range(1000):
        d.roll()
        assert d.value in range(1,7)
    for i in range(1200):
        d.roll()
        n[d.value-1] += 1
    for i in range(1,7):
        assert 150 < n[i-1] < 250


def test_char():
    d1 = Dice(5)
    d2 = Dice(2)
    d3 = Dice()
    assert d1.char() == 'P'
    assert d2.char() == 'Y'
    assert d3.char() == 'E'


def test_word():
    d1 = Dice(5)
    d2 = Dice(7)
    d3 = Dice()
    assert d1.word() == 'PILLOW'
    assert d2.word() == 'INVALID'
    assert d3.word() == 'EMPTY'


def test_names():
    assert Dice.EMPTY == 0
    assert Dice.INVALID == 7
    assert Dice.DISH == 4