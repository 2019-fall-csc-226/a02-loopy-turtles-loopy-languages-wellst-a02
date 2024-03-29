######################################################################
# Author: Taran Wells
# Username: wellst
#

# Assignment: A02: Exploring Turtles in Python
# Purpose: practice with loops and turtles
######################################################################
# Acknowledgements:

# Original code by: Taran Wells

# Google doc: https://docs.google.com/document/d/1uxFlK3YvEoEVq_XXDxMCyNvz4PJpU8r8TpwmFv4rRj0/edit?usp=sharing
######################################################################
import turtle


wn = turtle.Screen()
# background black
turtle.bgcolor("black")
# create red hidden turtle
Star = turtle.Turtle()
Circle = turtle.Turtle()
Star.hideturtle()
Circle.hideturtle()
Star.setpos(-100, 50)
Circle.setpos(-100, 50)
Star.color("red")

# move to circle start position
Circle.penup()
Circle.right(-144)
Circle.backward(200)
Circle.right(108)

for i in range(20):
    # create star
    Star.begin_fill()
    for t in range(0, 5):
        Star.forward(200)
        Star.right(144)
    # fill star
    Star.end_fill()
    # draw circle around star
    Circle.begin_fill()
    Circle.pendown()
    Circle.circle(105)
    # fill circle
    Circle.end_fill()

wn.exitonclick()
