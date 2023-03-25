import turtle

def polygon(t, size, n):
    t.pendown()
    n = 360/n
    for i in range(size):
        t.forward(size)
        t.right(n)


def star(t, size, n):
    t.pendown()
    n = 180 - 180/n
    for i in range(size):
        t.forward(100)
        t.right(n)


s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("grey")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("arrow")  
t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=1, speed=0)

t.penup()               
t.goto(-150,100) # move the pen to the left upper corner
t.color('pink')
polygon(t, 80, 8)

t.penup()               
t.goto(100,-100)        # move the pen to the right bottom corner
t.color('gold')
star(t, 5, 5)


t.penup()
t.home
