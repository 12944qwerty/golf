import pygame as pg
import math
from matplotlib.path import Path

class Wall:
    def __init__(self, coord:tuple, dir:int, size:tuple):
        self.x = coord[0]
        self.y = coord[1]
        self.dir = dir
        self.width = size[0]
        self.height = size[1]
        self.rect = pg.Rect((self.x, self.y), (self.width, self.height))

    def get_coords(self):
        topleft = (self.x, self.y)
        topright = (self.x + (self.width * math.sin(math.radians(90 - self.dir))),
                    self.y - (self.width * math.cos(math.radians(90 - self.dir))))
        bottomleft = (topright[0] + (self.height * math.sin(math.radians(self.dir))),
                      topright[1] + (self.height * math.cos(math.radians(self.dir))))
        bottomright = (self.x + (self.height * math.sin(math.radians(self.dir))),
                       self.y + (self.height * math.cos(math.radians(self.dir))))
        return topleft, topright, bottomleft, bottomright

    def draw(self, surface):
        if self.dir%90 == 0:
            self.rect = pg.draw.rect(surface, (255, 255, 255), self.rect)
        else:
            topleft, topright, bottomleft, bottomright = self.get_coords()
            self.rect = pg.draw.polygon(surface, (255,255,255), [topleft, topright, bottomleft, bottomright])

    def collision(self, ball):
        if self.dir%90 == 0:
            return self.rect.colliderect(ball.circle)
        else:
            """How to figure out if the ball is touching the actual shown rectangle, not the hitbox that pygame has.
            Credit to kenny2github for this"""
            points1 = self.get_coords()
            bx = ball.x    # x position of CENTER of the ball
            by = ball.y    # y position of likewise
            bd = 5         # RADIUS of the ball
            t = self.dir   # Direction of Rectangle
            points2 = [tuple(pg.math.Vector2(p).rotate(t) + (bx, by))
                       for p in [(bd, 0), (0, bd), (-bd, 0), (0, -bd)]]
            return any(Path(points1).contains_points(points2))