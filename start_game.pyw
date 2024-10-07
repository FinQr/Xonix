from game_pack.pythonix import game
from game_pack.menu import Menu
def main():
    menu = Menu()
    menu.show_menu()
    game(menu)
main()
