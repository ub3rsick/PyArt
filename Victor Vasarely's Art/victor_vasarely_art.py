__author__ = 'Rizal'

import turtle
from random import randint
import time


class Victor:
    color_list = ["#FA7AFA", "#C4A0F3", "#A0DFF3", "#7EFFFB", "#7AFABD",
                  "#5A53E8", "#F4FC07", "#FF21DD", "#A81FC6", "#441D7A",
                  "#0EFFFC", "#36FF27", "#FFFD26", "#FA6417", "#FF2622",
                  "#2C0EF0", "#B300FF", "#6751F0", "#8119FF", "#050505",
                  "#05CDFF", "#AC05FF", "#FF05BC", "#FFC905", "#951BE0",
                  "#F507B5", "#F5E907", "#B5E009", "#0E0414", "#FF1919",
                  "#FF5E19", "#FF9F19", "#E4FF19", "#29FF19", "#EB2217",
                  "#FF2BF8", "#FF2BA3", "#FF2B67", "#FF2B2B", "#93FF28",
                  "#CFFF04", "#270436", "#FF2253", "#FF521B", "#FF006F",
                  "#00A8A0", "#1DCF7C", "#49FF30", "#81FF26", "#BEFF30",
                  "#FF0586", "#F76336", "#F7C736", "#36A4F7", "#55C728",
                  "#FFFB00", "#EC00BD", "#AE2DCE", "#CAFC00", "#DDD2C2"]

    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def giv_color(self):
        return self.color_list[randint(0, len(self.color_list) - 1)]

    def draw_rect(self, coord, dist):
        self.pen.color(self.giv_color())
        self.pen.up()
        self.pen.goto(coord)
        self.pen.begin_fill()
        self.pen.down()
        for ix in range(4):
            self.pen.forward(dist)
            self.pen.rt(90)
        self.pen.end_fill()

    def draw_circle(self, rad, coord):
        self.pen.color(self.giv_color())
        self.pen.up()
        self.pen.goto(coord)
        self.pen.down()
        self.pen.begin_fill()
        self.pen.circle(rad)
        self.pen.end_fill()

    def clear_canvas(self):
        self.pen.clear()

    @staticmethod
    def save_img():
        sc = turtle.Screen()
        sc.getcanvas().postscript(file="img - %s.eps" % time.time())


if __name__ == "__main__":
    x, y = -300, 300

    # change grid size and square size as required
    grid_size = 5
    square_size = move_dist = 60
    small_square = int(square_size / 2)
    ob = Victor()

    # square inside square
    for z in range(grid_size):
        for i in range(grid_size):
            ob.draw_rect((x + i * square_size, y - z * square_size), move_dist)
            ob.draw_rect((x + int(small_square / 2) * (2 * i + 1) + i * small_square,
                          y - int(small_square / 2) * (2 * z + 1) - z * small_square),
                         int(move_dist / 2))
    ob.save_img()
    ob.clear_canvas()
    # circle inside square
    for z in range(grid_size):
        for i in range(grid_size):
            ob.draw_rect((x + i * square_size, y - z * square_size), move_dist)
            radii = randint(2, int(square_size / 3))
            ob.draw_circle(radii, (x + int(square_size / 2) * (2 * i + 1),
                                   y - int(square_size / 2) * (2 * z + 1) - radii))


    ob.save_img()