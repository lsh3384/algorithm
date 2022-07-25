def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[2])[2:]
        ans.append(("0" * (n- len(bin_str)) + bin_str).replace('1', '#').replace('0', ' '))
        print(bin_str)
    return ans

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))