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
    if state_key == "red":
        tess.pensize(pen_width)
        tess.backward(140)
        tess.fillcolor("green")
        state_key = "green"


def state_blue():
    global state_key
    if state_key == "green":
        tess.pensize(pen_width)
        tess.forward(70)
        tess.fillcolor("blue")
        state_key = "blue"


def state_red():
    global state_key
    if state_key == "blue":
        tess.pensize(pen_width)
        tess.forward(70)
        tess.fillcolor("red")
        state_key = "red"


def increase_width():
    global pen_width
    if pen_width < 20:
        pen_width += 1


def decrease_width():
    global pen_width
    if pen_width > 1:
        pen_width -= 1


background = 0


def change_background():
    global background
    if background == 0: # Transition from state 0 to state 1
        wn.bgcolor("black")
        background = 1
    elif background == 1: # Transition from state 1 to state 0
        wn.bgcolor("lightgreen")
        background = 0


wn.onkey(state_green, "g")
wn.onkey(state_blue, "b")
wn.onkey(state_red, "r")
wn.onkey(increase_width, "+")
wn.onkey(decrease_width, "-")
wn.onkey(change_background, "space")
wn.listen() # Listen for events
wn.mainloop()