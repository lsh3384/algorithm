import sys

price = int(sys.stdin.readline())

change = 1000 - price

change_list = [500, 100, 50, 10, 5, 1]


cnt = 0
for i in range(len(change_list)):
    while change / change_list[i] >= 1:
        change -= change_list[i]
        cnt += 1

    if change <= 0:
        break

print(cnt)