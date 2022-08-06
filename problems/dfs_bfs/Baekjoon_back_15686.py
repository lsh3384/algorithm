import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

# print(matrix)


chicken = []
house = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append((i+1, j+1))
        elif matrix[i][j] == 2:
            chicken.append((i+1, j+1))


# print(chicken)
# print(house)
result = 999999
for chi in combinations(chicken, M):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)