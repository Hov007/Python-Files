N = input("number: ")
inp_sequence = input().split()
numbers = []

for i in inp_sequence:
    i = int(i)
    numbers.append(i)
N = len(numbers)
asc = 0
desc = 0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i + 1]:
        asc += 1
    elif numbers[i] > numbers[i + 1]:
        desc += 1

if asc == N - 1:
    print("Ascending")
elif desc == N - 1:
    print("Descending")
else:
    print("Neither")