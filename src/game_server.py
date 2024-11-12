import json

from src.dice import Dice, DiceValues
from src.dice import DiceValues as DV
from src.player import Player
from src.game_state import GameState
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types
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
        self.player_types = player_types
        self.game_state = game_state

    @classmethod
    def load_game(cls, filename):
        with open(filename, 'r') as file_in:
            data = json.load(file_in)
            game_state = GameState.load(data)
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types = player_types, game_state = game_state)


    def save(self, filename):
        data = self.save_to_dict()
        with open(filename, 'w') as file_out:
            json.dumps(data, file_out, indent = 4)

    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data

    @classmethod
    def new_game(cls):
        player_count = cls.request_player_count()
        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name = name, player_type = all_player_types.Bot)
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
        print("Игра окончена")

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

        while True:
            try:
                kind = input("Какой это игрок?: ")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print("Виды игроков: Bot, Human")
        return name, kind

    def make_new_dices(self) -> GamePhase:
        print(f'Раунд {self.game_state.round_g}')
        self.game_state.dices_normal = [Dice() for _ in range(len(self.player_types)+1)]
        for i in range(len(self.game_state.dices_normal)): self.game_state.dices_normal[i].roll()
        return GamePhase.CHOOSE_DICE

    def choose_dice_phase(self) -> GamePhase:
        print(f'Фаза выбора кубика, ход {self.game_state.current_player().name}')
        current_player = self.game_state.current_player()
        print(f'Кубики: {self.game_state.dices_normal}')
        interaction = self.player_types[current_player]
        choice_dice = interaction.choose_dice(self.game_state.dices_normal)
        self.game_state.take_dice(choice_dice)
        self.inform_all("inform_dice_chosen", current_player, choice_dice)
        return GamePhase.NEXT_PLAYER

    def draw_object_phase(self) -> GamePhase:
        print(f'Фаза рисования предмета, ход {self.game_state.current_player().name}')
        current_player = self.game_state.current_player()
        interaction = self.player_types[current_player]
        pair = None
        print(f'Центральный кубик: {self.game_state.dices_normal}')
        print(f'Кубик: {current_player.dice}')
        print(f'Дом: {current_player.house.print()}')
        tower, choice_pair = interaction.draw_object(current_player.house, current_player.dice, self.game_state.dices_normal[0])
        if choice_pair is not None:
            pair_raw = current_player.house.valid_pairs(tower, current_player.dice, self.game_state.dices_normal[0])
            pair = pair_raw[choice_pair-1]
            self.game_state.draw_object(tower, choice_pair)
        else:
            current_player.dice = Dice(DiceValues.EMPTY)
        self.inform_all("inform_object_drawn", current_player, tower, pair)
        return GamePhase.NEXT_PLAYER

    def check_towers_phase(self) -> GamePhase:
        print('Фаза подсчёта очков')
        towers = [player.house.count_filled_columns() for player in self.player_types]
        if max(towers) >= 3:
            print('Обнаружен игрок с 3 и более заполненными башнями!')
            #null = input() # Трассировка игры!
            return GamePhase.COUNT_SCORE
        else:
            print('Раунд закончен.')
            #null = input()  # Трассировка игры!
            self.game_state.round_g += 1; self.game_state.phase = 0
            return GamePhase.NEW_DICES

    def count_score(self) -> list:
        y_players = [player.house.count_yarns() for player in self.player_types]
        y_max = [] #Надо придумать, как из [[x, x, x, x, x], [y, y, y, y, y], ...] сделать [z, z, z, z, z], где z = max(x, y, ...)
        return [player.house.count_final_score(y_max) for player in self.player_types]

    def next_player(self) -> GamePhase:
        self.game_state.next_player()
        if len(self.game_state.dices_normal) > 1:
            return GamePhase.CHOOSE_DICE
        elif self.game_state.current_player().dice != Dice(DV.EMPTY):
            return GamePhase.DRAW_OBJECT
        else:
            return GamePhase.CHECK_TOWERS

    def declare_winner(self) -> GamePhase:
        scores = GameServer.count_score()
        max_score = max(scores)
        # Выводим очки
        print('Очки игроков:')
        for i in range(len(scores)):
            print(f"{self.game_state.players[i]}: {scores[i]}")
        # Выводим победителей
        for i in range(len(scores)):
            if scores[i] == max_score: print(f"{self.game_state.players[i]} победитель!")
        return GamePhase.GAME_END

    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)

def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
    else:
        server = GameServer.new_game()
    server.run()

if __name__ == "__main__":
    __main__()
