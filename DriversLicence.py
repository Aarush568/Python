answer = str(input("Welcome to X Driving School! How can I help you? Do you want to apply for a driver's licence? "))
if answer == "Yes":
    name = str(input("Oh so you want a driver's licence. What is your name to get things started? "))
    print("Hello", name, "! Hope you are doing fine")
    job = str(input("What do you do or what do you want to become in the future? "))
    print("You are", name, "who works as a", job)
    age = int(input("What is your age? "))
    if age < 16:
        print("You are too young to have a driver's licence. ")
    elif age >= 16:
        print("You are old enough to have a driver's licence. ")
else:
    print("You may be looking for somehting else. But this is for the application for a driver's licence. ")