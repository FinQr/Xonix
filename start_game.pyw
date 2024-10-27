from game_pack.pythonix import game
from game_pack.menu import Menu
def main():
    # Создаем объект меню
    menu = Menu()

    # Запускаем главное меню и проверяем, что выбрал пользователь
    while True:
        choice = menu.show_menu()  # Предположим, что show_menu возвращает выбор пользователя

        if choice == "start_game":
            result = game(menu)  # Запускаем игру и получаем результат паузы
            if result == "exit_to_menu":
                continue  # Вернуться в меню
        elif choice == "exit":
            break  # Выход из приложения

# Запуск программы
if __name__ == "__main__":
    main()
