def is_palindromes(num):
    return str(num) == str(num)[::-1]

def generate_palindromes(n):
    if n <= 0:
        return []

    palindromes = []
    num = 1

    while len(palindromes) == n:
        if is_palindromes(num):
            palindromes.append(num)
        num +=1
        return palindromes

generate_palindromes(int(input("Enter the number of palindromes you want to add into the list. ")))
