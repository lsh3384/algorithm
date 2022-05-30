import sys

N = int(sys.stdin.readline())

road_length = []


road_length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

cur_min = cost[0]
total = cost[0] * road_length[0]
for i in range(1, N - 1):
    if cur_min <= cost[i]:
        total += cur_min * road_length[i]
    else:
        cur_min = cost[i]
        total += cur_min * road_length[i]

print(total)