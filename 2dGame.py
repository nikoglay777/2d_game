import pygame
from random import randint


def get_player():
    """
    the function cuses the player randomly
    tank bro 2
    rambro 1
    mechnik 3
    :return image ,rect object,n- random number of the player
    """
    n = randint(1, 3)
    player = pygame.image.load(f"player{n}.png")
    player = pygame.transform.scale(player, (0.1 * HEIGHT, 0.1 * HEIGHT ))
    player_rect = player.get_rect()
    player_rect.center = (50, HEIGHT - 50)
    return player, player_rect, n

def get_bullet(n):
    if n == 1:
        weapon = pygame.image.load("bullet.png")
        weapon = pygame.transform.scale(weapon, (50, 20))
        weapon_rect = weapon.get_rect()
        weapon_rect.left = player_rect.right
        weapon_rect.top = player_rect.bottom - 45.5

    elif n == 2:
        weapon = pygame.image.load("nedoraceta.png")
        weapon = pygame.transform.scale(weapon, (100, 20))
        weapon_rect = weapon.get_rect()
        weapon_rect.left = player_rect.right
        weapon_rect.top = player_rect.bottom - 70

    elif n == 3:
        weapon = pygame.image.load("knife.png")
        weapon = pygame.transform.scale(weapon, (100, 20))
        weapon_rect = weapon.get_rect()
        weapon_rect.left = player_rect.right
        weapon_rect.top = player_rect.bottom - 45.2
    return weapon_rect, weapon


def get_super(n):

    if n == 2:
        super = pygame.image.load("tank.png")
        super = pygame.transform.scale(super, (100, 100))
        super_rect = super.get_rect()
        super_rect.left = player_rect.right
        super_rect.top = player_rect.bottom - 70

    return super_rect, super


pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
FPS = 60
WIDTH = pygame.display.Info().current_w # 1280
HEIGHT = pygame.display.Info().current_h # 675
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# window = pygame.display.set_mode((WIDTH, HEIGHT))
lives = 3
score = 0
clock = pygame.time.Clock()
boom = pygame.mixer.Sound("boom.mp3")

pause_button = pygame.image.load("pause.png")
pause_button = pygame.transform.scale(pause_button, (40, 40))
pause_button_rect = pause_button.get_rect()
pause_button_rect.right = WIDTH

play_button = pygame.image.load("play.png")
play_button = pygame.transform.scale(play_button,  (45, 45))
play_button_rect = play_button.get_rect()
play_button_rect.right = WIDTH - pause_button.get_width()

best_button = pygame.image.load("cnopca.png")
best_button = pygame.transform.scale(best_button, (400, 150))
best_button_rect = best_button.get_rect()
best_button_rect.center = (WIDTH // 2, HEIGHT // 2 + 199)

super_rocket = pygame.image.load("nedoraceta.png")
super_rocket = pygame.transform.scale(super_rocket, (200, 40))
super_rocket_rect = super_rocket.get_rect()

menu_fon = pygame.image.load("nik.png")
menu_fon = pygame.transform.scale(menu_fon, (WIDTH, HEIGHT))

fon = pygame.image.load("forrest.jpg")
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))

game_over_fon = pygame.image.load("you are dead.png")
game_over_fon = pygame.transform.scale(game_over_fon, (WIDTH, HEIGHT))

podzkaska_pik = pygame.image.load("podzkaska.png")
podzkaska_pik = pygame.transform.scale(podzkaska_pik, (WIDTH/7, HEIGHT/7))

podzkaska_game = pygame.image.load("podzkaska_game.png")
podzkaska_game = pygame.transform.scale(podzkaska_game, (WIDTH, HEIGHT))

best_fon = pygame.image.load("best_fon.png")
best_fon = pygame.transform.scale(best_fon, (WIDTH, HEIGHT))

reg_fon = pygame.image.load("name.png")
reg_fon = pygame.transform.scale(reg_fon, (WIDTH, HEIGHT))

start = pygame.image.load("start.png")
start = pygame.transform.scale(start, (500, 200))
start_rect = start.get_rect()
start_rect.center = (WIDTH // 2, HEIGHT // 2)
game_over_fon = pygame.transform.scale(game_over_fon, (WIDTH, HEIGHT))

enemy = pygame.Rect(WIDTH, randint(40, HEIGHT - 30), 40, 40)
name_box = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 100, 400, 200)

bullets = []
x = 400
run = True
direction = "stop"
main_font = pygame.font.SysFont("Arial", 25)
best_font = pygame.font.SysFont("Comicsansms", 99)
mode = "registration"
pause = False
super_activated = False
name = ""

