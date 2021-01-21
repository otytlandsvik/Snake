import pygame

BLOCKSIZE = 25
SPEED = 5




# Snake classes
class Body:
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
        pygame.draw.rect(self.win, self.color, (self.x, (self.y + 5), BLOCKSIZE, (BLOCKSIZE - 5)))


class Tail(Body):
    def __init__(self, win, x, y, dir, color, nextBlock, listPos):
        super().__init__(win, x, y, dir, color)
        self.nextDir = dir
        self.nextBlock = nextBlock
        self.delay = listPos
        self.framesLeft = self.delay
    
    # Follows the block in front
    def updateDir(self):
        self.dir = self.nextDir
        self.nextDir = self.nextBlock.dir



class Snake:
    def __init__(self, win, size, color):
        self.blockList = []

        # Create a head
        head = Body(win, 500, 500, "Right", (255, 255, 255))

        # Add it to the block list
        self.blockList.append(head)

        # Add a tail to the snake
        offset = BLOCKSIZE
        for i in range(size-1):
            tail = Tail(win, (500 - offset), 500, "Right", (255, 255, 255), self.blockList[-1], len(self.blockList)-1)
            self.blockList.append(tail)
            offset += BLOCKSIZE

    # Change direction of snake
    def changeDir(self, newDir):
        self.blockList[0].changeDir(newDir)
    
    # Update snake directions
    def update(self, newDir):
        self.blockList[0].dir = newDir
        for block in self.blockList:
            if isinstance(block, Tail):
                if (block.framesLeft == 0):
                    block.updateDir()
                    block.framesLeft = block.delay
                else:
                    block.framesLeft -= 1
    
    # Move the snake
    def move(self):
        for block in self.blockList:
            block.move()

    # Draw the snake
    def draw(self):
        for block in self.blockList:
            block.draw()

    # Lengthen the snake by one
    def grow(self):
        pass