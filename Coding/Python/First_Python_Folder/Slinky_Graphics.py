import turtle

screen = turtle.Screen()
screen.bgcolor("black")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
screen.title("Slinky")

pen = turtle.Turtle()
pen.width(3)
pen.shape("turtle")
pen.speed(10)

pen.teleport(0, -100)

for i in range(10):
    colours = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "magenta", "pink", "lightpink"]
    pen.color(colours[i])
    pen.circle(60, 360, 25)
    pen.penup()
    pen.forward(25)
    pen.left(25)
    pen.forward(25)
    pen.pendown()
pen.penup()
pen.hideturtle()

screen.mainloop()