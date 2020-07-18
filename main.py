import turtle  
t = turtle.Turtle()
wn=turtle.Screen()
turtle.colormode(255)
wn.bgcolor(77, 77, 77)
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.end_fill()

t.goto(0,200)
#______yellow rectangle_________
rectangle("yellow")
#______green rectangle__________
t.right(180)
rectangle("green")
#______red rectangle___________
t.begin_fill()
t.fillcolor("red")
t.right(90)
t.goto(0,200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

#_______star portion____________
t.left(90)
t.goto(0,100)
t.left(90)
t.up()
t.forward(35)
t.down()
t.begin_fill()
t.fillcolor("black") 
for i in range(5): 
    t.forward(40) 
    t.right(144) 

t.end_fill()

#____credit__________
t.up()
t.forward(200)
t.left(90)
t.forward(200)
t.color("white")
style = ('Comic Sans MS', 30)
t.write('Flag of guinea-bissau', font=style)
#t.right(90)
t.forward(60)
style = ('Comic Sans MS', 24)
t.write('Jaima Jarnaz', font=style)
t.hideturtle()


turtle.done() 
