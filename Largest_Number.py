n = int(input("Enter a natural number: "))

# number must be positive
while n < 0:
    print("You must type non-negative number")
    n = int(input("Enter a number: "))

n = str(n)

# converting given number to list
not_sorted = list(n)
# converting given number to  deccending list
sorted = sorted(list(n), reverse=True)

# converting lists to numbers for comparing
sorted = ''.join(sorted)
sorted = int(sorted)

not_sorted = ''.join(not_sorted)
not_sorted = int(not_sorted)

# comparing numbers
if int(n) < 10:
    print("No")
elif sorted > not_sorted:
    print("Yes")
else:
    print("No")
