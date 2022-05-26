import sys

N = int(sys.stdin.readline())

meeting = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append([s, e])

meeting.sort(key=lambda x: (x[1], x[0]))

time = meeting[0][1]

cnt = 1
for i in range(1, N):
    if meeting[i][0] >= time:
        cnt += 1
        time = meeting[i][1]

print(cnt)
