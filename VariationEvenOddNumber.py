def sum_of_evens(numbers):
    """Compute the sum of all even numbers in the list."""
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
def max_odd(numbers):
    """Find the maximum odd number in the list."""
    max_odd_number = None
    for number in numbers:
        if number % 2 != 0:
            if max_odd_number is None or number > max_odd_number:
                max_odd_number = number
    return max_odd_number
def custom_sort(numbers):
    """Sort the list in ascending order without using the built-in sort method."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))    
    even_sum = sum_of_evens(numbers)
    max_odd_num = max_odd(numbers)
    sorted_numbers = custom_sort(numbers.copy())    
    print(f"Sum of even numbers: {even_sum}")
    print(f"Maximum odd number: {max_odd_num if max_odd_num is not None else 'No odd numbers in the list'}")
    print(f"Sorted list: {sorted_numbers}")
except ValueError:
    print("Please enter a valid list of integers.")