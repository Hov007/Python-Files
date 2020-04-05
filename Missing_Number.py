inp_sequence = input().split()
numbers = []

for i in inp_sequence:
    i = int(i)
    numbers.append(i)

N = len(numbers) + 1
ideal_sum = 0
for i in range(1, N+1):
    ideal_sum += i

print(ideal_sum - sum(numbers))