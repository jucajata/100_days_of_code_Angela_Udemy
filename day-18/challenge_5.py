'''Draw a Spirograph'''

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed("fastest")
r = 100

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(r)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(1)

screen = t.Screen()
screen.setup(width=800, height=800)
screen.exitonclick()