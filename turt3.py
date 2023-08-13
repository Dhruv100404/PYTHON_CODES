from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.shapesize(3)
timmy.color("Yellow")
for i in range(3,10):
    for y in range(0,i):

        timmy.forward(100)
        timmy.right(360/i)

screen = Screen()
screen.exitonclick()

