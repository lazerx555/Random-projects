from turtle import *;from colorsys import *

# setup
hideturtle()
speed(99999)
Screen().bgcolor("black")

# loop
for i in range(3000):
    # color
    i /= 5
    color(hsv_to_rgb(i/300,0.5,1))
    # circle
    circle(i/2)
    # move to next pos with faster render
    tracer(0,0)
    
    left(i/2+i)
    forward(i)
    
    update()
    
exitonclick()
