
from turtle import Turtle, Screen
import math
t = Turtle()

t.shape("turtle")
t.lt(90)

lv = 12
l  = 90
s  = 26

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l, level):
    l = 3.0/4.0*l
    t.lt(s)
    t.fd(l)
    level +=1
    if level<lv:
        draw_tree(l, level)

    t.bk(l)
    t.rt(2*s)
    t.fd(l)
    if level<=lv:
        draw_tree(l, level)
    t.bk(l)
    t.lt(s)
    level -=1

t.speed(100)
draw_tree(l, 3)

ny_screen = Screen()
ny_screen.exitonclick()