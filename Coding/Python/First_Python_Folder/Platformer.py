import pygame
import random

pygame.init()

# Screen setup (800x600 fits a 10x10 grid where each tile is 80x60 pixels)
WIDTH, HEIGHT = 800, 600
GRID_COLS, GRID_ROWS = 10, 10
TILE_W = WIDTH // GRID_COLS  # 80 pixels
TILE_H = HEIGHT // GRID_ROWS # 60 pixels

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Couple Tough Jumps - Grid Edition")

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
GRID_COLOR = (30, 30, 30)

# Player setup
player = pygame.Rect(0, 0, 30, 30) # Size remains the same
player_vel_y = 0
gravity = 0.7
jump_power = -10
speed = 5

# Game state
level = 0
coins_collected = 0
game_started = False
game_won = False

# --- GRID HELPER FUNCTIONS ---
# Converts [grid_x, grid_y] into a Pygame Rect object
def make_rect(coords, width_tiles=1, height_tiles=1):
    return pygame.Rect(coords[0] * TILE_W, coords[1] * TILE_H, TILE_W * width_tiles, TILE_H * height_tiles)

# Helper specifically for spikes to match your original smaller dimensions
def make_spike_rect(coords):
    # Centers a 40x20 spike at the bottom of the targeted grid tile
    pixel_x = coords[0] * TILE_W + (TILE_W - 40) // 2
    pixel_y = coords[1] * TILE_H + (TILE_H - 20)
    return pygame.Rect(pixel_x, pixel_y, 40, 20)

# Helper for coins to match original 20x20 dimensions
def make_coin_rect(coords):
    pixel_x = coords[0] * TILE_W + (TILE_W - 20) // 2
    pixel_y = coords[1] * TILE_H + (TILE_H - 20) // 2
    return pygame.Rect(pixel_x, pixel_y, 20, 20)

# --- EASY GRID-BASED LEVEL DESIGN ---
# Grid handles coordinates from 0 to 9. Row 9 is the floor.
grid_levels = {
    0: {
        "start": [1, 8],
        "platforms": [[i, 9] for i in range(10)], # Entire bottom row
        "spikes": [[3, 8], [4, 8], [5, 8]],       # Easily move spikes by changing these pairs!
        "coins": [[8, 8]]
    },
    1: {
        "start": [1, 8],
        "platforms": [[i, 9] for i in range(10)] + [[4, 7], [5, 7]],
        "spikes": [[3, 8], [5, 6], [6, 8]],
        "coins": [[8, 8]]
    },
    2: {
        "start": [1, 8],
        "platforms": [[i, 9] for i in range(10)] + [[3, 4], [4, 5], [4, 4], [4, 6], [4, 7], [5, 7], [5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [5, 0]],
        "spikes": [[3, 8], [6, 8], [5, 6]],
        "coins": [[7, 6]]
    }
}

# Convert grid coordinates into playable Rect instances
def load_level(lvl_idx):
    lvl_data = grid_levels[lvl_idx]
    
    # Generate standard lists
    platforms = [make_rect(p) for p in lvl_data["platforms"]]
    spikes = [make_spike_rect(s) for s in lvl_data["spikes"]]
    coins = [make_coin_rect(c) for c in lvl_data["coins"]]
    
    return platforms, spikes, coins

def reset_level():
    global player, player_vel_y, coins_collected, current_platforms, current_spikes, current_coins
    
    # Load raw rect data for collision engines
    current_platforms, current_spikes, current_coins = load_level(level)
    
    # Spawn player exactly at the designated grid coordinate
    start_grid = grid_levels[level]["start"]
    player.x = start_grid[0] * TILE_W + (TILE_W - player.width) // 2
    player.y = start_grid[1] * TILE_H + (TILE_H - player.height)
    
    player_vel_y = 0
    coins_collected = 0

# Initialize the first layout
current_platforms, current_spikes, current_coins = load_level(level)
reset_level()

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

    # Apply physics
    player_vel_y += gravity
    player.y += player_vel_y
    on_ground = False
    
    # Horizontal movement
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed
        
    # Collision check for platforms
    for p in current_platforms:
        if player.colliderect(p) and player_vel_y >= 0:
            player.bottom = p.top
            player_vel_y = 0
            on_ground = True
            
    # Jump
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_power
        on_ground = False
        
    # Spike collision
    for s in current_spikes:
        if player.colliderect(s):
            reset_level()
            
    # Coin collection
    for c in current_coins[:]:
        if player.colliderect(c):
            current_coins.remove(c)
            coins_collected += 1
            
    # Level win tracking
    if not current_coins:
        level += 1
        if level >= len(grid_levels):
            game_won = True
        else:
            reset_level()

    # --- DRAWING ---
    screen.fill(BLACK)
    
    # Draw Background Grid lines
    for x in range(0, WIDTH, TILE_W):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_H):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw elements
    for p in current_platforms:
        pygame.draw.rect(screen, WHITE, p)
        
    for s in current_spikes:
        pygame.draw.polygon(screen, RED, [(s.x, s.bottom), (s.x + s.width / 2, s.y), (s.right, s.bottom)])
        
    for c in current_coins:
        pygame.draw.circle(screen, YELLOW, (c.centerx, c.centery), 10)
        
    pygame.draw.rect(screen, BLUE, player)
    
    # HUD
    fps_text = font.render(f"FPS: {fps}", True, WHITE)
    coin_text = font.render(f"Coins: {coins_collected}/{len(grid_levels[level]['coins']) + coins_collected}", True, YELLOW)
    level_text = font.render(f"Level: {level + 1}", True, WHITE)
    screen.blit(fps_text, (WIDTH - 130, 10))
    screen.blit(coin_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.flip()

pygame.quit()