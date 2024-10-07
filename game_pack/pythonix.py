import pygame
from game_pack.player import Player
from game_pack.sparkle import Sparkle
from game_pack.board import Board
from game_pack.params import *
from game_pack.menu import Menu
from pygame.locals import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE

# Игрок
player = None

# Враги
sparkles = None
 
# Игровое поле
board = None

# Поверхность отрисовки
sc = None

# Загрузка изображения фона
background_image = pygame.image.load("Antichnost.jpg")

def game(Menu):
    global player, sparkles, board, sc

    pygame.init()
    sc = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()

    # Инициализация шрифта
    font = pygame.font.Font(None, 36)

    timer_interval = 30 # 30 секунд

    # Текущий уровень
    level = 1

    while True:
        # Формируем заголовок окна
        pygame.display.set_caption('Xonix. Level - ' + str(level))

        # Создаем нового игрока
        player = Player()
        menu = Menu
        # Создаем врагов
        sparkles = []
        for i in range(0, level):
            sparkles.append(Sparkle())

        # Создаем новое игровое поле и помещаем на него игрока
        board = Board(player, sparkles)

        width, height, min_col, min_row = get_front_area(board)
        
        # # Отрисовываем фон
        # sc.blit(background_image, (10, 10))
        # Отрисовываем игровое поле полностью
        draw_game_field(width, height, min_col, min_row)
        

        current_time = timer_interval  # Сброс времени на начало уровня

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        player.set_dir(LEFT)
                    elif event.key == K_RIGHT:
                        player.set_dir(RIGHT)
                    elif event.key == K_UP:
                        player.set_dir(UP)
                    elif event.key == K_DOWN:
                        player.set_dir(DOWN)
                    elif event.key == K_ESCAPE:
                        flag = menu.show_pause()
                        # Если вернулось false начинаем игру заново
                        if(flag == False):
                            game(menu)
                            return
                        draw_game_field(width, height, min_col, min_row)

            # Смещаем игрока и врагов
            result = board.next_positions()
            
            # Обновляем текущее время
            current_time -= (clock.get_time() / 1000)  # Уменьшаем время на время, прошедшее с последнего кадра

            # Проверяем, истекло ли время
            if current_time <= 0:
                break  # Выход из внутреннего цикла для перезапуска уровня

            # Если произошло удаление областей - полностью перерисовываем поле
            # В противном случае - перерисовываем только игрока и врагов
            if board.need_redraw_all:
                draw_game_field(width, height, min_col, min_row)
                board.need_redraw_all = False
            else:
                # Отрисовываем игрока
                draw_game(player.row - 1, player.col - 1, player.row + 1, player.col + 1)

                # Отрисовываем врагов
                for sparkle in sparkles:
                    draw_game(sparkle.row - 1, sparkle.col - 1, sparkle.row + 1, sparkle.col + 1)
            
            # Закрашиваем область, где отображается время (чёрным цветом)
            pygame.draw.rect(sc, (0, 0, 0), (SCREEN_W - 150, 10, 150, 30))

            # Создаем текст для отображения времени
            time_text = font.render(f"Time: {int(current_time)}", True, (255, 255, 255))  # Белый цвет текста

            # Отображаем текст на экране
            sc.blit(time_text, (SCREEN_W - 150, 10))  # Позиция текста (10, 10)

            if result == GAME_OVER:
                break

            if result == PLAYER_WIN:
                level += 1
                timer_interval += 30
                break
            
            # Обновляем экран
            pygame.display.flip()
            clock.tick(FPS)

def draw_game_field(width, height, min_col, min_row):
    
    # Отрисовываем фон
    sc.blit(pygame.transform.scale(background_image, (width, height)), (min_col * CELL_SIZE, min_row * CELL_SIZE))


    # Очищаем поверхность для отрисовки
    draw_surface.fill((0, 0, 0, 0))  # Полностью прозрачная поверхность

    for row in range(ROWS_COUNT):
        for col in range(COLS_COUNT):
            color = get_color_cell(row, col)
            if color == COLOR_IMAGE:
                continue
            else:
                pygame.draw.rect(draw_surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    sc.blit(draw_surface, (0, 0))
    pygame.display.update()

    
# Создаем поверхность для отрисовки элементов
draw_surface = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
# Отрисовываем игровое поле
def draw_game(row_0, col_0, row_1, col_1):
    row_0 = max(0, row_0)
    col_0 = max(0, col_0)
    row_1 = min(ROWS_COUNT - 1, row_1)
    col_1 = min(COLS_COUNT - 1, col_1)

    # Очищаем поверхность для отрисовки
    draw_surface.fill((0, 0, 0, 0))  # Полностью прозрачная поверхность

    for row in range(row_0, (row_1 + 1)):
        for col in range(col_0, (col_1 + 1)):
            color = get_color_cell(row, col)
            if color == COLOR_IMAGE:
                continue
            else:
                pygame.draw.rect(draw_surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    sc.blit(draw_surface, (0, 0))
    pygame.display.update()


# Получаем цвет ячейки в зависимости от её содержимого
def get_color_cell(row, col):
    cell_content = board.get_cell_content_for_draw(row, col)
    if cell_content == BACK_CELL:
        return COLOR_BACK_1
    if cell_content == FRONT_CELL:
        return COLOR_FRONT_1
    if cell_content == PLAYER_CELL:
        return COLOR_PLAYER
    if cell_content == SPARKLE_CELL:
        return COLOR_SPARKLE
    if cell_content == TRACK_CELL:
        return COLOR_TRACK
    if cell_content == IMAGE_CELL:
        return COLOR_IMAGE

def get_front_area(board):
    min_row, max_row = ROWS_COUNT, 0
    min_col, max_col = COLS_COUNT, 0

    for row in range(ROWS_COUNT):
        for col in range(COLS_COUNT):
            if board.cells[row][col] == FRONT_CELL:
                if row < min_row:
                    min_row = row
                if row > max_row:
                    max_row = row
                if col < min_col:
                    min_col = col
                if col > max_col:
                    max_col = col
    width = (max_col - min_col + 1) * CELL_SIZE
    height = (max_row - min_row + 1) * CELL_SIZE
    print(width, height)
    return width, height, min_col, min_row