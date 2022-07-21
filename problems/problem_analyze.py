from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    maxGap = -1e9
    candidates = list(combinations_with_replacement(range(0, 11), n))

    print(len(candidates))
    print(candidates)

    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0

        for score in candidate:
            info2[10 - score] += 1
            print(info2)


n = 5

info = [2,1,1,1,0,0,0,0,0,0,0]

solution(n, info)