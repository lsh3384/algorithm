n = int(input())  # 컴퓨터의 수
m = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# 1번부터 처리하기 위해 컴퓨터의수(n) + 1만큼 graph를 만들어줌
graph = [[] * n for _ in range(n + 1)]

# 네트워크에 있는 컴퓨터 수 만큼 반복문을 돌면서 그래프에 넣어줌
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 결과물 저장할 변수
cnt = 0

# 방문처리 하기 위한 리스트
visited = [0] * (n + 1)


def dfs(start):
    global cnt
    # 1) 첫번째 노드 방문처리
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

# 문제에 컴퓨터는 1번부터 시작한다고 되어있기 때문에 dfs(1)을 넣음
dfs(1)
print(cnt)