numberlist = [3298, 24398, 31, 12, 103, 3429, 39854, 842, 49258, 2498, 3147, 3183, 193, 1298, 340, 43190]
even = []
odd = []
for i in range(16):
    if numberlist[i] % 2 == 0:
        even.append(numberlist[i])
    else:
        odd.append(numberlist[i])
def sum_of_evens(even):
    resulteven = even[0]+even[1]+even[2]+even[3]+even[4]+even[5]+even[6]+even[7]+even[8]+even[9]
    print("The sum of all even numbers is", resulteven)
sum_of_evens(even)
def max_odd(odd):
    maxoddnumber = None
    for 
