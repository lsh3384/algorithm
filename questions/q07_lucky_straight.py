array = list(map(int, input()))

left_sum = 0
for i in range(len(array) // 2):
    print(array[i])
    left_sum += array[i]

right_sum = 0
for i in range(len(array) // 2, len(array)):
    print(array[i])
    right_sum += array[i]

if left_sum == right_sum:
    print('lucky')
else:
    print('ready')