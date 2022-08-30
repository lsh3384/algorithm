import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

# 치즈가 남았는지 체크
def check(cheese, n, m):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1: # 1이 하나라도 남아있으면 바로 False리턴
                return False
    return True


def dfs(cheese, n, m, i, j):

    # 4번 반복하는 이유는 상,하, 좌, 우를 담은 dx, dy 리스트 길이가 4임
    # 하나의 노드 i, j당 상, 하, 좌, 우를 검색하기 위해서 해야 함
    for k in range(4):
        x, y = i + dx[k], j + dy[k]

        # 벗어나면 안되는 범위 지정
        # 1) 모눈종이 범위 안
        # 2) 방문하지 않은 것
        if 0 <= x < n and 0 <= y < m and not visit[x][y]:
            if cheese[x][y] != 0:
                cheese[x][y] += 1
            else:
                visit[x][y] = 1
                dfs(cheese, n, m, x, y)



def remove_cheese(cheese, n, m):
    for i in range(n):
        for j in range(m):
            # 기존 치즈 1이 3이상이 되었다는 것은 2면이상 노출이 되었다는 뜻
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            # 3이상이 아니면서 0보다 크면, 즉 1번만 노출이 된 것들은 다시 원래대로 1로 변경
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
    return cheese


res = 0
while True:
    # 치즈를 체크해서 결과 치즈가 없다면 경과시간 출력
    if check(cheese, n, m):
        print(res)
        break

    # 방문처리에 사용되는 visit m * n 리스트
    visit = [[0 for _ in range(m)] for _ in range(n)]

    # 상하좌우 표현하는 리스트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 처음 시작하는 노드 방문처리
    visit[0][0] = 1

    # dfs시작
    dfs(cheese, n, m, 0, 0)

    # 2면 이상 노출된 치즈 녹이기
    cheese = remove_cheese(cheese, n, m)

    # 시간 1시간 경과시키기
    res += 1