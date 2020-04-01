n = int(input("Enter a number: "))

while n < 0:
    print("You must type non-negative number")
    n = int(input("Enter a number: "))


n = str(n)
sum = 0
# Taking odd positions
for i in n[ : : 2]:
    i = int(i)
    sum += i

sum1 = 0
# Taking even positions
for j in n[1: : 2]:
    j = int(j)
    sum1 += j

# condition for lucky number
if sum == sum1:
    print("Yes")
else:
    print("No")