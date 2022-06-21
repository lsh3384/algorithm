def solution(n, arr1, arr2):
    bin_arr1 = []

    for num in arr1:
        tmp_bin = ''
        for i in range(n - 1, -1, -1):
            binary = num // 2 ** (i)
            tmp_bin += str(binary)
            num = num % (2 ** (i))
        bin_arr1.append(tmp_bin)

    bin_arr2 = []
    for num in arr2:
        tmp_bin = ''
        for i in range(n - 1, -1, -1):
            binary = num // 2 ** (i)
            tmp_bin += str(binary)
            num = num % (2 ** (i))
        bin_arr2.append(tmp_bin)

    answer = []
    for a, b in zip(bin_arr1, bin_arr2):
        tmp_bin = ''
        for i, j in zip(a, b):
            if int(i) or int(j):
                tmp_bin += '#'
            else:
                tmp_bin += ' '
        answer.append(tmp_bin)

    return answer