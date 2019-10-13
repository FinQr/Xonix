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

        # Отрисовываем поле
        draw_game_field()

        clock.tick(FPS)


# Отрисовываем игровое поле
def draw_game_field():
    for row in range(0, ROWS_COUNT):
        for col in range(0, COLS_COUNT):
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
