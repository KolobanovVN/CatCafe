import pytest

from src.dice import Dice


def test_init():
    d1 = Dice(5)
    assert d1.value == 5
    assert d1.value_char == 'P'
    d2 = Dice(2)
    assert d2.value == 2
    assert d2.value_char == 'A'
    d3 = Dice()
    assert d3.value == 1
    assert d3.value_char == 'H'

    with pytest.raises(ValueError):
        Dice(0)
    with pytest.raises(ValueError):
        Dice(7)
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
    assert repr(d1) == '5'
    assert d1.save() == '5'
    d2 = Dice(2)
    assert repr(d2) == '2'
    assert d2.save() == '2'


def test_load():
    s = '5'
    d = Dice.load(s)
    assert d == Dice(5)
    s = '1'
    d = Dice.load(s)
    assert d == Dice(1)

    with pytest.raises(ValueError):
        s = 'bug'
        Dice.load(s)


def test_roll():
    d = Dice()
    for i in range(100):
        d.roll()
        assert d.value in range(1,7)
