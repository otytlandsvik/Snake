import pygame
pygame.init

win = pygame.display.set_mode(1000, 700)

pygame.display.set_caption("Snake")


# Game loop

run = True
while run:
    pygame.time.delay(100)