import pygame
from blocks import Block, Head, Body, Snake
pygame.init

blockSize = 25

win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Snake")

"""
i = 0
while i != 1000:
    i += 50
    pygame.draw.line(win, (255, 255, 255), (i, 0), (i, 1000))
"""

apple = Block(win, 0, 0, (255, 255, 255))
apple.draw()

snake = Snake(win, 5, (255, 255, 255))
snake.move()

# Game loop
run = True
while run:
    pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    snake.move()

    #win.fill((0,0,0))
    pygame.display.update()

pygame.quit()