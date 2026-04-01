def print_equilateral_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print(rows, end=" ")
        print()
def main():
    rows = int(input("Enter the number of rows for the equilateral triangle: "))
    print_equilateral_triangle(rows)
main()
