import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Couple Tough Jumps")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (40, 40, 40)

# Player setup
player = pygame.Rect(100, 500, 30, 30)
player_vel_y = 0
gravity = 0.7
jump_power = -14  # higher jump
speed = 5

# Game state
level = 0
coins_collected = 0
total_coins = 5
game_started = False
game_won = False

def r(x, y, w, h):
    return pygame.Rect(x, y, w, h)

# Level design
levels = {
    0: {
        "platforms": [r(0, 550, WIDTH, 50)],
        "spikes": [r(200 + i * 78, 530, 40, 20) for i in range(4)],  # smaller gap (pixel-perfect)
        "coins": [r(600, 500, 20, 20)]
    },
    1: {
        "platforms": [r(0, 550, WIDTH, 50), r(350, 450, 150, 20)],
        "spikes": [r(250, 530, 40, 20), r(450, 430, 40, 20)],
        "coins": [r(700, 500, 20, 20)]
    },
    2: {
        "platforms": [r(0, 550, WIDTH, 50), r(300, 450, 150, 20)],
        "spikes": [r(250, 530, 40, 20), r(500, 530, 40, 20)],
        "coins": [r(600, 420, 20, 20)]
    },
    3: {
        "platforms": [r(0, 550, WIDTH, 50), r(250, 450, 200, 20), r(550, 350, 150, 20)],
        "spikes": [r(400, 530, 40, 20), r(600, 330, 40, 20)],
        "coins": [r(750, 320, 20, 20)]
    },
    4: {
        "platforms": [r(0, 550, WIDTH, 50), r(250, 450, 150, 20), r(500, 350, 150, 20)],
        "spikes": [r(400, 530, 40, 20), r(650, 330, 40, 20)],
        "coins": [r(700, 320, 20, 20)]
    },
    5: {
        "platforms": [r(0, 550, WIDTH, 50), r(200, 400, 150, 20), r(500, 300, 150, 20)],
        "spikes": [r(150, 530, 40, 20), r(600, 280, 40, 20)],
        "coins": [r(750, 260, 20, 20)]
    },
    6: {
        "platforms": [r(0, 550, WIDTH, 50), r(300, 450, 200, 20), r(600, 350, 150, 20)],
        "spikes": [r(400, 530, 40, 20), r(700, 330, 40, 20)],
        "coins": [r(740, 320, 20, 20)]
    },
    7: {
        "platforms": [r(0, 550, WIDTH, 50), r(200, 400, 150, 20), r(500, 250, 150, 20)],
        "spikes": [r(250, 530, 40, 20), r(650, 230, 40, 20)],
        "coins": [r(740, 220, 20, 20)]
    },
    8: {
        "platforms": [r(0, 550, WIDTH, 50), r(300, 450, 200, 20), r(600, 350, 150, 20), r(700, 250, 100, 20)],
        "spikes": [r(400, 530, 40, 20), r(700, 330, 40, 20)],
        "coins": [r(750, 240, 20, 20)]
    },
    9: {
        "platforms": [r(0, 550, WIDTH, 50), r(250, 450, 150, 20), r(550, 350, 150, 20), r(700, 250, 100, 20)],
        "spikes": [r(300, 530, 40, 20), r(650, 330, 40, 20)],
        "coins": [r(750, 240, 20, 20)]
    }
}

def reset_level():
    global player, player_vel_y, coins_collected
    player.x, player.y = 100, 500
    player_vel_y = 0
    coins_collected = 0

# Game loop
running = True
while running:
    dt = clock.tick(60)
    fps = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_started:
        screen.fill(BLACK)
        title = font.render("A Couple Tough Jumps", True, WHITE)
        start_text = font.render("Press SPACE to Start", True, GRAY)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 50))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2 + 10))
        pygame.display.flip()
        if keys[pygame.K_SPACE]:
            game_started = True
        continue

    if game_won:
        screen.fill(BLACK)
        win_text = font.render("You Won! GG!", True, YELLOW)
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        continue

    # Apply gravity
    player_vel_y += gravity
    player.y += player_vel_y
    on_ground = False

    # Horizontal movement
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed

    # Collision check for platforms
    for p in levels[level]["platforms"]:
        if player.colliderect(p) and player_vel_y >= 0:
            player.bottom = p.top
            player_vel_y = 0
            on_ground = True

    # Jump (AFTER collision detection)
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_power
        on_ground = False

    # Spike collision
    for s in levels[level]["spikes"]:
        if player.colliderect(s):
            reset_level()

    # Coin collection
    for c in levels[level]["coins"][:]:
        if player.colliderect(c):
            levels[level]["coins"].remove(c)
            coins_collected += 1

    # Level win
    if coins_collected >= total_coins or not levels[level]["coins"]:
        level += 1
        if level >= len(levels):
            game_won = True
        else:
            reset_level()

    # Drawing
    screen.fill(BLACK)
    for p in levels[level]["platforms"]:
        pygame.draw.rect(screen, WHITE, p)
    for s in levels[level]["spikes"]:
        pygame.draw.polygon(screen, RED, [(s.x, s.bottom), (s.x + s.width / 2, s.y), (s.right, s.bottom)])
    for c in levels[level]["coins"]:
        pygame.draw.circle(screen, YELLOW, (c.x + 10, c.y + 10), 10)
    pygame.draw.rect(screen, BLUE, player)

    # HUD
    fps_text = font.render(f"FPS: {fps}", True, WHITE)
    coin_text = font.render(f"Coins: {coins_collected}/5", True, YELLOW)
    level_text = font.render(f"Level: {level + 1}", True, WHITE)
    screen.blit(fps_text, (WIDTH - 130, 10))
    screen.blit(coin_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()

pygame.quit()