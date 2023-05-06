# 내 풀이
nums = []
nums = list(map(int, input()))

result = 0
print(nums)
for i in nums:
    if i == 0 or i == 1 or result == 0:
        result += i
    else:
        result *= i

print(result)

# 정답지 풀이

# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <=1:
#         result += num
#     else:
#         result *= num
#
# print(result)