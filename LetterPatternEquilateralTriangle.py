def triangle(ascii_value):
    letter = chr(ascii_value)
    height = ascii_value - ord('A') + 1 if 'A' <= letter <= 'Z' else ascii_value - ord('a') + 1
    for i in range(1, height + 1):
        print(' ' * (height - i), end='')
        print((letter + ' ') * i)
ascii_value = int(input("Enter an ASCII value: "))
if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
    triangle(ascii_value)
else:
    print("Please enter a valid ASCII value for an alphabetic character (65-90 for uppercase or 97-122 for lowercase).")
