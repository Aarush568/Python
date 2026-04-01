def trianglearea(base,height):
    return 1/2 * base * height
base = int(input("The base of your triangle: "))
height = int(input("The height of your triangle: "))
area = trianglearea(base,height)
print("The area of your triangle is: ", area)