while run:
    if mode == "registration":
        window.blit(reg_fon, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i .type == pygame.KEYDOWN:
                if i.key == pygame.K_RETURN:
                    mode = "menu"
                elif i.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 10:
                    name += i.unicode
        pygame.draw.rect(window, WHITE, name_box, 3)
        name_text = best_font.render(name, True, BLACK)
        name_box.width = name_text.get_width() + 10
        window.blit(name_text, (name_box.x + 10, name_box.y + 10))

    elif mode == "menu":
        window.blit(menu_fon, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    run = False
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and start_rect.collidepoint(i.pos):
                    score = 0
                    lives = 3
                    player, player_rect, n = get_player()
                    enemies = []
                    for _ in range(3):
                        enemies.append(pygame.Rect(WIDTH, randint(40, HEIGHT - 30), 40, 40))
                    mode = "podzkaska"
                elif i.button == 1 and best_button_rect.collidepoint(i.pos):
                    mode = "your best"
        window.blit(start, start_rect)
        window.blit(best_button, best_button_rect)

    elif mode == "podzkaska":
        window.blit(podzkaska_game, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    mode = "menu"
                elif i.key == pygame.K_SPACE:
                    mode = "game"

    elif mode == "game":
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    direction = "up"
                elif i.key == pygame.K_DOWN:
                    direction = "down"
                elif i.key == pygame.K_SPACE:
                    bullets.append(get_bullet(n)[0])
                elif i.key == pygame.K_ESCAPE:
                    mode = "menu"
                elif i.key == pygame.K_RETURN:
                    super_rect, super = get_super(n)
                    super_rocket_rect.center = super_rect.center
                    super_rocket_rect.left = super_rect.right

                    super_activated = True
            elif i.type == pygame.KEYUP:
                direction = "stop"
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and pause_button_rect.collidepoint(i.pos):
                    pause = True
                elif i.button == 1 and play_button_rect.collidepoint(i.pos):
                    pause = False

        if not pause:
            window.blit(fon, (0, 0))
            window.blit(pause_button, pause_button_rect)
            window.blit(play_button, play_button_rect)
            pygame.draw.rect(window, BLACK, (0, 0, 160, 30))
            if super_activated:
                window.blit(super, super_rect)
                window.blit(super_rocket, super_rocket_rect)
                super_rocket_rect.right += 5
                if super_rocket_rect.left > WIDTH:
                    super_rocket_rect.center = super_rect.center
                    super_rocket_rect.left = super_rect.right

            window.blit(player, player_rect)
            lives_label = main_font.render("lives:" + str(lives), True, WHITE)
            window.blit(lives_label, (0, 0))
            score_label = main_font.render("score:" + str(score), True, WHITE)
            window.blit(score_label, (80, 0))
            if direction == "down" and player_rect.bottom < HEIGHT:

                player_rect.bottom += 10
            elif direction == "up" and player_rect.top > 0:
                player_rect.top -= 10
            if bullets:
                for (i, b) in enumerate(bullets):

                    window.blit(get_bullet(n)[1], b)
                    b.right += 20
                    if b.x > WIDTH:
                        bullets.pop(i)
                    if b.colliderect(enemy):
                        enemy.center = (WIDTH, randint(40, HEIGHT - 30))

            for e in enemies:
                pygame.draw.ellipse(window, BLUE, e)
                e.x -= 3
                for b in bullets:
                    if e.colliderect(b) or e.colliderect(super_rocket_rect):
                        e.center = (WIDTH, randint(40, HEIGHT - 30))
                        score += 1
                        boom.play()

                if e.x < 0 or e.colliderect(player_rect):
                    e.center = (WIDTH, randint(40, HEIGHT - 30))
                    lives -= 1
                    if lives == 0:
                        mode = "game over"
    elif mode == "game over":
        window.blit(game_over_fon, (0, 0))
        window.blit(podzkaska_pik, (WIDTH//2, HEIGHT-HEIGHT//7))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    mode = "menu"
                elif i.key == pygame.K_RETURN:
                    mode = "your best"
        try:
            with open("record.txt", "r+", encoding="utf-8") as file:
                if int(file.read().split()[1]) < score:
                    file.seek(0)
                    file.truncate()
                    file.write(name + " " + str(score))
        except FileNotFoundError:
            with open("record.txt", "w", encoding="utf-8") as file:
                file.write(name + " " + str(score))
    elif mode == "your best":
        window.blit(best_fon, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RETURN:
                    mode = "menu"

        with open("record.txt", "r", encoding="utf-8") as file:
            result = file.read()
            record_label = best_font.render(result, True, WHITE)
            window.blit(record_label, (WIDTH//2 - 80, HEIGHT//2 - 60,))
    pygame.display.update()
    clock.tick(FPS)
print(len(bullets))
pygame.quit()
