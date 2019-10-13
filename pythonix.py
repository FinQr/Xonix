import pygame
from player import Player
from board import Board
from params import *
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT

# Игрок
player = None

# Игровое поле
board = None

# Поверхность
sc = None


def game():
    global player, board, sc

    pygame.init()
    sc = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()

    # Создаем нового игрока
    player = Player()

    # Создаем новое игровое поле и помещаем на него игрока
    board = Board(player)

    # Отрисовываем игровое поле полностью
    draw_game_field(0, 0, ROWS_COUNT, COLS_COUNT)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                player.set_current_dir(LEFT)
            if event.key == K_RIGHT:
                player.set_current_dir(RIGHT)
            if event.key == K_UP:
                player.set_current_dir(TOP)
            if event.key == K_DOWN:
                player.set_current_dir(DOWN)

        # Смещаем игрока и врагов
        board.next_position()

        # Отрисовываем игрока
        draw_game_field(player.row - 1, player.col - 1, player.row + 1, player.col + 1)

        clock.tick(FPS)


# Отрисовываем игровое поле
def draw_game_field(row_0, col_0, row_1, col_1):
    if row_0 < 0:
        row_0 = 0
    if col_0 < 0:
        col_0 = 0
    if row_1 >= ROWS_COUNT:
        row_1 = (ROWS_COUNT - 1)
    if col_1 >= COLS_COUNT:
        col_1 = (COLS_COUNT - 1)
    for row in range(row_0, (row_1 + 1)):
        for col in range(col_0, (col_1 + 1)):
            color = get_color_cell(row, col)
            pygame.draw.rect(sc, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()


# Получаем цвет ячейки в зависимости от её содержимого
def get_color_cell(row, col):
    cell_content = board.get_cell_content(row, col)
    if cell_content == BACK_CELL:
        return COLOR_BACK_1 if (row + col) % 2 == 0 else COLOR_BACK_2
    if cell_content == FRONT_CELL:
        return COLOR_FRONT_1 if (row + col) % 2 == 0 else COLOR_FRONT_2
    if cell_content == PLAYER_CELL:
        return COLOR_PLAYER
