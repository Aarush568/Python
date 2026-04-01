import math
import time

def areatrapezoid(sideA, sideC, height):
    return (sideA + sideC) * height/2

def perimetertrapezoid(sideA, sideB, sideC, sideD):
    return sideA + sideB + sideC + sideD

def areacircle(radius):
    return math.pi * radius**2

def circumferencecircle(radius):
    return 2 * math.pi * radius

def timesleep():
    print("Give us some time to think.")
    time.sleep(2)

def main():
    
    shape = input("Enter the shape (trapezoid/circle): ")
    
    if shape == "trapezoid":
        calculation = str(input("What do you want to measure (area/perimeter)? "))
        
        if calculation == "area":
            
            sideA = int(input("Enter the first side of the trapezoid: "))
            sideC = int(input("Enter its parallel side: "))
            height = int(input("Enter the height of the trapezoid (the distance between the parallel sides): "))
            timesleep()
            area = areatrapezoid(sideA, sideC, height)
            print("The area of the trapezoid:", area)
        
        elif calculation == "perimeter":
            
            sideA = int(input("Enter the first side of the trapezoid: "))
            sideB = int(input("Enter the second side of the trapezoid: "))
            sideC = int(input("Enter the third side of the trapezoid: "))
            sideD = int(input("Enter the fourth side of the trapezoid: "))
            timesleep()
            perimeter = perimetertrapezoid(sideA, sideB,sideC,sideD) 
            print("The perimeter of the trapezoid:", perimeter)
            
        else:
            print("Invalid calculation!")
    
    
    elif shape == "circle":
        
        calculation = str(input("What do you want to measure (area/circumference)? "))
        
        if calculation == "area":
            radius = int(input("Enter the radius of the circle: "))
            timesleep()
            area = areacircle(radius)
            print("Area of the circle:", round(area, 2))
        
        elif calculation == "circumference":
            radius = int(input("Enter the radius of the circle: "))
            timesleep()
            circumference = circumferencecircle(radius)
            print("The circumference of the circle:", round(circumference, 2))
        
        else:
            print("Invalid calculation!")
    
    else:
        print("Invalid shape!")

main()

