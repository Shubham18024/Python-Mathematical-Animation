from turtle import Turtle, Screen
from random import choice

tim = Turtle()

tim.shape("turtle")
tim.color("indigo")
tim.pencolor("black")
tim.speed("normal")
screen = Screen()
screen.bgcolor("aqua")
tim.pensize(3)

colors = [
    "red", "green", "blue", "gold", "magenta", "silver", "black", "brown", "indigo", "IndianRed", "DarkOrchid",
    # Vibrant & strong
    "Crimson", "OrangeRed", "DeepPink", "DarkTurquoise", "Chartreuse", "LimeGreen", "DodgerBlue", "MediumVioletRed",
    # Elegant & rich
    "MidnightBlue", "DarkSlateGray", "RoyalBlue", "FireBrick", "DarkGoldenRod", "Chocolate", "OliveDrab", "SeaGreen",
    # Earthy & natural
    "Sienna", "Peru", "BurlyWood", "SaddleBrown", "DarkOliveGreen", "ForestGreen", "Teal",
    # Extra eye-catching
    "Orchid", "Turquoise", "SpringGreen", "SteelBlue", "Tomato", "Violet", "HotPink", "Coral",
    # Unique accents
    "SlateBlue", "Plum", "Khaki", "DarkCyan", "RosyBrown", "LightSlateGray"
]




def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for side in range(3,11):
    tim.color(choice(colors))
    draw_shape(side)


screen.exitonclick()