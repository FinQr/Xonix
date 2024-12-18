from game_pack.params import *
import pygame

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
        self.current_dir = NONE  # Текущее направление

    def set_dir(self, new_dir):
        # Проверяем, не является ли новое направление противоположным текущему
        if (self.current_dir == LEFT and new_dir == RIGHT) or \
           (self.current_dir == RIGHT and new_dir == LEFT) or \
           (self.current_dir == UP and new_dir == DOWN) or \
           (self.current_dir == DOWN and new_dir == UP):

            self.delta_row, self.delta_col = self.dirs_offsets[self.current_dir]
        else:
            self.current_dir = new_dir
            self.delta_row, self.delta_col = self.dirs_offsets[new_dir]
