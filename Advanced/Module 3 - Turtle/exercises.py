import turtle as tur
import random as r

# t = tur.Turtle()
# t.forward(100)
# t.left(30)
# t.backward(100)
# t.right(45)
# t.forward(-300)

# sides =  [100, 200]*2
# for i in sides:
#     t.forward(i)
#     t.right(90)
# tur.mainloop()

# t.forward(75)
# t.right(120)
# t.forward(150)
# t.right(120)
# t.forward(150)
# t.right(120)
# t.forward(75)
# tur.mainloop()

# n = 20
# inner_angle = (n-2)*180//n
# for x in range(n):
#     t.forward(100)
#     t.left(180 - inner_angle)


# t.pencolor("green")
#
#
# t.color("red")
# t.begin_fill()
# t.fillcolor("blue")
# t.circle(60)
# t.end_fill()



# t.color("brown")
# t.begin_fill()
# t.fillcolor("brown")
# t.forward(5)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(10)
# t.right(90)
# t.forward(100)
# t.right(5)
# t.end_fill()
#
# t.right(90)
# t.color("green")
# t.begin_fill()
# t.fillcolor("green")
# t.circle(60)
# t.end_fill()

# t.pensize(5)
# t.shapesize(5)
# t.hideturtle()
# t.showturtle()
# t.shape("turtle") #arrow ,turtle, circle ,square, trtiangle ,classic


# shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# colors = ["cyan", "magenta", "red", "yellow", "orange", "red", "pink"]
#
# for i in range(40):
#     t = tur.Turtle()
#     t.color(r.choice(colors))
#     t.left(r.randint(30, 120))
#     t.shape(r.choice(shapes))
#     t.forward(r.randint(30,300))

# t = tur.Turtle()
# for i in range(10):
#     if i % 2 == 0:
#         t.penup()
#     else:
#         t.pendown()
#     t.forward(10)


# def fun():
#     t.forward(100)
#     t.left(30)
#
# scr = tur.Screen()
# scr.onkey(fun, "space")
# scr.listen()

# scr = tur.Screen()
# t = tur.Turtle()

# def up():
#     t.forward(100)
#
# def down():
#     t.backward(100)
#
# def left():
#     t.left(90)
#
# def right():
#     t.right(90)
#
# scr.onkey(up, "up")
# scr.onkey(down, "down")
# scr.onkey(left, "left")
# scr.onkey(right, "right")
# scr.listen()

# def create_t(x,y):
#     t = tur.Turtle(shape="turtle", visible=False)
#     t.speed(-1)
#     t.color("magenta")
#     t.penup()
#     t.setpos(x,y)
#     t.shapesize(4)
#     t.showturtle()
#
# scr.onscreenclick(create_t, 1)
# scr.listen()
#
#
# tur.mainloop()

#1a - pięciokat
#1b - schody


t = tur.Turtle()
scr = tur.Screen()

#2a
# for i in range(6):
#     t.penup()
#     t.left(60)
#     t.forward(100)
#     t.pendown()
#     t.pensize(5)
#
#     t.fillcolor("red")
#     t.begin_fill()
#
#     for i in range(6):
#
#         t.left(150)
#         t.forward(100)
#
#         t.right(90)
#         t.forward(100)
#
#     t.end_fill()
#     t.hideturtle()

#2b
# side = 400
# for i in range (1,100):
#    t.forward(side)
#    t.left(90)
#    side=side-4

# colors = ["cyan", "magenta", "red", "yellow", "orange", "red", "pink", "green", "blue"]
# pen_state = 0
# pen_size = 2
# #3
def up():
    t.forward(50)

def down():
    t.backward(50)

def right():
    t.right(90)
    t.forward(50)

def left():
    t.left(90)
    t.forward(50)

def left_up():
    t.left(45)
    t.forward(50)

def right_up():
    t.right(45)
    t.forward(50)

def left_down():
    t.left(135)
    t.forward(50)

def right_down():
    t.right(135)
    t.forward(50)

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



tur.mainloop()

#for ambition

# t = tur.Turtle()
# t.begin_fill()
# t.color("red")
# t.pencolor("pink")
# t.pensize(10)
# t.penup()
# t.forward(240)
# t.left(90)
# t.forward(150)
# t.right(30)
# t.pendown()
# t.circle(120, 220)
# t.right(10)
# t.forward(400)
# t.left(148)
# t.forward(450)
# # t.left(160)
# # t.circle(120, 220)
# # t.left(5)
# # t.forward(381)
# # t.left(109.5)
# # t.forward(381)
# t.end_fill()
#
# tur.mainloop()

#projekt





