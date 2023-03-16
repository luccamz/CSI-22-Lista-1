import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.fd(sz)
        t.left(360/n)


# init window
wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Nested Squares")

# init turtle
t = turtle.Turtle()
t.pencolor("pink")
t.pensize(3)

#draw_poly(t, 10, 50)

wn.mainloop()