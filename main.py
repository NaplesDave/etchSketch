import turtle
from turtle import Turtle, Screen
# Dave King Etch-A-Sketch  via turtle drawing 2/9/2022
# press w to move forwards
#   s to move backwards
#   a to rotate counter-clockwise direction 10 deg
#   d to rotate clockwise direction 10 deg
#   c to clearscreen and reset turtle to center of screen
tim = Turtle()
screen = Screen()
turtle.degrees(360)

screen.listen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clear_screen():
    screen.reset()


def move_ccw():
    tim.left(10)


def move_cw():
    tim.right(10)


screen.onkey(move_forward, key="w")
screen.onkey(move_backwards, key="s")
screen.onkey(move_ccw, key="a")
screen.onkey(move_cw, key="d")
screen.onkey(clear_screen, key="c")

screen.exitonclick()
