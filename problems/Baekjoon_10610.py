import sys

N = sys.stdin.readline().rstrip()

total = 0
zero = False
for i in N:
    if i == '0':
        zero = True
    total += int(i)


if zero == True and total % 3 == 0:
    result = sorted(N, reverse=True)
    print(''.join(result))
else:
    print(-1)