from params import *


class Board:

    def __init__(self, player, sparkles):
        # Заполняем ячейки
        self.cells = []
        for i in range(0, ROWS_COUNT):
            row = [FRONT_CELL if (BORDER <= j <= (COLS_COUNT - BORDER - 1)) and (
                    BORDER <= i <= (ROWS_COUNT - BORDER - 1)) else BACK_CELL for j in
                   range(0, COLS_COUNT)]
            self.cells.append(row)

        # Сохраняем ссылку на игрока
        self.player = player

        # Сохраняем ссылку на список крагов
        self.sparkles = sparkles

    # Метод смещает игрока и врагов
    def next_positions(self):
        # Смещаем игрока
        new_row = self.player.row + self.player.delta_row
        new_col = self.player.col + self.player.delta_col
        if self.is_valid_position(new_row, new_col):
            self.player.row = new_row
            self.player.col = new_col

        # Смещаем врагов
        for sparkle in self.sparkles:
            # проверяем отскоки
            p1 = self.cells[sparkle.row][sparkle.col + sparkle.delta_col]
            p2 = self.cells[sparkle.row + sparkle.delta_row][sparkle.col + sparkle.delta_col]
            p3 = self.cells[sparkle.row + sparkle.delta_row][sparkle.col]

            # Отскок от внешенего угла
            if p1 != BACK_CELL and p2 == BACK_CELL and p3 != BACK_CELL:
                sparkle.delta_row *= (-1)
                sparkle.delta_col *= (-1)
            # Отскок от горизонтальной линии
            if p1 != BACK_CELL and p2 == BACK_CELL and p3 == BACK_CELL:
                sparkle.delta_row *= (-1)
            # Отскок от вертикальной линии
            if p1 == BACK_CELL and p2 == BACK_CELL and p3 != BACK_CELL:
                sparkle.delta_col *= (-1)
            # Отскок от внутреннего угла
            if p1 == BACK_CELL and p2 == BACK_CELL and p3 == BACK_CELL:
                sparkle.delta_row *= (-1)
                sparkle.delta_col *= (-1)

            sparkle.row += sparkle.delta_row
            sparkle.col += sparkle.delta_col

    # Метод возвращает содержимое ячейки
    def get_cell_content(self, row, col):
        if row == self.player.row and col == self.player.col:
            return PLAYER_CELL
        for sparkle in self.sparkles:
            if sparkle.row == row and sparkle.col == col:
                return SPARKLE_CELL
        return self.cells[row][col]

    # Метод проверяет выход за пределы поля
    @staticmethod
    def is_valid_position(row, col):
        if (row < 0) or (row >= ROWS_COUNT) or (col < 0) or (col >= COLS_COUNT):
            return False
        return True
