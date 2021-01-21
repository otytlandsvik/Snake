import pygame

BLOCKSIZE = 25
SPEED = 5

# Snake class
class Snake:
    def __init__(self, win, size, color):
        self.win = win
        self.size = size
        self.color = color
        