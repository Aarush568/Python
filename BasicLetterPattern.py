n = int(input("Define your number: "))
asciiValue = 64
for i in range(0, n):
    for j in range(0, i+1):
        asciiValue+=1
        letter = chr(asciiValue)
        print(letter, end ="")
    print("\r")

