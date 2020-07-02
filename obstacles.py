import pygame as pg
import math

class Wall:
    def __init__(self, coord:tuple, dir:int, size:tuple):
        self.x = coord[0]
        self.y = coord[1]
        self.dir = dir
        self.width = size[0]
        self.height = size[1]
        self.rect = pg.Rect((self.x, self.y), (self.width, self.height))

    def draw(self, surface):
        pg.draw.rect(surface, (255, 255, 255), self.rect)

    def collision(self, ball): #rleft, rtop, width, height,  # rectangle definition
    #               center_x, center_y, radius):  # circle definition
        """ Detect collision between a rectangle and circle. """

        return self.rect.colliderect(ball)

        # # complete boundbox of the rectangle
        # rright, rbottom = rleft + width / 2, rtop + height / 2
        #
        # # bounding box of the circle
        # cleft, ctop = center_x - radius, center_y - radius
        # cright, cbottom = center_x + radius, center_y + radius
        #
        # # trivial reject if bounding boxes do not intersect
        # if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        #     return False  # no collision possible
        #
        # # check whether any point of rectangle is inside circle's radius
        # for x in (rleft, rleft + width):
        #     for y in (rtop, rtop + height):
        #         # compare distance between circle's center point and each point of
        #         # the rectangle with the circle's radius
        #         if math.hypot(x - center_x, y - center_y) <= radius:
        #             return True  # collision detected
        #
        # # check if center of circle is inside rectangle
        # if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        #     return True  # overlaid
        #
        # return False  # no collision detected