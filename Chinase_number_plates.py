n = int(input("Enter a number: "))
cost = 1000

while n > 10 ** 9:
    print("Your number should  no be greater then 10^9")
    n = int(input("Enter a number: "))
# converting n to string to loop
n = str(n)

# defining a count for counting 8 in input number
count = 0

# looping through number
for i in n:
    i = int(i)
    if i == 8:
        count += 1

pay = count * cost
print(pay)

