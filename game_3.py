import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400
BLOCK = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)
RED = (200, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Snake initial
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# Food
def generate_food():
    x = random.randrange(0, WIDTH, BLOCK)
    y = random.randrange(0, HEIGHT, BLOCK)
    return (x, y)

food = generate_food()
score = 0
speed = 10


# Draw everything
def draw():
    screen.fill(BLACK)

    # Draw snake
    for i, segment in enumerate(snake):
        if i == 0:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))
        else:
            pygame.draw.rect(screen, DARK_GREEN, (*segment, BLOCK, BLOCK))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

    # Draw score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()


# Game loop
running = True
while running:
    clock.tick(speed)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    head_x, head_y = snake[0]

    if direction == "UP":
        new_head = (head_x, head_y - BLOCK)
    elif direction == "DOWN":
        new_head = (head_x, head_y + BLOCK)
    elif direction == "LEFT":
        new_head = (head_x - BLOCK, head_y)
    else:
        new_head = (head_x + BLOCK, head_y)

    # Collision with wall
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        break

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        speed += 0.5
        food = generate_food()
    else:
        snake.pop()

    draw()


# Game Over Screen
screen.fill(BLACK)
text1 = font.render("GAME OVER", True, RED)
text2 = font.render(f"Final Score: {score}", True, WHITE)

screen.blit(text1, (WIDTH//2 - 80, HEIGHT//2 - 20))
screen.blit(text2, (WIDTH//2 - 100, HEIGHT//2 + 20))

pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()