from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.shapesize(3)
timmy.color("Yellow")
for _ in range(0,4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()

