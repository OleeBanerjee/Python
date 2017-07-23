#FirstProject
import turtle

t = turtle.Turtle()
w = turtle.Screen()

t.color("blue")
t.fillcolor("pink")
t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.end_fill()
#CirclePart
t.fillcolor("purple")
t.begin_fill()

t.right(90)
t.forward(50)
t.right(180)
t.circle(50)

t.end_fill()

