from turtle import *
turtle = Turtle()
screen = Screen()
def function_name():
    for i in range(8):
        turtle.forward(70)
        turtle.left(45)
function_name()
def function_name2():
    for i in range(3):
        turtle.left(90)
        function_name()
function_name2()