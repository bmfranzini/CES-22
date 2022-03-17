import turtle


def draw_poly(t, n, size):
    for i in range(n):
        t.forward(size)
        t.left(360 / n)


wn = turtle.Screen()
tess = turtle.Turtle()
draw_poly(tess, 8, 50)
wn.mainloop()