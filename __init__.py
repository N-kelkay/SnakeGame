import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTO = self.direction

    def changeDirTo(self, dir):
        if dir ==  "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.dirction = "UP"
        if dir == "DOWN" and not self.dirction == "UP":
            self.dirction = "DOWN"

    def move(self, foodPos):
        if slef.direction == "RIGHT":
            self.position[0] += 10
        if slef.direction == "LEFT":
            self.position[0] -= 10
        if slef.direction == "UP":
            self.position[0] += 10
        if slef.direction == "DOWN":
            self.position[0] -= 10


        self.body.insert(0, self.position)
        if slef.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0 :
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body

class FoodSpawer():
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isFoodOnScreen = True


    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, b):
        self.isFoodOnScreen = b

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wow Snake")
fps = pygame.time.Clock()

score = 0

snake = Snake()

foodSpawner = FoodSpawer()

def gameOver():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT')
