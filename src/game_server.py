import inspect

from src.dice import Dice
from src.dice import DiceValues as DV
from src.house import House
from src.player import Player
from src.game_state import GameState
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

import logging

import enum

class GamePhase(enum.StrEnum):
    NEW_DICES = "New dices"
    CHOOSE_DICE = "Choose dice"
    DRAW_OBJECT = "Draw object"
    CHECK_TOWERS = "Check towers"
    COUNT_SCORE = "Count score"
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
        player_count = cls.request_player_count()
        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name = name, player_type = "DummyAI")
            player_types[player] = kind
        game_state = GameState(list(player_types.keys()))
        result = cls(player_types, game_state)
        return result

    def run(self):
        current_phase = GamePhase.NEW_DICES
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.NEW_DICES: self.make_new_dices,
                GamePhase.CHOOSE_DICE: self.choose_dice_phase,
                GamePhase.DRAW_OBJECT: self.draw_object_phase,
                GamePhase.CHECK_TOWERS: self.check_towers_phase,
                GamePhase.COUNT_SCORE: self.count_score,
                GamePhase.NEXT_PLAYER: self.next_player,
                GamePhase.DECLARE_WINNER: self.declare_winner,
            }
            current_phase = phases[current_phase]()

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("Сколько игроков? "))
                if 2 <= player_count <= 4:
                    return player_count
            except ValueError:
                pass
            print("Введите кол-во игроков от 2 до 4")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        while True:
            name = input("Как зовут игрока? ")
            if name.isalpha():
                break
            print("Имя игрока должно содержать только буквы")

        kind = "dummy_ai"
        return name, kind

    def make_new_dices(self) -> GamePhase:
        new_dices = [] # В одну строку
        for i in range(len(self.player_types)+1):
            dice = Dice()
            dice.roll()
            new_dices.append(dice)
        self.game_state.dices_normal = new_dices
        return GamePhase.CHOOSE_DICE

    def choose_dice_phase(self) -> GamePhase:
        current_player = self.game_state.current_player()
        interaction = self.player_types[current_player]
        choice_dice = interaction.choose_dice(self.game_state.dices_normal)
        self.game_state.take_dice(choice_dice)
        return GamePhase.NEXT_PLAYER

    def draw_object_phase(self) -> GamePhase:
        current_player = self.game_state.current_player()
        interaction = self.player_types[current_player]
        tower, choice_pair = interaction.draw_object(current_player.house.valid_pairs())
        if choice_pair is not None:
            self.game_state.draw_object(tower, choice_pair)
        return GamePhase.NEXT_PLAYER

    def check_towers_phase(self) -> GamePhase:
        towers = [] # В одну строку
        for i in range(len(self.player_types)):
            columns = self.player_types[i].house.count_filled_columns()
            towers.append(columns)
        if max(towers) >= 3:
            return GamePhase.COUNT_SCORE
        else:
            self.game_state.phase = 0
            return GamePhase.NEW_DICES

    def count_score(self) -> GamePhase: # Не отдельная фаза!
        scores = [] # В одну строку
        for i in range(len(self.player_types)):
            score = self.player_types[i].house.count_final_score()
            scores.append(score)
        self.game_state.turn = max(scores).index
        return GamePhase.DECLARE_WINNER

    def next_player(self) -> GamePhase:
        self.game_state.next_player()
        if self.game_state.dices_normal > 1:
            return GamePhase.CHOOSE_DICE
        elif self.game_state.current_player().dice != Dice(DV.EMPTY):
            return GamePhase.DRAW_OBJECT
        else:
            return GamePhase.CHECK_TOWERS

    def declare_winner(self) -> GamePhase:
        print(f"{self.game_state.current_player()} is the winner!")
        return GamePhase.GAME_END

    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)

def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
    server = GameServer.new_game()
    server.run()

if __name__ == "__main__":
    __main__()
