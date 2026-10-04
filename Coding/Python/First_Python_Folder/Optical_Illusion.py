import turtle

screen = turtle.Screen()
screen.title("Optical Illusion")
screen.bgcolor("black")
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

pen = turtle.Turtle()
pen.shape("turtle")
pen.width(3)
pen.speed(10)
pen.teleport(0, 0)

for i in range(120):
    colours = ["red", "green", "blue"]
    pen.color(colours[i % len(colours)])
    pen.circle(50, 360, 4)
    pen.penup()
    pen.right(5)
    pen.pendown()

pen.hideturtle()
screen.mainloop()