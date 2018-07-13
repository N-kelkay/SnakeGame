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
        
