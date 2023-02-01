from swampy.TurtleWorld import *

world = TurtleWorld()
tim = Turtle()
print(tim)
for i in range(4):
    fd(tim, 100)
    lt(tim)

wait_for_user()
