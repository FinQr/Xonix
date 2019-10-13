from params import *


class Board:

    def __init__(self, player):
        # Заполняем ячейки
        self.cells = []
        for i in range(0, ROWS_COUNT):
            row = [FRONT_CELL if (BORDER <= j <= (COLS_COUNT - BORDER - 1)) and (
                    BORDER <= i <= (ROWS_COUNT - BORDER - 1)) else BACK_CELL for j in
                   range(0, COLS_COUNT)]
            self.cells.append(row)

        # Сохраняем ссылку на игрока
        self.player = player

    # Метод смещает игрока и врагов
    def next_position(self):
        # Смещаем игрока
        if self.player.current_dir != NONE:
            self.player.move()
            if self.is_invalid_position(self.player.row, self.player.col):
                self.player.op_move()
                self.player.set_current_dir(NONE)

    # Метод возвращает содержимое ячейки
    def get_cell_content(self, row, col):
        if row == self.player.row and col == self.player.col:
            return PLAYER_CELL
        return self.cells[row][col]

    # Метод проверяет выход за пределы поля
    @staticmethod
    def is_invalid_position(row, col):
        if (row < 0) or (row > ROWS_COUNT) or (col < 0) or (col > COLS_COUNT):
            return True
        return False
