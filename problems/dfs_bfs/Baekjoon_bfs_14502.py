from collections import deque
from itertools import combinations

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 3
                queue.append((nx, ny))


# 바이러스 퍼뜨리고 바이러스 없는 곳 숫자 새기
def virus(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                bfs(graph, i, j)

    # 바이러스 안퍼진 곳 숫자 새기
    cnt = 0
    for row in graph:
        # print(i)
        for ele in row:
            if ele == 0:
                cnt += 1
    return cnt


# 벽을 세울 수 있는 곳 리스트에 담기
candi = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            candi.append((i, j))

# 벽을 세울 수 있는 모든 경우의 수
walls = combinations(candi, 3)

#
result = 0
for wall in walls:
    # print(wall)
    # 연구소 딥카피
    tmp = [item[:] for item in graph]

    # 해당 경우의수로 벽 세우기
    for i in wall:
        tmp[i[0]][i[1]] = 1
    # for j in tmp:
    #     print(j)
    # print()

    # 바이러스 퍼뜨리고 난 후 안퍼진 곳 개수 가져오기
    count = virus(tmp)
    # print(count)

    # 가장 많은 개수로 업데이트해주기
    if result < count:
        result = count

print(result)