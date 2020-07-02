import pygame as pg
import math
from random import randint, choice
from ball import Ball
import os
from obstacles import Wall

pg.init()

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

WIN_WIDTH = 1540
WIN_HEIGHT = 800

surface = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
font = pg.font.SysFont('comicsansms', 24)

def draw_window(surface, ball, level, obstacles):
    pg.draw.rect(surface, (98, 236, 93), pg.Rect((0, 0), (WIN_WIDTH, WIN_HEIGHT)))  # BG

    for obstacle in obstacles:
        obstacle.draw(surface)

    text1 = font.render(f"Level: {level}/500", True, (0, 0, 0))
    surface.blit(text1, (WIN_WIDTH-text1.get_width()-15 , 0))

    if ball.moveable:
        shootable = font.render("You can shoot now", True, (0, 0, 0))
    else:
        shootable = font.render("You cannot shoot now", True, (0, 0, 0))
    surface.blit(shootable, (3, 0))

    power = font.render('Power: ' + str(round(ball.power,1)), True, (0, 0, 0))
    surface.blit(power, ((WIN_WIDTH/2) - (power.get_width()/2), 0))

    ball.draw(surface)

def main():
    ball = Ball(200, 200)
    directions = {'left': 270, 'top': 0, 'right': 90, 'bottom': 180}
    obstacles = [Wall((0, 0),directions['left'],(10, WIN_HEIGHT)), #left
                 Wall((0, 0), directions['top'], (WIN_WIDTH, 10)), #top
                 Wall((WIN_WIDTH-10,0), directions['right'], (10, WIN_HEIGHT)), #right
                 Wall((0, WIN_HEIGHT-10), directions['bottom'], (WIN_WIDTH, 10)), #bottom
                 Wall((400, 200), directions['right'], (10, 100)) #random wall
                 ]

    clock = pg.time.Clock()

    level = 1
    mousedown = False
    tick = 0
    while True:
        clock.tick(30)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN and ball.moveable and not mousedown:
                ball.moveable = False
                mousedown = True
            if event.type == pg.MOUSEBUTTONUP and not ball.moveable and mousedown:
                mouse_x, mouse_y = pg.mouse.get_pos()
                offset_x = mouse_x - ball.x
                offset_y = mouse_y - ball.y
                ball.dir = math.atan2(offset_y, offset_x)
                ball.moveable = True
                mousedown = False

        ball.move(mousedown)
        if mousedown:
            tick += 1
            ball.power = (20*math.sin((3/28.64787)*math.radians(tick)))+20
        else:
            tick = 0
            ball.power *= .99
        draw_window(surface, ball, level, obstacles)

        for obstacle in obstacles:
            if obstacle.collision(ball.circle):#obstacle.x, obstacle.y, obstacle.width, obstacle.height, ball.x, ball.y, 5):
                # print(ball.dir, obstacle.dir, 'collision')
                # ball.dir += math.radians(2*(90-(math.degrees(ball.dir))+(obstacle.dir-90)))
                ball.dir += math.radians((obstacle.dir - math.degrees(ball.dir)) * 2)

        pg.display.update()

if __name__ == '__main__':
    main()