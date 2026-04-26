import turtle
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.speed("fastest")
tim.shape("turtle")
turtle.colormode(255)
tim.hideturtle()

screen = Screen()
screen.bgcolor(0,0,0)
screen.title("Spirograph")
screen.setup(width=1.0, height=1.0)
screen.screensize(3000, 3000)


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b


def draw_spiro(radius,size_gap):
    for _ in range(int(360/size_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.left(size_gap)

draw_spiro(50,15)

screen.exitonclick()