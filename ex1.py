import turtle


def draw_square(t, side):
    for i in range(4):
        t.fd(side)
        t.left(90)


def draw_nested_squares(ini_sz, step, n):
    #draw square then goto initial vertex of the next
    for sz in range(ini_sz, ini_sz + step * n, step):
        draw_square(t, sz)
        t.penup()
        t.goto(t.pos() - [step / 2, step / 2])
        t.pendown()


# init window
wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Nested Squares")

# init turtle
t = turtle.Turtle()
t.pencolor("pink")
t.pensize(3)

draw_nested_squares(20, 20, 5)

wn.mainloop()
