import sys

# sys.stdin.readline함수를 input에 대입해서 input처럼 사용할 수 있도록 만들어 놓음
input = sys.stdin.readline
INF = int(1e9)

print("노드의개수, 간선의 개수를 띄어쓰기 기준으로 입력하세요.")
n, m = map(int, input().split())

print("시작 노드를 입력하세요.")
start = int(input())


graph = [[] for i in range(n + 1)]

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

"""
노드의개수, 간선의 개수를 띄어쓰기 기준으로 입력하세요.
6 11
시작 노드를 입력하세요.
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""