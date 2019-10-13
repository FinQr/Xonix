from params import *


class Player:
    # Смещения для направлений движения
    dirs_offsets = {
        NONE: (0, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
        UP: (-1, 0),
        DOWN: (1, 0)
    }

    def __init__(self):
        self.row = 0
        self.col = 0
        self.delta_row, self.delta_col = self.dirs_offsets[NONE]

    def set_dir(self, new_dir):
        self.delta_row, self.delta_col = self.dirs_offsets[new_dir]
