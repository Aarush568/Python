def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i   
    if n > 2:
        factors.append(n)
    return factors

try:
    user_input = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1) 
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.") 
factors = prime_factors(user_input)
print(f"The prime factors of {user_input} are: {factors}")