from itertools import permutations, combinations
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operator_num = list(map(int, sys.stdin.readline().split()))

oper = ['+', '-', '*', '%']

operators = []
for i, o in enumerate(oper):
    for j, n in enumerate(operator_num):
        if i == j and n != 0:
            ops = (o * n)
            for op in ops:
                operators.append(op)


result = permutations(operators, len(operators))


total = []
for i in result:
    tmp = nums[0]
    for j, k in zip(range(1, len(nums)), i):
        if k == '+':
            # print('tmp', tmp, k, nums[j])
            tmp += nums[j]
        elif k == '-':
            # print('tmp', tmp, k, nums[j])
            tmp -= nums[j]
        elif k == '*':
            # print('tmp', tmp, k, nums[j])
            tmp *= nums[j]
        elif k == '%':
            # print('tmp', tmp, k, nums[j])
            if tmp < 0:
                tmp = -(abs(tmp) // nums[j])
            else:
                tmp //= nums[j]
    total.append(tmp)


    # print(i)


# print(total)

print(max(total))
print(min(total))