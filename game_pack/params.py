FPS = 30
# размер шрифта
FONT_SIZE = 50

# Размер одной ячейки
CELL_SIZE = 8

# Количество ячеек по горизонтали (строк) и вертикали (столбцов)
ROWS_COUNT = 75
COLS_COUNT = 100

# Размеры окна в пикселях
SCREEN_W = CELL_SIZE * COLS_COUNT
SCREEN_H = CELL_SIZE * ROWS_COUNT

# Ширина границы
BORDER = 5

# Маркеры содержимого ячеек
BACK_CELL = 0
FRONT_CELL = 1
PLAYER_CELL = 2
SPARKLE_CELL = 3
TRACK_CELL = 4
IMAGE_CELL = 5


# Цвета фона
COLOR_BACK_1 = (38, 40, 44)
COLOR_BACK_2 = (40, 40, 40)

# Цвета переднего плана
COLOR_FRONT_1 = (0, 113, 213)
COLOR_FRONT_2 = (0, 110, 210)

# Цвет игрока
COLOR_PLAYER = (255, 20, 20)

# Цвет трека
COLOR_TRACK = (50, 200, 50)

# Цвет врагов
COLOR_SPARKLE = (245, 245, 245)

COLOR_IMAGE = (245, 245, 245, 0)

# Направления движения игрока
NONE = 'none'
LEFT = 'left'
RIGHT = 'right'
UP = 'top'
DOWN = 'down'

# Состояния игры
GAME_CONTINUE = 'game continue'
GAME_OVER = 'game over'
PLAYER_WIN = 'player win'
