import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


orientations = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(10)
    
for _ in range(1000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(orientations))

screen = t.Screen()
screen.exitonclick()