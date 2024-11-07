from turtle import Turtle, Screen
import
from colorgram import *
import random
turtle = Turtle()
screen = Screen()
screen.colormode(255)
colors = colorgram.extract(dots.webp)
turtle.speed(10)



for x in range(int(360)):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.circle(100)
    turtle.right(turtle.heading() + 10)



screen.exitonclick()

