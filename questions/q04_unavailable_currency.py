n = int(input())

coins = list(map(int, input().split()))

iter_num = sum(coins)

print(iter_num)


min_num = iter_num + 1
coins.sort(reverse=True)

for i in range(iter_num+1):
    result = i
    for coin in coins:
        if result - coin >= 0:
            result -= coin
            if result == 0:
                continue
    if result != 0:
        min_num = i
        break

print(min_num)

# 정답지 풀이
# 
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()


target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

'''