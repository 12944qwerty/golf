import pygame as pg

class Hole:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        self.hole = pg.draw.circle(surface, (100, 100, 100), (self.x, self.y), 10)

    def collide(self, ball):
        return self.hole.contains(ball.circle) and ball.power <= 6