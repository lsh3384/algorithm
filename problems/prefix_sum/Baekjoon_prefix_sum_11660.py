import sys

N, M = map(int, sys.stdin.readline().split())

table = []
for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

coordinates = []
for _ in range(M):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

# print(N, M)
# print(table)
# print(coordinates)

sum = []
for coordi in coordinates:
    tmp = 0
    for i in range(coordi[0], coordi[2]+1):
        for j in range(coordi[1], coordi[3]+1):
            # print(i, j)
            tmp += table[i-1][j-1]
    print(tmp)