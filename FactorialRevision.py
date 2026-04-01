import math

def calculate_factorial():
    while True:
        try:
            # Get input from the user
            number = int(input("Enter a non-negative integer to find its factorial: "))
            
            if number < 0:
                print("Factorial is not defined for negative numbers. Please try again.")
                continue

            # Calculate and display the factorial
            result = math.factorial(number)
            print(f"The factorial of {number} is {result}")
        
        except ValueError:
            
            print("Invalid input. Please enter a valid integer.")
            continue

        # Ask the user if they want to run the code again
        retry = input("Do you want to calculate another factorial? (yes/no): ").strip().lower()
        
        if retry not in ('yes', 'y'):
            
            print("Goodbye!")
            break

# Run the function
calculate_factorial()
