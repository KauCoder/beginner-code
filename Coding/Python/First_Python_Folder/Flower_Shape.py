import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Kaushal's Symmetrical Rainbow Pattern with Lines")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

pen = turtle.Turtle()
pen.width(3)
pen.speed(50)
pen.shape("turtle")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "magenta", "pink", "lightpink"]

num_petals = 15
radius = 100

pen.penup()
pen.goto(0, 0)
pen.pendown()

for i in range(num_petals):
    pen.color(colors[i % len(colors)])
    pen.circle(60, 360)
    pen.right(360 / num_petals)

pen.hideturtle()
screen.mainloop()