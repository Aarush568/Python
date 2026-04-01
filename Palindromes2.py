def is_palindrome(num):

    return str(num) == str(num)[::-1]

def generate_non_palindromes(n):

    if n <= 0:
        return []
    
    non_palindromes = []
    num = 1
    
    while len(non_palindromes) < n:
        if not is_palindrome(num):
            non_palindromes.append(num)
        num += 1
    
    return non_palindromes

print(generate_non_palindromes(int(input("Enter the number:"))))