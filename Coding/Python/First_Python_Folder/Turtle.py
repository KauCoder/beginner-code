import turtle

pen = turtle.Turtle()
pen.color("green")
pen.pensize(3)
pen.speed(100)
pen.shape("turtle")

pen.right(90)

for i in range(50):
    pen.circle(100, 360, 1000)
    pen.forward(5)
turtle.done()