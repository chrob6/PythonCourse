import turtle as tur
import random as r

t = tur.Turtle()
scr = tur.Screen()

colors = ["cyan", "magenta", "red", "yellow", "orange", "red", "pink", "green", "blue"]
pen_state = 0
pen_size = 2
move = 10

def up():
    global move
    t.forward(move)

def down():
    global move
    t.backward(move)

def right():
    global move
    t.right(90)
    t.forward(move)

def left():
    global move
    t.left(90)
    t.forward(move)

def left_up():
    global move
    t.left(45)
    t.forward(move)

def right_up():
    global move
    t.right(45)
    t.forward(move)

def left_down():
    global move
    t.left(135)
    t.forward(move)

def right_down():
    global move
    t.right(135)
    t.forward(move)

def change_color():
    t.color(r.choice(colors))

def on_off_draw():
    global pen_state
    if pen_state == 0:
        t.penup()
        pen_state = 1
    elif pen_state == 1:
        t.pendown()
        pen_state = 0

def smaller(x,y):
    global pen_size

    try:
        if pen_size > 0:
            pen_size = pen_size - 1
            t.shapesize(pen_size)
    except tur.TurtleGraphicsError:
        print("Cannot be smaller")

def larger(x,y):
    global pen_size
    pen_size = pen_size + 1
    t.shapesize(pen_size)


scr.onkey(up, "8")
scr.onkey(down, "2")
scr.onkey(left, "4")
scr.onkey(right, "6")
scr.onkey(left_up, "7")
scr.onkey(left_down, "1")
scr.onkey(right_down, "3")
scr.onkey(right_up, "9")
scr.onkey(change_color, "5")
scr.onkey(on_off_draw, "0")
scr.onscreenclick(smaller, 1)
scr.onscreenclick(larger, 3)

scr.listen()

point = tur.Turtle()
point.penup()

finish_x = r.choice([r.randint(-400,-300), r.randint(300,400)])
finish_x = r.choice([r.randint(-400,-300), r.randint(300,400)])
point.setposition(finish_x,finish_x)

point.pendown()
point.begin_fill()
point.color("red")
point.circle(8)
point.end_fill()
point.hideturtle()


tur.mainloop()