import pygame
from params import *


def create_board():
    board = []
    for i in range(0, ROWS_COUNT):
        row = [1 if (5 <= j <= 194) and (5 <= i <= 114) else 0 for j in range(0, COLS_COUNT)]
        board.append(row)
    return board


def draw_background(sc, board):
    for row in range(0, ROWS_COUNT):
        for col in range(0, COLS_COUNT):
            if board[row][col] == 0:
                color = COLOR_BACK_1 if (row + col) % 2 == 0 else COLOR_BACK_2
            if board[row][col] == 1:
                color = COLOR_FRONT_1 if (row + col) % 2 == 0 else COLOR_FRONT_2
            pygame.draw.rect(sc, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
