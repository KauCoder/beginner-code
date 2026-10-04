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
pen.speed(2)

def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def draw_K():
    pen.setheading(90)
    pen.forward(100)
    pen.backward(50)
    pen.setheading(45)
    pen.forward(70)
    pen.backward(70)
    pen.setheading(-45)
    pen.forward(70)

def draw_A():
    pen.setheading(75)
    pen.forward(100)
    pen.setheading(-75)
    pen.forward(100)
    pen.backward(50)
    pen.setheading(180)
    pen.forward(26)

def draw_U():
    pen.penup()
    pen.goto(pen.xcor(), pen.ycor() + 100)
    pen.setheading(-90)
    pen.pendown()
    pen.forward(80)
    pen.circle(20, 180)
    pen.forward(80)

def draw_S():
    pen.setheading(0)
    pen.forward(40)
    pen.circle(20, 180)
    pen.forward(40)
    pen.circle(-20, 180)
    pen.forward(40)

def draw_H():
    pen.setheading(90)
    pen.forward(100)
    pen.backward(50)
    pen.setheading(0)
    pen.forward(40)
    pen.setheading(90)
    pen.forward(50)
    pen.backward(100)

def draw_L():
    pen.setheading(90)
    pen.forward(100)
    pen.backward(100)
    pen.setheading(0)
    pen.forward(50)

start_x = -300
y = -50
spacing = 80

move_to(start_x, y)
draw_K()

move_to(start_x + spacing, y)
draw_A()

move_to(start_x + spacing * 2, y)
draw_U()

move_to(start_x + spacing * 3, y)
draw_S()

move_to(start_x + spacing * 4, y)
draw_H()

move_to(start_x + spacing * 5, y)
draw_A()

move_to(start_x + spacing * 6, y)
draw_L()

pen.hideturtle()
screen.mainloop()