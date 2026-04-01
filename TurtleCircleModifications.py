from turtle import *
turtle = Turtle()
screen = Screen()
Score = 0
turtle.width(int(input("Width")))
turtle.speed(int(input("Speed")))
turtle.color(111,222,211)
for i in range(360):
    turtle.forward(1)
    Score = Score + 1 
    print(Score)
    turtle.left(1)
    
    
