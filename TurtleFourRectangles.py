from turtle import *
turtle = Turtle()
screen = Screen()
def function_name():
    for i in range(2):
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
function_name()
def function_name2():
    for i in range(3):
        turtle.left(90)
        function_name()
function_name2()