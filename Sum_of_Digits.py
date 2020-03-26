n = int(input("Enter a number: "))

while n < 0:
    print("You must type non-negative number")
    n = int(input("Enter a number: "))

n = str(n)
sum = 0
for i in n:
    m = int(i)
    sum += m

print("The sum of digits " + str(n) + " is " + str(sum))