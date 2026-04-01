import math
radius = int(input("Your radius for your cylinder"))
height = int(input("Your height for your cylinder"))
operation = str(input("Do you want to measure the Volume, CSA or TSA?"))
if operation == "Volume":
    result = 3.14 * radius * radius * height
    print("The volume of your cylinder is", result)
elif operation == "CSA":
    result = 2 * 3.14 * radius * height
    print("The CSA of your cylinder is", result)
elif operation == "TSA":
    result = 2 * 3.14 * radius * radius + 2 * 3.14 * radius * height
    print("The TSA of your cylinder is")
    
    