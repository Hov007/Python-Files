'''A thief stole N objects, but he has place in his backpack for only M
objects.Given numbers N, M and N real numbers denoting prices of
objects, print maximum total price of the objects that the thief can take
with him.
'''

N = input("Input a positive number N: ")
M = input("Input a positive number M: ")

while M > N:
    print("N must be greater than M!")
    N = input("Input a positive number N: ")
    M = input("Input a positive number M: ")

inp_sequence = input().split()
a = []

for i in inp_sequence:
    i = float(i)
    a.append(i)
a.sort(reverse = True)


print(sum(a[:M]))

# More optimal solution
'''N, M = [int(elem) for elem in input().split()]
weights = [float(elem) for elem in input().split()]
weights.sort(reverse=True)
print(sum(weights[:M]))'''