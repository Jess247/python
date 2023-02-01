from swampy.TurtleWorld import *
import math

world = TurtleWorld()
tom = Turtle()


def rect(t):
    for i in range(2):
        fd(t, 200)
        lt(t)
        fd(t, 100)
        lt(t)


def square(t, l):
    for i in range(4):
        fd(t, l)
        lt(t)


def polygon(t, l, n):
    ''' draw a polygon
    t: Turtle-Object
    l: length of a single segment
    n: number of line segments
    '''
    degree = 360.0 / n
    for i in range(n):
        fd(t, l)
        lt(t, degree)


def circle(t, r):
    outline = 2 * math.pi * r
    n = int(outline/3) + 1
    length = outline / n
    polygon(t, n, length)


# rect(tom)
# square(tom, 100)
polygon(tom, 7, 70)
# circle(tom, 30)
wait_for_user()
