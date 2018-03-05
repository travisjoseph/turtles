# This Python script uses the turtle package to draw a fractal using recursion
# Uses what I've learned from the Udacity Fullstack course in conjuction with 
# Daniel Shiffman's Nature of Code.

import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    timmy = turtle.Turtle()

    timmy.color("orange")
    timmy.width(1)
    timmy.speed(0)
    timmy.shape("turtle")

    draw_circle(timmy, 200, 0, 0)

    window.exitonclick()

def draw_circle(t, r, x, y):
    f=1.5 #scale factor for radius
    set_position(t,x,y) #moved to spearate function just to clean up this one
    t.circle(r)
    if r>50:
        draw_circle(t, r/f, x+r/f, y)
        draw_circle(t, r/f, x-r/f, y)
        draw_circle(t, r/f, x, y+r/f)
        draw_circle(t, r/f, x, y-r/f)

def set_position(t, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()

draw_art()