import pygame
pygame.init()
FPS = 60
WIDTH = 1280
HEIGHT = 675
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.rect(window, WHITE, (i.pos[0], i.pos[1], 10, 10))
            if i.button == 3:
                pygame.draw.rect(window, BLACK, (i.pos[0], i.pos[1], 10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
