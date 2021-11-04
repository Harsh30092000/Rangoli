from turtle import *

t = Turtle()
t.speed(0)

def makeFlower(radius,n): #6(leaf) 
    for i in range(n):
            t.circle(radius,720//n)
            t.left(360//n)


nc = 40
colors = ['red', 'purple']
for i in range(nc):
    for j in range(4):
        t.color(colors[i%len(colors)])
        t.fillcolor(colors[i%len(colors)])
        t.begin_fill()
        t.circle(90-i*2)
        t.end_fill()
        t.left(90)
    t.left(99)

#t is facing east
n=15

for i in range(1,n+1):
    t.up()
    t.forward(180)
    t.right(60) #adjust for the angle of the leaf
    t.down()
    for k in range(6):
        t.color(colors[k%len(colors)])
        t.fillcolor(colors[k%len(colors)])
        t.begin_fill()
        makeFlower(90-(k*10),6)
        t.end_fill()
    
    #Get the turtle to the starting position
    t.up()
    t.setx(0)
    t.sety(0)
    t.down()
    t.seth((360//n)*i)


mainloop()

