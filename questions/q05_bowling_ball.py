n, m = map(int, input().split())
pound = list(map(int, input().split()))

result = 0
for i in range(n):
    if i == n:
        break
    for j in range(i + 1, n):
        if pound[i] != pound[j]:
            result += 1

print(result)

# 정답지 풀이
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]
    
print(result)

'''