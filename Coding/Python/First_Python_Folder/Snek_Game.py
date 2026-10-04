import pygame
import random
import sys

def Snek_Game():
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    CELL_SIZE = 20
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snek Game")

    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)

    snake = [(100, 100), (80, 100)]
    direction = (CELL_SIZE, 0)
    food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))

    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.SysFont(None, 36)

    def move_snake(snake, direction):
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)
        return snake
    
    def check_collision(snake):
        head = snake[0]
        return (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]
        )
    
    def game_over_screen(score):
        while True:
            screen.fill(BLACK)
            over_text = font.render("Game Over!", True, WHITE)
            score_text = font.render(f"Score: {score}", True, WHITE)
            exit_text = font.render("Exit", True, WHITE)
            cont_text = font.render("Continue", True, WHITE)

            # Draw texts
            screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 80))
            screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 40))

            # Draw buttons
            exit_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 10, 100, 50)
            cont_rect = pygame.Rect(WIDTH//2 + 20, HEIGHT//2 + 10, 120, 50)
            pygame.draw.rect(screen, GRAY, exit_rect)
            pygame.draw.rect(screen, GRAY, cont_rect)
            screen.blit(exit_text, (exit_rect.x + 20, exit_rect.y + 10))
            screen.blit(cont_text, (cont_rect.x + 10, cont_rect.y + 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif cont_rect.collidepoint(event.pos):
                        return  # Restart the game

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        snake = move_snake(snake, direction)

        if snake[0] == food:
            food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
            score += 1
        else:
            snake.pop()

        if check_collision(snake):
            game_over_screen(score)
            return  # End this game and allow restart

        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

while True:
    Snek_Game()