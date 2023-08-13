import turtle

turtle.home()

size_of_gap = int(20)

for _ in range(int(360/size_of_gap)):
    turtle.circle(100)
    current_heading = turtle.heading()

    turtle.setheading(current_heading + size_of_gap)
    turtle.circle(100)

turtle.speed(1)
turtle.exitonclick()
