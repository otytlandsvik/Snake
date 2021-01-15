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
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    win.fill((0,0,0))
    snake.move()
    snake.draw()
    pygame.display.update()

    pygame.time.delay(100)

pygame.quit()