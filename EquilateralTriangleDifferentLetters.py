s = int(input("The rows of your equilateral triangle: "))
asciivalue = 65
m = (2*s)-2
for i in range (0,s):
  for j in range(0,m):
    print(end=' ')
  m-=1
  for j in range(0,i+1):
    alphabet = chr(asciivalue)
    print(alphabet, end=' ')
    asciivalue+=1
  print()