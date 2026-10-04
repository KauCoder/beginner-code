import pygame

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set Mouse
pygame.mouse.set_visible(False)

# Entities
player = pygame.Rect(300, 250, 50, 50)
object = pygame.Rect(200, 430, 30, 30)

# Colours
GREEN = (0, 255, 0)
def new_func():
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    return RED, BLUE, ORANGE 

RED, BLUE, ORANGE = new_func()

# Main function
def main():
    run = True
    col = GREEN  # Default color (no collision)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Make the player follow the cursor
        player.x = mouse_x - player.width // 2  # Center the player on the cursor
        player.y = mouse_y - player.height // 2  # Center the player on the cursor
                


        # Collision check
        if player.colliderect(object):
            col = RED  # Change color to red if colliding
        else:
            col = GREEN  # Default color if no collision

        # Fill screen with black
        SCREEN.fill((0, 0, 0))

        # Draw the player and object
        pygame.draw.rect(SCREEN, col, player)
        pygame.draw.rect(SCREEN, BLUE, object)

        # Update the display
        pygame.display.update()

    pygame.quit()

# Run the game
main()