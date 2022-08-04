from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

per = permutations(a)

total = 0
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j] - i[j+1])
    if total < s:
        total = s


print(total)