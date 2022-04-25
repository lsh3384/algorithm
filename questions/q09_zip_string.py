def solution(s):
    length = len(s)
    candidates = []

    if length == 1:
        return 1
    for dividend in range(1, length):
        answer = length
        start = 0
        last = dividend
        check = s[start:last]
        # print(check)
        times = 0
        start += dividend
        last += dividend

        while last <= length:
            if last <= length:
                now = s[start:last]
                if now == check:
                    # print('now == check')
                    if times == 0:
                        times += 1
                        answer -= (dividend-1)
                        # print(answer)
                    elif times >= 1:
                        times += 1
                        answer -= dividend
                        # print(answer)
                        if times == 9 or times == 99 or times == 999:
                            # print('times')
                            # print(times)
                            answer += 1
                else:
                    times = 0
                    check = now
                    # print('now')
                    # print(check)
            # print('times')
            # print(times)
            start += dividend
            last += dividend
        # print('answer')
        # print(answer)
        candidates.append(answer)

    return min(candidates)

# test cases
answer = solution("a") # 1
print(answer)

answer = solution("aabbaccc") # 7
print(answer)

answer = solution("ababcdcdababcdcd") # 9
print(answer)

answer = solution("abcabcdede") # 8
print(answer)

answer = solution("abcabcabcabcdededededede") # 14
print(answer)

answer = solution("xababcdcdababcdcd") # 17
print(answer)

answer = solution("aaaaaaaaaaaabcd") # 6
print(answer)

answer = solution("xxxxxxxxxxyyy") # 5
print(answer)