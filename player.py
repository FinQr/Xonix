from params import *


class Player:
    # Направления движение
    directions = {
        NONE: (0, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
        TOP: (-1, 0),
        DOWN: (1, 0)
    }

    # Словарь противоположных направлений
    op_directions = {
        NONE: NONE,
        LEFT: RIGHT,
        RIGHT: LEFT,
        TOP: DOWN,
        DOWN: TOP
    }

    def __init__(self):
        self.current_dir = 'none'
        self.row = 0
        self.col = 0

    def move(self):
        delta_row, delta_col = self.directions[self.current_dir]
        self.row += delta_row
        self.col += delta_col

    def op_move(self):
        delta_row, delta_col = self.directions[self.op_directions[self.current_dir]]
        self.row += delta_row
        self.col += delta_col

    def set_current_dir(self, new_dir):
        self.current_dir = new_dir
