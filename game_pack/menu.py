import pygame
import sys
from game_pack.params import *

class Menu:
    # Определение цветов
    WHITE = (245, 245, 245)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)
    GREEN = (70, 250, 8)

    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption('Меню игры')
        pygame.font.init()
        self.font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 24)

        # Индекс текущей кнопки
        self.current_option = 0
        self.options = ['Начать игру', 'Выйти']
        self.pause = ['Продолжить игру', 'Начать заново', 'Выйти']

    def draw_text(self, surface, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def draw_button(self, surface, text, font, color, rect, border_color, background_color, selected):
        if selected:
            background_color = self.GREEN  # Изменение цвета кнопки, если она выбрана
        pygame.draw.rect(surface, background_color, rect)
        pygame.draw.rect(surface, border_color, rect, 2)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)
    # окно меню
    def show_menu(self):
        menu = True
        while menu:
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
                            return
                        elif self.current_option == 1:  # Выйти
                            pygame.quit()
                            sys.exit()

            self.window.fill(self.WHITE)

            # Отрисовка заголовка меню
            self.draw_text(self.window, 'Меню игры', self.font, self.BLACK, SCREEN_W // 2 - 100, 100)

             # Определение кнопок меню
            start_button = pygame.Rect(SCREEN_W // 2 - 100, 250, 200, 50)
            quit_button = pygame.Rect(SCREEN_W // 2 - 100, 350, 200, 50)
            # Отрисовка кнопок меню
            self.draw_button(self.window, 'Начать игру', self.button_font, self.BLACK, start_button, self.BLACK, self.WHITE, self.current_option == 0)
            self.draw_button(self.window, 'Выйти', self.button_font, self.BLACK, quit_button, self.BLACK, self.WHITE, self.current_option == 1)

            pygame.display.update()
    # окно паузы        
    def show_pause(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_option = (self.current_option - 1) % len(self.pause)
                    elif event.key == pygame.K_DOWN:
                        self.current_option = (self.current_option + 1) % len(self.pause)
                    elif event.key == pygame.K_RETURN:  # Клавиша "ввод"
                        if self.current_option == 0:  # Продолжить игру
                            return True
                        elif self.current_option == 1:
                            return False
                        elif self.current_option == 2:  # Выйти
                            pygame.quit()
                            sys.exit()

            self.window.fill(self.WHITE)

            # Отрисовка заголовка меню
            self.draw_text(self.window, 'Пауза', self.font, self.BLACK, SCREEN_W // 2 - 100, 100)

             # Определение кнопок меню
            continue_button = pygame.Rect(SCREEN_W // 2 - 100, 250, 200, 50)
            restart_button = pygame.Rect(SCREEN_W // 2 - 100, 350, 200, 50)
            quit_button = pygame.Rect(SCREEN_W // 2 - 100, 450, 200, 50)
            # Отрисовка кнопок меню
            self.draw_button(self.window, self.pause[0], self.button_font, self.BLACK, continue_button, self.BLACK, self.WHITE, self.current_option == 0)
            self.draw_button(self.window, self.pause[1], self.button_font, self.BLACK, restart_button, self.BLACK, self.WHITE, self.current_option == 1)
            self.draw_button(self.window, self.pause[2], self.button_font, self.BLACK, quit_button, self.BLACK, self.WHITE, self.current_option == 2)

            pygame.display.update()