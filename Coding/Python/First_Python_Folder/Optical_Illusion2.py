import turtle
import colorsys

screen = turtle.Screen()
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call("wm", "attributes", ".", "-topmost", "1")
screen.title("Optical Illusion 2")
screen.colormode(255)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)
pen.width(3)
pen.color("white")


for i in range(360):
    hue = (i * 5) % 360 / 360
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    pen.color(r, g, b)

    pen.onclick(fun=pen.forward(1))

pen.hideturtle()
screen.mainloop()
