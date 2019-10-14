FPS = 50

# Размер одной ячейки
CELL_SIZE = 5

# Количество ячеек по горизонтали (строк) и вертикали (столбцов)
ROWS_COUNT = 120
COLS_COUNT = 200

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

# Цвета фона
COLOR_BACK_1 = (50, 50, 50)
COLOR_BACK_2 = (40, 40, 40)

# Цвета переднего плана
COLOR_FRONT_1 = (0, 120, 220)
COLOR_FRONT_2 = (0, 110, 210)

# Цвет игрока
COLOR_PLAYER = (255, 20, 20)

# Цвет трека
COLOR_TRACK = (50, 200, 50)

# Цвет врагов
COLOR_SPARKLE = (245, 245, 245)

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
