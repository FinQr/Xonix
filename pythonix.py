from funcs import *

pygame.init()
sc = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

board = create_board()
draw_background(sc, board)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            # Начать движение игрока
            pass
        if event.type == pygame.KEYUP:
            # Прекратить движение игрока
            pass

    clock.tick(FPS)
