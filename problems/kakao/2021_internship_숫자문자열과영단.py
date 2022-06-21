def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    while True:
        for i in range(len(eng)):
            if eng[i] in s:
                s = s.replace(eng[i], str(i))
                print(s)
        if s.isdigit():
            break

    answer = int(s)
    return answer