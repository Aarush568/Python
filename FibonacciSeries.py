def calculate_nth_number_of_fibonacci():
    n = int(input("Which position in the Fibonacci series' value do you want to know? "))
    i = 0
    z = 0
    y = 1
    
    # Different conditions for n
    if n <= 0:
        print("Invalid input! Please enter a positive integer. ")
    elif n == 1:
        print(z)
    elif n == 2:
        print(y)
    
    else:    
        
        while i < n-2 and n > 2: # Set conditions for n and repeat until i = n
            
            # Creating the sequence and changing the position of each variable
            x = y + z
            z = y
            y = x
            i+=1 # Makes sure that the values get changed (incrementing of i)
        
        print(x)

calculate_nth_number_of_fibonacci() # Calling the function

# Asking user to redo the code
while True:
    again = str(input("Do you want another value? "))
    
    if again == "yes" or again == "Yes":
        calculate_nth_number_of_fibonacci()
    
    else:
        print("Thank you for running our code. ")
        break
            
# 0 1 1 2 3 5 8 13 21 34