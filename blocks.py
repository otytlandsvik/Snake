import pygame

blockSize = 50

class Block:
    def __init__(self, win, x, y, color):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, blockSize, blockSize))


# Snake classes
class Head:
    def __init__(self, block, dir):
        self.block = block
        self.dir = dir

    def changeDir(self, newDir):
        self.dir = newDir

    def move(self):
        if self.dir == "Up":
            self.block.y -= blockSize
        elif self.dir == "Down":
            self.block.y += blockSize
        elif self.dir == "Left":
            self.block.x -= blockSize
        elif self.dir == "Right":
            self.block.x += blockSize

        self.block.draw()
