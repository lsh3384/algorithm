# 가운데 위치한 숫자가 입력된 경우 현재 손가락의 위치와 주 손잡이에 따라 다른 결과 도출
def pos(num, left, right, hand):
    # 엄지손가락의 현재 위치를 파악하기 위해 딕셔너리로 키패드 생성
    kp = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    # (x1, y2), (x2, y2)의 좌표간 거리는 |x1 - x2| + |y1 - y2|
    dist_left = abs(kp[num][0] - kp[left][0]) + abs(kp[num][1] - kp[left][1])
    dist_right = abs(kp[num][0] - kp[right][0]) + abs(kp[num][1] - kp[right][1])

    # 입력된 키와 거리가 가까운 손가락의 결과 리턴
    if dist_left < dist_right:
        return 'L'
    elif dist_left > dist_right:
        return 'R'
    # 입력된 키와 왼손, 오른손의 거리가 같은 경우 오른손잡이면 R, 왼손잡이면 L 출력
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'


def solution(nums, hand):
    result = ''

    # 현재 엄지손가락의 위치 가리킬 변수(처음에는 왼손, 오른손 각각 *, #으로 초기화
    left = '*'
    right = '#'

    for num in nums:
        if num in [1, 4, 7]:  # 입력된 숫자가 1, 4, 7이면 왼손 엄지손가락
            result += 'L'
            left = num
        elif num in [3, 6, 9]:  # 입력된 숫자가 3, 6, 9이면 오른손 엄지손가락
            result += 'R'
            right = num
        else:  # 입력된 숫자가 2, 5, 8, 0일 경우
            mid = pos(num, left, right, hand)
            result += mid
            if mid == 'R':
                right = num
            else:
                left = num

    return result