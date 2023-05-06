import sys
import heapq

N, M = map(int, sys.stdin.readline().split())


six_arr = []
one_arr = []
for i in range(M):
    six, one = map(int, sys.stdin.readline().split())
    heapq.heappush(six_arr, six)
    heapq.heappush(one_arr, one)

# print(six_arr)
# print(one_arr)


six_min = heapq.heappop(six_arr)
# print(six_min)
one_min = heapq.heappop(one_arr)
# print(one_min)

print(min((N // 6) * six_min + (N % 6) * one_min, ((N // 6) + 1) * six_min, N * one_min))