'''N players want to divide into 2 teams in such way, that the strongest
player is in the first team, second strongest is in the second team, third
strongest is in the first team and so on. Given number of players N and
N whole numbers denoting strengths of the players, print the strengths of
the first team on the first line, strengths of the second team - on the
second line'''


N=int(input())
strengths=list(map(int,input().split()))
strengths.sort(reverse=True)
# print(strengths)
print(strengths[::2])
print(strengths[1::2])

