import time
name = str(input("What's your name? "))
def bdaysong():
    print("Happy Birthday to you!")
    time.sleep(3)
for i in range(2):
    bdaysong()
def sayname():
    print("Happy Birthday dear", name)
    time.sleep(3)
sayname()
bdaysong()
def maygodblessyou():
    for i in range(2):
        print("May god bless you!")
        time.sleep(3)
maygodblessyou()
sayname()
bdaysong()

    