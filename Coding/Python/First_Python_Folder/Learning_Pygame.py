import pygame

pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Couple Tough Jumps")

# --- Colors ---
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BROWN = (150, 75, 0)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# --- Clock and font ---
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- Player setup ---
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5
jump_power = -15
velocity_y = 0
gravity = 0.6
on_ground = False

# --- Developer FPS display toggle ---
show_fps = True

# --- Helper ---
def r(x, y, w, h): return pygame.Rect(x, y, w, h)

# --- Title screen / mode selection ---
def show_title_screen():
    mode = None
    while mode is None:
        screen.fill(WHITE)
        title_font = pygame.font.SysFont(None, 72)
        text = title_font.render("A Couple Tough Jumps", True, RED)
        easy_text = font.render("Press E for Easy", True, BLACK)
        hard_text = font.render("Press H for Hard", True, BLACK)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 100))
        screen.blit(easy_text, (WIDTH//2 - easy_text.get_width()//2, HEIGHT//2))
        screen.blit(hard_text, (WIDTH//2 - hard_text.get_width()//2, HEIGHT//2 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            mode = "easy"
        if keys[pygame.K_h]:
            mode = "hard"
        clock.tick(60)
    return mode

mode = show_title_screen()

# --- Easy Levels ---
easy_levels = [
    { "platforms": [r(0,550,WIDTH,50), r(150,450,150,20)],
      "spikes": [r(300,530,40,20), r(500,530,40,20)],
      "coins": [r(200,420,20,20), r(450,320,20,20), r(600,500,20,20), r(350,500,20,20), r(500,400,20,20)] },
    { "platforms": [r(0,550,WIDTH,50), r(100,430,150,20), r(400,350,150,20)],
      "spikes": [r(180,530,40,20), r(420,530,40,20)],
      "coins": [r(150,400,20,20), r(450,320,20,20), r(600,500,20,20), r(350,500,20,20), r(500,400,20,20)] },
    { "platforms": [r(0,550,WIDTH,50), r(200,450,150,20), r(500,350,150,20)],
      "spikes": [r(220,530,40,20), r(520,530,40,20)],
      "coins": [r(400,500,20,20), r(600,500,20,20), r(250,500,20,20), r(650,500,20,20), r(350,500,20,20)] }
]

# --- Hard Levels ---
hard_levels = []
def spike_set(x_start, y, gap=100):
    return [r(x_start + i*gap, y, 40, 20) for i in range(4)]

# Level 1 example
hard_levels.append({
    "platforms": [r(0,550,WIDTH,50), r(50,400,200,20)],
    "spike_sets": [spike_set(150,530,100), spike_set(500,530,100)],
    "coin_positions": [(400,500),(550,500),(650,500),(700,500),(750,500)]
})

# Generate remaining 9 levels
for i in range(1,10):
    hard_levels.append({
        "platforms": [r(0,550,WIDTH,50), r(100+i*10,400,150,20)],
        "spike_sets": [spike_set(150+i*10,530,100), spike_set(500+i*10,530,100)],
        "coin_positions": [(200+i*10,500),(350+i*10,500),(500+i*10,500),(650+i*10,500),(750-i*5,500)]
    })

# --- Load level ---
current_level = 0
levels = easy_levels if mode=="easy" else hard_levels

def load_level(level_index):
    data = levels[level_index]
    plat = data["platforms"]
    if mode=="easy":
        return plat, data["spikes"], data["coins"], 0
    else:
        spikes_flat = []
        for s in data["spike_sets"]:
            spikes_flat.extend(s)
        return plat, spikes_flat, data["coin_positions"], 0

platforms, spikes, coin_seq, coin_index = load_level(current_level)
player.x, player.y = 100, 500
velocity_y = 0
on_ground = False

# --- Game loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: player.x -= player_speed
    if keys[pygame.K_d]: player.x += player_speed
    if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and on_ground:
        velocity_y = jump_power
        on_ground = False

    velocity_y += gravity
    player.y += velocity_y
    on_ground = False

    for plat in platforms:
        if player.colliderect(plat):
            if velocity_y > 0 and player.bottom <= plat.bottom:
                player.bottom = plat.top
                velocity_y = 0
                on_ground = True
            elif velocity_y < 0 and player.top >= plat.top:
                player.top = plat.bottom
                velocity_y = 0

    if player.left < 0: player.left = 0
    if player.right > WIDTH: player.right = WIDTH

    for spike in spikes:
        if player.colliderect(spike):
            player.x, player.y = 100, 500
            velocity_y = 0
            coin_index = 0
            break

    if coin_index < len(coin_seq):
        coin_rect = r(coin_seq[coin_index][0], coin_seq[coin_index][1], 20, 20)
        if player.colliderect(coin_rect):
            coin_index += 1

    if coin_index >= len(coin_seq):
        current_level += 1
        if current_level >= len(levels):
            print("🎉 YOU WON THE GAME! 🎉")
            running = False
        else:
            platforms, spikes, coin_seq, coin_index = load_level(current_level)
            player.x, player.y = 100, 500
            velocity_y = 0

    screen.fill(WHITE)
    for plat in platforms: pygame.draw.rect(screen, BROWN, plat)
    for spike in spikes:
        pygame.draw.polygon(screen, RED, [(spike.left, spike.bottom),(spike.centerx, spike.top),(spike.right, spike.bottom)])
    if coin_index < len(coin_seq):
        pygame.draw.circle(screen, YELLOW, r(coin_seq[coin_index][0], coin_seq[coin_index][1],20,20).center,10)
    pygame.draw.rect(screen, BLUE, player)

    text = font.render(f"Coin {coin_index+1}/{len(coin_seq)} | Level {current_level+1}/{len(levels)}", True, BLACK)
    screen.blit(text, (10,10))
    if show_fps:
        fps_text = font.render(f"{int(clock.get_fps())} FPS", True, GRAY)
        screen.blit(fps_text, (WIDTH-100,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()