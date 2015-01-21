#!/usr/local/bin/env python

import turtle
import random

myTurtle = turtle.Turtle()
myCanvas = turtle.Screen()


def draw_fractal(mt, branch):
    mt.pensize(branch // 5)
    angle = random.randrange(15, 40)
    color = "#%02xFF%02x" % (150 - branch * 150 // 75, 150 - branch * 150 // 75)
    myTurtle.color(color)
    if branch > 5:
        mt.forward(branch)
        mt.right(angle)
        draw_fractal(mt, branch - 15)
        mt.left(2 * angle)
        draw_fractal(mt, branch - 15)
        mt.right(angle)
        mt.backward(branch)


def main():
    myTurtle.color("#00FF00")
    myTurtle.left(90)
    myTurtle.backward(50)
    draw_fractal(myTurtle, 75)
    myCanvas.exitonclick()


if __name__ == '__main__':
    main()
