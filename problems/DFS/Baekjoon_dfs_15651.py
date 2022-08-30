# N과 M (3)
import sys

N, M = map(int, sys.stdin.readline().split())
result = []


def back(n, start):
    if n == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N + 1):
        result.append(i)
        back(n+1, i)
        result.pop()

back(0, 1)