import pygame
import sys
from game_pack.params import *

class Menu:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption('Меню игры')
        pygame.font.init()
        self.font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 24)
        self.txt_font = pygame.font.Font(None, 24)

        # Индекс текущей кнопки
        self.current_option = 0
        self.options = ['Начать игру','Об игре', 'Выйти']
        self.pause_options = ['Продолжить игру', 'Начать заново', 'Выйти']

    def draw_text(self, surface, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def draw_button(self, surface, text, font, color, rect, border_color, background_color, selected):
        if selected:
            background_color = GREEN  # Изменение цвета кнопки, если она выбрана
        pygame.draw.rect(surface, background_color, rect)
        pygame.draw.rect(surface, border_color, rect, 2)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

    # Основное меню
    def show_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_option = (self.current_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.current_option = (self.current_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:  # Клавиша "ввод"
                        if self.current_option == 0:  # Начать игру
                            return "start_game"
                        elif self.current_option == 1: # Об игре
                            self.show_about()
                        elif self.current_option == 2:  # Выйти
                            return "exit"

            self.window.fill(WHITE)
            self.draw_text(self.window, 'Меню игры', self.font, BLACK, SCREEN_W // 2 - 100, 100)

            # Определение и отрисовка кнопок
            start_button = pygame.Rect(SCREEN_W // 2 - 100, 250, 200, 50)
            instruction_button = pygame.Rect(SCREEN_W // 2 - 100, 350, 200, 50)
            quit_button = pygame.Rect(SCREEN_W // 2 - 100, 450, 200, 50)
            self.draw_button(self.window, 'Начать игру', self.button_font, BLACK, start_button, BLACK, WHITE, self.current_option == 0)
            self.draw_button(self.window, 'Об игре', self.button_font, BLACK, instruction_button, BLACK, WHITE, self.current_option == 1)
            self.draw_button(self.window, 'Выйти', self.button_font, BLACK, quit_button, BLACK, WHITE, self.current_option == 2)

            pygame.display.update()

    # Окно паузы
    def show_pause(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_option = (self.current_option - 1) % len(self.pause_options)
                    elif event.key == pygame.K_DOWN:
                        self.current_option = (self.current_option + 1) % len(self.pause_options)
                    elif event.key == pygame.K_RETURN:  # Клавиша "ввод"
                        if self.current_option == 0:  # Продолжить игру
                            return "continue"
                        elif self.current_option == 1:  # Начать заново
                            return "restart"
                        elif self.current_option == 2:  # Выйти в главное меню
                            return "exit_to_menu"

            self.window.fill(WHITE)
            self.draw_text(self.window, 'Пауза', self.font, BLACK, SCREEN_W // 2 - 50, 100)

            # Определение и отрисовка кнопок
            continue_button = pygame.Rect(SCREEN_W // 2 - 100, 250, 200, 50)
            restart_button = pygame.Rect(SCREEN_W // 2 - 100, 350, 200, 50)
            quit_button = pygame.Rect(SCREEN_W // 2 - 100, 450, 200, 50)
            self.draw_button(self.window, 'Продолжить игру', self.button_font, BLACK, continue_button, BLACK, WHITE, self.current_option == 0)
            self.draw_button(self.window, 'Начать заново', self.button_font, BLACK, restart_button, BLACK, WHITE, self.current_option == 1)
            self.draw_button(self.window, 'Выйти в меню', self.button_font, BLACK, quit_button, BLACK, WHITE, self.current_option == 2)

            pygame.display.update()

# Окно «Об игре»
    def show_about(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Нажатие Enter на кнопке «Назад»
                        return

            # Заливка фона окна «Об игре»
            self.window.fill((WHITE))

            # Заголовок
            self.draw_text(self.window, 'Об игре', self.font, (COLOR_BACK_1), 350, 100)

            # Кнопка «Назад»
            back_button = pygame.Rect(0, 0, 200, 50)
            pygame.draw.rect(self.window, (COLOR_TRACK), back_button) 
            pygame.draw.rect(self.window, (COLOR_BACK_1), back_button, 2)  # Цвет границы
            self.draw_text(self.window, 'Назад', self.button_font, (COLOR_BACK_1), 70, 18)

            # Текстовый блок с описанием игры
            text_box = pygame.Rect(100, 200, 620, 200)
            pygame.draw.rect(self.window, (50, 200, 50), text_box)  # Цвет заливки #32C832
            game_info = """Xonix — это увлекательная аркадная игра, в которой игрок управляет\nперсонажем, стремящимся захватить как можно больше территории на\nигровом поле. Ваша задача — обойти врагов и замкнуть участки, чтобы\nувеличить свою территорию. Чтобы пройти уровень, вам необходимо\nзахватить заданный процент территории, избегая при этом столкновений\nс врагами. Игра состоит из нескольких уровней, каждый из которых\nстановится все сложнее. Управление персонажем происходит с помощью\nклавиш WASD: W – вверх, A – влево, S – вниз, D – вправо. """
            text_lines = game_info.split("\n")
            for i, line in enumerate(text_lines):
                self.draw_text(self.window, line, self.txt_font, (COLOR_BACK_1), 110, 220 + i * 20)

            pygame.display.update()