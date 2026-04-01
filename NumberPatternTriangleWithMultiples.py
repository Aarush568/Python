rows = int(input("The number of rows: "))
for i in range(0, rows+1):
    for j in range(1, i+1):
        print(i * j, end = "")
    print()