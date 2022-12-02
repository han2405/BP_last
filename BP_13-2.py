Type "help", "copyright", "credits" or "license()" for more information.
from turtle import *

t1=Turtle()
t1.shape("circle")

t2=Turtle()
t2.shape("turtle")

t3=Turtle()
t3.shape("square")

t1.penup()
t2.penup()
t1.goto(0,100)
t2.goto(0,50)
#t3은 0,0에 있으니까 안쓰는게?

t1.pendown()
t2.pendown()

while True:
    t1.circle(100)
    t2.circle(150)
    t3.circle(200)

