def find_hcf(a, b):
    while b != 0: 
        a, b = b, a % b
    return a

def find_lcm(a, b):
    hcf = find_hcf(a, b)
    return abs(a * b) // hcf

def print_star_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# Main section
def main():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        hcf = find_hcf(a, b)
        lcm = find_lcm(a, b)

        print(f"The HCF of {a} and {b} is: {hcf}")
        print(f"The LCM of {a} and {b} is: {lcm}")

        n = int(input("Enter the number of rows for the star pattern: "))
        print_star_pattern(n)

    except ValueError:
        print("Please enter valid integers.")

main()