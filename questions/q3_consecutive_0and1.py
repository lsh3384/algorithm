data = input()

consec_1 = 0
consec_0 = 0

print(len(data))

for i in range(len(data)):
    if i == 0:
        if data[i] == '0':
            consec_0 += 1
            continue
        else:
            consec_1 += 1
            continue

    if data[i -1] == '0' and data[i] == '1':
        consec_1 += 1
    elif data[i - 1] == '1' and data[i] =='0':
        consec_0 += 1
    else:
        continue

if consec_0 != 0 and consec_0 < consec_1:
    print(consec_0)
else:
    print(consec_1)


# 정답지 풀이법

# data = input()
# count0 = 0
# count1 = 0
#
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(data)-1):
#     if data[i] != data[i + 1]:
#         if data[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0, count1))