from turtle import *
def name():
    while True:
        turtle = Turtle()
        screen = Screen()
        for i in range(360):
            turtle.forward(1)
            turtle.right(1)
name()
input = str(input("Do you want to do it again? "))
if input == "Yes":
    name()