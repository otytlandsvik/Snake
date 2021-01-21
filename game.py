import pygame
from blocks import Snake
pygame.init

blockSize = 25

win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Snake")


snake = Snake(win, 5, (255, 255, 255))
snake.move()
snake.draw()

# Game loop
snakeDir = "Right"
cycleCount = 0;
run = True
while run:
    cycleCount += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snakeDir = "Left"
    if keys[pygame.K_RIGHT]:
        snakeDir = "Right"
    if keys[pygame.K_UP]:
        snakeDir = "Up"
    if keys[pygame.K_DOWN]:
        snakeDir = "Down"
    
    

    win.fill((0,0,0))
    if (cycleCount == 5):
        snake.update(snakeDir)
        cycleCount = 0

    snake.move()
    snake.draw()
    pygame.display.update()

    pygame.time.delay(100)

pygame.quit()