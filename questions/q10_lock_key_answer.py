# 90도 회전
def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

# 자물쇠가 열리는지 체크
def check(startX, startY, key, lock, expendSize, start, end):
    # 자물쇠를 확장함(핵심 개념)
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i - start][j - start]
            if expendList[i][j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key) - 1  # expendList에서 lock의 시작 지점
    end = start + len(lock)  # expendList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2  # expendList 배열의 크기

    # lock은 고정이고 key가 움직이면서 체크
    for a in range(0, 4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendSize, start, end):
                    return True
        key = rotation(key)

    return False