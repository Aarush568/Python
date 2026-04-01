def compute_hcf(x, y):
    # This function implements the Euclidean algorithm to find the HCF
    while(y):
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    # LCM is calculated using the formula: (x * y) // HCF(x, y)
    hcf = compute_hcf(x, y)
    lcm = (x * y) // hcf
    return lcm

def main():
    # Taking input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculating HCF and LCM
    hcf = compute_hcf(num1, num2)
    lcm = compute_lcm(num1, num2)
    
    # Displaying the results
    print(f"The HCF of {num1} and {num2} is: {hcf}")
    print(f"The LCM of {num1} and {num2} is: {lcm}")

# Running the main function
main()
