import time
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

t.shape("square")
t.shapesize(1, 3)
t.color("White")


t.forward(100)


s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My snake game")
time.sleep(10)

s.exitonclick()
