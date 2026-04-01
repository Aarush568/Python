def registration():
    
    print("First you need to complete your registration. ")
    
    username = str(input("Enter your username: "))
    password = str(input("Create your desired password: "))
    rpassword = str(input("Repeat the password. "))

    if rpassword != password:
        rpassword2 = str(input("Wrong password. Repeat again please. "))

        if rpassword2 != password:
            print("Sorry, you will be able to register in a few minutes. ")

        else:
            print("Registration successfully completed. ")
            login()

    else:
        print("Registration successfully completed. ")
        login()

def login():
    loginusername = str(input("Enter your registered username. "))
    loginpassword = str(input("Enter your registered password. "))

    if loginusername != username or loginpassword != password:
        print("Either your username or password was incorrect. ")
        
        loginusername2 = str(input("Enter your registered username again. "))
        loginpassword2 = str(input("Enter your registered password again. "))

        if loginusername2 != username or loginpassword2 != password:

            print("Either your username or password was wrong. You will be able to login again after a few minutes. ")

        else:
            print("Login successfully completed. ")

    else:
        print("Login successfully completed. ")

registration()