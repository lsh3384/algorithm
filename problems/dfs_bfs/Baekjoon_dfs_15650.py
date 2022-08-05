import sys

N, M = map(int, sys.stdin.readline().split())
result = []
visited = [False] * (N + 1)


def back(n, start):
    if n == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N + 1):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            back(n+1, i+1)
            visited[i] = False
            result.pop()

back(0, 1)