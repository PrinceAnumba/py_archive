import turtle
from turtle import Turtle, Screen

from pynput.keyboard import Listener
# or
import keyboard

def on_press(event):
    print(f"Key pressed: {event.name}")

keyboard.on_press(on_press)


timmy = Turtle()
screen = Screen()

actions = []

def move_fowards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()


print(screen.onkey(move_fowards, key="Up"))
screen.onkey(move_backwards, key="Down")
screen.onkey(turn_left, key="Left")
screen.onkey(turn_right, key="Right")
screen.onkey(clear, key="space")

turtle.listen()

print(turtle.listen())


ny_screen = Screen()
ny_screen.exitonclick()