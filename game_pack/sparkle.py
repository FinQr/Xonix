import random
from game_pack.params import *


class Sparkle:
    dirs_offsets = [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1)
    ]

    def __init__(self):
        random.seed()
        self.row = random.randint(BORDER, (ROWS_COUNT - BORDER - 1))
        self.col = random.randint(BORDER, (COLS_COUNT - BORDER - 1))
        self.delta_row, self.delta_col = self.dirs_offsets[random.randint(0, 3)]
