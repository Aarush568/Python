def changepassword():
    print("Now we will change the password to be secure. ")
    checkpassword = str(input("Enter the starting password. "))
    if checkpassword != password:
        checkpassword2 = str(input("Enter the password again. "))
        
        if checkpassword2 != password:
            print("Sorry, you won't be able to change the password now. ")
        
        else:
            newpassword = int(input("Enter your prefered password. "))
            newpassword2 = int(input("Enter the same password again. "))
            
            if newpassword2 != newpassword:
                newpassword3 = int(input("Enter the same password again. "))
                
                if newpassword3 != newpassword:
                    print("Sorry, you won't be able to change the password now. ")
               
                else:
                    print("You successfully changed your password. ")
            else:
                print("You successfully changed your password. ")
                   


def registration(): 
    username = str(input("Enter your username for registration. "))
    password = "hello5"
    print("Your password is 'hello5'. ")



def login():
    loginusername = str(input("Enter your registered username: "))
    loginpassword = str(input("Enter the given password. "))
    
    if loginusername != username or loginpassword != password:
        print("Please try again. ")
        loginusername2 = str(input("Enter your registered username again: "))
        loginpassword2 = str(input("Enter the given password again. "))
        
        if loginusername2 != username or loginpassword2 != password:
            print("Sorry, you will be able to login in a few minutes. ")
        else:
            print("You successfully logged in. ")
            changepassword()
    
    else:
        print("You successfully logged in. ")
        changepassword()

registration()
login()
            