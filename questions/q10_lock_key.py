def turn(key, n):
    tmp = [[0] * n for k in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = key[i][j]
    return tmp

def up(tmp, n):
    for i in range(n):
        for j in range(n):
            if i != n-1:
                tmp[i][j] = tmp[i+1][j]
            else:
                tmp[i][j] = 0
    return tmp

def down(tmp, n):
    for i in range(n):
        for j in range(n):
            if i < n-1:
                if i == 0:
                    tmp[i+1][j] = tmp[i][j]
                    tmp[i][j] = 0
                else:
                    tmp[i+1][j] = tmp[i][j]
    return tmp


def left(tmp, n):
    for i in range(n):
        for j in range(n):
            if j < n-1:
                tmp[i][j] = tmp[i][j + 1]
            else:
                tmp[i][j] = 0
    return tmp

def right(tmp, n):
    for i in range(n):
        for j in range(n-1, -1, -1):
            if j == 0:
                tmp[i][j] = 0
            else:
                tmp[i][j] = tmp[i][j - 1]
    return tmp

def solution(key, lock):
    original_key = key
    # 키 90도 돌리기
    n = len(key)

    turn_array = []
    print(key)

    # 90도씩 돌려서 4개의 키 모양 저장해놓기
    for i in range(4):
        turn_array.append(key)
        key = turn(key, n)
        if key == lock:
            return True

    print(turn_array)

    # 출력해보기
    for i in turn_array:
        for j in range(n):
            for k in range(n):
                print(i[j][k], end=' ')
            print()
        print()


    mid_array = []

    mid_array
    for i in range(3):
        tmp = turn_array[i]
        for _ in range(1):
            tmp = left(tmp, n)
        mid_array.append(tmp)
        if tmp == lock:
            return True
    print(mid_array)
    # 출력해보기
    for i in mid_array:
        for j in range(n):
            for k in range(n):
                print(i[j][k], end=' ')
            print()
        print()



    # 일치 불일치 판별
    for new_key in turn_array:
        if key == lock:
            print('일치')
        else:
            print('불일치')



    # # 상하좌우 확인하기
    # # 상
    # for i in range(n):
    #     for j in range(n):
    #         if i != n-1:
    #             tmp[i][j] = tmp[i+1][j]
    #         else:
    #             tmp[i][j] = 0
    # print(tmp)
    #
    # # 하
    # for i in range(n):
    #     for j in range(n):
    #         if i < n-1:
    #             if i == 0:
    #                 tmp[i+1][j] = tmp[i][j]
    #                 tmp[i][j] = 0
    #             else:
    #                 tmp[i+1][j] = tmp[i][j]
    # print(tmp)
    #
    # # 우
    # for i in range(n):
    #     for j in range(n-1, -1, -1):
    #         if j == 0:
    #             tmp[i][j] = 0
    #         else:
    #             tmp[i][j] = tmp[i][j - 1]
    # print(tmp)
    #
    # # 좌
    # for i in range(n):
    #     for j in range(n):
    #         if j < n-1:
    #             tmp[i][j] = tmp[i][j + 1]
    #         else:
    #             tmp[i][j] = 0
    # print(tmp)





    # 상 우
    # 하 좌
    # 하 우

    # 시계방향 90도씩 3번 돌리면서
    # 상, 하, 좌, 우 n -1 번씩 옮기면서
    # lock과 일치 여부 확인
    # 일치하면 answer = True
    # answer 디폴트는 False

    answer = True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key, lock)