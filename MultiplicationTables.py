multiplication = []
exponent = []
a = 0
b = 0
mul = int(input("The number for your multiplication: "))
ex = int(input("The number for your exponent(2-5): "))
if ex > 5:
    print("Invalid choice!")
for i in range(10):
    a = a + 1
    result = mul * a
    multiplication.append(result)
print(multiplication)
for i in range(10):
    b = b + 1
    result = b ** ex
    exponent.append(result)
print(exponent)


    