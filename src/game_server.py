import inspect

from src.dice import Dice
from src.house import House
from src.Player import Player
from src.game_state import GameState
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

import logging

import enum

class GamePhase(enum.StrEnum):
    CHOOSE_DICE = "Choose dice"
    DRAW_OBJECT = "Draw object"
    CHECK_TOWERS = "Check towers"
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"

class GameServer:
    def __init__(self, player_types, game_state):
        self.game_state = game_state
        self.player_types = player_types

    @classmethod
    def load_game(cls):
        pass

    @classmethod
    def new_game(cls):
        pass

    def run(self):
        pass

    @staticmethod
    def request_player_count() -> int:
        pass

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        pass

    def choose_dice_phase(self) -> GamePhase:
        pass

    def draw_object_phase(self) -> GamePhase:
        pass

    def check_towers_phase(self) -> GamePhase:
        pass

    def next_player_phase(self) -> GamePhase:
        pass

    def declare_winner_phase(self) -> GamePhase:
        pass

    def inform_all(self, method: str, *args, **kwargs):
        pass

def __main__():
    server = GameServer.new_game()
    server.run()

if __name__ == "__main__":
    __main__()
