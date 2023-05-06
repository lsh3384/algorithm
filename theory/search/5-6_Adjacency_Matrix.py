INF = 99999999

# 자기 자신은 0
# 연결되어 있지 않으면 INF
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)