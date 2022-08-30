import sys
from itertools import combinations

N = int(sys.stdin.readline())

abil = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    abil.append(tmp)

players = [x for x in range(N)]

comb = combinations(players, N // 2)


ans = 99999999

for team1 in comb:
    team2 = []
    for i in players:
        if i not in team1:
            team2.append(i)

    team1_comb = combinations(team1, 2)

    team1_abil = 0
    for j in team1_comb:
        team1_abil += abil[j[0]][j[1]] + abil[j[1]][j[0]]


    team2_comb = combinations(team2, 2)

    team2_abil = 0
    for j in team2_comb:
        team2_abil += abil[j[0]][j[1]] + abil[j[1]][j[0]]

    diff = abs(team1_abil - team2_abil)
    if diff < ans:
        ans = diff
    # print(abs(team1_abil - team2_abil))

print(ans)