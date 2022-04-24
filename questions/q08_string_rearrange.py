def is_number(string):
    if int(string) >=0 and int(string) <= 9:
        return True
    else:
        return False

arr_string = []
arr_numbers = []

arr_whole = input()

for i in arr_whole:
    try:
        is_number(i)
        arr_numbers.append(int(i))
    except:
        arr_string.append(i)

arr_string.sort()

concat_string = ''
for i in arr_string:
    concat_string += i

print(concat_string + str(sum(arr_numbers)))


# 정답지
'''
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

'''