import math
radius = int(input("The radius of your cone: "))
height = int(input("The height of your cone: "))
operation = str(input("Do you want to measure the Volume, LSA or TSA? "))
if operation == "Volume":
    result = 1/3 * math.pi * radius**2 * height
    print("The volume of your cone is: ", round(result, 2))
elif operation == "LSA":
    result = math.pi * radius * math.sqrt(radius**2 + height**2)
    print("The LSA of your cone is: ", round(result, 2))
elif operation == "TSA":
    result = math.pi * radius**2 + math.pi * radius * math.sqrt(radius**2 + height**2)
    print("The TSA of your cone is: ", round(result, 2))
else:
    print("Sorry, we don't know what you want to measure.")
