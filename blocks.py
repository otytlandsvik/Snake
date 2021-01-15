import pygame

blockSize = 25
SPEED = 5

class Block:
    def __init__(self, win, x, y, color):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, (self.y + 5), blockSize, (blockSize - 5)))


# Snake classes
class Head:
    def __init__(self, block, dir):
        self.block = block
        self.dir = dir

    # Change direction of snake head
    def changeDir(self, newDir):
        self.dir = newDir

    # Move and draw block
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

class NBody:
    def __init__(self, win, x, y, dir, color ):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
        self.dir = dir

    def changeDir(self, newDir):
        self.dir = newDir

    def move(self):
        if self.dir == "Up":
            self.y -= SPEED
        elif self.dir == "Down":
            self.y += SPEED
        elif self.dir == "Left":
            self.x -= SPEED
        elif self.dir == "Right":
            self.x += SPEED

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, (self.y + 5), blockSize, (blockSize - 5)))


class Tail(NBody):
    def __init__(self, win, x, y, dir, color, nextBlock):
        super().__init__(win, x, y, dir, color)
        self.nextDir = dir
        self.nextBlock = nextBlock
    
    # Follows the block in front
    def updateDir(self):
        self.dir = self.nextDir
        self.nextDir = self.nextBlock.dir

class Body(Head):
    def __init__(self, block, dir, nextBlock):
        super().__init__(block, dir)
        self.nextDir = dir
        self.nextBlock = nextBlock

    # Follows the blocks in front
    def updateDir(self):
        self.dir = self.nextDir
        self.nextDir = self.nextBlock.dir


class Snake:
    def __init__(self, win, size, color):
        self.blockList = []

        # Create a block object
        block = Block(win, 500, 500, color)

        # Create a head
        head = Head(block, "Right")

        # Add it to the block list
        self.blockList.append(head)

        # Add a body to the snake
        for i in range(size-1):
            block.x -= blockSize
            body = Body(block, "Right", self.blockList[-1])
            self.blockList.append(body)

    # Change direction of snake
    def changeDir(self, newDir):
        self.blockList[0].changeDir(newDir)
    
    # Update snake
    def update(self):
        for block in self.blockList:
            if isinstance(block, Body):
                block.updateDir()
    
    # Move the snake
    def move(self):
        for block in self.blockList:
            block.move()
    
    # Lengthen the snake by one
    def grow(self):
        pass