#!/usr/local/bin/env python

import turtle


def getMid(p, q):
    return [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def sierpinski(myPoints, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(myPoints, colormap[degree], myTurtle)
    if (degree > 0):
        sierpinski([myPoints[0], getMid(myPoints[0], myPoints[1]), getMid(myPoints[0], myPoints[2])], degree - 1, myTurtle)
        sierpinski([myPoints[1], getMid(myPoints[1], myPoints[0]), getMid(myPoints[1], myPoints[2])], degree - 1, myTurtle)
        sierpinski([myPoints[2], getMid(myPoints[2], myPoints[0]), getMid(myPoints[2], myPoints[1])], degree - 1, myTurtle)


def main():
    t = turtle.Turtle()
    scr = turtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, t)
    scr.exitonclick()


if __name__ == '__main__':
    main()