radius = int(input("Radius of your circle"))
operation = input("Do you want to measure the Area or Circumference")
if operation == "Area":
    result = 3.14 * radius * radius
    print(result)
elif operation == "Circumference":
    result = 2 * 3.14 * radius
    print(result)
else:
    print("Sorry, we don't know that do with your circle")