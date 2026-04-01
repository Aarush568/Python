import math
SideA = int(input("First side: "))
SideB = int(input("Second side: "))
SideC = round(math.sqrt(SideA**2 + SideB**2), 2)
print("The length of your hypotenuse is around", SideC)