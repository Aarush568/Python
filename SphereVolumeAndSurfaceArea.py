import math
radius = int(input("The radius of your sphere"))
operation = str(input("Do you want to measure the Volume or Surface Area?"))
if operation == "Volume":
    result = 4/3 * 3.14 * radius * radius * radius
    print("The volume of your sphere is", result)
elif operation == "Surface Area":
    result = 4 * 3.14 * radius * radius
    print("The surface area of your sphere is", result)
else:
    print("Sorry, we don't know what you want to measure")