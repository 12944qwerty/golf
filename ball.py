import pygame as pg
import math

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = 0
        self.dir = 0
        self.moveable = True

    def move(self, mousedown):
        if not mousedown:
            if self.power <= 0.3:
                self.moveable = True
                self.power = 0
            else:
                self.moveable = False
                x_vel = self.power*math.cos(self.dir)
                y_vel = self.power*math.sin(self.dir)
                self.x += x_vel
                self.y += y_vel
                self.power = round(self.power*0.98,3)

    def draw(self, surface):
        self.circle = pg.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), 5)