import math
import time
def function_name():
    print("Give us some time to figure out the answer.")
    time.sleep(2)
radius = int(input("The radius of your hemisphere: "))
operation = input("Do you want to measure the Volume, CSA or TSA? ")
if operation == "Volume":
    function_name()
    result = 2/3 * math.pi * radius**3
    print("The volume of your hemisphere is:", round(result, 2))
elif operation == "CSA":
    function_name()
    result = 2 * math.pi * radius**2
    print("The CSA of your hemisphere is:", round(result, 2))        
elif operation == "TSA":
    function_name()
    result = 3 * math.pi * radius**2
    print("The TSA of your hemisphere is:", round(result, 2))
else:
    print("Sorry, we don't know what you want to measure.")

    
    