import turtle

screen = turtle.Screen()
screen.title("Coily Sphere")
screen.bgcolor("black")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10000000)
pen.teleport(0, 0)

for i in range(100):
    colours = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "magenta", "pink", "lightpink"]
    pen.color(colours[i % len(colours)])
    pen.circle(50, 360, 100)
    pen.penup()
    pen.left(5)
    pen.forward(1)
    pen.pendown()

pen.hideturtle()
screen.mainloop()