import pygame
from blocks import Block
pygame.init

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

# Game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()