import turtle

screen = turtle.Screen()
screen.bgcolor("black")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
screen.title("Kaushal's Turtle")

pen = turtle.Turtle()
pen.width(5)
pen.shape("turtle")
pen.color("green")
pen.speed(1)
pen.teleport(100, -100)
def rainbow_square():
    for i in range(3):
        colours = ["red", "blue", "yellow", "green"]
        pen.color(colours[i])
        pen.forward(100)
        pen.right(90)
    pen.forward(100)

rainbow_square()

for i in range(3):
    pen.forward(200)
    rainbow_square()
pen.forward(200)
pen.hideturtle()
screen.mainloop()