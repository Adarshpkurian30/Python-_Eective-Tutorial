n=int(input("enter the number of stars:"))

import turtle 
import math
t=turtle.Turtle()
t.penup()


t.goto(100, 0)
t.pendown()

t.penup()
def star():
    t.fillcolor("blue")
    t.begin_fill()
    t.right(36)  
    for i in range(5):  
        t.forward(50)
        t.right(144)  
        t.forward(50)
        t.left(72)  
    t.end_fill()

for i in range(n):

    angle = (360 / n) * i  
    x = 100* math.cos(math.radians(angle))
    y = 100 * math.sin(math.radians(angle))
    t.goto(x, y)
    t.pendown()
    star()
    t.penup()
        


