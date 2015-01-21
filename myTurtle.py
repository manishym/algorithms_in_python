#!/usr/local/bin/env python

import turtle

myTurtle = turtle.Turtle()
myCanvas = turtle.Screen()


def draw_spiral(mt, lineLen):
    if lineLen > 0:
        mt.forward(lineLen)
        mt.right(90)
        draw_spiral(mt, lineLen - 5)



def main():
    draw_spiral(myTurtle, 200)
    myCanvas.exitonclick()


if __name__ == '__main__':
    main()
