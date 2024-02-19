
'''Generate a random walk'''

'''
Requerimientos:
1. Poner a caminar a la tortuga cierta distancia
2. Luego de caminar elegir una dirección aleatoria hacia el norte, sur, este u oeste.
3. Cada que camina se debe cambiar el color.
4. Aumentar el grosor de la linea.
5. Aumentar la velocidad de la linea.
'''

from turtle import Turtle, Screen
import random

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


orientations = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(10)
    
for _ in range(1000):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(orientations))

screen = Screen()
screen.exitonclick()