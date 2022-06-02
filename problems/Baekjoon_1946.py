import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    rank = []
    cnt = 1
    N = int(sys.stdin.readline().rstrip())
    for j in range(N):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        tmp.append(tmp[0] - tmp[1])
        rank.append(tmp)
    rank.sort(key=lambda x: (x[2], x[0]), reverse=True)

    compare = [rank[0][0], rank[0][1]]
    for i in range(1, len(rank)):
        if compare[0] -rank[i][0] > 0 and compare[1] - rank[i][1] < 0:
            cnt += 1
            compare[0] = rank[i][0]
            compare[1] = rank[i][1]

    print(cnt)