# Colorgram Package
'https://pypi.org/project/colorgram.py/'

import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)

# Obtenemos los colores de la imagen
colors = colorgram.extract("day-18-start/hirst-painting/hirst_spot_painting.jpg", 40)
rgb_colors = [color.rgb for color in colors]
colors = [(rgb.r, rgb.g, rgb.b) for rgb in rgb_colors][3:]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def build_ten_points():
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range(10):
    build_ten_points()

screen = t.Screen()
screen.exitonclick()

