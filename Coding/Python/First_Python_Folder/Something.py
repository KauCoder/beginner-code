#PYGAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import pygame

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
def new_func(SCREEN_WIDTH, SCREEN_HEIGHT):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen
screen = new_func(SCREEN_WIDTH, SCREEN_HEIGHT)

# Entities
player = pygame.Rect( (300, 250, 50, 50) )
object = pygame.Rect((200, 430, 30, 30 ))

#Colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Main
run = True
while run:

    screen.fill((0, 0, 0))

    # Define Colour
    col = GREEN
    if player.colliderect(object):
        col = RED
    pygame.draw.rect(screen, (col), player)
    pygame.draw.rect(screen, (BLUE), object) 
    
    pygame.mouse.set_visible(False)
    
   
    # Controls
    def controls():
        pos = pygame.mouse.get_pos()
        player.center = pos
    controls()

    # If it doesn't run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()