from src.game_state import GameState

y_players = [[0, 0, 1, 2, 1], [3, 3, 1, 1, 0]]
y_max = GameState.get_y_max(y_players)
print(y_max)