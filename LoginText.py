Login_app = ["Aarush", 13, "Berlin", 15754227021, 48, "Login Successful", "Login Fail", "Try again"]
name = str(input("What is your name? "))
age = int(input("What is your age? "))
city = str(input("Where do you live? "))
number = int(input("What is your phone number? "))
question = int(input("What is 20 + 7 * 4? "))
if name == Login_app[0] and age == Login_app[1] and city == Login_app[2] and number == Login_app[3] and question == Login_app[4]:
  print(Login_app[5])
if name != Login_app[0] or age != Login_app[1] or city != Login_app[2] or number != Login_app[3] or question != Login_app[4]:
  print(Login_app[6])
