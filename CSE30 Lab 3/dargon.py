import turtle

def Dragon_curve(t,l,angle,n):
    t.pendown()
    if n ==0:
        t.forward(l)
    else:
        Dragon_curve(t,l,90,n-1)
        t.left(angle)
        Dragon_curve(t,l,-90,n-1)

s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("yellow")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("arrow")  
t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=1, speed=1000)


t.penup()
t.goto(-100,0)
t.color('pink')

Dragon_curve(t,4,90,50)

t.penup()
t.home
