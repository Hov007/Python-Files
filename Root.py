n = int(input("Enter a number: "))

while n < 0:
    print("You must type non-negative number")
    n = int(input("Enter a number: "))


# Function that sums digits of the given number
def root(a):
    sum = 0
    a = str(a)
    for i in a:
        i = int(i)
        sum += i
    return sum
print(n)
# Calling function root for sum of the digits
our_number = root(n)
print(our_number)

# Giving condition for sum
while our_number > 9:
    our_number = root(our_number)
    print(our_number)

