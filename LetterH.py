def print_letter_h(size):
    width = size * 2 - 1
    for i in range(size):
        for j in range(width):
            if j == 0 or j == width - 1:
                print(size, end="")
            elif i == size // 2 and j % 2 == 0:
                print(size, end="")
            else:
                print(" ", end="")
        print()
def main():
    size = int(input("Enter the size of the letter 'H': "))
    print_letter_h(size)
main()
