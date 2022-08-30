from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

candi = combinations(cards, 3)

ans = 0
for i in candi:
    tmp = sum(i)
    if ans < tmp and tmp <= M:
        ans = tmp

print(ans)