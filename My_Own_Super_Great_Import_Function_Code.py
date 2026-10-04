import turtle
import colorsys
t = turtle
s = turtle.Screen().bgcolor("White")
turtle.speed(15)
n = 70
h = 70
turtle.shapesize(h, 5, 5)
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 15, 15)
    h+= 1/n
    t.color(h)
    t.left(4)
    t.fd(1)
    for i in range(2):
        t.left(2)
        t.circle(100)