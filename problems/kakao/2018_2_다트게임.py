def solution(dartResult):
    answer = []
    index = -1
    dartResult = dartResult.replace('10', 'A')
    for i in dartResult:
        if i.isdigit():
            answer.append(int(i))
            index += 1
        elif i == 'A':
            answer.append(10)
            index += 1
        elif i == 'D':
            answer[index] = answer[index] * answer[index]
        elif i == 'T':
            answer[index] = answer[index] * answer[index] * answer[index]
        elif i == '*':
            print('*')
            if index == 0:
                answer[index] = answer[index] * 2
            if index >= 1:
                answer[index - 1] = answer[index - 1] * 2
                answer[index] = answer[index] * 2
        elif i == '#':
            print('#')
            answer[index] = answer[index] * (-1)

    result = sum(answer)

    return result