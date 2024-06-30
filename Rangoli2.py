from turtle import *
import math

t = Turtle()
t.speed(0)
t.width(2)
t.screen.bgcolor("black")
t.color('white')
scale = 1

#Util
#-------------------------------------------------------------------------------
def default(t):
    t.up()
    t.setx(0)
    t.sety(0)
    t.seth(0)
    t.down()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.left(90)

#Inner Square
#--------------------------------------------------------------------------------
def innerCircle():
    default(t)
    t.fillcolor('#73070A')
    t.begin_fill()
    t.up()
    t.right(90)
    t.forward(10*scale)
    t.down()
    t.left(90)
    t.circle(10*scale)
    t.end_fill()

def buds():
    default(t)
    for i in range(1,5):
        t.up()
        t.forward(10*scale)
        t.down()
        t.forward(25*scale)
        t.right(90)
        t.fillcolor('white')
        t.begin_fill()
        t.circle(5*scale)
        t.end_fill()
        default(t)
        t.left(90*i)

def flower():
    default(t)
    for i in range(1,5):
        t.right(15)
        t.begin_fill()
        t.fillcolor('orange')
        for j in range(2):
            t.circle(20*scale,120)
            t.left(60)
        t.end_fill()
        default(t)
        t.left(90*i)


def point():
    default(t)
    for i in range(1,5):
        t.up()
        t.forward(40*scale)
        t.left(90)
        t.forward(35*scale)
        t.right(90)
        t.down()
        t.fillcolor('white')
        t.begin_fill()
        t.circle(5*scale)
        t.end_fill()
        default(t)
        t.left(90*i)
    

def outerLayer():
    t.fillcolor('#3B1E13')
    t.up()
    t.goto(-60,-60)  #inner square
    t.down()
    t.begin_fill()
    square(t,60*2*scale)
    t.end_fill()


#--------------------------------------------------------------------------------


#Outer Square
#--------------------------------------------------------------------------------
def outerBigLayer():
    default(t)
    t.fillcolor('purple')
    t.up()
    t.goto(-(100*(8)**(1/2)),0)  #inner square
    t.right(45)
    t.down()
    t.begin_fill()
    square(t,200*2*scale)
    t.end_fill()


def smallFlower():
    default(t)
    for i in range(1,5):
        t.right(25)
        t.begin_fill()
        t.fillcolor('orange')
        t.up()
        t.forward(50*scale)
        t.down()
        for j in range(2):
            t.circle(36*scale,150)
            t.left(35)
        t.end_fill()
        default(t)
        t.left(90*i)

def outersquareFlower():
    default(t)
    n = 19
    for i in range(n):
        t.up()
        t.backward(150*math.pow(2, (1/2))*scale)
        t.right(45)
        t.down()
        t.fillcolor('#FA2C96')
        t.begin_fill()
        square(t, 300)
        t.end_fill()
        default(t)
        t.left(360/n *(i))
        
    

#--------------------------------------------------------------------------------
def innerSquare():
    default(t)
    #outbox
    outerLayer()

    t.fillcolor('#3B1E13')
    t.up()
    t.goto(-50,-50)  #inner square
    t.down()
    t.begin_fill()
    square(t, 50*2*scale)
    t.end_fill()
    default(t)
    flower()
    innerCircle()
    buds()
    point()
    
    
def outerSquare():
    #outerBigLayer()
    outersquareFlower()
    smallFlower()

def extdesign():
    default(t)

#--------------------------------------------------------------------------------
def final():
    
    outerSquare()
    innerSquare()
    extdesign()

#--------------------------------------------------------------------------------)
final()
t.ht()
mainloop()