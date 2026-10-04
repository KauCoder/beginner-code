import pygame
import os
pygame.init()

# ------------------ CONSTANTS ------------------ #
ROWS, COLS = 11, 11
CELL_SIZE = 100
PLAYER_SIZE = 60

WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (50, 50, 50)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Border thickness for outlines in pixels
BORDER_WIDTH = 4

GRAVITY = 1
JUMP_STRENGTH = -21
FPS = 60
MOVE_SPEED = 10

# ------------------ SETUP ------------------ #
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("11x11 Grid Platformer")
clock = pygame.time.Clock()

# Fonts for HUD and win screen
font_large = pygame.font.SysFont(None, 120)
font_small = pygame.font.SysFont(None, 36)

# ------------------ GRID ------------------ #
# 0 = empty
# 1 = platform
# 2 = player spawn
# 3 = spike
# 4 = goal
gameMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],  
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], 
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 4], 
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 3, 4], 
    [1, 1, 1, 0, 0, 0, 0, 3, 0, 1, 1], 
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1], 
    [1, 3, 0, 2, 0, 0, 0, 0, 0, 3, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

def load_image(name, size):
    path = os.path.join("images", name)
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (size, size))
    return None

class Tile:
    def __init__(self, col, row, image, kind='solid'):
        # Use provided image or create a fallback surface
        if image is None:
            self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            if kind == 'goal':
                self.image.fill(YELLOW)
            else:
                pygame.draw.rect(self.image, GRAY, self.image.get_rect())
        else:
            self.image = image
        self.rect = self.image.get_rect(topleft=(col * CELL_SIZE, row * CELL_SIZE))
        self.mask = pygame.mask.from_surface(self.image)
        self.kind = kind

# ------------------ PLAYER ------------------ #
class Player:
    def __init__(self, tile_x, tile_y):
        offset = (CELL_SIZE - PLAYER_SIZE) // 2
        self.spawn = (tile_x + offset, tile_y + offset)
        self.rect = pygame.Rect(self.spawn[0], self.spawn[1], PLAYER_SIZE, PLAYER_SIZE)

        # Velocities for axis-separated collision
        self.x_vel = 0
        self.y_vel = 0
        self.on_ground = False
        self.dead = False
        self.death_time = 0
        self.won = False
        self.won_time = 0

        # Load player image or fallback to a simple rectangle
        img = load_image("player.png", PLAYER_SIZE)
        if img is None:
            self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(self.image, RED, (0, 0, PLAYER_SIZE, PLAYER_SIZE))
        else:
            self.image = img
        self.mask = pygame.mask.from_surface(self.image)

    def jump(self):
        if self.on_ground:
            self.y_vel = JUMP_STRENGTH
            self.on_ground = False

    def move_right(self):
        self.x_vel = MOVE_SPEED

    def move_left(self):
        self.x_vel = -MOVE_SPEED

    def handle_move(self):
        keys = pygame.key.get_pressed()
        # Reset horizontal velocity each frame and set from input
        self.x_vel = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move_right()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move_left()

    def apply_gravity(self):
        # Only update y velocity here; movement happens in move_and_collide
        self.y_vel += GRAVITY

    def respawn(self):
        self.rect.topleft = self.spawn
        self.x_vel = 0
        self.y_vel = 0
        self.on_ground = False

    def die(self):
        # Start death timer, prevent movement and physics
        self.dead = True
        self.death_time = pygame.time.get_ticks()
        self.x_vel = 0
        self.y_vel = 0

    def reach_goal(self):
        if not getattr(self, 'won', False):
            self.won = True
            self.won_time = pygame.time.get_ticks()
            print("Goal reached!")
            self.x_vel = 0
            self.y_vel = 0

    def update(self):
        # Handle death (respawn after 1s). Win now pauses the game and shows a win screen until player restarts.
        if self.dead:
            if pygame.time.get_ticks() - self.death_time >= 1000:
                self.respawn()
                self.dead = False
        elif getattr(self, 'won', False):
            # When won, freeze updates (no movement/physics) and let main loop handle restart/quit
            return
        else:
            self.handle_move()
            self.apply_gravity()
            self.move_and_collide()

    def move_and_collide(self):
        # Horizontal movement & side collisions (use rect then precise mask check)
        self.rect.x += int(self.x_vel)
        for tile in tiles:
            if tile.kind == 'solid' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    if self.x_vel > 0:               # moving right -> hit left side
                        self.rect.right = tile.rect.left
                    elif self.x_vel < 0:             # moving left -> hit right side
                        self.rect.left = tile.rect.right
                    self.x_vel = 0
            elif tile.kind == 'spike' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    self.die()
            elif tile.kind == 'goal' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    self.reach_goal()

        # Vertical movement & top/bottom collisions
        self.rect.y += int(self.y_vel)
        self.on_ground = False
        for tile in tiles:
            if tile.kind == 'solid' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    if self.y_vel > 0:              # falling -> land on platform
                        self.rect.bottom = tile.rect.top
                        self.y_vel = 0
                        self.on_ground = True
                    elif self.y_vel < 0:            # jumping -> hit head
                        self.rect.top = tile.rect.bottom
                        self.y_vel = 0
            elif tile.kind == 'spike' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    self.die()
            elif tile.kind == 'goal' and self.rect.colliderect(tile.rect):
                offset = (tile.rect.x - self.rect.x, tile.rect.y - self.rect.y)
                if self.mask.overlap(tile.mask, offset):
                    self.reach_goal()


