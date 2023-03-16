import turtle

"""
Creates a state.
:param t: turtle to be used
:param ini_sz: initial line length
:param step: increment size
:param n: number of lines
:param turn_angle: degrees of rotation for consecutive lines
"""
def draw_spiral(t, step, ini_sz, n, turn_angle):
    for sz in range(ini_sz,ini_sz+n*step,step):
        t.fd(sz)
        t.right(turn_angle)


# init window
wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Nested Squares")

# init turtle
t = turtle.Turtle()
t.pencolor("blue")
t.pensize(2)

t.goto(0,0)
t.setheading(-90)

draw_spiral(t, 3, 3, 80, 90)

t.penup()
t.goto(300,0)
t.pendown()

draw_spiral(t, 3, 3, 80, 88)

wn.mainloop()