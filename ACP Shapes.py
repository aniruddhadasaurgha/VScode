import turtle

t = turtle.Turtle()
t.speed(2)
t.pensize(3)
turtle.bgcolor("black")
t.pencolor("White")

turtle.title("Shapes with Turtle Graphics")
turtle.colormode(255)
turtle.setup(width=800, height=600)

t.penup()
t.fillcolor("Green")
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-250, -100) 
t.pendown()
t.fillcolor("Blue")
t.begin_fill()
for _ in range(3):
        t.forward(200)
        t.left(120)
t.end_fill()
t.penup()
t.goto(250, 300)
t.pendown()
t.fillcolor("Red")
t.begin_fill()
for _ in range(6):
        t.forward(100)
        t.right(60)
t.end_fill()
t.penup()
turtle.done()

