from collections import deque

# x, y의 위치 이동을 위한 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    count = 0
    n = len(graph)
    queue = deque()

    # 집이 있을 경우 처리 로직
    graph[a][b] = 0  # 방문처리
    queue.append((a, b)) # 큐에 삽입
    count += 1 # 집 1개 늘려줌

    while queue:
        x, y = queue.popleft()

        # x,y로부터 4 방면으로 이동하면서 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 범위를 벗어나면 확인하지 않음
                continue
            if graph[nx][ny] == 1: # 탐색한 곳에 집이 있으면 위에서 한 로직과 동일하게 처리 해줌
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []

# 인접행렬 모든 곳 탐색하기 위한 bfs 트리거
# bfs는 집이 있는 경우, 즉 1인 경우에만 bfs를 하면 됨
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)