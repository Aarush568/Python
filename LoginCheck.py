list = ["Aarush", 15, "Berlin", 2405, "India", 15754227021, 54]
name = str(input("What is your name? "))
if name == list[0]:
    age = int(input("What is your age? "))
    if age == list[1]:
        city = str(input("Where do you live? "))
        if city == list[2]:
            birthdate = int(input("What is your date of birth? "))
            if birthdate == list[3]:
                home_country = str(input("What is your home country? "))
                if home_country == list[4]:
                    number = int(input("What is your phone number (ignore the 0 in front)? "))
                    if number == list[5]:
                        print("And lastly for verification, answer this question correctly. ")
                        question = int(input("What is 25/0.5 + 2^2? "))
                        if question == list[6]:
                            print("Login successfully completed. ")
                        else:
                            print("Login unsuccessful. Please try again in a few minutes. ")
                    else:
                        print("Login unsuccessful. Please try again in a few minutes. ")
                else:
                    print("Login unsuccessful. Please try again in a few minutes. ")
            else:
                print("Login unsuccessful. Please try again in a few minutes. ")
        else:
            print("Login unsuccessful. Please try again in a few minutes. ")
    else:
        print("Login unsuccessful. Please try again in a few minutes. ")
else:
    print("Login unsuccessful. Please try again in a few minutes. ")