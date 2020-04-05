a = 30
b = 40
count = 0
min1 = 0

for i in range(1, a + 1):
    if a % i == 0:
        min1 += 1

number = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            if count > min1:
                min1 = count
                count = 0
                number = i

print(min1)
print(number)