import sys

sys.setrecursionlimit(10 ** 4)  # 재귀스택 확장


def dfs(x, y):

    # 지도 범위를 벗어나면 종료
    if x < 0 or y < 0 or y >= w or x >= h:
        return False

    # 1 = 섬 이면 주위(상하좌우대각선) dfs탐색
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)  # 반 시계 방향 순환
        dfs(x - 1, y - 1)
        dfs(x, y - 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        dfs(x, y + 1)
        dfs(x - 1, y + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    else:
        result = 0
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if dfs(i, j) == True:
                    result += 1
        print(result)