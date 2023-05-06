# 좋은수열
def choose_num(result, count):
    # 좋은 수열인지 아닌지를 판별
    for i in range(1, count//2+1):
        if str(result)[count-i:] == str(result)[count-2*i:count-i]:
            return

    # 종료 조건, 수열이 처음 지정한 길이가 되면 종료
    if count == N:
        print(result)
        exit(0)

    # 자리수를 늘려가며 체크한다. 나쁜수열이라면 1,2,3 순서대로 늘려가며 체크하게 된다.
    for i in range(1, 4):
        temp = result * 10 + i
        choose_num(temp, count+1)


N = int(input())
choose_num(0, 0)