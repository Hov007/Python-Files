inp_sequence = input().split()
a = []

for i in inp_sequence:
    i = float(i)
    a.append(i)

b = []
summ = sum(a)
b.append(summ)
# print(b)
print(summ, end=" ")
for i in range(len(a) - 1):
    summ = summ - a[i]
    # b.append(int(summ))
    print(summ, end=" ")
