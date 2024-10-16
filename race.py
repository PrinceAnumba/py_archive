import random
from turtle import Turtle, Screen
screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="What is your bet?", prompt="Who will win the race, input a color")
turtle_y_positions = [70, 40, 10, -20, -50, -80]
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
turtles = []
winner = ''


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle" )
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtles.append(new_turtle)



if user_choice:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winner = t.pencolor()
            # print(winner)
            if user_choice == winner:
                print("Congratulations! You Win")
            else:
                print(f"Sorry, {winner} is the winner")

        t.forward(random.randint(0, 10))







screen.exitonclick()