import pygame,sys
from pygame.locals import *

class graphVisual:
    def __init__(self) -> None:
        self.__init__pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.sqaureWidth = 10
        self.squareHeight =10
        self.matrix = [[1 ,1 ,0 ,1],
          [1 ,0 ,0 ,1],
          [1 ,1 ,0 ,1],
          [1 ,1 ,1 ,1]]
        print("f")

    def __init__pygame(self):
        pygame.init()
        pygame.display.set_caption("Path Finding Visuals")

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            white = 200,200,200
            screen.fill(white)
            pygame.display.update()

    def createSquare(self,x,y,color):
        pygame.draw.rect(self.screen, color, [x,y,self.sqaureWidth,self.squareHeight])

    def visualizeGrid(self):
        y = 0
        for row in self.matrix:
            x = 0
            for item in row:
                if item ==0:
                    self.createSquare(x,y,(255,255,255))
                else:
                    self.createSquare(x,y,(0,0,0))
            x += self.sqaureWidth
        y += self.squareHeight
    
        



pygame.init()
size = width, height = 600, 600
print(type(size))
DISPLAYSURF = pygame.display.set_mode(size)


pygame.display.set_caption('Hello World!')
screen = pygame.display.set_mode(size)

while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
        

            sys.exit()
    white = 200,200,200
    screen.fill(white)
    pygame.display.update()
g = graphVisual()