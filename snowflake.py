import turtle

def koch_snowflake(t,l,n):
    t.pendown()
    if n ==0:
        t.forward(l)
    else:
        koch_snowflake(t,l,n-1)
        t.left(60)
        koch_snowflake(t,l,n-1)
        t.right(120)
        koch_snowflake(t,l,n-1)
        t.left(60)
        koch_snowflake(t,l,n-1)




s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("yellow")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("arrow")  
t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=1, speed=0)


t.penup()
t.goto(-100,0)
t.color('pink')

for i in range(3):
    koch_snowflake(t,4,4)
    t.right(120)

t.penup()
t.home
