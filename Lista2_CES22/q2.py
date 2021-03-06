import turtle # Tess becomes a traffic light.


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


state_key = "green"
pen_width = 1


def state_green():
    global state_key
    tess.pensize(pen_width)
    tess.backward(140)
    tess.fillcolor("green")
    state_key = "green"
    wn.ontimer(state_blue, 3000)


def state_blue():
    global state_key
    tess.pensize(pen_width)
    tess.forward(70)
    tess.fillcolor("blue")
    state_key = "blue"
    wn.ontimer(state_red, 3000)


def state_red():
    global state_key
    tess.pensize(pen_width)
    tess.forward(70)
    tess.fillcolor("red")
    state_key = "red"
    wn.ontimer(state_green, 3000)


wn.ontimer(state_blue, 0)

wn.listen() # Listen for events
wn.mainloop()