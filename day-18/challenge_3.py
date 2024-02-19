
'''Drawing Different Shapes'''

from turtle import Turtle, Screen
from random import randint

tim = Turtle()

colors = [
    'medium aquamarine', 
    'dark green', 
    'dark red', 
    'gold',
    'blue',
    'dark violet',
    'medium purple',
    'medium violet red',
    'orange red',
    'medium sea green'
    ]

for _ in range(3, 11):
    angle = 360/_
    tim.color(colors[randint(0, len(colors)-1)])
    for i in range(_):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()