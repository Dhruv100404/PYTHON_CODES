import random
from turtle import Turtle, Screen

colors = ["Blue", "Yellow", "Wheat", "Red", "Orange"]

tim = Turtle()
s = Screen()

movement = [0, 90, 180, 270]

tim.pensize(10)

for _ in range(500):
    tim.color(random.choice(colors))


    tim.forward(20)
    tim.speed(0)
    tim.setheading(random.choice(movement))

s.exitonclick()
