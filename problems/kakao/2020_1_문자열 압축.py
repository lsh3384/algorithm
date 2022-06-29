def solution(s):
    length = len(s)
    candidates = []

    if length == 1:
        return 1

    for dividend in range(1, length):
        answer = length
        start = 0
        last = dividend
        times = 0
        check = s[start:last]

        start += dividend
        last += dividend
        while last <= length and start <= length:

            if last <= length:
                now = s[start:last]
                if now == check:

                    if times == 0:
                        times += 1
                        answer -= (dividend - 1)

                    elif times >= 1:

                        times += 1
                        answer -= dividend

                        if times == 9 or times == 99 or times == 999:
                            answer += 1
                else:
                    times = 0
                    check = now
            start += dividend
            last += dividend

        candidates.append(answer)

    return min(candidates)