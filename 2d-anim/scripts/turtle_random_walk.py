import turtle
from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.pencolor("black")
tim.speed("fastest")
screen = Screen()
screen.bgcolor("aqua")
tim.pensize(15)

angle =  [90,180,270,360]

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

for _ in range(1000):
    tim.pencolor(random_color())
    tim.forward(25)
    tim.right(choice(angle))

screen.setup(width=1.0, height=1.0)
screen.screensize(3000, 3000)
screen.exitonclick()


