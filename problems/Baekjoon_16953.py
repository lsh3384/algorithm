import sys

A, B = map(int, sys.stdin.readline().split())

cnt = 0
while B > A:
    if B % 10 == 1:
        B = B // 10
        cnt += 1
    else:
        B = B / 2
        cnt += 1


if A == B:
    print(cnt+1)
else:
    print(-1)

