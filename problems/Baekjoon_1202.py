import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewel = []
for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, (-V, M))


bags = []
for j in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)


bags.sort(reverse=True)
# print(bags)

total_value = 0
for k in range(K):
    while True:
        V, M = heapq.heappop(jewel)
        # print(-V, M)
        if M <= bags[k]:
            total_value += -V
            break

print(total_value)