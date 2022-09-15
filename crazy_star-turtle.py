from turtle import *;from colorsys import *

# setup
hideturtle()
speed(99999)
Screen().bgcolor("black")
pensize(3)

#square func
def square(size):
    forward(size)
    left(90)

# loop
for i in range(3000):
    # color
    i /= 5
    color(hsv_to_rgb(i/300,1,1))
    # square
    square(i)
    # move to next pos with faster render
    tracer(0,0)
    left(45)
    forward(i)
    update()
exitonclick()
