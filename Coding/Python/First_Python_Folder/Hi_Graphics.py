import turtle

screen = turtle.Screen()
screen.title("Hi")
screen.bgcolor("black")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

pen = turtle.Turtle()
pen.width(2)
pen.shape("turtle")
pen.speed(3)


def Hi():
    pen.penup()
    pen.goto(-250, 250)
    pen.setheading(-90)
    pen.pendown()

    def H():
        pen.forward(150)
        pen.right(180)
        pen.penup()
        pen.forward(50)
        pen.pendown()
        pen.right(90)
        pen.forward(100)
        pen.penup()
        pen.left(90)
        pen.forward(100)
        pen.pendown()
        pen.right(180)
        pen.forward(150)

    def I():
        pen.forward(50)
        pen.right(180)
        pen.penup()
        pen.forward(25)
        pen.pendown()
        pen.left(90)
        pen.forward(100)
        pen.penup()
        pen.right(90)
        pen.forward(25)
        pen.pendown()
        pen.right(180)
        pen.forward(50)

    H()
    pen.penup()
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.pendown()
    I()

Hi()

screen.mainloop()