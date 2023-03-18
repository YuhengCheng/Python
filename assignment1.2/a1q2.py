'''
Yuheng Cheng
COMP 1405
Teacher: Professor Hillen
Date: October 04, 2020
Program overview: Utilises the python turtle function to create a grass field under 
a golden full moon on a starry night
'''
import turtle
t =turtle.Turtle()
turtle.screensize(1000,750)


#set colour of black sky
turtle.bgcolor('black')



#draw the ground
t.penup()
t.setposition(-500,-395)
t.pencolor('green')
t.pendown()
t.fillcolor('green')
t.begin_fill()
#use loop to draw rectangle for most of the grass
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(320)
    t.left(90)
t.end_fill()
#draw grass peaks
t.penup()
t.setposition(-500,-75)
t.pensize(3)
t.pendown()
#repeat for 10 peaks
for i in range(10):
    t.fillcolor('green')
    t.begin_fill()
    #draw a triangle
    for _ in range(3): 
         t.forward(100) 
         t.right(-120) 
    t.end_fill()
    t.forward(100)


#draw the golden full moon
t.penup()
t.setposition(250,250)
t.pencolor('yellow')
t.pensize(3)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()


#draw stars
#draw first row
t.setposition(-450,200)
t.pencolor('white')
#draw 5 stars
for i in range (5):
    t.fillcolor('white')
    t.begin_fill()
    #draw stars
    for i_ in range(5):
        t.pendown()
        t.forward(20) 
        t.right(144)
    t.end_fill()
    t.penup()
    t.forward(200)
#draw second row
t.setposition(-300,300)
t.pencolor('white')
#draw 4 stars
for i in range (4):
    t.fillcolor('white')
    t.begin_fill()
    #draw stars
    for _ in range(5):
        t.pendown()
        t.forward(20) 
        t.right(144)
    t.end_fill()
    t.penup()
    t.forward(200)

t.done()
