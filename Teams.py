'''N players want to divide into 2 teams in such way, that the strongest
player is in the first team, second strongest is in the second team, third
strongest is in the first team and so on. Given number of players N and
N whole numbers denoting strengths of the players, print the strengths of
the first team on the first line, strengths of the second team - on the
second line'''


inp_sequence = input().split()
list_ = []

for i in inp_sequence:
    i = int(i)
    list_.append(i)

# meking given list to descending list to iterate and take numbers
list_.sort(reverse = True)


a = []
b = []

# adding even indexes to list "a" and odd numbers to list "b"
for i in range(len(list_) - 1):
    if i % 2 == 0:
        a.append(list_[i])
    else:
        b.append(list_[i])

# because we iterate antil the last item of the list, had to add the last number to one of
# our lists, with the same logic as in loop above
if len(list_) % 2 == 0:
    b.append(list_[len(list_) - 1])
else:
    a.append(list_[len(list_) - 1])

# printing results from 2 lists
for i in a:
    if i == a[len(a) - 1]:
        print(i)
    else:
        print(i, end=" ")

for j in b:
    print(j, end=" ")