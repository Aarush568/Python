#Start code here
while True:
  num = int(input("Enter your prime number test: "))
  if num > 2:
    for i in range(int(num / 2)):
      i = i + 2
      if num % i == 0:
        print(num, "is divisible by", i, ", as it isn't a prime number.")
        break
    else:
      print(num, "is only divisible by 1 and itself, ", "it is a prime number")
  print()
