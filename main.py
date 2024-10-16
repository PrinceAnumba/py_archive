# Import another module

from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)


def cube():
    timmy.home()

    timmy.lt(90)
    timmy.forward(50)
    timmy.lt(120)
    timmy.forward(50)
    timmy.lt(60)
    timmy.forward(50)
    timmy.lt(120)
    timmy.forward(50)
    # timmy.forward(300)
    # timmy.left(120)
    # timmy.forward(250)


cube()

# print(round(timmy.xcor(), 5))

ny_screen = Screen()
ny_screen.exitonclick()