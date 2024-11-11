from src.dice import Dice, DiceValues
from src.player import Player


class GameState:
    """Состояние игры Котокафе"""

    # Стандартные __init__, __eq__:
    def __init__(self, players: list[Player], round_g: int = 1, phase: int = 0, turn: int = 0, dices: str = ''):
        self.players: list[Player] = players
        self.round_g: int = round_g
        self.phase: int = phase
        self.turn: int = turn
        self.dices_normal = []
        raw_dices = dices.split()
        for i in raw_dices:
            self.dices_normal.append(Dice(int(i)))

    def __eq__(self, other):
        if self.players != other.players:
            return False
        if self.round_g != other.round_g:
            return False
        if self.phase != other.phase:
            return False
        if self.turn != other.turn:
            return False
        if self.dices_normal != other.dices_normal:
            return False
        return True

    # Методы сохранения и загрузки:
    def save(self) -> dict:
        return {
            "round_g": self.round_g,
            "phase": self.phase,
            "turn": self.turn,
            "dices": ' '.join(str(self.dices_normal[i].value) for i in range(len(self.dices_normal))),
            "players": [p.save() for p in self.players],
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]
        return cls(
            players = players,
            round_g = int(data["round_g"]),
            phase = int(data["phase"]),
            turn = int(data["turn"]),
            dices = str(data["dices"]),
        )

    # Другие методы:
    def current_player(self) -> Player:
        return self.players[self.turn]

    def next_player(self):
        """Ход переходит к следующему игроку."""
        n = len(self.players)
        self.turn = (self.turn + 1) % n

    def take_dice(self, choice_dice: int):
        """Текущий игрок берёт кубик."""
        self.current_player().dice = Dice(choice_dice)
        self.dices_normal.remove(Dice(choice_dice))

    def draw_object(self, tower: int, choice_pair: int):
        """Текущий игрок рисует у себя объект"""
        pairs = self.current_player().house.valid_pairs(tower, self.current_player().dice, self.dices_normal[0])
        self.current_player().house.field[tower][pairs[choice_pair - 1][0]] = Dice(pairs[choice_pair - 1][1])
        self.current_player().dice = Dice(DiceValues.EMPTY)
