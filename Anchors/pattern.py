__author__ = 'Rizal'
import turtle
from random import randint
import datetime
import math


class Pat:
    def __init__(self):
        # Screen setup
        self.window = turtle.Screen()
        self.window.setup(1000, 800)
        # self.window.bgcolor(self.giv_color())
        # Pen setup
        self.pen = turtle.Turtle()
        self.pen.width(2)
        self.pen.speed(0)
        # self.pen.hideturtle()

    def draw_pat(self, coord):
        l = 50
        d = 20 / math.cos(math.radians(60))
        self.pen.up()
        self.pen.goto(coord)
        self.pen.down()
        # self.pen.begin_fill()
        # self.pen.right(180)
        # self.pen.forward(20)
        #self.pen.right(90)
        self.pen.left(90)
        self.pen.forward(150)
        self.pen.left(120)
        self.pen.forward(l)
        self.pen.right(30)
        self.pen.forward(d)
        self.pen.right(150)
        self.pen.forward(l - 10 + 2 * d * math.cos(math.radians(30)))

        self.pen.right(60)
        self.pen.forward(l - 10 + 2 * d * math.cos(math.radians(30)))
        self.pen.right(150)
        self.pen.forward(d)
        self.pen.right(30)
        self.pen.forward(l)
        self.pen.left(120)
        self.pen.forward(150)
        self.pen.right(90)
        self.pen.forward(20)

        #self.pen.end_fill()

    def dra(self, coords):
        mov_len = 100
        self.pen.up()
        self.pen.goto(coords)
        self.pen.down()
        self.pen.left(90)
        self.pen.forward(mov_len)
        self.pen.left(120)
        self.pen.forward(mov_len / 2)
        self.pen.up()
        self.pen.backward(mov_len / 2)
        self.pen.down()
        self.pen.left(120)
        self.pen.forward(mov_len / 2)


    def clear_canvas(self):
        self.window.clear()

    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def save_img(self):
        self.window.getcanvas().postscript(file="bauhaus - {0}_{1}.eps".format(self.get_time(), str(randint(0, 10000))))


if __name__ == "__main__":
    ob = Pat()
    x, y = -400, 400
    offset = 50 * math.cos(math.radians(30)) - 5
    '''
    ob.draw_pat((x, y))
    ob.pen.right(60)
    ob.draw_pat((x, y))
    ob.pen.right(60)
    ob.draw_pat((x, y))
    '''
    for i in range(5):
        y = 400
        if i % 2 == 0:
            y -= offset
        else:
            y += offset
        x += 100 * math.cos(math.radians(30)) * 1.5 #- 15
        for k in range(5):
            y -= 100 * math.cos(math.radians(30)) * 1.5
            ob.dra((x, y))
            ob.pen.right(90)
            ob.dra((x, y))
            ob.pen.right(90)
            ob.dra((x, y))
            ob.pen.right(90)
    input()