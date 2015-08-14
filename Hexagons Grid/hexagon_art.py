__author__ = 'Rizal'

import turtle
from random import randint
import time, datetime
import math


class HoneyComb:
    def __init__(self):
        # Screen setup
        self.window = turtle.Screen()
        self.window.setup(1000, 800)
        self.window.bgcolor(self.giv_color())
        # Pen setup
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    @staticmethod
    def giv_color():
        color_1 = hex(randint(0, 255))[2:]
        color_2 = hex(randint(0, 255))[2:]
        color_3 = hex(randint(0, 255))[2:]
        hex_color = "#" + (2 - len(color_1)) * '0' + color_1 + \
                    (2 - len(color_2)) * '0' + color_2 + \
                    (2 - len(color_3)) * '0' + color_3
        return hex_color

    def draw_hexagon(self, coord, dist):
        self.pen.color(self.giv_color())
        self.pen.up()
        self.pen.goto(coord)
        self.pen.rt(90)
        self.pen.begin_fill()
        self.pen.down()
        for turn in range(6):
            self.pen.forward(dist)
            self.pen.lt(60)
        self.pen.end_fill()
        self.pen.lt(90)

    def clear_canvas(self):
        self.window.clear()

    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def save_img(self):
        self.window.getcanvas().postscript(file="hexagon - {0}_{1}.eps".format(self.get_time(), str(randint(0, 10000))))


if __name__ == "__main__":
    x, y = -400, 300
    ob = HoneyComb()
    grid_size = 10
    move_dist = 30

    nxt_x = 2 * move_dist * math.cos(math.radians(30))  # base of isosceles triangle , base = 2 * side *cos@
    nxt_y = move_dist + move_dist * math.sin(math.radians(30))  # height = side * sin@
    offset_backup = int(nxt_x / 2)

    for i in range(grid_size):
        for j in range(grid_size):
            if i % 2 == 0:
                offset = 0
            else:
                offset = offset_backup
            ob.draw_hexagon((x + nxt_x * j + offset, (y - nxt_y * i)), move_dist)

    ob.save_img()
