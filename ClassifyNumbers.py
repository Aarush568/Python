def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
    return numbers


def classify_numbers(lst):
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []

    for num in lst:
        if num >= 0:
            positive_numbers.append(num)
        if num < 0:
            negative_numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
        if num % 2 != 0:
            odd_numbers.append(num)
    
    return positive_numbers, negative_numbers, even_numbers, odd_numbers


numbers = get_numbers()
positive, negative, even, odd = classify_numbers(numbers)

print("\nPositive numbers:", positive)
print("Negative numbers:", negative)
print("Even numbers:", even)
print("Odd numbers:", odd)