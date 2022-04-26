def solution(key, lock):
    # 키 90도 돌리기
    n = len(key)
    tmp = [[0] * n for k in range(n)]
    print(tmp)
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = key[i][j]
    print(tmp)

    # 상하좌우 확인하기
    # 상
    for i in range(n):
        for j in range(n):
            if i != n-1:
                tmp[i][j] = tmp[i+1][j]
            else:
                tmp[i][j] = 0
    print(tmp)

    # 하
    for i in range(n):
        for j in range(n):
            if i < n-1:
                if i == 0:
                    tmp[i+1][j] = tmp[i][j]
                    tmp[i][j] = 0
                else:
                    tmp[i+1][j] = tmp[i][j]
    print(tmp)

    # 좌


    # 우



    # 상 우
    # 하 좌
    # 하 우



    answer = True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key, lock)