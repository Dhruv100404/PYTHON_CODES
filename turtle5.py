from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move():
    t.forward(10)


s.listen()
s.onkey(key="space", fun=move)
s.exitonclick()