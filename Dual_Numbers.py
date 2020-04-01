import sys

n = int(input("Enter a number: "))

while n < 0:
    print("You must type non-negative number")
    n = int(input("Enter a number: "))

if n < 10 and n >= 0:
    print("Dual")
    sys.exit()

# converting given number to a list for iterating and comparing
n = str(n)
n = list(n)
sum = 1
a = int(n[1])
k = int(n[1])
# looping through the list
for i in n:
    i = int(i)
    # look comment in line 32, 33
    if i != a and i != k:
        if i == k:
            sum = sum
        else:
            # if i is not equal to 1 index(second digit of number) of number then add sum, and variable a is equal to i in that case
            sum += 1
            a = i
            # defining index of i in the list
            ind = n.index(str(i))
            # if the next number of i is same 1 index(second digit of number) it means that sum should not be added
            # and thats why we need if statment in line 22
            if n[ind + 1] == n[1]:
                k = i
                a = int(n[1])
    else:
        continue

# conditions for dual and not dual numbers
if sum <= 2:
    print("Dual")
else:
    print("Not Dual")


