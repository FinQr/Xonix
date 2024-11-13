from game_pack.params import *


class Board:

    def __init__(self, player, sparkles):
        # Заполняем ячейки
        self.cells = []
        for i in range(0, ROWS_COUNT):
            row = [FRONT_CELL if (BORDER <= j <= (COLS_COUNT - BORDER - 1)) and (
                    BORDER <= i <= (ROWS_COUNT - BORDER - 1)) else BACK_CELL for j in
                   range(0, COLS_COUNT)]
            self.cells.append(row)

        # Подсчитываем начальную площадь поля
        self.begin_area = self.calc_area()

        # Сохраняем ссылку на игрока
        self.player = player

        # Сохраняем ссылку на список крагов
        self.sparkles = sparkles

        # Устанавливаем признак необходимости полной отрисовки поля
        self.need_redraw_all = False

    def get_current_state(self):
        # Создаем копию текущего состояния ячеек
        return [row[:] for row in self.cells]
    

    # Метод смещает игрока и врагов
    def next_positions(self):
        # Смещаем игрока
        old_row = self.player.row
        old_col = self.player.col
        new_row = self.player.row + self.player.delta_row
        new_col = self.player.col + self.player.delta_col
        if self.is_valid_position(new_row, new_col):
            self.player.row = new_row
            self.player.col = new_col

            # Проверяем условие поражения - игрок столкнулся с врагом, либо игрок столкнулся с треком
            if self.is_collision():
                self.player.row = old_row
                self.player.col = old_col
                return GAME_OVER

            # Отслеживаем создание трека
            if self.cells[old_row][old_col] == FRONT_CELL:
                self.cells[old_row][old_col] = TRACK_CELL

            # Проверяем завершение создания трека и условие победы
            if self.cells[old_row][old_col] == TRACK_CELL and (self.cells[new_row][new_col] == BACK_CELL or self.cells[new_row][new_col] == IMAGE_CELL):
                # Удаляем трек
                self.remove_track()
                # Удаляем все области, кроме самой большой
                self.remove_minimal_areas()
                # Устанавливаем признак необходимости полной отрисовки поля
                self.need_redraw_all = True
                # Подсчитываем текущую площадь поля
                current_area = self.calc_area()
                # Если текущая площадь составляет менее четверти от исходной - игрок победил
                if (current_area / self.begin_area) < 0.25:
                    return PLAYER_WIN

        # Смещаем врагов
        for sparkle in self.sparkles:
            new_row = sparkle.row + sparkle.delta_row
            new_col = sparkle.col + sparkle.delta_col

            p1 = self.cells[sparkle.row][new_col]
            p2 = self.cells[new_row][new_col]
            p3 = self.cells[new_row][sparkle.col]

            # Проверяем условие поражения игрока - столкновение с самим игроком или его треком
            if (new_row == self.player.row and new_col == self.player.col) or p2 == TRACK_CELL:
                return GAME_OVER

            # Отскок от внешнего угла
            if (p1 != BACK_CELL and p1 != IMAGE_CELL) and (p2 == BACK_CELL or p2 == IMAGE_CELL) and (p3 != BACK_CELL and p3 != IMAGE_CELL):
                sparkle.delta_row *= (-1)
                sparkle.delta_col *= (-1)

            # Отскок от горизонтальной линии
            if (p1 != BACK_CELL and p1 != IMAGE_CELL) and (p2 == BACK_CELL or p2 == IMAGE_CELL) and (p3 == BACK_CELL or p3 == IMAGE_CELL):
                sparkle.delta_row *= (-1)

            # Отскок от вертикальной линии
            if (p1 == BACK_CELL or p1 == IMAGE_CELL) and (p2 == BACK_CELL or p2 == IMAGE_CELL) and (p3 != BACK_CELL and p3 != IMAGE_CELL):
                sparkle.delta_col *= (-1)

            # Отскок от внутреннего угла
            if (p1 == BACK_CELL or p1 == IMAGE_CELL) and (p2 == BACK_CELL or p2 == IMAGE_CELL) and (p3 == BACK_CELL or p3 == IMAGE_CELL):
                sparkle.delta_row *= (-1)
                sparkle.delta_col *= (-1)

            sparkle.row = sparkle.row + sparkle.delta_row
            sparkle.col = sparkle.col + sparkle.delta_col

        # Возвращаем признак продолжения игры
        return GAME_CONTINUE

    # Метод удаляет с поля все области, кроме той, площадь которой максимальна
    def remove_minimal_areas(self):
        # Сперва "раскрашиваем" области
        # Текущая "краска"
        paint = 9

        # Словарь областей, состоящий из элементов 'Площадь закрашенной области':'Краска, которой эта область закрашена'
        paint_areas = {}

        # Объект для временного хранения списка ячеек
        cells_list = []

        # Смещения
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Ищем незакрашенные ячейки
        for row in range(0, ROWS_COUNT):
            for col in range(0, COLS_COUNT):
                if self.cells[row][col] == FRONT_CELL:
                    paint += 1
                    cells_list.clear()
                    cells_list.append((row, col))

                    # Площадь области, закрашенной текущей краской
                    current_area = 0

                    while True:
                        # Закрашиваем все ячейки списка
                        for r, c in cells_list:
                            self.cells[r][c] = paint
                            current_area += 1

                        # Добавляем в список новые ячейки
                        cells_list_tmp = []
                        for r, c in cells_list:
                            for dr, dc in offsets:
                                if self.cells[r + dr][c + dc] == FRONT_CELL and (r + dr, c + dc) not in cells_list_tmp:
                                    cells_list_tmp.append((r + dr, c + dc))

                        cells_list = cells_list_tmp

                        # Если новый список пуст - выходим
                        if len(cells_list) == 0:
                            break

                    # Вносим краску и площадь в словарь закрашенных областей
                    paint_areas[current_area] = paint

        

        # Перебираем краски и удаляем закрашенные ими области
        for area, paint in paint_areas.items():
        # Проверяем, есть ли враги в области
            enemy_found = any(self.cells[sparkle.row][sparkle.col] == paint for sparkle in self.sparkles)

            # Удаляем область, если в ней нет врагов
            if not enemy_found:
                for row in range(ROWS_COUNT):
                    for col in range(COLS_COUNT):
                        if self.cells[row][col] == paint:
                            self.cells[row][col] = IMAGE_CELL

        # Удаляем остатки краски
        for row in range(0, ROWS_COUNT):
            for col in range(0, COLS_COUNT):
                if self.cells[row][col] >= 10:
                    self.cells[row][col] = FRONT_CELL

    # Метод удаляет трек
    def remove_track(self):
        for row in range(0, ROWS_COUNT):
            for col in range(0, COLS_COUNT):
                if self.cells[row][col] == TRACK_CELL:
                    self.cells[row][col] = IMAGE_CELL

    # Метод возвращает содержимое ячейки для отрисовки
    def get_cell_content_for_draw(self, row, col):
        if row == self.player.row and col == self.player.col:
            return PLAYER_CELL
        for sparkle in self.sparkles:
            if sparkle.row == row and sparkle.col == col:
                return SPARKLE_CELL
        return self.cells[row][col]

    # Метод подсчитывает площадь оставшегося поля
    def calc_area(self):
        area = 0
        for row in range(0, ROWS_COUNT):
            for col in range(0, COLS_COUNT):
                if self.cells[row][col] == FRONT_CELL:
                    area += 1
        return area

    # Метод проверяет столкновление игрока с врагом, врагов с треком и игрока с треком
    def is_collision(self):
        for sparkle in self.sparkles:
            if sparkle.row == self.player.row and sparkle.col == self.player.col:
                return True
            if self.cells[sparkle.row][sparkle.col] == TRACK_CELL:
                return True
            if self.cells[self.player.row][self.player.col] == TRACK_CELL:
                return True
        return False

    # Метод проверяет выход за пределы поля
    @staticmethod
    def is_valid_position(row, col):
        if (row < 0) or (row >= ROWS_COUNT) or (col < 0) or (col >= COLS_COUNT):
            return False
        return True