# ------------------ FIND PLAYER / BUILD TILES ------------------ #
# Preload the images we'll use for tiles
block_img = load_image("regularGDblock.webp", CELL_SIZE)
spike_img = load_image("regularGDspike.webp", CELL_SIZE)

tiles = []
player = None
for r in range(ROWS):
    for c in range(COLS):
        val = gameMap[r][c]
        if val == 1:
            tiles.append(Tile(c, r, block_img, 'solid'))
        elif val == 3:
            tiles.append(Tile(c, r, spike_img, 'spike'))
        elif val == 4:
            tiles.append(Tile(c, r, None, 'goal'))
        elif val == 2:
            # spawn player and clear tile
            player = Player(c * CELL_SIZE, r * CELL_SIZE)
            gameMap[r][c] = 0


# ------------------ DRAW GRID ------------------ #
def draw_grid():
    # Draw tiles
    for tile in tiles:
        screen.blit(tile.image, tile.rect.topleft)
        # Colored outline per tile kind
        if tile.kind == 'solid':
            pygame.draw.rect(screen, GREEN, tile.rect, BORDER_WIDTH)
        elif tile.kind == 'spike':
            # Draw an outline that follows the sprite's non-transparent pixels
            outline = tile.mask.outline()
            if outline:
                pts = [(tile.rect.x + x, tile.rect.y + y) for x, y in outline]
                if len(pts) >= 2:
                    pygame.draw.lines(screen, RED, True, pts, BORDER_WIDTH)
                else:
                    pygame.draw.rect(screen, RED, tile.rect, BORDER_WIDTH)
            else:
                pygame.draw.rect(screen, RED, tile.rect, BORDER_WIDTH)
        elif tile.kind == 'goal':
            pygame.draw.rect(screen, YELLOW, tile.rect, BORDER_WIDTH)

    # Grid lines (optional)
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, WHITE, rect, 2)

def draw_win_screen():
    # Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    # Title
    title = font_large.render("YOU WIN!!!", True, YELLOW)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title, title_rect)

    # Instruction
    sub = font_small.render("Press R to play again or ESC to quit", True, WHITE)
    sub_rect = sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(sub, sub_rect)

# ------------------ MAIN LOOP ------------------ #
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # If player has won, handle win-screen keys
            if getattr(player, 'won', False):
                if event.key == pygame.K_r:
                    player.respawn()
                    player.won = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
            else:
                if event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
                    player.jump()

    # Update
    player.update()

    # Draw
    draw_grid()
    screen.blit(player.image, player.rect.topleft)

    # Show win screen overlay if player reached goal
    if getattr(player, 'won', False):
        draw_win_screen()

    pygame.display.flip()

pygame.quit()