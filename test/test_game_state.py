import pytest

from src.dice import Dice
from src.player import Player
from src.game_state import GameState

data = {
    "round_g": 4,
    "phase": 3,
    "turn": 0,
    "dices": "4",
    "players": [
    {
      "name": "Alice",
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
      ],
    },
    {
      "name": "Bob",
      "dice": 3,
      "score": 0,
      "house":
      [
        "I I I I I I I I",
        "I E E E I E I I",
        "I E E D E E E I",
        "I E M I Y E E I",
        "I E E E H E E I",
        "I E I E E I I I",
        "I I I I I I I I"
      ],
    }
  ]
}

alice = Player.load(data["players"][0])
bob = Player.load(data["players"][1])

def test_init():
    players = [alice, bob]
    game = GameState(players=players, round_g = 4, phase = 3, turn = 0, dices = "4")
    assert game.players == players
    assert game.round_g == 4
    assert game.phase == 3
    assert game.turn == 0
    assert game.dices == [Dice(4)]

def test_eq():
    players = [alice, bob]
    game1 = GameState(players=players, round_g = 4, phase = 3, turn = 0, dices = "4")
    game2 = GameState(players=players.copy(), round_g = 4, phase = 3, turn = data["turn"], dices = "4")
    game3 = GameState(players=players, round_g = 4, phase = 3, turn = 0, dices = "4 5")
    assert game1 == game2
    assert game1 != game3

def test_save():
    players = [alice, bob]
    game = GameState(players=players, round_g = 4, phase = 3, turn = 0, dices = "4")
    assert game.save() == data

def test_load():
    game = GameState.load(data)
    assert game.save() == data

def test_current_player():
    players = [alice, bob]

    game = GameState(players=players, round_g=4, phase=3, turn=0, dices="4")
    assert game.current_player() == alice

    game = GameState(players=players, round_g=4, phase=3, turn=1, dices="4")
    assert game.current_player() == bob

def test_next_player():
    game = GameState.load(data)
    assert game.current_player() == alice

    game.next_player()
    assert game.current_player() == bob

    game.next_player()
    assert game.current_player() == alice

def test_take_dice():
    players = [alice, bob]
    game = GameState(players=players, round_g=5, phase=1, turn=0, dices="2 3 6")
    game.current_player().dice = 0
    assert game.dices == [Dice(2), Dice(3), Dice(6)]

    game.take_dice(3)
    assert game.dices == [Dice(2), Dice(6)]
    assert game.current_player().dice == Dice(3)

def test_draw_object():
    players = [alice, bob]
    game = GameState(players=players, round_g=5, phase=2, turn=0, dices="2")

    assert game.dices == [Dice(2)]
    assert game.current_player().dice == Dice(3)

    game.draw_object(4, 1)
    assert game.current_player().house.field[4][3] == Dice(2)

def test_get_y_max():
    y_players = [[0, 0, 1, 2, 1], [3, 3, 1, 1, 0]]
    y_max = GameState.get_y_max(y_players)
    assert y_max == [3, 3, 1, 2, 1]
