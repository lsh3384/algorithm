import sys

T = int(sys.stdin.readline())

buttons = [300, 60, 10]

cnt = [0] * 3
for i in range(len(buttons)):
    while T / buttons[i] >= 1:
        T -= buttons[i]
        cnt[i] += 1

if T > 0:
    print(-1)
else:
    for i in range(len(cnt)):
        print(cnt[i], end=' ')