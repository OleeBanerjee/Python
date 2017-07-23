import turtle

t = turtle.Turtle()
w = turtle.Screen()

t.color("saddlebrown")
t.fillcolor("saddlebrown")
t.begin_fill()

t.forward(76)
t.right(90)
t.forward(350)
t.right(90)
t.forward(76)
t.right(90)
t.forward(350)

t.end_fill()
t.color("green")
t.fillcolor("green")
t.begin_fill()

t.right(90)
t.forward(38)
t.right(90)
t.circle(50)

t.right(90)
t.right(90)
t.circle(50)

t.right(90)
t.circle(50)

t.right(180)
t.circle(50)

t.end_fill()
