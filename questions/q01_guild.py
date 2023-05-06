n = int(input())

member = []
member = list(map(int, input().split(' ')))

member.sort()

print(member)
group = 0
count = 0

for i in member:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)