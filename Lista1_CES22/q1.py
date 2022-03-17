import turtle


def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


wn = turtle.Screen()
tt = turtle.Turtle()
for e in range(1, 6):
    draw_square(tt, 20*e)
    tt.penup()
    tt.goto(-10*e, -10*e)
    tt.pendown()
wn.mainloop()